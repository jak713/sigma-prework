#!/usr/bin/env python3

from datetime import datetime
import sys

today = datetime.today()
print(f"Today's date: {today.day}-{today.month}-{today.year}")

try:
    argument = sys.argv[1]
    date = datetime.strptime(argument, "%d-%m-%Y")
    print(f"DOB given: {date.day}-{date.month}-{date.year}")
    timedelta = today - date
    print(f"Age: {int(timedelta.days/365.25)}")

except Exception as error:
    print(f"This script requires an argument of DOB in the form DD-MM-YYYY.\nError: {error}")


# Alternatively this should also work:
#age = (today.year - date.year) if (today.month - date.month > 0) or (today.month == date.month and  today.day - date.day >= 0) else (today.year - date.year - 1)