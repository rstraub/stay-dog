from sessions import next_session_duration


def main():
    print("Enter amount of successfully completed sessions:")
    successful_sessions = int(input())
    next_session = next_session_duration(successful_sessions)
    print("Next session: " + str(next_session) + " minutes")


if __name__ == "__main__":
    main()
