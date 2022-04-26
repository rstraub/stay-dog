__COMPLETED_SESSIONS = 0


def get_session_count():
    print(__get_stored_session_count())
    return __COMPLETED_SESSIONS


# Assumes there is one line in the file containing the number of completed sessions
def __get_stored_session_count():
    file = open(".staydog-sessions", "r")
    stored_session_count = file.readlines()[0].replace("\n", "")
    return stored_session_count


def update_session_count(completed_count):
    file = open(".staydog-sessions", "w")
    file.write(str(completed_count))
    file.close()
    global __COMPLETED_SESSIONS
    __COMPLETED_SESSIONS = completed_count
