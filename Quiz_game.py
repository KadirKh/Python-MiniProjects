# Defining the questions and answers with list of dictionaries.
quiz_data = [
    {
        "question": "When was python first released?",
        "options": ["A) 1972", "B) 1988", "C) 1980", "D) 1990"],
        "answer": "C"
    },
    {
        "question": "Who is the creator of python?",
        "options": ["A) Guido van Rossum", "B) Dennis Ritchie", "C) James Gosling", "D) Bjarne Stroustrup"],
        "answer": "A"
    },
    {
        "question": "Which of the following is the correct extension for Python files?",
        "options": ["A) .pt", "B) .pn", "C) .pyth", "D ) .py"],
        "answer": "D"
    },
    {
        "question": "What is the data type of print(type({})) in Python?",
        "options": ["A) set", "B) dictionary", "C) list", "D) None of the mentioned"],
        "answer": "B"
    },
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "options": ["A) {}", "B) ()", "C) indentation", "D) none of the mentioned"],
        "answer": "C"
    }
]


def display_question(question_data):
    """Display a single question and its options."""
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)


def get_user_answer():
    """Get the user's answer and validate it."""
    answer = input("Your answer (A, B, C, or D): ").strip().upper()
    while answer not in ["A", "B", "C", "D"]:
        print("Invalid answer. Please choose A, B, C, or D.")
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
    return answer


def run_quiz(quiz_data):
    """Run the quiz game."""
    score = 0
    total_questions = len(quiz_data)

    for question_data in quiz_data:
        display_question(question_data)
        user_answer = get_user_answer()

        if user_answer == question_data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question_data['answer']}.\n")

    print(f"You scored {score} out of {total_questions}.")


print("Welcome to the Quiz Game!")
run_quiz(quiz_data)
print("Thank you for playing!")