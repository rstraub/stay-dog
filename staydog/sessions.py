def next_session_length(passed_session_count):
    if passed_session_count == 1:
        return 2
    if passed_session_count == 2:
        return 4
    if passed_session_count == 3:
        return 8
    if passed_session_count == 4:
        return 16
    return 1
