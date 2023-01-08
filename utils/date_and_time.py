import datetime as dt


def format_time_now():
    """Formats the current datetime as a string containing up to the millisecond as str."""
    return str(dt.datetime.now())[0:21]
