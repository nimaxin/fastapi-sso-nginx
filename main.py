import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi_sso.sso.google import GoogleSSO

load_dotenv()

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]

app = FastAPI()

sso = GoogleSSO(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="https://preprodxin.ddns.net/auth/google/callback",
    allow_insecure_http=True,
)


@app.get("/auth/google/login")
async def auth_init():
    """Initialize auth and redirect"""
    async with sso:
        return await sso.get_login_redirect(
            params={"prompt": "consent", "access_type": "offline"}
        )


@app.get("/auth/google/callback")
async def auth_callback(request: Request):
    """Verify login"""
    async with sso:
        user = await sso.verify_and_process(request)
    return user
