from . import mod_add
from ..tasks import addition_task

@mod_add.route('/')
def welcome():
    return 'Welcome'

@mod_add.route('/add/<int:int1>/<int:int2>')
def submit_task(int1, int2):
    task = addition_task.apply_async((int1, int2))
    return task.task_id

@mod_add.route('/result/<task_id>')
def get_result(task_id):
    print "here"
    result = addition_task.AsyncResult(task_id)
    print "here1"
    print result.get()
    return result.get()
