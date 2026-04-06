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

    # --- Academic Buildings ---

    # Anderson Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Anderson Hall", "academic", "Central Campus",
         "Houses the College of Forest Resources and environmental science programs")
    )
    anderson_id = cursor.fetchone()[0]

    anderson_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in anderson_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (anderson_id, day, open_time, close_time, is_closed)
        )

    # Architecture Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Architecture Hall", "academic", "Central Campus",
         "Home to the College of Built Environments including architecture and landscape architecture")
    )
    arch_id = cursor.fetchone()[0]

    arch_hours = [
        ("Monday", "07:00", "22:00", False),
        ("Tuesday", "07:00", "22:00", False),
        ("Wednesday", "07:00", "22:00", False),
        ("Thursday", "07:00", "22:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", "09:00", "17:00", False),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in arch_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (arch_id, day, open_time, close_time, is_closed)
        )

    # Art Building
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Art Building", "academic", "West Campus",
         "Houses the School of Art + Art History + Design with studios and gallery spaces")
    )
    art_id = cursor.fetchone()[0]

    art_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in art_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (art_id, day, open_time, close_time, is_closed)
        )

    # Bagley Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Bagley Hall", "academic", "Central Campus",
         "Chemistry building with lecture halls, teaching labs, and research facilities")
    )
    bagley_id = cursor.fetchone()[0]

    bagley_hours = [
        ("Monday", "07:00", "21:30", False),
        ("Tuesday", "07:00", "21:30", False),
        ("Wednesday", "07:00", "21:30", False),
        ("Thursday", "07:00", "21:30", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in bagley_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (bagley_id, day, open_time, close_time, is_closed)
        )

    # Benson Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Benson Hall", "academic", "Central Campus",
         "Houses Chemical Engineering and Materials Science & Engineering departments")
    )
    benson_id = cursor.fetchone()[0]

    benson_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in benson_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (benson_id, day, open_time, close_time, is_closed)
        )

    # Clark Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Clark Hall", "academic", "North Campus",
         "Residence hall and classroom space on north campus")
    )
    clark_id = cursor.fetchone()[0]

    clark_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in clark_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (clark_id, day, open_time, close_time, is_closed)
        )

    # Communications Building (CMU)
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Communications Building", "academic", "Central Campus",
         "Home to the Department of Communication and related programs")
    )
    cmu_id = cursor.fetchone()[0]

    cmu_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in cmu_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (cmu_id, day, open_time, close_time, is_closed)
        )

    # Condon Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Condon Hall", "academic", "West Campus",
         "Former law school building, now houses various academic departments and offices")
    )
    condon_id = cursor.fetchone()[0]

    condon_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in condon_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (condon_id, day, open_time, close_time, is_closed)
        )

    # Denny Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Denny Hall", "academic", "Central Campus",
         "Oldest building on campus (1895), houses the Classics and Near Eastern Languages departments")
    )
    denny_id = cursor.fetchone()[0]

    denny_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in denny_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (denny_id, day, open_time, close_time, is_closed)
        )

    # Eagleson Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Eagleson Hall", "academic", "West Campus",
         "Houses academic offices and classroom spaces")
    )
    eagleson_id = cursor.fetchone()[0]

    eagleson_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in eagleson_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (eagleson_id, day, open_time, close_time, is_closed)
        )

    # Electrical Engineering Building
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Electrical & Computer Engineering Building", "academic", "Central Campus",
         "Home to the Electrical and Computer Engineering department with labs and classrooms")
    )
    eeb_id = cursor.fetchone()[0]

    eeb_hours = [
        ("Monday", "07:00", "21:30", False),
        ("Tuesday", "07:00", "21:30", False),
        ("Wednesday", "07:00", "21:30", False),
        ("Thursday", "07:00", "21:30", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", "09:00", "17:00", False),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in eeb_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (eeb_id, day, open_time, close_time, is_closed)
        )

    # Engineering Annex
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Engineering Annex", "academic", "Central Campus",
         "Additional engineering classrooms and lab spaces")
    )
    ega_id = cursor.fetchone()[0]

    ega_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in ega_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (ega_id, day, open_time, close_time, is_closed)
        )

    # Gerberding Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Gerberding Hall", "academic", "Central Campus",
         "Main administration building housing the Office of the President and Provost")
    )
    gerberding_id = cursor.fetchone()[0]

    gerberding_hours = [
        ("Monday", "07:30", "17:00", False),
        ("Tuesday", "07:30", "17:00", False),
        ("Wednesday", "07:30", "17:00", False),
        ("Thursday", "07:30", "17:00", False),
        ("Friday", "07:30", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in gerberding_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (gerberding_id, day, open_time, close_time, is_closed)
        )

    # Gould Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Gould Hall", "academic", "Central Campus",
         "College of Built Environments including urban design and planning programs")
    )
    gould_id = cursor.fetchone()[0]

    gould_hours = [
        ("Monday", "07:00", "22:00", False),
        ("Tuesday", "07:00", "22:00", False),
        ("Wednesday", "07:00", "22:00", False),
        ("Thursday", "07:00", "22:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", "09:00", "17:00", False),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in gould_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (gould_id, day, open_time, close_time, is_closed)
        )

    # Gowen Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Gowen Hall", "academic", "Central Campus",
         "Houses the Jackson School of International Studies and History department")
    )
    gowen_id = cursor.fetchone()[0]

    gowen_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in gowen_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (gowen_id, day, open_time, close_time, is_closed)
        )

    # Guggenheim Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Guggenheim Hall", "academic", "Central Campus",
         "Home to the Department of Aeronautics and Astronautics")
    )
    guggenheim_id = cursor.fetchone()[0]

    guggenheim_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in guggenheim_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (guggenheim_id, day, open_time, close_time, is_closed)
        )

    # Guthrie Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Guthrie Hall", "academic", "Central Campus",
         "Houses the Department of Psychology with research labs and classrooms")
    )
    guthrie_id = cursor.fetchone()[0]

    guthrie_hours = [
        ("Monday", "07:00", "21:30", False),
        ("Tuesday", "07:00", "21:30", False),
        ("Wednesday", "07:00", "21:30", False),
        ("Thursday", "07:00", "21:30", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in guthrie_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (guthrie_id, day, open_time, close_time, is_closed)
        )

    # Henderson Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Henderson Hall", "academic", "West Campus",
         "Academic building with classrooms and departmental offices")
    )
    henderson_id = cursor.fetchone()[0]

    henderson_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in henderson_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (henderson_id, day, open_time, close_time, is_closed)
        )

    # Hitchcock Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Hitchcock Hall", "academic", "Central Campus",
         "Houses the Department of Biology with teaching and research labs")
    )
    hitchcock_id = cursor.fetchone()[0]

    hitchcock_hours = [
        ("Monday", "07:00", "21:30", False),
        ("Tuesday", "07:00", "21:30", False),
        ("Wednesday", "07:00", "21:30", False),
        ("Thursday", "07:00", "21:30", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in hitchcock_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (hitchcock_id, day, open_time, close_time, is_closed)
        )

    # Hutchinson Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Hutchinson Hall", "academic", "West Campus",
         "Home to the School of Drama with performance and rehearsal spaces")
    )
    hutchinson_id = cursor.fetchone()[0]

    hutchinson_hours = [
        ("Monday", "07:00", "22:00", False),
        ("Tuesday", "07:00", "22:00", False),
        ("Wednesday", "07:00", "22:00", False),
        ("Thursday", "07:00", "22:00", False),
        ("Friday", "07:00", "22:00", False),
        ("Saturday", "09:00", "22:00", False),
        ("Sunday", "12:00", "22:00", False),
    ]

    for day, open_time, close_time, is_closed in hutchinson_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (hutchinson_id, day, open_time, close_time, is_closed)
        )

    # Johnson Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Johnson Hall", "academic", "Central Campus",
         "Houses the Department of Earth and Space Sciences with labs and classrooms")
    )
    johnson_id = cursor.fetchone()[0]

    johnson_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in johnson_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (johnson_id, day, open_time, close_time, is_closed)
        )

    # Loew Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Loew Hall", "academic", "Central Campus",
         "Civil and Environmental Engineering building with labs and classrooms")
    )
    loew_id = cursor.fetchone()[0]

    loew_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in loew_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (loew_id, day, open_time, close_time, is_closed)
        )

    # Mechanical Engineering Building
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Mechanical Engineering Building", "academic", "Central Campus",
         "Home to the Mechanical Engineering department with machine shops and labs")
    )
    meb_id = cursor.fetchone()[0]

    meb_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in meb_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (meb_id, day, open_time, close_time, is_closed)
        )

    # Miller Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Miller Hall", "academic", "Central Campus",
         "Houses the College of Education with classrooms and faculty offices")
    )
    miller_id = cursor.fetchone()[0]

    miller_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in miller_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (miller_id, day, open_time, close_time, is_closed)
        )

    # More Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("More Hall", "academic", "Central Campus",
         "Engineering building with classrooms and structural engineering labs")
    )
    more_id = cursor.fetchone()[0]

    more_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in more_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (more_id, day, open_time, close_time, is_closed)
        )

    # Mueller Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Mueller Hall", "academic", "Central Campus",
         "Engineering building adjacent to the engineering quad")
    )
    mueller_id = cursor.fetchone()[0]

    mueller_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in mueller_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (mueller_id, day, open_time, close_time, is_closed)
        )

    # Padelford Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Padelford Hall", "academic", "Central Campus",
         "Large classroom building housing the English department and language programs")
    )
    padelford_id = cursor.fetchone()[0]

    padelford_hours = [
        ("Monday", "07:00", "21:30", False),
        ("Tuesday", "07:00", "21:30", False),
        ("Wednesday", "07:00", "21:30", False),
        ("Thursday", "07:00", "21:30", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in padelford_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (padelford_id, day, open_time, close_time, is_closed)
        )

    # Parrington Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Parrington Hall", "academic", "Central Campus",
         "Historic building on the Quad housing academic departments")
    )
    parrington_id = cursor.fetchone()[0]

    parrington_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in parrington_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (parrington_id, day, open_time, close_time, is_closed)
        )

    # Physics Astronomy Building
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Physics Astronomy Building", "academic", "Central Campus",
         "Houses the Physics and Astronomy departments with lecture halls and research labs")
    )
    pab_id = cursor.fetchone()[0]

    pab_hours = [
        ("Monday", "07:00", "21:30", False),
        ("Tuesday", "07:00", "21:30", False),
        ("Wednesday", "07:00", "21:30", False),
        ("Thursday", "07:00", "21:30", False),
        ("Friday", "07:00", "21:30", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in pab_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (pab_id, day, open_time, close_time, is_closed)
        )

    # Raitt Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Raitt Hall", "academic", "Central Campus",
         "Houses the Department of Anthropology and the Linguistics department")
    )
    raitt_id = cursor.fetchone()[0]

    raitt_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in raitt_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (raitt_id, day, open_time, close_time, is_closed)
        )

    # Roberts Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Roberts Hall", "academic", "Central Campus",
         "Engineering building with classrooms and lab spaces")
    )
    roberts_id = cursor.fetchone()[0]

    roberts_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in roberts_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (roberts_id, day, open_time, close_time, is_closed)
        )

    # Schmitz Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Schmitz Hall", "academic", "Central Campus",
         "Brutalist-style administration building housing student services and financial aid")
    )
    schmitz_id = cursor.fetchone()[0]

    schmitz_hours = [
        ("Monday", "07:30", "17:00", False),
        ("Tuesday", "07:30", "17:00", False),
        ("Wednesday", "07:30", "17:00", False),
        ("Thursday", "07:30", "17:00", False),
        ("Friday", "07:30", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in schmitz_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (schmitz_id, day, open_time, close_time, is_closed)
        )

    # Sieg Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Sieg Hall", "academic", "Central Campus",
         "Houses the Department of Mathematics and computer labs")
    )
    sieg_id = cursor.fetchone()[0]

    sieg_hours = [
        ("Monday", "07:00", "21:30", False),
        ("Tuesday", "07:00", "21:30", False),
        ("Wednesday", "07:00", "21:30", False),
        ("Thursday", "07:00", "21:30", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in sieg_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (sieg_id, day, open_time, close_time, is_closed)
        )

    # Smith Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Smith Hall", "academic", "Central Campus",
         "Houses the Department of History and various humanities programs")
    )
    smith_id = cursor.fetchone()[0]

    smith_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in smith_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (smith_id, day, open_time, close_time, is_closed)
        )

    # Thomson Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Thomson Hall", "academic", "Central Campus",
         "Large lecture hall building with auditorium-style classrooms for introductory courses")
    )
    thomson_id = cursor.fetchone()[0]

    thomson_hours = [
        ("Monday", "07:00", "21:30", False),
        ("Tuesday", "07:00", "21:30", False),
        ("Wednesday", "07:00", "21:30", False),
        ("Thursday", "07:00", "21:30", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in thomson_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (thomson_id, day, open_time, close_time, is_closed)
        )

    # Wilcox Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Wilcox Hall", "academic", "Central Campus",
         "Engineering building near the engineering quad")
    )
    wilcox_id = cursor.fetchone()[0]

    wilcox_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in wilcox_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (wilcox_id, day, open_time, close_time, is_closed)
        )

    # William H. Gates Hall (Law)
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("William H. Gates Hall", "academic", "North Campus",
         "Houses the UW School of Law with classrooms, moot courtroom, and the Gallagher Law Library")
    )
    gates_law_id = cursor.fetchone()[0]

    gates_law_hours = [
        ("Monday", "07:00", "22:00", False),
        ("Tuesday", "07:00", "22:00", False),
        ("Wednesday", "07:00", "22:00", False),
        ("Thursday", "07:00", "22:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", "09:00", "17:00", False),
        ("Sunday", "12:00", "22:00", False),
    ]

    for day, open_time, close_time, is_closed in gates_law_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (gates_law_id, day, open_time, close_time, is_closed)
        )

    # Paccar Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Paccar Hall", "academic", "North Campus",
         "Home to the Foster School of Business with classrooms, study rooms, and the business library")
    )
    paccar_id = cursor.fetchone()[0]

    paccar_hours = [
        ("Monday", "07:00", "22:00", False),
        ("Tuesday", "07:00", "22:00", False),
        ("Wednesday", "07:00", "22:00", False),
        ("Thursday", "07:00", "22:00", False),
        ("Friday", "07:00", "18:00", False),
        ("Saturday", "09:00", "17:00", False),
        ("Sunday", "12:00", "20:00", False),
    ]

    for day, open_time, close_time, is_closed in paccar_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (paccar_id, day, open_time, close_time, is_closed)
        )

    # Meany Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Meany Hall", "academic", "Central Campus",
         "Performing arts venue with a main theater for concerts, lectures, and dance performances")
    )
    meany_id = cursor.fetchone()[0]

    meany_hours = [
        ("Monday", "07:00", "22:00", False),
        ("Tuesday", "07:00", "22:00", False),
        ("Wednesday", "07:00", "22:00", False),
        ("Thursday", "07:00", "22:00", False),
        ("Friday", "07:00", "22:00", False),
        ("Saturday", "09:00", "22:00", False),
        ("Sunday", "12:00", "22:00", False),
    ]

    for day, open_time, close_time, is_closed in meany_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (meany_id, day, open_time, close_time, is_closed)
        )

    # Bloedel Hall
    cursor.execute(
        "INSERT INTO resources (name, type, location, description) VALUES (%s, %s, %s, %s) RETURNING id",
        ("Bloedel Hall", "academic", "Central Campus",
         "Houses the School of Environmental and Forest Sciences")
    )
    bloedel_id = cursor.fetchone()[0]

    bloedel_hours = [
        ("Monday", "07:00", "21:00", False),
        ("Tuesday", "07:00", "21:00", False),
        ("Wednesday", "07:00", "21:00", False),
        ("Thursday", "07:00", "21:00", False),
        ("Friday", "07:00", "17:00", False),
        ("Saturday", None, None, True),
        ("Sunday", None, None, True),
    ]

    for day, open_time, close_time, is_closed in bloedel_hours:
        cursor.execute(
            "INSERT INTO hours (resource_id, day_of_week, open_time, close_time, is_closed) VALUES (%s, %s, %s, %s, %s)",
            (bloedel_id, day, open_time, close_time, is_closed)
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
    conn.commit()
    conn.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed()