__SESSIONS_FILE = ".staydog-sessions"


def get_session_count():
    try:
        contents = open(__SESSIONS_FILE).readline()
        stored_session_count = int(contents.replace("\n", ""))
        return stored_session_count
    except IOError:
        print("No previous sessions found")
        return 0
    except ValueError:
        print("Corrupt session file found, creating a new one...")
        return 0


# Assumes there is one line in the file containing the number of completed sessions


def update_session_count(completed_count):
    file = open(__SESSIONS_FILE, "w+")
    file.write(str(completed_count))
    file.close()
