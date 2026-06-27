import pytest
from app import app as flask_app


# --- Mock Data ---

MOCK_RESOURCES = [
    {
        "id": 1,
        "name": "Odegaard Undergraduate Library",
        "type": "library",
        "location": "South Central Campus",
        "description": "Main undergraduate library with study spaces and computer labs",
        "husky_access": False
    },
    {
        "id": 2,
        "name": "Bill & Melinda Gates Center (CSE2)",
        "type": "academic",
        "location": "Central Campus",
        "description": "Second building of the Paul G. Allen School",
        "husky_access": True
    },
    {
        "id": 3,
        "name": "Local Point",
        "type": "dining",
        "location": "West Campus (Lander Hall)",
        "description": "West campus dining hall with all-you-can-eat meals",
        "husky_access": False
    },
]

MOCK_HOURS = [
    {
        "resource_id": 1,
        "day_of_week": "Thursday",
        "open_time": "07:00",
        "close_time": "23:00",
        "is_closed": False
    },
    {
        "resource_id": 2,
        "day_of_week": "Thursday",
        "open_time": "07:00",
        "close_time": "21:00",
        "is_closed": False
    },
    {
        "resource_id": 3,
        "day_of_week": "Thursday",
        "open_time": "07:30",
        "close_time": "23:00",
        "is_closed": False
    },
]

MOCK_HOURS_FULL_WEEK = [
    {"day_of_week": "Monday", "open_time": "07:00", "close_time": "23:00", "is_closed": False},
    {"day_of_week": "Tuesday", "open_time": "07:00", "close_time": "23:00", "is_closed": False},
    {"day_of_week": "Wednesday", "open_time": "07:00", "close_time": "23:00", "is_closed": False},
    {"day_of_week": "Thursday", "open_time": "07:00", "close_time": "23:00", "is_closed": False},
    {"day_of_week": "Friday", "open_time": "07:00", "close_time": "20:00", "is_closed": False},
    {"day_of_week": "Saturday", "open_time": "10:00", "close_time": "18:00", "is_closed": False},
    {"day_of_week": "Sunday", "open_time": None, "close_time": None, "is_closed": True},
]

MOCK_FAVORITES = [
    {
        "id": 1,
        "name": "Odegaard Undergraduate Library",
        "type": "library",
        "location": "South Central Campus",
        "description": "Main undergraduate library with study spaces and computer labs",
        "husky_access": False
    },
]


# --- Fixtures ---

@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


@pytest.fixture
def mock_resources():
    return MOCK_RESOURCES.copy()


@pytest.fixture
def mock_hours():
    return MOCK_HOURS.copy()


@pytest.fixture
def mock_hours_full_week():
    return MOCK_HOURS_FULL_WEEK.copy()


@pytest.fixture
def mock_favorites():
    return MOCK_FAVORITES.copy()