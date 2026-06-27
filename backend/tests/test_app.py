import json
from unittest.mock import patch, MagicMock


class TestResourceRoutes:
    @patch("app.get_all_resources")
    def test_list_resources_returns_200(self, mock_get_all, client):
        mock_get_all.return_value = [
            {"id": 1, "name": "Odegaard", "type": "library", "location": "South Campus", "description": "Library", "husky_access": False}
        ]

        response = client.get("/api/resources")

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 1
        assert data[0]["name"] == "Odegaard"

    @patch("app.get_all_resources")
    def test_list_resources_returns_empty_list(self, mock_get_all, client):
        mock_get_all.return_value = []

        response = client.get("/api/resources")

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data == []

    @patch("app.get_resource_by_id")
    def test_get_resource_returns_200(self, mock_get, client):
        mock_get.return_value = {"id": 1, "name": "Odegaard", "type": "library", "location": "South Campus", "description": "Library", "husky_access": False}

        response = client.get("/api/resources/1")

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["name"] == "Odegaard"

    @patch("app.get_resource_by_id")
    def test_get_resource_returns_404_when_not_found(self, mock_get, client):
        mock_get.return_value = None

        response = client.get("/api/resources/999")

        assert response.status_code == 404
        data = json.loads(response.data)
        assert "error" in data

    @patch("app.get_hours_for_resource")
    def test_resource_hours_returns_200(self, mock_hours, client):
        mock_hours.return_value = [
            {"day_of_week": "Monday", "open_time": "07:00", "close_time": "23:00", "is_closed": False}
        ]

        response = client.get("/api/resources/1/hours")

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 1
        assert data[0]["day_of_week"] == "Monday"


class TestHoursRoutes:
    @patch("app.get_hours_for_day")
    def test_today_hours_returns_200(self, mock_hours, client):
        mock_hours.return_value = [
            {"resource_id": 1, "day_of_week": "Thursday", "open_time": "07:00", "close_time": "23:00", "is_closed": False}
        ]

        response = client.get("/api/hours/today")

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data[0]["resource_id"] == 1


class TestOpenNowRoute:
    @patch("app.get_open_now")
    def test_open_now_returns_200(self, mock_open, client):
        mock_open.return_value = [
            {"id": 1, "name": "Odegaard", "type": "library", "location": "South Campus", "description": "Library", "husky_access": False, "open_time": "07:00", "close_time": "23:00"}
        ]

        response = client.get("/api/resources/open")

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 1

    @patch("app.get_open_now")
    def test_open_now_returns_empty_when_all_closed(self, mock_open, client):
        mock_open.return_value = []

        response = client.get("/api/resources/open")

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data == []


class TestSearchRoute:
    @patch("app.search_resources")
    def test_search_returns_results(self, mock_search, client):
        mock_search.return_value = [
            {"id": 1, "name": "Odegaard", "type": "library", "location": "South Campus", "description": "Library", "husky_access": False}
        ]

        response = client.get("/api/resources/search?q=odegaard")

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 1

    @patch("app.search_resources")
    def test_search_returns_empty_for_no_match(self, mock_search, client):
        mock_search.return_value = []

        response = client.get("/api/resources/search?q=nonexistent")

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data == []

    def test_search_returns_empty_for_no_query(self, client):
        response = client.get("/api/resources/search")

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data == []


class TestFavoriteRoutes:
    @patch("app.get_favorites")
    def test_list_favorites_returns_200(self, mock_favs, client):
        mock_favs.return_value = [
            {"id": 1, "name": "Odegaard", "type": "library", "location": "South Campus", "description": "Library", "husky_access": False}
        ]

        response = client.get("/api/favorites/user_123")

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 1

    @patch("app.add_favorite")
    def test_add_favorite_returns_201(self, mock_add, client):
        response = client.post(
            "/api/favorites",
            data=json.dumps({"user_id": "user_123", "resource_id": 1}),
            content_type="application/json"
        )

        assert response.status_code == 201
        data = json.loads(response.data)
        assert data["status"] == "added"
        mock_add.assert_called_once_with("user_123", 1)

    @patch("app.remove_favorite")
    def test_remove_favorite_returns_200(self, mock_remove, client):
        response = client.delete(
            "/api/favorites",
            data=json.dumps({"user_id": "user_123", "resource_id": 1}),
            content_type="application/json"
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["status"] == "removed"
        mock_remove.assert_called_once_with("user_123", 1)


class TestRecommendRoute:
    @patch("app.get_recommendation")
    def test_recommend_returns_200(self, mock_rec, client):
        mock_rec.return_value = "I recommend Odegaard Library."

        response = client.post(
            "/api/recommend",
            data=json.dumps({"query": "study spot"}),
            content_type="application/json"
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert "recommendation" in data
        assert "Odegaard" in data["recommendation"]

    def test_recommend_returns_400_for_empty_query(self, client):
        response = client.post(
            "/api/recommend",
            data=json.dumps({"query": ""}),
            content_type="application/json"
        )

        assert response.status_code == 400
        data = json.loads(response.data)
        assert "error" in data

    def test_recommend_returns_400_for_missing_query(self, client):
        response = client.post(
            "/api/recommend",
            data=json.dumps({}),
            content_type="application/json"
        )

        assert response.status_code == 400

    @patch("app.get_recommendation")
    def test_recommend_returns_500_on_api_failure(self, mock_rec, client):
        mock_rec.side_effect = Exception("Anthropic API is down")

        response = client.post(
            "/api/recommend",
            data=json.dumps({"query": "study spot"}),
            content_type="application/json"
        )

        assert response.status_code == 500
        data = json.loads(response.data)
        assert "error" in data