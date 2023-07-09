import json

class Question:
    def __init__(self, difficulty: str, id: str, title: str, titleSlug: str):
        self.difficulty = difficulty
        self.id = id
        self.title = title
        self.titleSlug = titleSlug
    
    def __init__(self, q: dict[str]):
        self.difficulty = q["difficulty"]
        self.id = q["frontendQuestionId"]
        self.title = q["title"]
        self.titleSlug = q["titleSlug"]

class QuestionsService:
    def __init__(self, file_path = "questions.json"):
        self.questions: list(Question) = []
        self.file_path = file_path
    
    def get_questions(self) -> list[Question]:
        """
        get list of leetcode questions
        """
        questions_file = open(self.file_path)
        self.questions = json.load(questions_file)
        questions_file.close()

        return self.questions
    
    def get_question(self, questionId: int) -> Question:
        """
        get a leetcode question by ID
        """
        if not self.questions: self.get_questions()
        return Question(self.questions[questionId])