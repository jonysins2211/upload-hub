from uuid import uuid4

tasks = {}

def create_task(message):
    task_id = str(uuid4())

    tasks[task_id] = {
        "message": message
    }

    return task_id