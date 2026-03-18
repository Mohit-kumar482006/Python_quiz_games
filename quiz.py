# 🎯 Simple Quiz Game (Beginner Friendly)

# This function asks one question
def ask_question(question, options, correct_answer):
    print("\n" + question)  # show the question
    
    # show all options (a, b, c, d)
    for key in options:
        print(key + ")", options[key])
    
    # take input from user
    user_answer = input("Enter your answer (a/b/c/d): ").lower()
    
    # check if answer is correct
    if user_answer == correct_answer:
        print("Correct!")
        return 1   # return 1 point
    else:
        print("Wrong answer!")
        print("Correct answer was:", correct_answer)
        return 0   # return 0 points


# Main program starts here
print("Welcome to Quiz Game!")
print("----------------------")

score = 0  # keeps track of score

# Question 1
q1_options = {
    "a": "Paris",
    "b": "London",
    "c": "Berlin",
    "d": "Rome"
}
score += ask_question("What is the capital of France?", q1_options, "a")

# Question 2
q2_options = {
    "a": "Java",
    "b": "Python",
    "c": "C++",
    "d": "Ruby"
}
score += ask_question("Which language is used to create this game?", q2_options, "b")

# Question 3
q3_options = {
    "a": "Central Processing Unit",
    "b": "Computer Personal Unit",
    "c": "Central Performance Utility",
    "d": "Computer Processing Unit"
}
score += ask_question("What does CPU stand for?", q3_options, "a")

# Question 4
q4_options = {
    "a": "Earth",
    "b": "Mars",
    "c": "Jupiter",
    "d": "Venus"
}
score += ask_question("Which planet is called the Red Planet?", q4_options, "b")

# Question 5
q5_options = {
    "a": "integer",
    "b": "string",
    "c": "list",
    "d": "All of the above"
}
score += ask_question("Which is a Python data type?", q5_options, "d")

# Final score
print("\nYour final score is:", score, "/ 5")