import json

class AttemptedService:
    def __init__(self, file_path = "attempted.json"):
        self.file_path = file_path
        self.attempted = []
        self.attempted = self.get_attempted()

    def get_attempted(self) -> list:
        """
        return a list of attempted problem IDs
        """
        if self.attempted: return self.attempted

        attempted_file = open(self.file_path, "r")
        attempted = json.load(attempted_file)
        attempted_file.close()  
        
        return attempted

    def mark_as_attempted(self, problemId: int) -> None:
        """
        mark a question as attempted. Returns true if succesful, false otherwise
        """
        if not self.was_attempted(problemId): 
            attempted_file = open(self.file_path, "w")
            self.attempted.append(problemId)
            attempted_file.write(json.dumps(self.attempted, indent=4))
            attempted_file.close()
    
    def was_attempted(self, problemId: int) -> bool:
        """
        return True if the problem was already attempted,
        False otherwise
        """
        return problemId in self.attempted