from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/register-page")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/login-page")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/register")
def register():
    return {"access_token": "demo_token", "token_type": "bearer"}

@app.post("/login")
def login():
    return {"access_token": "demo_token", "token_type": "bearer"}
