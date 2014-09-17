from datetime import datetime
import time
from sqlalchemy.types import TypeDecorator, Integer


class UTCTimestampType(TypeDecorator):
    impl = Integer

    def process_bind_param(self, value, dialect):
        if value is None:
            return None  # support nullability
        elif isinstance(value, datetime):
            return int(time.mktime(value.timetuple()))
        raise ValueError("not instance of datetime")

    def process_result_value(self, value, dialect):
        if value is not None:  # support nullability
            return datetime.fromtimestamp(float(value))
