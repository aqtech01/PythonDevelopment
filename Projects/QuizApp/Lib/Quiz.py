import json


def load_data():
    with open("Data/questions.json") as files:
        question = json.load(files)
        return question


def main_selection():
    print("""
        <---- Select Menu ---->
            1. Print all questions
            2. Print a question given id
            3. Add a new question
            4. Delete a question given id
            5. Shuffle questions
            6. Take quiz
            8. Exit
""")


questions = load_data()


def view_all_questions():
    count = 0

    for question in questions:
        count += 1
        statement = question["statement"]
        print(f"Q.No: {count} {statement}")
        option = question["options"]
        for options in option:
            print(options)


def view_questions_id():
    si = int(input("Enter Question Id"))
    count = 0
    for question in questions:
        count += 1
        statement = question["statement"]
        print(f"Q.No: {count} {statement}")
        option = question["options"]
        for options in option:
            print(options)
