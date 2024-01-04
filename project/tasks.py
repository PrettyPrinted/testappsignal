from celery import shared_task

@shared_task(ignore_result=False)
def add_togethers(a: int, b: int) -> int:
    raise ValueError("intentional error 2")
    return a + b