def next_session_length(passed_session_count):
    if passed_session_count == 1:
        return 2
    if passed_session_count == 2:
        return 4
    return 1
