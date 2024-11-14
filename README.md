1. clone the repo:

```
git clone https://github.com/nimaxin/fastapi-sso-nginx.git
```

2. create .env file:

```
CLIENT_ID =
CLIENT_SECRET =
```

3. change the domain name and ssl certificate dirs in `nginx.conf`, `compose.yml` and `redirect_uri` if you are not me!
4. run the project:

```
docker compose up
```
