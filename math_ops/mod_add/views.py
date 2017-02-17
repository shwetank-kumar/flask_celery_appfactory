from . import mod_add
from .tasks import addition_task

@mod_add.route('/')
def welcome():
    return 'Welcome'

@mod_add.route('/add/<int:int1>/<int:int2>')
def submit_task(int1, int2):
    task = addition_task.apply_async((int1, int2))
    print task.task_id
    return task.task_id

@mod_add.route('/result/<task_id>')
def get_result(task_id):
    result = addition_task.AsyncResult(task_id)
    if result.status == 'SUCCESS':
        ans = result.get()
        return str(ans)
    else:
        return result.status, 202
