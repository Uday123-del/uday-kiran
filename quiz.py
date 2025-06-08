quiz_data = {
    "What is the capital of France?": (["Berlin", "Madrid", "Paris", "Rome"], 2),
    "Which planet is known as the Red Planet?": (["Earth", "Mars", "Jupiter", "Venus"], 1),
    "Who wrote 'Hamlet'?": (["Mark Twain", "William Shakespeare", "Charles Dickens", "J.K. Rowling"], 1),
    "What is the largest ocean on Earth?": (["Atlantic", "Indian", "Arctic", "Pacific"], 3)
}

score = 0

# Function to run the quiz
def run_quiz():
    global score
    for question, (options, correct_index) in quiz_data.items():
        print("\n" + question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        # Get user input
        try:
            user_choice = int(input("Enter the number of your answer: ")) - 1
            if user_choice == correct_index:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer is {options[correct_index]}.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    print(f"\nYour final score: {score}/{len(quiz_data)}")

# Run the quiz
run_quiz()
