class MB_Question():
    def __init__(self):
        self.question = ""
        self.answer = ""

    def __repr__(self):
        return "Question: " + self.question + "\nAnswer: " + self.answer


q1 = MB_Question()
q1.question = "What is 13 + 7 ?"
q1.answer = "20"

print(q1)