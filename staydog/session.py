class Session:
    __session_durations = [
        1,
        2,
        5,
        10,
        15,
        20,
        25,
        30,
        40,
        50,
        60,
        75,
        90,
        105,
        120,
        150,
        180,
        240,
        300,
    ]

    def __init__(self, completed_sessions=0):
        self.duration = self.__next_session_duration(completed_sessions)

    def __next_session_duration(self, passed_session_count):
        durations = self.__session_durations
        if passed_session_count < len(durations):
            return durations[passed_session_count]

        max_duration = durations[len(durations) - 1]
        return max_duration
