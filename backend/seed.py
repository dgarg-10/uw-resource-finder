from db import get_connection

def seed():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM favorites")
    cursor.execute("DELETE FROM hours")
    cursor.execute("DELETE FROM resources") #favorites and hours have to be deleted first as they are the children

    # --- Libraries ---

    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Odegaard Undergraduate Library", "library", "South Central Campus",
         "Main undergraduate library with study spaces, computer labs, and research help")
    )
    odegaard_id = cursor.fetchone()[0]

    odegaard_hours = [
        ("Monday", "08:00", "23:59", False),
        ("Tuesday", "08:00", "23:59", False),
        ("Wednesday", "08:00", "23:59", False),
        ("Thursday", "08:00", "23:59", False),
        ("Friday", "08:00", "20:00", False),
        ("Saturday", "12:00", "20:00", False),
        ("Sunday", "12:00", "23:59", False),
    ]

    for day, open_time, close_time, is_closed in odegaard_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (odegaard_id, day, open_time, close_time, is_closed)
        )

    # Suzzallo Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Suzzallo and Allen Libraries", "library", "Central Campus",
         "Historic main library featuring the renowned reading room with Gothic architecture, with a beautiful silent study space. Allen Library is a research library connected to Suzzallo with extensive collections and study spaces")
    )
    suzzallo_id = cursor.fetchone()[0]

    suzzallo_hours = [
        ("Monday", "08:00", "20:00", False),
        ("Tuesday", "08:00", "20:00", False),
        ("Wednesday", "08:00", "20:00", False),
        ("Thursday", "08:00", "20:00", False),
        ("Friday", "08:00", "18:00", False),
        ("Saturday", None, None, False),
        ("Sunday", "13:00", "20:00", False),
    ]

    for day, open_time, close_time, is_closed in suzzallo_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (suzzallo_id, day, open_time, close_time, is_closed)
        )

   
    # Health Sciences Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Health Sciences Library", "library", "South Campus",
         "Specialized library for health sciences research and study")
    )
    hsl_id = cursor.fetchone()[0]

    hsl_hours = [
        ("Monday", "07:30", "21:00", False),
        ("Tuesday", "07:30", "21:00", False),
        ("Wednesday", "07:30", "21:00", False),
        ("Thursday", "07:30", "21:00", False),
        ("Friday", "07:30", "18:00", False),
        ("Saturday", "10:00", "18:00", False),
        ("Sunday", "12:00", "21:00", False),
    ]

    for day, open_time, close_time, is_closed in hsl_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (hsl_id, day, open_time, close_time, is_closed)
        )

    # Foster Business Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Foster Business Library", "library", "South Campus",
         "Business-focused library in PACCAR Hall with availability for all ")
    )
    foster_id = cursor.fetchone()[0]

    foster_hours = [
        ("Monday", "09:00", "20:00", False),
        ("Tuesday", "09:00", "20:00", False),
        ("Wednesday", "09:00", "20:00", False),
        ("Thursday", "09:00", "20:00", False),
        ("Friday", "09:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", "13:00", "20:00", False),
    ]

    for day, open_time, close_time, is_closed in foster_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (foster_id, day, open_time, close_time, is_closed)
        )

    # Art Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Art Library", "library", "Central Campus",
         "Supports teaching, research, and learning in art history, studio art, and design")
    )
    art_id = cursor.fetchone()[0]

    art_hours = [
        ("Monday", "10:00", "17:00", False),
        ("Tuesday", "10:00", "17:00", False),
        ("Wednesday", "10:00", "17:00", False),
        ("Thursday", "10:00", "17:00", False),
        ("Friday", "10:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in art_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (art_id, day, open_time, close_time, is_closed)
        )

    # Built Environments Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Built Environments Library", "library", "Central Campus",
         "Serves the College of Built Environments including Architecture, Construction Management, Landscape Architecture, Real Estate, and Urban Design and Planning")
    )
    be_id = cursor.fetchone()[0]

    be_hours = [
        ("Monday", "10:00", "17:00", False),
        ("Tuesday", "10:00", "17:00", False),
        ("Wednesday", "10:00", "17:00", False),
        ("Thursday", "10:00", "17:00", False),
        ("Friday", "10:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in be_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (be_id, day, open_time, close_time, is_closed)
        )

    # Drama Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Drama Library", "library", "Central Campus",
         "Serves the UW School of Drama and the theatre community of the Puget Sound region")
    )
    drama_id = cursor.fetchone()[0]

    drama_hours = [
        ("Monday", "13:00", "17:00", False),
        ("Tuesday", "13:00", "17:00", False),
        ("Wednesday", "13:00", "17:00", False),
        ("Thursday", "13:00", "17:00", False),
        ("Friday", "13:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in drama_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (drama_id, day, open_time, close_time, is_closed)
        )

    # Engineering Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Engineering Library", "library", "Central Campus",
         "Supports the College of Engineering and serves as a Patent and Trademark Resource Center (PTRC)")
    )
    eng_id = cursor.fetchone()[0]

    eng_hours = [
        ("Monday", "09:00", "18:00", False),
        ("Tuesday", "09:00", "18:00", False),
        ("Wednesday", "09:00", "18:00", False),
        ("Thursday", "09:00", "18:00", False),
        ("Friday", "09:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in eng_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (eng_id, day, open_time, close_time, is_closed)
        )

    # Friday Harbor Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Friday Harbor Library", "library", "Friday Harbor Laboratories",
         "Supports research and teaching at UW Friday Harbor Labs on San Juan Island; by appointment only")
    )
    fh_id = cursor.fetchone()[0]

    fh_hours = [
        ("Monday", "08:00", "17:00", False),
        ("Tuesday", "08:00", "17:00", False),
        ("Wednesday", "08:00", "17:00", False),
        ("Thursday", "08:00", "17:00", False),
        ("Friday", "08:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in fh_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (fh_id, day, open_time, close_time, is_closed)
        )


    # Li Lu Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Li Lu Library", "library", "Central Campus",
         "Extension of the Health Sciences Library facilitating research and learning support, located in the Health Sciences Education Building")
    )
    lilu_id = cursor.fetchone()[0]

    lilu_hours = [
        ("Monday", "08:00", "17:00", False),
        ("Tuesday", "08:00", "17:00", False),
        ("Wednesday", "08:00", "17:00", False),
        ("Thursday", "08:00", "17:00", False),
        ("Friday", "08:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in lilu_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (lilu_id, day, open_time, close_time, is_closed)
        )

    # Mathematics Research Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Mathematics Research Library", "library", "Central Campus",
         "Provides research help and access to materials in Applied Mathematics, Mathematics, and Statistics")
    )
    math_id = cursor.fetchone()[0]

    math_hours = [
        ("Monday", "10:00", "17:00", False),
        ("Tuesday", "10:00", "17:00", False),
        ("Wednesday", "10:00", "17:00", False),
        ("Thursday", "10:00", "17:00", False),
        ("Friday", "10:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in math_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (math_id, day, open_time, close_time, is_closed)
        )

    # Music Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Music Library", "library", "Central Campus",
         "Provides research help and access to music collections")
    )
    music_id = cursor.fetchone()[0]

    music_hours = [
        ("Monday", "10:00", "16:30", False),
        ("Tuesday", "10:00", "16:30", False),
        ("Wednesday", "10:00", "16:30", False),
        ("Thursday", "10:00", "16:30", False),
        ("Friday", "10:00", "16:30", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in music_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (music_id, day, open_time, close_time, is_closed)
        )

    # Open Scholarship Commons
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Open Scholarship Commons", "library", "Central Campus",
         "Interdisciplinary spaces and services in Suzzallo Library to advance open, public, and emerging forms of scholarship")
    )
    osc_id = cursor.fetchone()[0]

    osc_hours = [
        ("Monday", "08:00", "20:00", False),
        ("Tuesday", "08:00", "20:00", False),
        ("Wednesday", "08:00", "20:00", False),
        ("Thursday", "08:00", "20:00", False),
        ("Friday", "08:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", "13:00", "20:00", False),
    ]

    for day, open_time, close_time, is_closed in osc_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (osc_id, day, open_time, close_time, is_closed)
        )

    # Research Commons
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Research Commons", "library", "Central Campus",
         "A place to collaborate and connect with fellow students and faculty on research projects, located in Allen Library South")
    )
    rc_id = cursor.fetchone()[0]

    rc_hours = [
        ("Monday", "08:00", "20:00", False),
        ("Tuesday", "08:00", "20:00", False),
        ("Wednesday", "08:00", "20:00", False),
        ("Thursday", "08:00", "20:00", False),
        ("Friday", "08:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", "13:00", "20:00", False),
    ]

    for day, open_time, close_time, is_closed in rc_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (rc_id, day, open_time, close_time, is_closed)
        )


    # Tateuchi East Asia Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Tateuchi East Asia Library", "library", "Central Campus",
         "One of the leading East Asian libraries in North America, located in Gowen Hall on the Quad")
    )
    eastasia_id = cursor.fetchone()[0]

    eastasia_hours = [
        ("Monday", "09:00", "18:00", False),
        ("Tuesday", "09:00", "18:00", False),
        ("Wednesday", "09:00", "18:00", False),
        ("Thursday", "09:00", "18:00", False),
        ("Friday", "09:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in eastasia_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (eastasia_id, day, open_time, close_time, is_closed)
        )

    # The 8
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("The 8", "library", "North Campus",
         "A study space located in the basement of McMahon hall with maker tools and games.")
    )
    the8_id = cursor.fetchone()[0]

    the8_hours = [
        ("Monday", "13:00", "23:00", False),
        ("Tuesday", "13:00", "23:00", False),
        ("Wednesday", "13:00", "23:00", False),
        ("Thursday", "13:00", "23:00", False),
        ("Friday", "13:00", "23:00", False),
        ("Saturday", "13:00", "23:00", False),
        ("Sunday", "13:00", "23:00", False),
    ]

    for day, open_time, close_time, is_closed in the8_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (the8_id, day, open_time, close_time, is_closed)
        )
    

   

    # --- Academic Buildings ---

    cursor.execute(
        "INSERT INTO resources (name, type, location, description, husky_access) VALUES (%s, %s, %s, %s, %s) RETURNING id",
        ("Bill & Melinda Gates Center (CSE2)", "academic", "South Campus",
         "24/7 after hours cardkey entry, allowing access to student spaces, study rooms, and lab spaces.", True)
    )
    cse2_id = cursor.fetchone()[0]

    cse2_hours = [
        ("Monday", "08:00", "19:00", False),
        ("Tuesday", "08:00", "19:00", False),   
        ("Wednesday", "08:00", "19:00", False),
        ("Thursday", "08:00", "19:00", False),
        ("Friday", "08:00", "19:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in cse2_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (cse2_id, day, open_time, close_time, is_closed)
        )

    cursor.execute(
        "INSERT INTO resources (name, type, location, description, husky_access) VALUES (%s, %s, %s, %s, %s) RETURNING id",
        ("Health Science Education Building", "academic", "South West Campus",
         "24/7 after hours cardkey entry, allowing access to student spaces, study rooms, and lab spaces.", True)
    )
    hseb_id = cursor.fetchone()[0]

    hseb_hours = [
        ("Monday", "08:00", "17:00", False),
        ("Tuesday", "08:00", "17:00", False),   
        ("Wednesday", "08:00", "17:00", False),
        ("Thursday", "08:00", "17:00", False),
        ("Friday", "08:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in hseb_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (hseb_id, day, open_time, close_time, is_closed)
        )

    
    # --- Dining ---

    # By George
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("By George", "dining", "South Campus",
         "Coffee and grab-and-go items including pastries, sandwiches, and snacks")
    )
    bygeorge_id = cursor.fetchone()[0]

    bygeorge_hours = [
        ("Monday", "07:30", "20:00", False),
        ("Tuesday", "07:30", "20:00", False),   
        ("Wednesday", "07:30", "20:00", False),
        ("Thursday", "07:30", "20:00", False),
        ("Friday", "07:30", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in bygeorge_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (bygeorge_id, day, open_time, close_time, is_closed)
        )

    # Center Table
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Center Table", "dining", "North Campus",
         "North campus dining hall with all-you-can-eat meals and diverse food stations")
    )
    centertable_id = cursor.fetchone()[0]

    centertable_hours = [
        ("Monday", "07:30", "22:00", False),
        ("Tuesday", "07:30", "22:00", False),
        ("Wednesday", "07:30", "22:00", False),
        ("Thursday", "07:30", "22:00", False),
        ("Friday", "07:30", "22:00", False),
        ("Saturday", "07:30", "22:00", False),
        ("Sunday", "07:30", "22:00", False),
    ]

    for day, open_time, close_time, is_closed in centertable_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (centertable_id, day, open_time, close_time, is_closed)
        )

    # Cultivate
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Cultivate", "dining", "West Campus",
         "West campus gastro pub serving lunch and dinner with a rotating seasonal menu")
    )
    cultivate_id = cursor.fetchone()[0]

    cultivate_hours = [
        ("Monday", "11:00", "20:30", False),
        ("Tuesday", "11:00", "20:30", False),
        ("Wednesday", "11:00", "20:30", False),
        ("Thursday", "11:00", "20:30", False),
        ("Friday", "11:30", "15:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in cultivate_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (cultivate_id, day, open_time, close_time, is_closed)
        )

    # Husky Den Food Court
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Husky Den Food Court", "dining", "Central Campus (HUB)",
         "Food court in the HUB featuring multiple vendors including burgers, Asian cuisine, and more")
    )
    huskyden_id = cursor.fetchone()[0]

    huskyden_hours = [
        ("Monday", "10:15", "19:00", False),
        ("Tuesday", "10:15", "19:00", False),
        ("Wednesday", "10:15", "19:00", False),
        ("Thursday", "10:15", "19:00", False),
        ("Friday", "10:15", "16:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in huskyden_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (huskyden_id, day, open_time, close_time, is_closed)
        )

    # Local Point
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Local Point", "dining", "West Campus (Lander Hall)",
         "West campus dining hall with all-you-can-eat meals, late-night hours, and diverse food options")
    )
    localpoint_id = cursor.fetchone()[0]

    localpoint_hours = [
        ("Monday", "07:30", "23:00", False),
        ("Tuesday", "07:30", "23:00", False),
        ("Wednesday", "07:30", "23:00", False),
        ("Thursday", "07:30", "23:00", False),
        ("Friday", "07:30", "23:00", False),
        ("Saturday", "08:00", "23:00", False),
        ("Sunday", "08:00", "22:00", False),
    ]

    for day, open_time, close_time, is_closed in localpoint_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (localpoint_id, day, open_time, close_time, is_closed)
        )

    # Dawg Bites
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Dawg Bites", "dining", "South Campus (IMA)",
         "Café inside the IMA serving smoothies, protein shakes, and light bites to fuel your workout")
    )
    dawgbites_id = cursor.fetchone()[0]

    dawgbites_hours = [
        ("Monday", "11:30", "21:00", False),
        ("Tuesday", "11:30", "21:00", False),
        ("Wednesday", "11:30", "21:00", False),
        ("Thursday", "11:30", "21:00", False),
        ("Friday", "11:30", "21:00", False),
        ("Saturday", None, None, True),
        ("Sunday", "11:30", "19:00", False),
    ]

    for day, open_time, close_time, is_closed in dawgbites_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (dawgbites_id, day, open_time, close_time, is_closed)
        )

    # Husky Den Café
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Husky Den Café", "dining", "Central Campus (HUB)",
         "Espresso bar and café inside the HUB for coffee and quick bites")
    )
    huskydencafe_id = cursor.fetchone()[0]

    huskydencafe_hours = [
        ("Monday", "08:00", "17:00", False),
        ("Tuesday", "08:00", "17:00", False),
        ("Wednesday", "08:00", "17:00", False),
        ("Thursday", "08:00", "17:00", False),
        ("Friday", "08:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in huskydencafe_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (huskydencafe_id, day, open_time, close_time, is_closed)
        )

    # Husky Grind Café, District Market Alder
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Husky Grind Café, District Market Alder", "dining", "West Campus (Alder Hall)",
         "UW coffeehouse inside Alder Hall's District Market serving espresso and baked goods")
    )
    grind_alder_id = cursor.fetchone()[0]

    grind_alder_hours = [
        ("Monday", "07:00", "20:00", False),
        ("Tuesday", "07:00", "20:00", False),
        ("Wednesday", "07:00", "20:00", False),
        ("Thursday", "07:00", "20:00", False),
        ("Friday", "07:00", "20:00", False),
        ("Saturday", "08:00", "20:00", False),
        ("Sunday", "08:00", "20:00", False),
    ]

    for day, open_time, close_time, is_closed in grind_alder_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (grind_alder_id, day, open_time, close_time, is_closed)
        )

    # Husky Grind Café, District Market Oak
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Husky Grind Café, District Market Oak", "dining", "West Campus (Oak Hall)",
         "UW coffeehouse near Denny Field inside Oak Hall's District Market")
    )
    grind_oak_id = cursor.fetchone()[0]

    grind_oak_hours = [
        ("Monday", "07:00", "20:00", False),
        ("Tuesday", "07:00", "20:00", False),
        ("Wednesday", "07:00", "20:00", False),
        ("Thursday", "07:00", "20:00", False),
        ("Friday", "07:00", "20:00", False),
        ("Saturday", "08:00", "20:00", False),
        ("Sunday", "08:00", "20:00", False),
    ]

    for day, open_time, close_time, is_closed in grind_oak_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (grind_oak_id, day, open_time, close_time, is_closed)
        )

    # Husky Grind Café, Mercer Court
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Husky Grind Café, Mercer Court", "dining", "West Campus (Mercer Court)",
         "UW coffeehouse in Mercer Court near the Burke-Gilman Trail")
    )
    grind_mercer_id = cursor.fetchone()[0]

    grind_mercer_hours = [
        ("Monday", "07:00", "20:00", False),
        ("Tuesday", "07:00", "20:00", False),
        ("Wednesday", "07:00", "20:00", False),
        ("Thursday", "07:00", "20:00", False),
        ("Friday", "07:00", "20:00", False),
        ("Saturday", "09:00", "20:00", False),
        ("Sunday", "09:00", "20:00", False),
    ]

    for day, open_time, close_time, is_closed in grind_mercer_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (grind_mercer_id, day, open_time, close_time, is_closed)
        )

    # Microsoft Café
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Microsoft Café", "dining", "Central Campus (Gates Center)",
         "Café inside the Bill & Melinda Gates Center for Computer Science & Engineering")
    )
    mscafe_id = cursor.fetchone()[0]

    mscafe_hours = [
        ("Monday", "07:30", "17:00", False),
        ("Tuesday", "07:30", "17:00", False),
        ("Wednesday", "07:30", "17:00", False),
        ("Thursday", "07:30", "17:00", False),
        ("Friday", "07:30", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in mscafe_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (mscafe_id, day, open_time, close_time, is_closed)
        )

    # Orin's Place
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Orin's Place", "dining", "North Campus (Paccar Hall)",
         "Coffee and grab-and-go items in Paccar Hall at the Foster School of Business")
    )
    orins_id = cursor.fetchone()[0]

    orins_hours = [
        ("Monday", "07:30", "19:00", False),
        ("Tuesday", "07:30", "19:00", False),
        ("Wednesday", "07:30", "19:00", False),
        ("Thursday", "07:30", "19:00", False),
        ("Friday", "07:30", "15:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in orins_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (orins_id, day, open_time, close_time, is_closed)
        )

    # Public Grounds
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Public Grounds", "dining", "Central Campus (Parrington Hall)",
         "Coffee and grab-and-go items in Parrington Hall on the Quad")
    )
    publicgrounds_id = cursor.fetchone()[0]

    publicgrounds_hours = [
        ("Monday", "09:30", "17:30", False),
        ("Tuesday", "09:30", "17:30", False),
        ("Wednesday", "09:30", "17:30", False),
        ("Thursday", "09:30", "17:30", False),
        ("Friday", None, None, True),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in publicgrounds_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (publicgrounds_id, day, open_time, close_time, is_closed)
        )

    # The Rotunda
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("The Rotunda", "dining", "South Campus (Health Sciences)",
         "Grab-and-go items in the Magnuson Health Sciences Center I-Court")
    )
    rotunda_id = cursor.fetchone()[0]

    rotunda_hours = [
        ("Monday", "07:30", "18:00", False),
        ("Tuesday", "07:30", "18:00", False),
        ("Wednesday", "07:30", "18:00", False),
        ("Thursday", "07:30", "18:00", False),
        ("Friday", "07:30", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in rotunda_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (rotunda_id, day, open_time, close_time, is_closed)
        )

    # Starbucks, Population Health
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Starbucks, Population Health", "dining", "South Campus (Hans Rosling Center)",
         "Starbucks location at the Hans Rosling Center for Population Health")
    )
    sbux_ph_id = cursor.fetchone()[0]

    sbux_ph_hours = [
        ("Monday", "07:30", "17:00", False),
        ("Tuesday", "07:30", "17:00", False),
        ("Wednesday", "07:30", "17:00", False),
        ("Thursday", "07:30", "17:00", False),
        ("Friday", "07:30", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in sbux_ph_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (sbux_ph_id, day, open_time, close_time, is_closed)
        )

    # Starbucks, Suzzallo
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Starbucks, Suzzallo", "dining", "Central Campus (Suzzallo Library)",
         "Iconic Starbucks café inside Suzzallo Library on the ground floor")
    )
    sbux_suzz_id = cursor.fetchone()[0]

    sbux_suzz_hours = [
        ("Monday", "08:00", "19:00", False),
        ("Tuesday", "08:00", "19:00", False),
        ("Wednesday", "08:00", "19:00", False),
        ("Thursday", "08:00", "19:00", False),
        ("Friday", "08:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", "13:00", "19:00", False),
    ]

    for day, open_time, close_time, is_closed in sbux_suzz_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (sbux_suzz_id, day, open_time, close_time, is_closed)
        )

    # Tower Café
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Tower Café", "dining", "West Campus (UW Tower)",
         "Café in the UW Tower serving coffee, breakfast, and lunch items")
    )
    towercafe_id = cursor.fetchone()[0]

    towercafe_hours = [
        ("Monday", "07:30", "14:30", False),
        ("Tuesday", "07:30", "14:30", False),
        ("Wednesday", "07:30", "14:30", False),
        ("Thursday", "07:30", "14:30", False),
        ("Friday", "07:30", "14:30", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in towercafe_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (towercafe_id, day, open_time, close_time, is_closed)
        )

    # District Market, Alder
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("District Market, Alder", "dining", "West Campus (Alder Hall)",
         "Neighborhood grocery store in Alder Hall with fresh produce, hot and cold dishes, and snacks")
    )
    dm_alder_id = cursor.fetchone()[0]

    dm_alder_hours = [
        ("Monday", "07:00", "22:00", False),
        ("Tuesday", "07:00", "22:00", False),
        ("Wednesday", "07:00", "22:00", False),
        ("Thursday", "07:00", "22:00", False),
        ("Friday", "07:00", "22:00", False),
        ("Saturday", "08:00", "22:00", False),
        ("Sunday", "08:00", "22:00", False),
    ]

    for day, open_time, close_time, is_closed in dm_alder_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (dm_alder_id, day, open_time, close_time, is_closed)
        )

    # District Market, Oak
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("District Market, Oak", "dining", "West Campus (Oak Hall)",
         "Neighborhood grocery store in Oak Hall with fresh produce, frozen food, and household items")
    )
    dm_oak_id = cursor.fetchone()[0]

    dm_oak_hours = [
        ("Monday", "07:00", "22:00", False),
        ("Tuesday", "07:00", "22:00", False),
        ("Wednesday", "07:00", "22:00", False),
        ("Thursday", "07:00", "22:00", False),
        ("Friday", "07:00", "22:00", False),
        ("Saturday", "08:00", "22:00", False),
        ("Sunday", "08:00", "22:00", False),
    ]

    for day, open_time, close_time, is_closed in dm_oak_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (dm_oak_id, day, open_time, close_time, is_closed)
        )

    # Etc., The HUB
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Etc., The HUB", "dining", "Central Campus (HUB)",
         "Express market inside the HUB with grab-and-go snacks, drinks, and essentials")
    )
    etc_id = cursor.fetchone()[0]

    etc_hours = [
        ("Monday", "07:30", "19:00", False),
        ("Tuesday", "07:30", "19:00", False),
        ("Wednesday", "07:30", "19:00", False),
        ("Thursday", "07:30", "19:00", False),
        ("Friday", "07:30", "16:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in etc_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (etc_id, day, open_time, close_time, is_closed)
        )

    # --- Student Centers ---

    # Husky Union Building (HUB)
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Husky Union Building (HUB)", "student_center", "Central Campus",
         "Student union with dining, event spaces, bowling alley, and student organization offices")
    )
    hub_id = cursor.fetchone()[0]

    hub_hours = [
        ("Monday", "07:00", "23:00", False),
        ("Tuesday", "07:00", "23:00", False),
        ("Wednesday", "07:00", "23:00", False),
        ("Thursday", "07:00", "23:00", False),
        ("Friday", "07:00", "23:00", False),
        ("Saturday", "10:00", "23:00", False),
        ("Sunday", "10:00", "23:00", False),
    ]

    for day, open_time, close_time, is_closed in hub_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (hub_id, day, open_time, close_time, is_closed)
        )

    # IMA (Intramural Activities Building)
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("IMA (Intramural Activities)", "student_center", "South Campus",
         "Recreation and fitness center with gym, pool, climbing wall, and courts")
    )
    ima_id = cursor.fetchone()[0]

    ima_hours = [
        ("Monday", "06:00", "22:30", False),
        ("Tuesday", "06:00", "22:30", False),
        ("Wednesday", "06:00", "22:30", False),
        ("Thursday", "06:00", "22:30", False),
        ("Friday", "06:00", "22:30", False),
        ("Saturday", "09:00", "20:30", False),
        ("Sunday", "09:00", "20:30", False),
    ]

    for day, open_time, close_time, is_closed in ima_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (ima_id, day, open_time, close_time, is_closed)
        )

    # Samuel E. Kelly Ethnic Cultural Center
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Samuel E. Kelly Ethnic Cultural Center", "student_center", "North Campus",
         "Cultural center with event space, lounges, and multicultural student organization offices")
    )
    ecc_id = cursor.fetchone()[0]

    ecc_hours = [
        ("Monday", "08:00", "21:00", False),
        ("Tuesday", "08:00", "21:00", False),
        ("Wednesday", "08:00", "21:00", False),
        ("Thursday", "08:00", "21:00", False),
        ("Friday", "08:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in ecc_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (ecc_id, day, open_time, close_time, is_closed)
        )

    # Area 01
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Area 01", "student_center", "West Campus (Maple Hall)",
         "Makerspace and community center featuring a Dabble Lab with 3D printers and laser cutters, Sound Lab, Image Lab for content creation, and Game Lab with consoles, arcade games, pool, and ping pong. Free for HFS residents, quarterly membership available for other students")
    )
    area01_id = cursor.fetchone()[0]

    area01_hours = [
        ("Monday", "13:00", "23:00", False),
        ("Tuesday", "13:00", "23:00", False),
        ("Wednesday", "13:00", "23:00", False),
        ("Thursday", "13:00", "23:00", False),
        ("Friday", "13:00", "23:00", False),
        ("Saturday", "13:00", "23:00", False),
        ("Sunday", "13:00", "23:00", False),
    ]

    for day, open_time, close_time, is_closed in area01_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (area01_id, day, open_time, close_time, is_closed)
        )


    conn.commit()
    conn.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed()