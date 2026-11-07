

# USER -> kattintgat lskjdskjfksdfjdsk -> BE (user-adat) <- -> FE (user) | DB


class User:
    def __init__(self):
        pass

    def auth():
        pass

    def allowed():
        pass

    def register():
        pass

    def login():
        pass


class FileHandler:
    def safe_read():
        pass

    def safe_write():
        pass


class Session:
    def __init__(self):
        pass

    def is_logged_in():
        pass

    def login():
        pass

    def logout():
        pass


class DatabaseConnection:
    def __init__(self, ip_addr):
        pass

    def connect():
        return object(DB)

    def close():
        pass


class DatabaseHanlder():
    def __init__(self):
        self.db = DatabaseConnection

    def is_user_auth(username):
        self.db.connect()
        return self.db.tunnel(method="SELECT username, is_logged_in from users where users.username like '%username'")