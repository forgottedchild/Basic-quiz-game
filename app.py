def quiz_app():
    questions = {
        "What is the capital of India?": "a",
        "Which planet is known as the Red Planet?": "b",
        "What is the largest ocean on Earth?": "c"
    }
    options = [
        {"a": "New Delhi", "b": "Mumbai", "c": "Kolkata"},
        {"a": "Earth", "b": "Mars", "c": "Jupiter"},
        {"a": "Atlantic", "b": "Arctic", "c": "Pacific"}
    ]
    score = 0
    for i, (question, correct) in enumerate(questions.items()):
        print(f"\nQ{i+1}: {question}")
        for key, value in options[i].items():
            print(f"  {key}. {value}")
        answer = input("Your answer: ").lower()
        if answer == correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct}.")
    print(f"\nYou scored {score}/{len(questions)}")

quiz_app()
