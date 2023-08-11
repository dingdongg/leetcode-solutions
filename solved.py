from aifc import Error
import sys
from services.attempted import AttemptedService
from services.file_writer import FileWriterService
from services.questions import QuestionsService

if __name__ == "__main__":
    try:
        index = int(sys.argv[1])

        attempted_service = AttemptedService()
        questions_service = QuestionsService()

        question = questions_service.get_question(index)
        attempted = attempted_service.was_attempted(index)

        FileWriterService.mark_solved(question, attempted)

        if not attempted:
            retry = input("Re-try the problem another time? (y/n)\n")
            if retry == "y": FileWriterService.mark_as_retry(question)

        attempted_service.mark_as_attempted(index)
    except Error as e:
        print(e)
        print("Enter an integral problem number")