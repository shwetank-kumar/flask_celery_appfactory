from math_ops import celery

@celery.task
def addition_task(int1, int2):
    print("Celery background job")
    sum = int1 + int2
    print("Celery background job Done!")
    return sum
