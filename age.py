#!/usr/bin/env python3

from datetime import datetime
import sys

def print_results(today, date):
    print(f"Today's date: {today.day}-{today.month}-{today.year}")
    print(f"DOB given: {date.day}-{date.month}-{date.year}")
    age = int(timedelta.days/365.25)

    if age < 120:
        print(f"Age: {age}")
    else:
        print(f"Either there is a vampire among us, or something is wrong with your input.\nAge: {age}")

# Gather necessary arguments first, if at any point this fails, the program states the error and gracefully exits.
try:
    today = datetime.today()

    argument = sys.argv[1]
    date = datetime.strptime(argument, "%d-%m-%Y")
    if date > today:
        raise ValueError(f"Date ({date}) is invalid - given date cannot be in the future.")
    
    timedelta = today - date

    print_results(today, date)

except IndexError:
    print(f"This script requires an argument: Date of birth in the format DD-MM-YYYY.\n example: ./age.py 01-01-2001")
except ValueError as error:
    print(f"There is an issue with your input: {error}")