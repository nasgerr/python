class ConnectionError(Exception):
    pass
class DatabaseConnection:
    def __init__(self):
        self.fl_connection_open = False

    def connect(self, login, password):
        self.fl_connection_open = True
        raise ConnectionError

    def close(self):
        self.fl_connection_open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
