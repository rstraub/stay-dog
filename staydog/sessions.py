def next_session_duration(passed_session_count):
    durations = __session_durations()
    if passed_session_count < len(durations):
        return durations[passed_session_count]

    max_duration = durations[len(durations) - 1]
    return max_duration


def __session_durations():
    max_session_duration = 5 * 60
    longest_session = 1
    result = []

    while longest_session < max_session_duration:
        if longest_session < 16:
            longest_session = 2 ** len(result)
        else:
            longest_session = longest_session + int(longest_session / 2)
        if longest_session > max_session_duration:
            longest_session = max_session_duration
        result.append(longest_session)

    return result
