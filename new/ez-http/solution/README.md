# {EZ http}

## Write-up

Request for 201th page returns an extra header : WWW-Authenticate which tells you should use basic auth.
do another request to the same page with Authorization : Basic <creds in base64> creds are admin:admin

