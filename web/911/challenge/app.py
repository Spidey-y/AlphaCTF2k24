from fastapi import FastAPI, Header, Cookie
from os import environ
from fastapi.responses import JSONResponse


app = FastAPI()
flag = environ.get("FLAG", "AlphaCTF{fake_flag}")


@app.get("/")
def welcome():
    return {"msg": "Welcome to your first Web Challenge! don't hesitate to ask for help if you need it :)", "ps": "I'm powered by FastAPI"}


@app.get("/s3cr3t")
def s3cr3t(agent_type: str = Header(default="visitor", include_in_schema=False), my_cookie=Cookie(None, include_in_schema=False)):
    if my_cookie is None:
        return JSONResponse(content="Where is my_cookie? Only users who give me a cookie are welcomed here :P")
    if agent_type.lower() == "visitor":
        return JSONResponse(content="Nope, visitor detected", headers={"Agent-Type": agent_type})
    if agent_type.lower() == "h4ck3r1337":
        return flag
    else:
        modified_value = "".join(
            [i if i == "h4ck3r1337"[idx%10] else "*" for idx, i in enumerate(agent_type)])
        return JSONResponse(content=f"Nice try hacker, agent {agent_type} not found in agents list", headers={"Agent-Type": modified_value})
