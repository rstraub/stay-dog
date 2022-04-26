from sessions import next_session_length


def main():
    print("Enter amount of successful sessions:")
    successful_sessions = int(input())
    next_session = next_session_length(successful_sessions)
    print("Next session: " + str(next_session) + " minutes")


if __name__ == "__main__":
    main()
