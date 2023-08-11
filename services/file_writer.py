from datetime import datetime

from services.questions import Question

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

class FileWriterService:
    def append_to_file(path: str, text: str):
        with open(path, "a") as file:
            file.write(text)
            file.close()

    def get_formatted_date(
        y = datetime.now().year,
        m = datetime.now().month,
        d = datetime.now().day,
    ) -> str:
        desired_date = datetime(y, m, d)
        day = dayOfWeek[desired_date.weekday()]
        month = months[m - 1]

        return f"{day}, {month} {d}, {y}"

    def get_problem_link(question: Question) -> str:
        problem_url = base_url + question.titleSlug
        hyperlink_text = f"#{question.id} - {question.title}"

        return f'<a href="{problem_url}">{hyperlink_text}</a>'

    def generate_message(
        attempted: bool, 
        solved_q: Question,
    ) -> str:
        date_formatted = FileWriterService.get_formatted_date()
        hyperlink = FileWriterService.get_problem_link(solved_q)

        difficulty_emoji = diff_emojis[solved_q.difficulty.lower()]
        action = "REATTEMPTED" if attempted else "Solved"

        return f"\n{difficulty_emoji} {date_formatted}: {action} {hyperlink}\n"

    def mark_as_retry(question: Question):
        days_offset = 3
        diff_emoji = diff_emojis[question.difficulty.lower()]
        date = FileWriterService.get_formatted_date(d=datetime.now().day + days_offset)
        hyperlink = FileWriterService.get_problem_link(question)

        msg_to_append = f"\n{diff_emoji} On {date}, redo: {hyperlink}\n"

        FileWriterService.append_to_file("RETRY.md", msg_to_append)
        print(f"Do problem #{question.title} again in {days_offset} days!")

    def mark_solved(question: Question, attempted: bool):
        msg_to_append = FileWriterService.generate_message(attempted, question)

        FileWriterService.append_to_file("README.md", msg_to_append)
        print("Recorded!", msg_to_append)