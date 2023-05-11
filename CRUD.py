from typing import Optional,List
from azure.cosmos import  CosmosClient

from models import User , Task

# Initialize the Cosmos DB client
endpoint = "https://ahmadeinieh.documents.azure.com:443/"
key = "co6xHurFZbrgPkWebmCqdVHQIWflPuSZZBHx48nU8QklUl8GoXYxLPryBaHhXcpdmxqUNvw9i7j8ACDbVSOUlg=="
client = CosmosClient(endpoint, key)

# Create or retrieve the database
database_name = "tasks"
database = client.create_database_if_not_exists(id=database_name)

# Create or retrieve the container for users
container_name = "users"
container = database.create_container_if_not_exists(id=container_name, partition_key="/id")

# Create or retrieve the container for tasks
task_container_name = "tasks"
task_container = database.create_container_if_not_exists(id=task_container_name, partition_key="/id")


# Create a user
def create_user(user: User):
    container.create_item(body=user.dict())

# Retrieve a user by ID
def get_user(user_id: str) -> Optional[User]:
    query = f"SELECT * FROM {container_name} c WHERE c.id = @user_id"
    items = list(container.query_items(query, parameters=[{"name": "@user_id", "value": user_id}]))
    if items:
        return User(**items[0])
    return None

# Update a user
def update_user(user_id: str, updated_user: User):
    user = get_user(user_id)
    if user:
        user_data = updated_user.dict(exclude_unset=True)
        container.replace_item(item=user_data, partition_key=user_id)

# Delete a user
def delete_user(user_id: str):
    user = get_user(user_id)
    if user:
        container.delete_item(item=user.dict(), partition_key=user_id)

# Create a task
def create_task(task: Task):
    task_container.create_item(body=task.dict())

# Retrieve a task by ID
def get_task(task_id: str) -> Optional[Task]:
    query = f"SELECT * FROM {task_container_name} c WHERE c.id = @task_id"
    items = list(task_container.query_items(query, parameters=[{"name": "@task_id", "value": task_id}]))
    if items:
        return Task(**items[0])
    return None

# Update a task
def update_task(task_id: str, updated_task: Task):
    task = get_task(task_id)
    if task:
        task_data = updated_task.dict(exclude_unset=True)
        task_container.replace_item(item=task_data, partition_key=task_id)

# Delete a task
def delete_task(task_id: str):
    task = get_task(task_id)
    if task:
        task_container.delete_item(item=task.dict(), partition_key=task_id)

# Get tasks by userId
def get_tasks_by_user_id(user_id: str) -> List[Task]:
    query = f"SELECT * FROM {task_container_name} c WHERE ARRAY_CONTAINS(c.owner, {{'id': '{user_id}'}})"
    items = list(task_container.query_items(query))
    return [Task(**item) for item in items]
