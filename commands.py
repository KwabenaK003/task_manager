import db

def save_task(task):
    # save task to database
    db.tasks.insert_one(task)
    # return response
    return True

def delete_task(id):
    # delete task from database
    db.tasks.delete_one({"_id": id})
    # return response
    return True

from db import tasks

def get_tasks():
    # Get all tasks from database
    all_tasks = db.tasks.find()
    # Return response
    return all_tasks

def update_task(task, update):
    # update task in database
    # Return response
    return True