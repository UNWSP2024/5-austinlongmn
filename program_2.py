# Programmer: Austin Long
# Date: 2/20/25
# Program: Math Quiz

# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

# import necessary modules
import sys
import random
import argparse


def check_user_input(correct_answer: int) -> bool:
    """This function checks whether the user enters correct_answer."""
    try:
        # The two spaces are to pad the plus sign in the problem.
        user_input = int(input("  "))
        return user_input == correct_answer
    except ValueError:
        print("Error: you must enter an integer.", file=sys.stderr)
        return check_user_input(correct_answer)


def display_question(lhs_addend: int, rhs_addend: int, max_num: int):
    """This function displays an addition problem of `lhs_addend + rhs_addend`.
    `max_num` is used for padding."""
    lhs_addend_str = str(lhs_addend)
    rhs_addend_str = str(rhs_addend)

    # The max length a number in the problem could be is if it was max_num + max_num,
    # or max_num * 2.
    max_len = len(str(max_num * 2))
    padding_len = max_len + 2

    # Justify strings for proper formatting
    lhs_addend_str = lhs_addend_str.rjust(padding_len)
    rhs_addend_str = rhs_addend_str.rjust(max_len)
    print(f"{lhs_addend_str}\n+ {rhs_addend_str}\n{'-' * padding_len}")


def ask_question(max_num: int, min_num: int, instant_feedback: bool) -> bool:
    """Asks the addition question and returns whether the user got it right."""

    # Get random numbers
    lhs_addend = random.randrange(min_num, max_num)
    rhs_addend = random.randrange(min_num, max_num)

    display_question(lhs_addend, rhs_addend, max_num)

    # Calculate correct answer
    correct_answer = lhs_addend + rhs_addend

    user_correct = check_user_input(correct_answer)

    # Display feedback (if desired)
    if instant_feedback:
        if user_correct:
            print("Correct! Great job!")
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.")

    return user_correct


def main():
    parser = argparse.ArgumentParser(prog="mathquiz", description="A program to test your math skills.")
    parser.add_argument("-m", "--max-num", type=int, default=100, help="The max number to add (exclusive)")
    parser.add_argument("-n", "--min-num", type=int, default=0,   help="The min number to add (inclusive)")
    parser.add_argument("-l", "--quiz-length", type=int, default=5,   help="The length of the quiz")
    parser.add_argument("--instant-feedback", default=True, action=argparse.BooleanOptionalAction, help="Display feedback after every question.")

    arguments = parser.parse_args()

    quiz_length = arguments.quiz_length
    num_correct = 0
    # Loop quiz_length times
    for i in range(quiz_length):
        print(f"Question {i+1}:")
        try:
            if ask_question(arguments.max_num, arguments.min_num, arguments.instant_feedback):
                num_correct += 1
        except EOFError:
            print("Quitter!", file=sys.stderr)
            exit(0)
        except KeyboardInterrupt:
            print("Quitter!", file=sys.stderr)
            exit(0)
    
    # Print score
    score = num_correct / quiz_length
    message = "Great job!" if score >= 0.8 else "Hmm. More practice, you need. Use the force, you must."
    print(f"{message}\nYou got {num_correct} out of {quiz_length}. That's {num_correct/quiz_length:.0%}.")


# Run the program
if __name__ == "__main__":
    main()
