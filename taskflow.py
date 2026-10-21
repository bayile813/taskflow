# taskflow.py
print('--- TaskFlow ULTMATE v1.0 ---')

tasks = []

def add_task(task_name):
    tasks.append(task_name)
    print(f"Task '{task_name} is added successfully!")


# Test the feature
add_task('Buy groceries')