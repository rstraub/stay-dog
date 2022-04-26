import pytest

from staydog.session import next_session_duration


class TestSessions:
    @pytest.mark.parametrize(
        "passed_session_count,expected_minutes",
        [
            (0, 1),
            (1, 2),
            (2, 4),
            (3, 8),
            (4, 16),
            (5, 24),
            (6, 36),
            (7, 54),
            (8, 81),
            (9, 121),
            (10, 181),
            (11, 271),
        ],
    )
    def test_next_session_duration_should_increment_given_less_than_five_hours(
        self, passed_session_count, expected_minutes
    ):
        assert next_session_duration(passed_session_count) == expected_minutes

    def test_next_sessions_duration_should_remain_five_hours_given_more_than_12_sessions(
        self,
    ):
        assert next_session_duration(20) == 300
