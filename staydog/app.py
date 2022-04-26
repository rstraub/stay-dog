from session_repository import get_session_count
from sessions import next_session_duration


def main():
    successful_sessions = get_session_count()
    print("Completed sessions so far: " + successful_sessions)

    next_session = next_session_duration(int(successful_sessions))
    print(f"Did the dog stay alone successfully for {next_session} minutes? (y/n)")

    y_or_n = input()
    if y_or_n == "n":
        print("Too bad, next session will be shorter")
    elif y_or_n == "y":
        print("Great! Next session will be longer")
    else:
        print("Please enter 'y' or 'n'")


if __name__ == "__main__":
    main()
