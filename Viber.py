class Viber:
    messages = []

    @classmethod
    def add_message(cls, msg):
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg):
        if msg in cls.messages:
            cls.messages.remove(msg)

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls):
        if cls.messages:
            print(cls.messages[-1])

    @classmethod
    def total_messages(cls):
        return len(cls.messages)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like