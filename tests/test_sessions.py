from staydog.sessions import next_session_length


class TestSessions:
    def test_first_session_should_be_one_minute(self):
        result = next_session_length(0)
        assert result == 1

    def test_second_session_should_be_two_minutes(self):
        result = next_session_length(1)
        assert result == 2

    def test_third_session_should_be_four_minutes(self):
        result = next_session_length(2)
        assert result == 4
