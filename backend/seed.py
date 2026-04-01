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
        ("Monday", "07:00", "23:00", False),
        ("Tuesday", "07:00", "23:00", False),
        ("Wednesday", "07:00", "23:00", False),
        ("Thursday", "07:00", "23:00", False),
        ("Friday", "07:00", "20:00", False),
        ("Saturday", "10:00", "18:00", False),
        ("Sunday", "10:00", "23:00", False),
    ]

    for day, open_time, close_time, is_closed in odegaard_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (odegaard_id, day, open_time, close_time, is_closed)
        )

    # Suzzallo Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Suzzallo Library", "library", "Central Campus",
         "Historic main library featuring the renowned reading room with Gothic architecture, with a beautiful silent study space")
    )
    suzzallo_id = cursor.fetchone()[0]

    suzzallo_hours = [
        ("Monday", "07:30", "23:00", False),
        ("Tuesday", "07:30", "23:00", False),
        ("Wednesday", "07:30", "23:00", False),
        ("Thursday", "07:30", "23:00", False),
        ("Friday", "07:30", "18:00", False),
        ("Saturday", "10:00", "18:00", False),
        ("Sunday", "12:00", "23:00", False),
    ]

    for day, open_time, close_time, is_closed in suzzallo_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (suzzallo_id, day, open_time, close_time, is_closed)
        )

    # Allen Library
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Allen Library", "library", "Central Campus",
         "Research library connected to Suzzallo with extensive collections and study spaces")
    )
    allen_id = cursor.fetchone()[0]

    allen_hours = [
        ("Monday", "07:30", "22:00", False),
        ("Tuesday", "07:30", "22:00", False),
        ("Wednesday", "07:30", "22:00", False),
        ("Thursday", "07:30", "22:00", False),
        ("Friday", "07:30", "18:00", False),
        ("Saturday", "10:00", "18:00", False),
        ("Sunday", "12:00", "22:00", False),
    ]

    for day, open_time, close_time, is_closed in allen_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (allen_id, day, open_time, close_time, is_closed)
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
        ("Monday", "08:00", "18:00", False),
        ("Tuesday", "08:00", "18:00", False),
        ("Wednesday", "08:00", "18:00", False),
        ("Thursday", "08:00", "18:00", False),
        ("Friday", "08:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
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
        ("Monday", None, None, True),
        ("Tuesday", None, None, True),
        ("Wednesday", None, None, True),
        ("Thursday", None, None, True),
        ("Friday", None, None, True),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in fh_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (fh_id, day, open_time, close_time, is_closed)
        )

    # Government Publications, Maps, Microforms & Newspapers
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Government Publications, Maps, Microforms & Newspapers", "library", "Central Campus",
         "Offers government publications, maps, microforms, and newspaper collections on the ground floor of Suzzallo Library")
    )
    gmmn_id = cursor.fetchone()[0]

    gmmn_hours = [
        ("Monday", "09:00", "19:50", False),
        ("Tuesday", "09:00", "19:50", False),
        ("Wednesday", "09:00", "19:50", False),
        ("Thursday", "09:00", "19:50", False),
        ("Friday", "09:00", "16:50", False),
        ("Saturday", None, None, True),
        ("Sunday", "13:00", "19:50", False),
    ]

    for day, open_time, close_time, is_closed in gmmn_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (gmmn_id, day, open_time, close_time, is_closed)
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

    # Special Collections
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Special Collections", "library", "Central Campus",
         "Collects, preserves, and makes accessible rare books, manuscripts, photographs, moving images, and architectural drawings in Allen Library South")
    )
    sc_id = cursor.fetchone()[0]

    sc_hours = [
        ("Monday", "13:00", "16:45", False),
        ("Tuesday", "13:00", "16:45", True),
        ("Wednesday", "13:00", "16:45", False),
        ("Thursday", "13:00", "16:45", False),
        ("Friday", "13:00", "16:45", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in sc_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (sc_id, day, open_time, close_time, is_closed)
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

  

   

    # --- Academic Buildings ---

    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Paul G. Allen Center (CSE)", "academic", "Central Campus",
         "Home of the Paul G. Allen School of Computer Science and Engineering")
    )
    cse_id = cursor.fetchone()[0]

    cse_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", "09:00", "17:00", False),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in cse_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (cse_id, day, open_time, close_time, is_closed)
        )

    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Bill & Melinda Gates Center (CSE2)", "academic", "Central Campus",
         "Second building of the Paul G. Allen School, and is open 24/7 for all CSE students through Husky ID")
    )
    gates_id = cursor.fetchone()[0]

    gates_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", "09:00", "17:00", False),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in gates_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (gates_id, day, open_time, close_time, is_closed)
        )

    # Mary Gates Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Mary Gates Hall", "academic", "Central Campus",
         "Academic building with classrooms, advising offices, and the Center for Experiential Learning")
    )
    mgh_id = cursor.fetchone()[0]

    mgh_hours = [
        ("Monday", "07:00", "22:00", False),
        ("Tuesday", "07:00", "22:00", False),
        ("Wednesday", "07:00", "22:00", False),
        ("Thursday", "07:00", "22:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", "09:00", "17:00", False),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in mgh_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (mgh_id, day, open_time, close_time, is_closed)
        )

    # Kane Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Kane Hall", "academic", "Central Campus",
         "Large lecture hall building near Red Square with auditorium-style classrooms")
    )
    kane_id = cursor.fetchone()[0]

    kane_hours = [
        ("Monday", "07:00", "22:00", False),
        ("Tuesday", "07:00", "22:00", False),
        ("Wednesday", "07:00", "22:00", False),
        ("Thursday", "07:00", "22:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in kane_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (kane_id, day, open_time, close_time, is_closed)
        )

    # Savery Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Savery Hall", "academic", "Central Campus",
         "Houses political science, sociology, and other social science departments")
    )
    savery_id = cursor.fetchone()[0]

    savery_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in savery_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (savery_id, day, open_time, close_time, is_closed)
        )

    # --- Student Centers ---

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
        ("Monday", "06:00", "22:00", False),
        ("Tuesday", "06:00", "22:00", False),
        ("Wednesday", "06:00", "22:00", False),
        ("Thursday", "06:00", "22:00", False),
        ("Friday", "06:00", "21:00", False),
        ("Saturday", "09:00", "21:00", False),
        ("Sunday", "09:00", "21:00", False),
    ]

    for day, open_time, close_time, is_closed in ima_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (ima_id, day, open_time, close_time, is_closed)
        )

    # Ethnic Cultural Center
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

    conn.commit()
    conn.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed()