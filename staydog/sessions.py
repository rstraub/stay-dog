def next_session_length(passed_session_count):
    return session_lengths()[passed_session_count]


def session_lengths():
    return [1, 2, 4, 8, 16, 24, 32]
