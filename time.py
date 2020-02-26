import datetime

def get_current_date_time():
    current_date_time = datetime.datetime.now().strftime("%a, %d/%m/%y, %H:%M")
    return (current_date_time)

import datetime

def get_current_date_time():
    current_date_time = datetime.datetime.now().strftime("%a, %d/%m/%y, %H:%M")
    return (current_date_time)

def choose_date_time():
    while True:
        try:
            date = input("Please enter date (DD/MM/YYYY): ")
            day, month, year = (int(x) for x in date.split("/"))
            time = input("Please enter time (e.g. 23:59): ")
            hour, minute = (int(x) for x in time.split(":"))
            chosen_date_time = datetime.datetime(year, month, day, hour, minute).strftime("%a, %d/%m/%y, %H:%M")
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                break
            else:
                print("Please enter a valid time.")
                continue
        except ValueError:
            print("Please enter a valid date/time.")

    return (chosen_date_time)

