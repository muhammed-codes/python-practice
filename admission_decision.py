# Admission Decision Maker

name = input("Enter your name: ")
subjectCombination = input("Enter your subject combination (e.g., Math, Science, English): ")
firstSubject = float(input("Enter your first subject score: "))
secondSubject = float(input("Enter your second subject score: "))
thirdSubject = float(input("Enter your third subject score: "))
fourthSubject = float(input("Enter your fourth subject score: "))

jamboreeScore = (firstSubject + secondSubject + thirdSubject + fourthSubject) 

courseChoices = ["Engineering", "Medicine", "Law", "Business", "Arts", "Computer Science"]

userCourseChoice = input(f"Enter your preferred course from the following options: {', '.join(courseChoices)}: ")

if userCourseChoice == "Engineering" and jamboreeScore >= 300:
    print(f"Congratulations {name}! You have been admitted to Engineering with a score of {jamboreeScore}.")
elif userCourseChoice == "Medicine" and jamboreeScore >= 280:
    print(f"Congratulations {name}! You have been admitted to Medicine with a score of {jamboreeScore}.")
elif userCourseChoice == "Law" and jamboreeScore >= 260:
    print(f"Congratulations {name}! You have been admitted to Law with a score of {jamboreeScore}.")
elif userCourseChoice == "Business" and jamboreeScore >= 240:
    print(f"Congratulations {name}! You have been admitted to Business with a score of {jamboreeScore}.")
elif userCourseChoice == "Arts" and jamboreeScore >= 220:
    print(f"Congratulations {name}! You have been admitted to Arts with a score of {jamboreeScore}.")
elif userCourseChoice == "Computer Science" and jamboreeScore >= 250:
    print(f"Congratulations {name}! You have been admitted to Computer Science with a score of {jamboreeScore}.")
else:
    print(f"Sorry {name}, you have not met the admission criteria for {userCourseChoice}. Your score of {jamboreeScore} is insufficient.")