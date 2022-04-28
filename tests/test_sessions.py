import pytest

from staydog.session import Session


class TestSession:
    @pytest.mark.parametrize(
        "passed_session_count,expected_minutes",
        [
            (0, 1),
            (1, 2),
            (2, 5),
            (3, 10),
            (4, 15),
            (5, 20),
            (6, 25),
            (7, 30),
            (8, 40),
            (9, 50),
            (10, 60),
            (11, 75),
            (12, 90),
            (13, 105),
            (14, 120),
            (15, 150),
            (16, 180),
            (17, 240),
            (18, 300),
        ],
    )
    def test_session_duration_should_increment_given_less_than_five_hours(
        self, passed_session_count, expected_minutes
    ):
        assert Session(passed_session_count).duration == expected_minutes

    def test_session_duration_should_remain_five_hours_given_more_than_five_hours(
        self,
    ):
        assert Session(20).duration == 300

    def test_session_should_return_duration_of_zero_given_no_completed_sessions(self):
        assert Session().duration == 1

    def test_session_should_return_duration_given_completed_sessions(self):
        assert Session(1).duration == 2
