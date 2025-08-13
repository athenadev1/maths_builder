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

q2 = MB_Question()
q2.question = "You have 5 cakes and you give 2 to your friend.  How many do you have left?"
q2.answer = "2"

print(q2)

q3 = MB_Question()
q3.question = "What is the area of a square that has 2cm sides?"
q3.answer = "4cm\u00b2"

print(q3)
