import hashlib
from database.database import get_db
import config

class UserService():
  
    @staticmethod
    def verify(login, password):
        db = get_db()
        hashed_passorwd = hashlib.sha256(f'{password}{config.PASSWORD_SALT}'.encode())

        user = db.execute('''
                SELECT * FROM users 
                JOIN user_types ON users.user_type_id = user_types.id
                WHERE login = ? AND password = ?''', [login, hashed_passorwd.hexdigest()]).fetchone()
        if user:
            return user
        else:
            return None

    @staticmethod
    def hash_password(password):
        hashed_password = hashlib.sha256(f'{password}{config.PASSWORD_SALT}'.encode())

        return hashed_password.hexdigest()


    @staticmethod
    def get_all_users():
        db = get_db()
        return db.execute(
            "SELECT * FROM users "
        ).fetchall()

    @staticmethod
    def get_employees():
        db = get_db()
        return db.execute(
            "SELECT id_user, name FROM users WHERE user_type_id = 2",
            
        ).fetchall()

    @staticmethod
    def get_user_types():
        db = get_db()
        return db.execute(
            "SELECT id, role FROM user_types",

        ).fetchall()


    @staticmethod
    def get_hourly_rate_by_id(id):
        db = get_db()
        return db.execute(
            "SELECT hourly_rate FROM users WHERE id_user = ?",
            [id]
        ).fetchone()


    @staticmethod
    def insert_user(login, password, user_type_id, name, surname, telephone, email, hourly_rate):
        db = get_db()
        db.execute(
            'INSERT INTO USERS (login, password, user_type_id, name, surname, telephone, email, hourly_rate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            [login, password, user_type_id, name, surname, telephone, email, hourly_rate]
        )
        db.commit()

    @staticmethod
    def update_user(login, password, name, surname, telephone, email, id_user):
        db = get_db()
        db.execute(
            'UPDATE USERS SET login = ?, password = ?, name = ?, surname = ?, telephone = ?, email = ? WHERE id_user = ?',
            [login, password, name, surname, telephone, email, id_user]


        )
        db.commit()

    @staticmethod
    def delete_by_id(id_user):
        db = get_db()
        db.execute("DELETE FROM users WHERE id_user = ?", [id_user])
        db.commit()


    @staticmethod
    def get_all_employees():
        db = get_db()

        sql = "SELECT * FROM users WHERE user_type_id != 3"

        return db.execute(sql).fetchall()

        