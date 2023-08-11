from datetime import datetime

from services.questions import Question

# CONSTANTS

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
        """Append `text` to the specified file at `path`

        Args:
            path (str): Relative path to the file
            text (str): Text to append
        """
        with open(path, "a") as file:
            file.write(text)
            file.close()

    def get_formatted_date(
        y = datetime.now().year,
        m = datetime.now().month,
        d = datetime.now().day,
    ) -> str:
        """Returns the specified date in the format '<day>, <month> <date> <year>'

        Args:
            y (int, optional): Custom year. Defaults to datetime.now().year.
            m (int, optional): Custom month. Defaults to datetime.now().month.
            d (int, optional): Custom day. Defaults to datetime.now().day.

        Returns:
            str: Formatted date
        """
        desired_date = datetime(y, m, d)
        day = dayOfWeek[desired_date.weekday()]
        month = months[m - 1]

        return f"{day}, {month} {d}, {y}"

    def get_problem_link(question: Question) -> str:
        """Generate an HTML <a/> tag that links to the LC question

        Args:
            question (Question): LC question

        Returns:
            str: HTML <a/> tag that links to the LC question
        """
        problem_url = base_url + question.titleSlug
        hyperlink_text = f"#{question.id} - {question.title}"

        return f'<a href="{problem_url}">{hyperlink_text}</a>'

    def generate_message(
        attempted: bool, 
        solved_q: Question,
    ) -> str:
        """Generate and return a message indicating that `solved_q` was solved

        Args:
            attempted (bool): Whether or not this is a re-attempt
            solved_q (Question): Question solved

        Returns:
            str: Message indicating that `solved_q` was solved
        """
        date_formatted = FileWriterService.get_formatted_date()
        hyperlink = FileWriterService.get_problem_link(solved_q)

        difficulty_emoji = diff_emojis[solved_q.difficulty.lower()]
        action = "REATTEMPTED" if attempted else "Solved"

        return f"\n{difficulty_emoji} {date_formatted}: {action} {hyperlink}\n"

    def mark_as_retry(question: Question):
        """Add `question` to the retry list

        Args:
            question (Question): Question to retry
        """
        days_offset = 3
        diff_emoji = diff_emojis[question.difficulty.lower()]
        date = FileWriterService.get_formatted_date(d=datetime.now().day + days_offset)
        hyperlink = FileWriterService.get_problem_link(question)

        msg_to_append = f"\n{diff_emoji} On {date}, redo: {hyperlink}\n"

        FileWriterService.append_to_file("RETRY.md", msg_to_append)
        print(f"Do problem #{question.title} again in {days_offset} days!")

    def mark_solved(question: Question, attempted: bool):
        """Mark a question as solved

        Args:
            question (Question): Question solved
            attempted (bool): Whether or not this was a re-attempt
        """
        msg_to_append = FileWriterService.generate_message(attempted, question)

        FileWriterService.append_to_file("README.md", msg_to_append)
        print("Recorded!", msg_to_append)