import json
import sys
from datetime import datetime

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]

dayOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def mark_solved(problem_num: dict):
    today = datetime.now()
    day = dayOfWeek[today.weekday()]
    month = months[today.month - 1]
    date = today.day
    year = today.year

    today_formatted = f"{day}, {month} {date}, {year}"
    solved_msg = f"Solved #{problem_num['id']} - {problem_num['title']}"
    msg_to_append = f"\n{today_formatted}: {solved_msg}\n"

    with open("README.md", "a") as file:
        file.write(msg_to_append)
        file.close()
        print("Recorded!", msg_to_append)

if __name__ == "__main__":
    try:
        json_file = open("problems.json")

        questions_hash_table = json.load(json_file)
        question = questions_hash_table[sys.argv[1]]
        mark_solved(question)
        
        json_file.close()
    except:
        print("Enter an integral problem number")