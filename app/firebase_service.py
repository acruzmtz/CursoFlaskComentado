import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


project_id = 'platzi-todo-296923'
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential, {
  'projectId': project_id,
})


db = firestore.client()

def add_user(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})

def get_users():
    return db.collection('users').get()

def get_user(user_id):
    return db.collection('users').document(user_id).get()

def get_todos(username):
    return db.collection('users').document(username).collection('todos').get()

def add_todo(user_id, description):
    todos_collection_ref = db.collection('users').document(user_id).collection('todos')
    todos_collection_ref.add({'description': description, 'done': False})

def delete(user_id, todo_id):
    todo_ref = db.document('users/{}/todos/{}'.format(user_id, todo_id))
    todo_ref.delete()

def update_todo(user_id, todo_id, done):
    todo_done = not bool(done)
    todo_ref = db.document('users/{}/todos/{}'.format(user_id, todo_id))
    todo_ref.update({'done': todo_done})