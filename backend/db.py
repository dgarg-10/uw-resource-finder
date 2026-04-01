import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() #loads variable from the .env file


def get_connection():
    database_url = os.environ.get("DATABASE_URL")
    if database_url is None:
        raise ValueError("Database URL has not been set up.")
    connection = psycopg2.connect(database_url)
    return connection 

def get_all_resources() -> list:
    """
        Returns all resources present within the database, in the provided format. 
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, type, location, description FROM resources ORDER BY name")
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "type": row[2],
            "location": row[3], 
            "description": row[4]
        }
        for row in rows
    ]

def get_resource_by_id(id) -> dict | None:
    """
        Returns a specific resource based on the id that is given, in the provided format
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, type, location, description FROM resources WHERE id = %s", (id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "type": row[2],
        "location": row[3], 
        "description": row[4]
    }
    

def get_hours_for_resource(id):
    """
        Returns the hours for each day based on a certain resource id in the provided format
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT day_of_week, open_time, close_time, is_closed FROM hours WHERE resource_id = %s", (id,)
    )
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "day_of_week": row[0],
            "open_time": str(row[1])[:5] if row[1] else None, #Would be none if the resource is closed on that day
            "close_time": str(row[2])[:5] if row[2] else None,
            "is_closed": row[3]
        }
        for row in rows
    ]

def get_hours_for_day():
    """
        Returns all resources' hours for the current day
    """
    today = datetime.now().strftime("%A")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT resource_id, day_of_week, open_time, close_time, is_closed FROM hours WHERE day_of_week = %s", (today,))
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "resource_id": row[0],
            "day_of_week": row[1],
            "open_time": str(row[2])[:5] if row[2] else None,
            "close_time": str(row[3])[:5] if row[3] else None,
            "is_closed": row[4]
        }
        for row in rows
    ]
    

def get_open_now():
    """
        Returns all available resources that are currently open. 
    """
    today = datetime.now().strftime("%A")
    current_time = datetime.now().strftime("%H:%M:%S")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT r.id, r.name, r.type, r.location, r.description,
                  h.open_time, h.close_time
           FROM resources r
           JOIN hours h ON r.id = h.resource_id
           WHERE h.day_of_week = %s
           AND h.is_closed = FALSE
           AND h.open_time <= %s
           AND h.close_time > %s
           ORDER BY r.name""",
        (today, current_time, current_time)
    )
    rows = cursor.fetchall()
    conn.close()

    return [ 
        {
            "id": row[0],
            "name": row[1],
            "type": row[2],
            "location": row[3],
            "description": row[4],
            "open_time": str(row[5])[:5] if row[5] else None,
            "close_time": str(row[6])[:5] if row[6] else None
        }
        for row in rows
    ]



def search_resources(query):
    """
        Searches through the database and returns the resource that matches the query.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT id, name, type, location, description
           FROM resources
           WHERE name ILIKE %s
           ORDER BY name""",
        (f"%{query}%",)
    )
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "type": row[2],
            "location": row[3],
            "description": row[4]
        }
        for row in rows
    ]


def get_favorites(user_id):
    """
        Returns all of the favorites within the favorites list
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT r.id, r.name, r.type, r.location, r.description
           FROM resources r
           JOIN favorites f ON r.id = f.resource_id
           WHERE f.user_id = %s
           ORDER BY r.name""",
        (user_id,)
    )
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "type": row[2],
            "location": row[3],
            "description": row[4]
        }
        for row in rows
    ]

def add_favorite(user_id, resource_id):
    """
        Adds a resource to the favorites collection as long as it is unique.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO favorites (user_id, resource_id) VALUES (%s, %s)",
            (user_id, resource_id)
        )
        conn.commit()
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
    finally:
        conn.close()


def remove_favorite(user_id, resource_id):
    """
        Removes a resource from the favorites collection
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM favorites WHERE user_id = %s AND resource_id = %s",
        (user_id, resource_id)
    )
    conn.commit()
    conn.close()



