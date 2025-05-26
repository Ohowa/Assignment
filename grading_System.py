import math

def prompt_names_and_scores() -> tuple[list[str], list[float]]:
    while True:
        try:
            count = int(input("Input the number of students to grade: "))
            if count <= 0:
                print("Input a number greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    names = []
    scores = []

    print("\nEnter student names and their scores:")

    for i in range(count):
        name = input(f"Student {i + 1} name: ").strip()
        if not name:
            name = f"Student{i+1}"
        names.append(name)

        while True:
            try:
                score = float(input(f"Enter score for {name}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
