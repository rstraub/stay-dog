class Session:
    def __init__(self, completed_sessions=0):
        self.duration = self.__next_session_duration(completed_sessions)

    def __next_session_duration(self, passed_session_count):
        durations = self.__session_durations()
        if passed_session_count < len(durations):
            return durations[passed_session_count]

        max_duration = durations[len(durations) - 1]
        return max_duration

    def __session_durations(self):
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
