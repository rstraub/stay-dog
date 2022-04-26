from session_repository import get_session_count
from sessions import next_session_duration


def main():
    successful_sessions = get_session_count()
    print("Completed sessions so far: " + successful_sessions)

    next_session = next_session_duration(int(successful_sessions))
    print("Next session: " + str(next_session) + " minute(s)")


if __name__ == "__main__":
    main()
