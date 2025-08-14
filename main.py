import add
import show
import update
import delete

add_task_response = add.add_task("Sleep")
print(add_task_response)

show_task_response = show.show_tasks()
print(show_task_response)

update_task_response = update.update_task("Sleep", "Washing")
print(update_task_response)

delete_task_response = delete.delete_task("Washing")
print(delete_task_response)

