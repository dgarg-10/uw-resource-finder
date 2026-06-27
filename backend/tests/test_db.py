from unittest.mock import MagicMock, patch


class TestGetAllResources:
    @patch("db.get_connection")
    def test_returns_list_of_resources(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, "Odegaard", "library", "South Campus", "Main library", False),
            (2, "Gates Center", "academic", "Central Campus", "CSE building", True),
        ]
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import get_all_resources
        result = get_all_resources()

        assert len(result) == 2
        assert result[0]["name"] == "Odegaard"
        assert result[1]["husky_access"] is True

    @patch("db.get_connection")
    def test_returns_empty_list_when_no_resources(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import get_all_resources
        result = get_all_resources()

        assert result == []

    @patch("db.get_connection")
    def test_resources_ordered_by_name(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, "Allen Library", "library", "Central Campus", "Research library", False),
            (2, "Bagley Hall", "academic", "Central Campus", "Chemistry building", False),
        ]
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import get_all_resources
        result = get_all_resources()

        assert result[0]["name"] == "Allen Library"
        assert result[1]["name"] == "Bagley Hall"


class TestGetResourceById:
    @patch("db.get_connection")
    def test_returns_resource_when_found(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = (1, "Odegaard", "library", "South Campus", "Main library", False)
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import get_resource_by_id
        result = get_resource_by_id(1)

        assert result is not None
        assert result["name"] == "Odegaard"
        assert result["id"] == 1

    @patch("db.get_connection")
    def test_returns_none_when_not_found(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import get_resource_by_id
        result = get_resource_by_id(999)

        assert result is None

    @patch("db.get_connection")
    def test_passes_correct_id_to_query(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = (5, "HUB", "student_center", "Central", "Student union", False)
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import get_resource_by_id
        get_resource_by_id(5)

        mock_cursor.execute.assert_called_once()
        call_args = mock_cursor.execute.call_args
        assert call_args[0][1] == (5,)


class TestGetHoursForResource:
    @patch("db.get_connection")
    def test_returns_seven_days(self, mock_conn):
        from datetime import time
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            ("Monday", time(7, 0), time(23, 0), False),
            ("Tuesday", time(7, 0), time(23, 0), False),
            ("Wednesday", time(7, 0), time(23, 0), False),
            ("Thursday", time(7, 0), time(23, 0), False),
            ("Friday", time(7, 0), time(20, 0), False),
            ("Saturday", time(10, 0), time(18, 0), False),
            ("Sunday", None, None, True),
        ]
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import get_hours_for_resource
        result = get_hours_for_resource(1)

        assert len(result) == 7
        assert result[0]["day_of_week"] == "Monday"
        assert result[6]["is_closed"] is True

    @patch("db.get_connection")
    def test_closed_day_has_null_times(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            ("Sunday", None, None, True),
        ]
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import get_hours_for_resource
        result = get_hours_for_resource(1)

        assert result[0]["open_time"] is None
        assert result[0]["close_time"] is None
        assert result[0]["is_closed"] is True


class TestGetHoursForDay:
    @patch("db.get_connection")
    def test_returns_hours_for_today(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, "Thursday", "07:00", "23:00", False),
            (2, "Thursday", "07:00", "21:00", False),
        ]
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import get_hours_for_day
        result = get_hours_for_day()

        assert len(result) == 2
        assert result[0]["resource_id"] == 1


class TestSearchResources:
    @patch("db.get_connection")
    def test_returns_matching_resources(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, "Odegaard Undergraduate Library", "library", "South Campus", "Main library", False),
        ]
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import search_resources
        result = search_resources("odegaard")

        assert len(result) == 1
        assert result[0]["name"] == "Odegaard Undergraduate Library"

    @patch("db.get_connection")
    def test_returns_empty_for_no_match(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import search_resources
        result = search_resources("nonexistent")

        assert result == []

    @patch("db.get_connection")
    def test_passes_wildcard_query(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import search_resources
        search_resources("ode")

        call_args = mock_cursor.execute.call_args
        assert "%ode%" in call_args[0][1][0]


class TestFavorites:
    @patch("db.get_connection")
    def test_get_favorites_returns_list(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, "Odegaard", "library", "South Campus", "Main library", False),
        ]
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import get_favorites
        result = get_favorites("user_123")

        assert len(result) == 1
        assert result[0]["name"] == "Odegaard"

    @patch("db.get_connection")
    def test_get_favorites_empty_for_new_user(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import get_favorites
        result = get_favorites("user_new")

        assert result == []

    @patch("db.get_connection")
    def test_add_favorite_commits(self, mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import add_favorite
        add_favorite("user_123", 1)

        mock_conn.return_value.commit.assert_called_once()

    @patch("db.get_connection")
    def test_remove_favorite_commits(self, mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import remove_favorite
        remove_favorite("user_123", 1)

        mock_conn.return_value.commit.assert_called_once()

    @patch("db.get_connection")
    def test_add_duplicate_favorite_handles_unique_violation(self, mock_conn):
        import psycopg2
        mock_cursor = MagicMock()
        mock_cursor.execute.side_effect = psycopg2.errors.UniqueViolation()
        mock_conn.return_value.cursor.return_value = mock_cursor

        from db import add_favorite
        add_favorite("user_123", 1)

        mock_conn.return_value.rollback.assert_called_once()