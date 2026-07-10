import os
from datetime import datetime
from zoneinfo import ZoneInfo
from anthropic import Anthropic
from dotenv import load_dotenv
from db import get_all_resources, get_hours_for_day

load_dotenv()

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def get_recommendation(user_query):
    resources = get_all_resources()
    today_hours = get_hours_for_day()

    hours_map = {}
    for h in today_hours:
        hours_map[h["resource_id"]] = h
    
    building_info = []
    for r in resources:
        hours = hours_map.get(r["id"])
        if hours and not hours["is_closed"]:
            status = f"Open today: {hours['open_time']} - {hours['close_time']}"
        elif hours and hours["is_closed"]:
            status = "Closed today"
        else:
            status = "Hours unknown"

        husky = " (Husky Card access after hours)" if r.get("husky_access") else ""

        building_info.append(
            f"- {r['name']} (Type: {r['type']}, Location: {r['location']}): "
            f"{r['description']}.{husky} Status: {status}"
        )

    buildings_text = "\n".join(building_info)
    now = datetime.now(ZoneInfo("America/Los_Angeles"))
    current_time = now.strftime("%I:%M %p")
    current_day = now.strftime("%A")

    system_prompt = f"""You are a helpful University of Washington Seattle campus assistant. You help students find the best buildings and spaces based on their needs and what is provided.
        Here is the current campus data:
        Current day: {current_day}
        Current time: {current_time}

        Available buildings and their current status:
        {buildings_text}

        Rules:
        - Only recommend buildings that are currently open or accessible when the student needs them
        - Only recommend based on the data that has been provided, do not invent information.
        - If a building has Husky Card access after hours, mention that it requires a Husky Card
        - Be specific about why you're recommending each place
        - Keep recommendations to 2-3 options maximum
        - Be concise and conversational, not formal
        - If nothing matches well, say so honestly
        - Include the building's hours in your recommendation
        - Do not use any markdown formatting like bold (**), italics, or headers. Use plain text only.
        """
    
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_query}
        ]
    )

    return message.content[0].text
    