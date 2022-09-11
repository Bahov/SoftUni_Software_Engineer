
from math import floor

number_of_pages = int(input())
pages_per_hour = int(input())
req_days_per_book = int(input())

req_hours_per_day = (number_of_pages/req_days_per_book)/pages_per_hour

print(floor(req_hours_per_day))
