const express = require('express');
const path = require('path');
const router = express.Router();
const fs = require('fs');
const { exec } = require('child_process');
const { isSafeUrl } = require('../Middlewares/isSafeUrl');
const { checkApiKey } = require('../Middlewares/CheckApiKey');
const { isSysAdmin } = require('../Middlewares/authMiddleware');
const { onlyLocalhost } = require('../Middlewares/OnlyLocalhost');
const bodyParser = require('body-parser');
const axios = require('axios');

router.use(bodyParser.urlencoded({ extended: true }));
router.use(bodyParser.json());
const instance = axios.create({ baseURL: process.env.AXIOS_BASE_URL });


router.get('/', isSysAdmin, (req, res) => {
  res.sendFile('dashboard.html', { root: 'public' });
});


router.get('/reports/report', isSysAdmin, (req, res) => {
  let { reportId } = req.query;
  console.log(reportId);
  reportId = reportId.replace(/\.\.\//g, '');


  if (!reportId) {
    res.status(400).json({ error: 'reportId parameter is required.' });
  } else {
    if (reportId.includes('flag')) {
      return res.status(403).send('You didn\'t expect me to give you the flag this easily, did you?\nWork harder!');
    }
    console.log(reportId)
    p = path.join(__dirname, '..', 'reports', reportId)
    console.log(p)
    const filePath = p;

    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        console.error(`Error reading file: ${err}`);
        res.status(404).json({ error: `Report ${reportId} not found!` });
      } else {
        fs.readFile(path.join(__dirname, '..', 'public', 'report.html'), 'utf8', (htmlErr, htmlData) => {
          if (htmlErr) {
            console.error(`Error reading HTML file: ${htmlErr}`);
            res.status(500).send('Internal Server Error');
          } else {
            console.log(data)
            const styledData = htmlData.replace('<pre id="fileContent"></pre>', `<pre>${data}</pre>`);
            console.log(styledData)
            res.send(styledData);
          }
        });
      }
    });
  }
});


router.get('/reports', isSysAdmin, (req, res) => {
  fs.readdir('./reports/', (err, files) => {
    if (err) {
      res.status(500).send('Internal Server Error');
    } else {
      const reports = files
        .map(file => {
          const reportId = file;
          return `<a href="/reports/report?reportId=${reportId}" class="report-link">Report ${reportId}</a>`;
        })
        .join('');
      res.send(`
          <!DOCTYPE html>
          <html>
          <head>
            <title>SysAdmin</title>
            <link rel="stylesheet" href="/styles.css">
          </head>
          <body>
            <div class="container">
              <h1>Available Reports</h1>
              ${reports}
            </div>
          </body>
          </html>
        `);
    }
  });
});

router.get('/healthchecker', isSysAdmin, (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'public', 'healthchecker.html'));
});


router.post('/api/healthchecker', isSysAdmin, isSafeUrl, async (req, res) => {
  const { url } = req.body;
  const header = req.headers.authorization;
  if (!url || url.trim() === '') {
    return res.status(400).json({ error: 'URL parameter is missing or empty.' });
  }


  const headers = {
    'Content-Type': 'application/json',
    'authorization': header
  };
  try {
    instance.defaults.headers.common['Authorization'] = header;
    const response = await instance.get(url, { headers });
    res.status(200).send('server is up');
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch data from the provided URL.', details: error.message });
  }
});


router.get('/api/remote-task-handler',onlyLocalhost, checkApiKey, (req, res) => {
  const command = req.query.command;

  if (command && command.trim() !== '') {
    exec(command, (err, stdout, stderr) => {
      if (err) {
        return res.status(500).json({ error: 'Command execution failed', details: err.message });
      }
      res.status(200).send(stdout);
    });
  } else {
    res.status(400).json({ error: 'Command parameter missing or empty.' });
  }
});




module.exports = router;
