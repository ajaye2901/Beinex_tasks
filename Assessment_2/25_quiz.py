print("   Quiz Game  ")

score = 0

ques_1 = input("Who is Lionel Messi?\n"
               "1. Politician\n"
               "2. Footballer\n"
               "3. Singer\n"
               "4. Cricketer\n"
               "Choose an option: ")

if ques_1 == '2':
    print("Congratulations! Correct answer.")
    score += 1
else:
    print("Oops! Wrong answer. correct answer is Footballer.")

print()

ques_2 = input("Who invented Python?\n"
               "1. George Russell\n"
               "2. Bill Gates\n"
               "3. Sam Altmann\n"
               "4. Guido van Rossum\n"
               "Choose an option: ")

if ques_2 == '4':
    print("Congratulations! Correct answer.")
    score += 1
else:
    print("Oops! Wrong answer. correct answer is Guido van Rossum.")

ques_3 = input("Which planet is known as red planet?\n"
               "1. Mars\n"
               "2. Venus\n"
               "3. Earth\n"
               "4. Saturn\n"
               "Choose an option: ")
if ques_3 == '1':
    print("Congratulations! Correct answer.")
    score += 1
else:
    print("Oops! Wrong answer. correct answer is Mars")

ques_4 = input("Who developed Theory of Relativity?\n"
               "1. Isaac Newton\n"
               "2. Galileo Galieli\n"
               "3. Edwin Hubble\n"
               "4. Albert Einstein\n"
               "Choose an option: ")
if ques_4 == '4':
    print("Congratulations! Correct answer.")
    score += 1
else:
    print("Oops! Wrong answer. correct answer is Albert Einstein")

ques_5 = input("What is the largest planet in our solar system?\n"
               "1. Jupiter\n"
               "2. Uranus\n"
               "3. Saturn\n"
               "4. Mars\n"
               "Choose an option: ")
if ques_5 == '1':
    print("Congratulations! Correct answer.")
    score += 1
else:
    print("Oops! Wrong answer. correct answer is Jupiter")


print("Quizz done")
print("Your Scored :", score)
