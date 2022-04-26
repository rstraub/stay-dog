__COMPLETED_SESSIONS = 0


def get_session_count():
    return __COMPLETED_SESSIONS


def update_session_count(completed_count):
    global __COMPLETED_SESSIONS
    __COMPLETED_SESSIONS = completed_count
