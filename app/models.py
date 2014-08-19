#! python
# -*- coding: utf-8 -*-

import datetime

from sqlalchemy import Column
from sqlalchemy import Integer, String, Boolean, DateTime, Text, Float

from app import db


class Friend(db.Model):
    __tablename__ = 'friend'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    birthday = Column(DateTime, default=datetime.datetime(1900, 1, 1))
    height = Column(Float)
    image_url = Column(String(512))
    notes = Column(Text)
    is_special = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    last_update = Column(DateTime, default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow)

    def to_json(self):
        j = {
            'id': self.id,
            'name': self.name,
            'birthday': self.birthday.isoformat(),
            'height': self.height,
            'image_url': self.image_url,
            'notes': self.notes,
            'is_special': self.is_special,
            'created': self.created,
            'last_update': self.last_update,
        }
        return j
