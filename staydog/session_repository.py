__SESSIONS_FILE = ".staydog-sessions"


def get_session_count():
    file = open(__SESSIONS_FILE, "r")
    stored_session_count = file.readlines()[0].replace("\n", "")
    return stored_session_count


# Assumes there is one line in the file containing the number of completed sessions


def update_session_count(completed_count):
    file = open(__SESSIONS_FILE, "w")
    file.write(str(completed_count))
    file.close()
