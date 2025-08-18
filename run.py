from mb_question import MB_Question


main_question_list = []

q1 = MB_Question()
q1.question_image = "question1.png"
q1.question_text = "What is 13 + 7 ?"
q1.answer = "20"

main_question_list.append(q1)

q2 = MB_Question()
q2.question_image = "question2.png"
q2.question_text = "You have 5 cakes and you give 2 to your friend.  How many do you have left?"
q2.answer = "3"

main_question_list.append(q2)


q3 = MB_Question()
q3.question_image = "question3.png"
q3.question_text = "What is the area of a square that has 2cm sides?"
q3.answer = "4cm\u00b2"

main_question_list.append(q3)

while len(main_question_list) > 0:
    print(main_question_list.pop())