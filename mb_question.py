class MB_Question():
    def __init__(self):
        self.question_text = ""
        self.question_image = ""
        self.answer = ""

    def __repr__(self):
        return "\nQuestion Image: " + self.question_image + "\nQuestion: " + self.question_text  + "\nAnswer: " + self.answer