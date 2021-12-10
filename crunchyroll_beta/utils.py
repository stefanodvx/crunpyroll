from datetime import datetime

def get_date() -> datetime: 
    now = datetime.utcnow()
    return datetime.strptime(
        "{}-{}-{}T{}:{}:{}Z".format(
            now.year, now.month,
            now.day, now.hour,
            now.minute, now.second
        ),
        "%Y-%m-%dT%H:%M:%SZ"
    )

def str_to_date(string: str) -> datetime: 
    return datetime.strptime(
        string,
        "%Y-%m-%dT%H:%M:%SZ"
    )