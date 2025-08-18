class MB_Question():
    def __init__(self):
        self.question_text = ""
        self.question_image = ""
        self.answer = ""

    def __repr__(self):
        return "Question: " + self.question_text + + "\nQuestion Image: " + self.question_image + "\nAnswer: " + self.answer