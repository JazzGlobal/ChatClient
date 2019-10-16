# PROTOTYPE MESSAGE PACKET OBJECT

from datetime import datetime
class Message:
    def __init__(self, message, author):
        self.message = message
        self.author = author
        now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        self.postedOn = now
    def export(self):
        to_send = {
            'message': self.message,
            'author': self.author,
            'postedOn': self.postedOn
        }
        return to_send

