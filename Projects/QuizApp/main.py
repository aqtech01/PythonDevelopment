import Lib.Quiz as quiz


def main():
    while True:
        quiz.main_selection()
        sm = int(input("Select Menu:- "))
        match sm:
            case 1:
                print(quiz.view_all_questions())


if __name__ == "__main__":
    main()
