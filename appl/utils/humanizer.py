from datetime import datetime
import time


def format_timedelta(ms):
    ms = int(ms)
    hours, remainder = divmod(ms, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    seconds, milliseconds = divmod(remainder, 1000)
    if hours:
        return '{0} hours, {1} miniuts'.format(hours, minutes)
    else:
        return '{0} minutes, {1} seconds'.format(minutes, seconds)


def humanize_ts(timestamp):
    now = int(time.time() * 1000)
    ts = now - timestamp
    return format_timedelta(ts)


def humanize_dt(dt):
    now = datetime.now()
    ts = (now - dt).total_seconds() * 1000
    return format_timedelta(ts)
