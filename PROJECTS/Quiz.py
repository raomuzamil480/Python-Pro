# Quiz Program using List and Tuple

questions = [
    "What is the capital of Pakistan?",
    "How many continents are there?",
    "Python kis type ki language hai?"
]

options = [
    ("A. Lahore", "B. Islamabad", "C. Karachi", "D. Multan"),
    ("A. 5", "B. 6", "C. 7", "D. 8"),
    ("A. Programming", "B. Game", "C. Browser", "D. OS")
]

answers = ["B", "C", "A"]

score = 0

for i in range(len(questions)):
    print("\n" + questions[i])

    for option in options[i]:
        print(option)

    user = input("Enter Answer (A/B/C/D): ").upper()

    if user == answers[i]:
        print("Correct ")
        score += 1
    else:
        print("Wrong ")

print(f"\nYour Final Score = {score}/{len(questions)}")