# taskflow.py
print('--- TaskFlow ULTMATE v1.0 ---')

tasks = []

def add_task(task_name):
    tasks.append(task_name)
    print(f"Task '{task_name} is added successfully!")


# Test the feature
add_task('Buy groceries')


# delete function
def delete_task(task_name):
    if task_name in tasks:
        tasks.remove(task_name)
        print(f"Task '{task_name}' deleted successfully!")
    else:
        print(f"Task '{task_name}' not founds")

# Test the delete task feature
add_task("Buy groceries")
delete_task("Buy groceries")