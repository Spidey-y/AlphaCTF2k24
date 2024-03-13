## WEB - Proxy

A straightforward website, upon receiving a `url`, sends an HTTP request to that URL. In the description, we're informed that there are hidden secrets. The blacklist seems ineffective as the secrets are located on the same host (the proxy app), but are actually found in the Nginx service (refer to the docker-compose.yml file). The objective here is to grasp networking concepts within Docker and Docker Compose. You can delve deeper into this topic through YouTube tutorials or the official documentation. By default, Docker Compose creates a network for services within the same project, typically on `172.18.0.0/16`. It also establishes DNS records to enable reaching a service through its name specified in the .yml file, such as `http://nginx`. Despite a regex ensuring the host is an IP address, this isn't a hurdle. Regarding Docker Compose networks:

- `172.18.0.1`: gateway
- `172.18.0.2`: nginx (because the web service depends on nginx in the .yml file)
- `172.18.0.2`: web

However, it's important to note that `172.18.0.0` isn't always the network, as there might be other Docker Compose instances running on `172.18.0.0`. Thus, the correct network must be identified by iterating through addresses like `172.18.0.2`, `172.19.0.2`, `172.20.0.2` … and so on (using `.2` because nginx has a default welcome page on port 80; a response confirms the correct service address).

As for obtaining the flag, we simply need to iterate through ports until we receive a response (a hint suggests trying ports above 6000, in a clue left on port 1337). Looping through ports continues until the flag is obtained.
