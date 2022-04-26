import pytest

from staydog.sessions import next_session_duration


class TestSessions:
    @pytest.mark.parametrize(
        "passed_session_count,expected_minutes",
        [(0, 1), (1, 2), (2, 4), (3, 8), (4, 16), (5, 24), (6, 36), (7, 54), (8, 81), (9, 121), (10, 181), (11, 271),
         (12, 300)],
    )
    def test_next_session_duration_should_return_duration_given_passed_sessions(
            self, passed_session_count, expected_minutes
    ):
        assert next_session_duration(passed_session_count) == expected_minutes
