from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "RepoPilot practice app"}


@app.get("/login")
def login(email: str | None = None):
    if email is None:
        raise ValueError("Email is required")

    return {"message": f"Welcome {email}"}
