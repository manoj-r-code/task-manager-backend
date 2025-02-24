from fastapi import FastAPI
from app.routes import tasks

app = FastAPI(title="Task Manager API")

# Include Routes
app.include_router(tasks.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Task Manager API"}
