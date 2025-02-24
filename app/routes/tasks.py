from fastapi import APIRouter, HTTPException
from app.models.task_model import Task
from app.database import tasks_db

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return tasks_db

@router.post("/tasks")
def create_task(task: Task):
    new_task = {"id": len(tasks_db) + 1, "task": task.task, "done": task.done}
    tasks_db.append(new_task)
    return new_task

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for t in tasks_db:
        if t["id"] == task_id:
            t["task"] = task.task
            t["done"] = task.done
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks_db
    tasks_db = [t for t in tasks_db if t["id"] != task_id]
    return {"message": "Task deleted"}
