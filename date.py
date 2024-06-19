from dateutil import parser
from datetime import datetime
def retrive(date):
    date_obj = parser.parse(date).date()
    formatted_date_str = date_obj.strftime("%d/%m/%Y")
    return formatted_date_str
