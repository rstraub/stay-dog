from staydog.sessions import next_session_length


class TestSessions:
    def test_first_session_should_be_one_minute(self):
        result = next_session_length()
        assert result == 1
