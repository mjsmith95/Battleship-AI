from time import time
from database_connector import get_connection
from populate_database import populate_database

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
        if cur.execute("SELECT COUNT(*) FROM carriers;").fetchone()[0] == 0:
            cur.execute("INSERT INTO carriers VALUES (NULL, NULL, NULL, NULL, NULL);")

        cur.execute(
            f"""
                        DELETE FROM battleships
                        WHERE cord0 = {coordinate}
                        OR cord1 = {coordinate}
                        OR cord2 = {coordinate}
                        OR cord3 = {coordinate}
                    """
        )
        if cur.execute("SELECT COUNT(*) FROM battleships;").fetchone()[0] == 0:
            cur.execute("INSERT INTO battleships VALUES (NULL, NULL, NULL, NULL);")

        cur.execute(
            f"""
                        DELETE FROM destroyers
                        WHERE cord0 = {coordinate}
                        OR cord1 = {coordinate}
                        OR cord2 = {coordinate}
                    """
        )
        if cur.execute("SELECT COUNT(*) FROM destroyers;").fetchone()[0] == 0:
            cur.execute("INSERT INTO destroyers VALUES (NULL, NULL, NULL);")

        cur.execute(
            f"""
                        DELETE FROM submarines
                        WHERE cord0 = {coordinate}
                        OR cord1 = {coordinate}
                        OR cord2 = {coordinate}
                    """
        )
        if cur.execute("SELECT COUNT(*) FROM submarines;").fetchone()[0] == 0:
            cur.execute("INSERT INTO submarines VALUES (NULL, NULL, NULL);")

        cur.execute(
            f"""
                        DELETE FROM patrol_boats
                        WHERE cord0 = {coordinate}
                        OR cord1 = {coordinate}
                    """
        )
        if cur.execute("SELECT COUNT(*) FROM patrol_boats;").fetchone()[0] == 0:
            cur.execute("INSERT INTO patrol_boats VALUES (NULL, NULL);")

        # print("Carriers remaining: " + str(cur.execute("SELECT COUNT(*) FROM carriers;").fetchone()[0]))
        # print("Battleships remaining: " + str(cur.execute("SELECT COUNT(*) FROM battleships;").fetchone()[0]))
        # print("Destroyers remaining: " + str(cur.execute("SELECT COUNT(*) FROM destroyers;").fetchone()[0]))
        # print("Submarines remaining: " + str(cur.execute("SELECT COUNT(*) FROM submarines;").fetchone()[0]))
        # print("Patrol boats remaining: " + str(cur.execute("SELECT COUNT(*) FROM patrol_boats;").fetchone()[0]))

        conn.commit()
    finally:
        conn.close()


def remove_ship_by_type(ship_name):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(f"DELETE FROM {ship_name};")
        col_count = cur.execute(f"pragma table_info({ship_name});").fetchall()[-1][0] + 1
        cur.execute(f"INSERT INTO {ship_name} VALUES ({('NULL, ' * col_count)[:-2]});")

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


def check_duplicates(permutation):
    perm_set = set()
    for coord in permutation:
        if coord in perm_set:
            return True
        elif coord is not None:
            perm_set.add(coord)
    return True


def generate_configurations():
    x = 0
    start = time()

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        for permutation in cur.execute(
                """
                    SELECT * FROM carriers
                    CROSS JOIN battleships
                    CROSS JOIN destroyers
                    CROSS JOIN submarines
                    CROSS JOIN patrol_boats;
                """
        ):
            if check_duplicates(permutation):
                carrier = permutation[:5]
                battleship = permutation[5:9]
                destroyer = permutation[9:12]
                submarine = permutation[12:15]
                patrol_boat = permutation[15:]

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

                if time() - start > 60:  # stop after a minute
                    print("timed out")
                    return

        # for carrier in cur.execute("SELECT * FROM carriers;").fetchall():
        #     for battleship in cur.execute("SELECT * FROM battleships;").fetchall():
        #         if check_overlap(battleship, carrier):
        #             continue
        #         for destroyer in cur.execute("SELECT * FROM destroyers;").fetchall():
        #             if check_overlap(destroyer, carrier, battleship):
        #                 continue
        #             for submarine in cur.execute("SELECT * FROM submarines;").fetchall():
        #                 if check_overlap(submarine, carrier, battleship, destroyer):
        #                     continue
        #                 for patrol_boat in cur.execute("SELECT * FROM patrol_boats;").fetchall():
        #                     if check_overlap(patrol_boat, carrier, battleship, destroyer, submarine):
        #                         continue
        #
        #                     if non_sunk_hits:
        #                         for coordinate in non_sunk_hits:
        #                             if coordinate in carrier or \
        #                                     coordinate in battleship or \
        #                                     coordinate in destroyer or \
        #                                     coordinate in submarine or \
        #                                     coordinate in patrol_boat:
        #                                 x += 1
        #                                 yield carrier, battleship, destroyer, submarine, patrol_boat
        #                     else:
        #                         x += 1
        #                         yield carrier, battleship, destroyer, submarine, patrol_boat
        #
        #                     if time() - start > 60:  # stop after a minute
        #                         print("timed out")
        #                         return

    finally:
        # print(time() - start)
        # print(x)

        if conn:
            conn.close()


populate_database()  # populate database immediately when package is loaded
if __name__ == "__main__":
    for _ in generate_configurations():
        pass
