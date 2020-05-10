import sqlite3


def get_connection():
    return sqlite3.connect('ship_configurations.db')  # this even creates the file if it doesn't exist


def create_tables():
    """Make sure each table exists. If not, create it."""
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS carriers
                (cord0 INTEGER, cord1 INTEGER, cord2 INTEGER, cord3 INTEGER, cord4 INTEGER);
            """
        )
        cur.execute("DELETE FROM carriers;")

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS battleships
                (cord0 INTEGER, cord1 INTEGER, cord2 INTEGER, cord3 INTEGER);
            """
        )
        cur.execute("DELETE FROM battleships;")

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS destroyers
                (cord0 INTEGER, cord1 INTEGER, cord2 INTEGER);
            """
        )
        cur.execute("DELETE FROM destroyers;")

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS submarines
                (cord0 INTEGER, cord1 INTEGER, cord2 INTEGER);
            """
        )
        cur.execute("DELETE FROM submarines;")

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS patrol_boats
                (cord0 INTEGER, cord1 INTEGER);
            """
        )
        cur.execute("DELETE FROM patrol_boats;")

        conn.commit()
    finally:
        if conn:
            conn.close()


def populate_carriers():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        for i in range(10):
            for j in range(6):
                h_start = i*10 + j
                v_start = j*10 + i
                h = (h_start, h_start+1, h_start+2, h_start+3, h_start+4)
                v = (v_start, v_start+10, v_start+20, v_start+30, v_start+40)

                cur.execute(
                    f"""
                        INSERT INTO carriers
                        VALUES ({h[0]}, {h[1]}, {h[2]}, {h[3]}, {h[4]});
                    """
                )
                cur.execute(
                    f"""
                        INSERT INTO carriers
                        VALUES ({v[0]}, {v[1]}, {v[2]}, {v[3]}, {v[4]});
                    """
                )

        conn.commit()
    finally:
        if conn:
            conn.close()


def populate_battleships():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        for i in range(10):
            for j in range(7):
                h_start = i*10 + j
                v_start = j*10 + i
                h = (h_start, h_start+1, h_start+2, h_start+3)
                v = (v_start, v_start+10, v_start+20, v_start+30)

                cur.execute(
                    f"""
                        INSERT INTO battleships
                        VALUES ({h[0]}, {h[1]}, {h[2]}, {h[3]});
                    """
                )
                cur.execute(
                    f"""
                        INSERT INTO battleships
                        VALUES ({v[0]}, {v[1]}, {v[2]}, {v[3]});
                    """
                )

        conn.commit()
    finally:
        if conn:
            conn.close()


def populate_destroyers():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        for i in range(10):
            for j in range(8):
                h_start = i*10 + j
                v_start = j*10 + i
                h = (h_start, h_start+1, h_start+2)
                v = (v_start, v_start+10, v_start+20)

                cur.execute(
                    f"""
                        INSERT INTO destroyers
                        VALUES ({h[0]}, {h[1]}, {h[2]});
                    """
                )
                cur.execute(
                    f"""
                        INSERT INTO destroyers
                        VALUES ({v[0]}, {v[1]}, {v[2]});
                    """
                )

        conn.commit()
    finally:
        if conn:
            conn.close()


def populate_submarines():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        for i in range(10):
            for j in range(8):
                h_start = i*10 + j
                v_start = j*10 + i
                h = (h_start, h_start+1, h_start+2)
                v = (v_start, v_start+10, v_start+20)

                cur.execute(
                    f"""
                        INSERT INTO submarines
                        VALUES ({h[0]}, {h[1]}, {h[2]});
                    """
                )
                cur.execute(
                    f"""
                        INSERT INTO submarines
                        VALUES ({v[0]}, {v[1]}, {v[2]});
                    """
                )

        conn.commit()
    finally:
        if conn:
            conn.close()


def populate_patrol_boats():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        for i in range(10):
            for j in range(9):
                h_start = i*10 + j
                v_start = j*10 + i
                h = (h_start, h_start+1)
                v = (v_start, v_start+10)

                cur.execute(
                    f"""
                        INSERT INTO patrol_boats
                        VALUES ({h[0]}, {h[1]});
                    """
                )
                cur.execute(
                    f"""
                        INSERT INTO patrol_boats
                        VALUES ({v[0]}, {v[1]});
                    """
                )

        conn.commit()
    finally:
        if conn:
            conn.close()


def populate_database():
    """Creates, cleans, and populates the tables in the database."""
    create_tables()
    populate_carriers()
    populate_battleships()
    populate_destroyers()
    populate_submarines()
    populate_patrol_boats()


if __name__ == "__main__":
    populate_database()
