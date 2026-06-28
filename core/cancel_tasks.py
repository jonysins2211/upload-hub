# core/cancel_tasks.py

cancel_tasks = {}


def create_cancel_task(task_id: str):
    """Register a new cancellable task."""
    cancel_tasks[task_id] = False


def cancel_task(task_id: str):
    """Mark a task as cancelled."""
    if task_id in cancel_tasks:
        cancel_tasks[task_id] = True


def is_cancelled(task_id: str) -> bool:
    """Check whether a task has been cancelled."""
    return cancel_tasks.get(task_id, False)


def remove_cancel_task(task_id: str):
    """Remove a task from the cancellation registry."""
    cancel_tasks.pop(task_id, None)