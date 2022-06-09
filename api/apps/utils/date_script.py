from datetime import datetime

def format_date_actual_for_file():
    return str(datetime.now().date()).replace('-', '/')

def date_actual():
    return datetime.now().date()