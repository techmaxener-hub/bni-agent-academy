from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from agent import ask_agent

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "answer": None})

@app.post("/", response_class=HTMLResponse)
async def handle_form(request: Request, user_input: str = Form(...)):
    # Simply pass the text to the agent
    ai_answer = ask_agent(user_input)
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "user_input": user_input, 
        "answer": ai_answer
    })