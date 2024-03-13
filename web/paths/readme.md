## WEB - Paths

Nginx off-by-slash fail, When a Nginx directive does not end with a slash, it is possible to traverse one step up. This incorrect configuration could allow an attacker to read file stored outside the target folder. in our case

```python
#nginx.conf
location /static {
        alias /var/www/html/static/;
    }
```

payload:
`https://host:port/static../flag.html`
