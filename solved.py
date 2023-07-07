import sys
from datetime import datetime

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]

dayOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def mark_solved(problem_num: int):
    today = datetime.now()
    day = dayOfWeek[today.weekday()]
    month = months[today.month - 1]
    date = today.day
    year = today.year
    today_formatted = f"{day}, {month} {date}, {year}"
    with open("README.md", "a") as file:
        file.write(f"{today_formatted} - Solved #{problem_num}\n\n")
        file.close()

if __name__ == "__main__":
    if type(int(sys.argv[1])) is int:
        mark_solved(int(sys.argv[1]))
    else:
        print("Enter an integral problem number")