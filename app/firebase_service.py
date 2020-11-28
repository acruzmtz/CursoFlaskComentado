import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


project_id = 'platzi-todo-296923'
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential, {
  'projectId': project_id,
})


db = firestore.client()

def get_users():
    return db.collection('users').get()


def get_todos(username):
    return db.collection('users').document(username).collection('todos').get()
