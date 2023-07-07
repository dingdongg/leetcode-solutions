import json
import sys
from datetime import datetime

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]

dayOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

base_url = "https://leetcode.com/problems/"

diff_emojis = {
    "easy": "🟢",
    "medium": "🟠",
    "hard": "🔴",
}

def mark_solved(problem: dict):
    today = datetime.now()
    day = dayOfWeek[today.weekday()]
    month = months[today.month - 1]
    date = today.day
    year = today.year

    today_formatted = f"{day}, {month} {date}, {year}"
    problem_url = base_url + problem['titleSlug']
    hyperlink_text = f"#{problem['id']} - {problem['title']}"
    hyperlink = f'<a href="{problem_url}">{hyperlink_text}</a>'
    difficulty_emoji = diff_emojis[problem["difficulty"].lower()]

    msg_to_append = f"\n{difficulty_emoji} {today_formatted}: Solved {hyperlink}\n"

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