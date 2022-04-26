from session import next_session_duration
from session_repository import get_session_count, update_session_count


def main():
    successful_sessions = get_session_count()
    print(f"Successful sessions alone so far: {successful_sessions}")

    session_duration = next_session_duration(int(successful_sessions))
    print(
        f"Was the dog stay alone successfully for {session_duration} minute(s)? (y/n)"
    )

    y_or_n = input()
    if y_or_n == "n":
        if successful_sessions > 0:
            successful_sessions = successful_sessions - 1
        update_session_count(successful_sessions)
        next_duration = next_session_duration(successful_sessions)
        print(f"Too bad, next session will be {next_duration} minute(s)")
    elif y_or_n == "y":
        successful_sessions = successful_sessions + 1
        update_session_count(successful_sessions)
        next_duration = next_session_duration(successful_sessions)
        print(f"Great! Next session will be {next_duration} minute(s)")
    else:
        print("Please enter 'y' or 'n'")


if __name__ == "__main__":
    main()
