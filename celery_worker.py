from math_ops import celery, create_app


app = create_app('default')
print app.config
app.app_context().push()
