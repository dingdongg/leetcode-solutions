from aifc import Error
import sys
from datetime import datetime
from scripts.attempted import AttemptedService
from scripts.questions import Question, QuestionsService

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

def mark_solved(question: Question, attempted: bool):
    today = datetime.now()
    day = dayOfWeek[today.weekday()]
    month = months[today.month - 1]
    date = today.day
    year = today.year

    today_formatted = f"{day}, {month} {date}, {year}"
    problem_url = base_url + question.titleSlug
    hyperlink_text = f"#{question.id} - {question.title}"
    hyperlink = f'<a href="{problem_url}">{hyperlink_text}</a>'
    difficulty_emoji = diff_emojis[question.difficulty.lower()]

    action = "REATTEMPTED" if attempted else "Solved"

    msg_to_append = f"\n{difficulty_emoji} {today_formatted}: {action} {hyperlink}\n"

    with open("README.md", "a") as file:
        file.write(msg_to_append)
        file.close()
        print("Recorded!", msg_to_append)

if __name__ == "__main__":
    try:
        index = int(sys.argv[1])

        attempted_service = AttemptedService()
        questions_service = QuestionsService()

        mark_solved(
            questions_service.get_question(index), 
            attempted_service.was_attempted(index),
        )

        attempted_service.mark_as_attempted(index)
    except Error as e:
        print(e)
        print("Enter an integral problem number")