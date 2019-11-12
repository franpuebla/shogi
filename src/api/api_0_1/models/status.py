from model import *


class Status(Model, db.Model):
    __tablename__ = 'status'

    message_id = db.Column(db.String(250))
    msg_cuid_id = db.Column(db.String(250))
    ack = db.Column(db.String(250))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(250))
    caller_id = db.Column(db.String(250))
