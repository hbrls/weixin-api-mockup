# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, Integer, SmallInteger, Text
from appl.utils.custom_columns import UTCTimestampType
from appl.utils.db_base import Base
from appl.user.models import read_user


ACTIVITY_TYPE_CLEAN = 1

ACTIVITY_VERB_CREATE = 1
ACTIVITY_VERB_READ = 2
ACTIVITY_VERB_UPDATE = 3
ACTIVITY_VERB_DELETE = 4


class ActivityStream(Base):

    '''
    user_id              user who generated activity
    activity_type  ENUM  tells me the type of activity, e.g. "plan"
    source_id            如果type是clean，那么source_id就是clean_id
    verb           ENUM  e.g. "create"
    data           JSON  冗余换性能
    '''

    __tablename__ = 'activity_stream'
    id = Column(Integer, primary_key=True)
    created = Column(UTCTimestampType, nullable=False)
    updated = Column(UTCTimestampType, nullable=False)
    user_id = Column(Integer, nullable=False)  # 先不用外键，最后反正要写raw sql的
    activity_type = Column(SmallInteger, nullable=False)
    source_id = Column(Integer)
    verb = Column(SmallInteger, nullable=False)
    data = Column(Text)

    def __init__(self):
        self.created = datetime.utcnow()
        self.updated = datetime.utcnow()

    def __repr__(self):
        return '<ActivityStream> created: %s, type: %s, verb: %s> ' % \
               (self.created, self.activity_type, self.verb)

    def rep(self):
        return Representation(self)


class Representation:

    def __init__(self, activity):
        self.id = activity.id
        self.created = activity.created
        self.actor = read_user(activity.user_id)

        if activity.activity_type == ACTIVITY_TYPE_CLEAN:
            self.object = None
            self.target = None
            if activity.verb == ACTIVITY_VERB_CREATE:
                self.action = 'plan-create'
        else:
            pass
