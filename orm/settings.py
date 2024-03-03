from mongoengine import connect

DB_HOST = '127.0.0.1'
DB_PORT = '27017'
DB_NAME = 'aci_db'
DB_USER = 'aci_user'
DB_USER_PASS = '12345'

connect(
    host=f'mongodb://{DB_USER}:{DB_USER_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?authSource={DB_NAME}'
)
