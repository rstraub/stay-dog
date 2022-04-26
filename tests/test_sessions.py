import pytest

from staydog.session import Session


class TestSession:
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
    def test_session_duration_should_increment_given_12_or_less_completed_sessions(
        self, passed_session_count, expected_minutes
    ):
        assert Session(passed_session_count).duration == expected_minutes

    def test_session_duration_should_remain_five_hours_given_more_than_12_completed_sessions(
        self,
    ):
        assert Session(20).duration == 300

    def test_session_should_return_duration_of_zero_given_no_completed_sessions(self):
        assert Session().duration == 1

    def test_session_should_return_duration_given_completed_sessions(self):
        assert Session(1).duration == 2
