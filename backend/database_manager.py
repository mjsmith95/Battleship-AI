from time import time
from populate_database import get_connection, populate_database


non_sunk_hits = []


def remove_ship_by_coordinate(coordinate):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            f"""
                    DELETE FROM carriers
                    WHERE cord0 = {coordinate}
                    OR cord1 = {coordinate}
                    OR cord2 = {coordinate}
                    OR cord3 = {coordinate}
                    OR cord4 = {coordinate}
                """
        )
        cur.execute(
            f"""
                        DELETE FROM battleships
                        WHERE cord0 = {coordinate}
                        OR cord1 = {coordinate}
                        OR cord2 = {coordinate}
                        OR cord3 = {coordinate}
                    """
        )
        cur.execute(
            f"""
                        DELETE FROM destroyers
                        WHERE cord0 = {coordinate}
                        OR cord1 = {coordinate}
                        OR cord2 = {coordinate}
                    """
        )
        cur.execute(
            f"""
                        DELETE FROM submarines
                        WHERE cord0 = {coordinate}
                        OR cord1 = {coordinate}
                        OR cord2 = {coordinate}
                    """
        )
        cur.execute(
            f"""
                        DELETE FROM patrol_boats
                        WHERE cord0 = {coordinate}
                        OR cord1 = {coordinate}
                    """
        )

        print("Carriers remaining: " + str(cur.execute("SELECT COUNT(*) FROM carriers;").fetchone()[0]))
        print("Battleships remaining: " + str(cur.execute("SELECT COUNT(*) FROM battleships;").fetchone()[0]))
        print("Destroyers remaining: " + str(cur.execute("SELECT COUNT(*) FROM destroyers;").fetchone()[0]))
        print("Submarines remaining: " + str(cur.execute("SELECT COUNT(*) FROM submarines;").fetchone()[0]))
        print("Patrol boats remaining: " + str(cur.execute("SELECT COUNT(*) FROM patrol_boats;").fetchone()[0]))

        conn.commit()
    finally:
        conn.close()


def remove_ship_by_type(ship_name):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(f"DELETE FROM {ship_name};")

        conn.commit()
    finally:
        if conn:
            conn.close()


def check_overlap(new_ship, *old_ships):
    """Assume all old ships do not overlap. Check each old ship against new ship. If anything overlaps, return True,
    otherwise return False."""
    for ship in old_ships:
        for coordinate in ship:
            if coordinate in new_ship:
                return True
    return False


def generate_configurations():
    x = 0
    start = time()

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        for carrier in cur.execute("SELECT * FROM carriers;").fetchall():
            for battleship in cur.execute("SELECT * FROM battleships;").fetchall():
                if check_overlap(battleship, carrier):
                    continue
                for destroyer in cur.execute("SELECT * FROM destroyers;").fetchall():
                    if check_overlap(destroyer, carrier, battleship):
                        continue
                    for submarine in cur.execute("SELECT * FROM submarines;").fetchall():
                        if check_overlap(submarine, carrier, battleship, destroyer):
                            continue
                        for patrol_boat in cur.execute("SELECT * FROM patrol_boats;").fetchall():
                            if check_overlap(patrol_boat, carrier, battleship, destroyer, submarine):
                                continue

                            if non_sunk_hits:
                                for coordinate in non_sunk_hits:
                                    if coordinate in carrier or \
                                            coordinate in battleship or \
                                            coordinate in destroyer or \
                                            coordinate in submarine or \
                                            coordinate in patrol_boat:
                                        x += 1
                                        yield carrier, battleship, destroyer, submarine, patrol_boat
                            else:
                                x += 1
                                yield carrier, battleship, destroyer, submarine, patrol_boat

                            if time() - start > 600:
                                return

    finally:
        print(time() - start)
        print(x)

        if conn:
            conn.close()


if __name__ == "__main__":
    populate_database()
    # remove_miss(0)
    for _ in generate_configurations():
        pass
