from typing import Optional,List
from azure.cosmos import  CosmosClient

from models import User , Task , TaskDocument

import uuid

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
    user.id = uuid.uuid4().__str__()
    container.create_item(body=user.dict())

def get_user_by_email(email: str) -> Optional[User]:
    query = f"SELECT * FROM {container_name} c WHERE c.email = @email"
    items = list(container.query_items(query,
                                    parameters=[{"name": "@email", "value": email}],
                                    enable_cross_partition_query=True  # Enable cross-partition query
                                    ))

    if items:
        return User(**items[0])
    return None

# Retrieve a user by ID
def get_user(user_id: str) -> Optional[User]:
    query = f"SELECT * FROM {container_name} c WHERE c.id = @user_id"
    items = list(container.query_items(query, parameters=[{"name": "@user_id", "value": user_id}],enable_cross_partition_query=True))
    if items:
        return User(**items[0])
    return None

# Create a task
def create_task(task: Task):
    task.id = uuid.uuid4().__str__()
    task_container.create_item(body=task.dict())
    return task

# Retrieve a task by ID
def get_task(task_id: str) -> Optional[Task]:
    query = f"SELECT * FROM {task_container_name} c WHERE c.id = @task_id"
    items = list(task_container.query_items(query, parameters=[{"name": "@task_id", "value": task_id}],enable_cross_partition_query=True))
    if items:
        return Task(**items[0])
    return None


# Delete a task
def delete_task(task_id: str):
    task = get_task(task_id)
    if task:
        print(task)
        task_container.delete_item(item=task.id, partition_key=task_id)


def get_tasks_by_user_id(user_id: str) -> List[Task]:
    query = f"SELECT * FROM {task_container_name} c WHERE ARRAY_CONTAINS(c.userId, '{user_id}')"
    items = list(task_container.query_items(query, enable_cross_partition_query=True))
    return [Task(**item) for item in items]

def update_complete_task(taskId: str, isComplete: bool):
    task = get_task(taskId)
    if task:
        delete_task(taskId)
        task.isComplete = isComplete
        create_task(task)

def add_user_to_task(taskId: str, userEmail:str):
    task = get_task(taskId)
    userId = get_user_by_email(userEmail).id
    if task:
        delete_task(taskId)
        task.userId.append(userId)
        create_task(task)