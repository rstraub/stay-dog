from session_repository import get_session_count, update_session_count
from sessions import next_session_duration


def main():
    successful_sessions = get_session_count()
    print(f"Completed sessions so far: {successful_sessions}")

    session_duration = next_session_duration(int(successful_sessions))
    print(f"Did the dog stay alone successfully for {session_duration} minutes? (y/n)")

    y_or_n = input()
    if y_or_n == "n":
        print("Too bad, next session will be shorter")
        update_session_count(successful_sessions - 1)
    elif y_or_n == "y":
        print("Great! Next session will be longer")
        update_session_count(successful_sessions + 1)
    else:
        print("Please enter 'y' or 'n'")


if __name__ == "__main__":
    main()
