import pytest

from staydog.sessions import next_session_length


class TestSessions:
    @pytest.mark.parametrize(
        "passed_session_count,expected_minutes",
        [(0, 1), (1, 2), (2, 4), (3, 8), (4, 16)],
    )
    def test_next_session_length_should_double_given_16_minutes_or_less(
        self, passed_session_count, expected_minutes
    ):
        assert next_session_length(passed_session_count) == expected_minutes
