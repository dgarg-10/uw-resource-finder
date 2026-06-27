from unittest.mock import patch, MagicMock


class TestGetRecommendation:
    @patch("recommend.client")
    @patch("recommend.get_hours_for_day")
    @patch("recommend.get_all_resources")
    def test_returns_recommendation_text(self, mock_resources, mock_hours, mock_client):
        mock_resources.return_value = [
            {
                "id": 1,
                "name": "Odegaard",
                "type": "library",
                "location": "South Campus",
                "description": "Main library",
                "husky_access": False
            },
        ]
        mock_hours.return_value = [
            {
                "resource_id": 1,
                "is_closed": False,
                "open_time": "07:00",
                "close_time": "23:00"
            },
        ]

        mock_message = MagicMock()
        mock_message.content = [MagicMock(text="I recommend Odegaard Library.")]
        mock_client.messages.create.return_value = mock_message

        from recommend import get_recommendation
        result = get_recommendation("Where should I study?")

        assert "Odegaard" in result

    @patch("recommend.client")
    @patch("recommend.get_hours_for_day")
    @patch("recommend.get_all_resources")
    def test_calls_anthropic_with_user_query(self, mock_resources, mock_hours, mock_client):
        mock_resources.return_value = []
        mock_hours.return_value = []

        mock_message = MagicMock()
        mock_message.content = [MagicMock(text="No buildings available.")]
        mock_client.messages.create.return_value = mock_message

        from recommend import get_recommendation
        get_recommendation("quiet study spot")

        call_args = mock_client.messages.create.call_args
        messages = call_args.kwargs.get("messages") or call_args[1].get("messages")
        assert messages[0]["content"] == "quiet study spot"
        assert messages[0]["role"] == "user"

    @patch("recommend.client")
    @patch("recommend.get_hours_for_day")
    @patch("recommend.get_all_resources")
    def test_includes_building_data_in_system_prompt(self, mock_resources, mock_hours, mock_client):
        mock_resources.return_value = [
            {
                "id": 1,
                "name": "Suzzallo Library",
                "type": "library",
                "location": "Central Campus",
                "description": "Historic main library",
                "husky_access": False
            },
        ]
        mock_hours.return_value = [
            {
                "resource_id": 1,
                "is_closed": False,
                "open_time": "07:30",
                "close_time": "23:00"
            },
        ]

        mock_message = MagicMock()
        mock_message.content = [MagicMock(text="Try Suzzallo.")]
        mock_client.messages.create.return_value = mock_message

        from recommend import get_recommendation
        get_recommendation("study spot")

        call_args = mock_client.messages.create.call_args
        system = call_args.kwargs.get("system") or call_args[1].get("system")
        assert "Suzzallo Library" in system
        assert "07:30" in system

    @patch("recommend.client")
    @patch("recommend.get_hours_for_day")
    @patch("recommend.get_all_resources")
    def test_includes_husky_access_in_prompt(self, mock_resources, mock_hours, mock_client):
        mock_resources.return_value = [
            {
                "id": 1,
                "name": "Gates Center",
                "type": "academic",
                "location": "Central Campus",
                "description": "CSE building",
                "husky_access": True
            },
        ]
        mock_hours.return_value = [
            {
                "resource_id": 1,
                "is_closed": True,
                "open_time": None,
                "close_time": None
            },
        ]

        mock_message = MagicMock()
        mock_message.content = [MagicMock(text="Gates Center has Husky access.")]
        mock_client.messages.create.return_value = mock_message

        from recommend import get_recommendation
        get_recommendation("anywhere open late")

        call_args = mock_client.messages.create.call_args
        system = call_args.kwargs.get("system") or call_args[1].get("system")
        assert "Husky Card" in system

    @patch("recommend.client")
    @patch("recommend.get_hours_for_day")
    @patch("recommend.get_all_resources")
    def test_includes_closed_status_in_prompt(self, mock_resources, mock_hours, mock_client):
        mock_resources.return_value = [
            {
                "id": 1,
                "name": "Kane Hall",
                "type": "academic",
                "location": "Central Campus",
                "description": "Lecture hall",
                "husky_access": False
            },
        ]
        mock_hours.return_value = [
            {
                "resource_id": 1,
                "is_closed": True,
                "open_time": None,
                "close_time": None
            },
        ]

        mock_message = MagicMock()
        mock_message.content = [MagicMock(text="Kane Hall is closed.")]
        mock_client.messages.create.return_value = mock_message

        from recommend import get_recommendation
        get_recommendation("any building")

        call_args = mock_client.messages.create.call_args
        system = call_args.kwargs.get("system") or call_args[1].get("system")
        assert "Closed today" in system

    @patch("recommend.client")
    @patch("recommend.get_hours_for_day")
    @patch("recommend.get_all_resources")
    def test_handles_api_error(self, mock_resources, mock_hours, mock_client):
        mock_resources.return_value = []
        mock_hours.return_value = []
        mock_client.messages.create.side_effect = Exception("API is down")

        from recommend import get_recommendation

        try:
            get_recommendation("study spot")
            assert False, "Should have raised an exception"
        except Exception as e:
            assert "API is down" in str(e)