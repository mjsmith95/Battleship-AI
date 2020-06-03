from time import time
from load_ships import *

non_sunk_hits = []

carriers = load_carriers()
battleships = load_battleships()
destroyers = load_destroyers()
submarines = load_submarines()
patrol_boats = load_patrol_boats()


def remove_ship_by_coordinate(coordinate):
    global carriers, battleships, destroyers, submarines, patrol_boats

    if carriers != [()]:
        for ship in carriers:
            for ship_coord in ship:
                if ship_coord == coordinate:
                    carriers.remove(ship)
                    break
        if len(carriers) == 0:
            carriers = [()]

    if battleships != [()]:
        for ship in battleships:
            for ship_coord in ship:
                if ship_coord == coordinate:
                    battleships.remove(ship)
                    break
        if len(battleships) == 0:
            battleships = [()]

    if destroyers != [()]:
        for ship in destroyers:
            for ship_coord in ship:
                if ship_coord == coordinate:
                    destroyers.remove(ship)
                    break
        if len(destroyers) == 0:
            destroyers = [()]

    if submarines != [()]:
        for ship in submarines:
            for ship_coord in ship:
                if ship_coord == coordinate:
                    submarines.remove(ship)
                    break
        if len(submarines) == 0:
            submarines = [()]

    if patrol_boats != [()]:
        for ship in patrol_boats:
            for ship_coord in ship:
                if ship_coord == coordinate:
                    patrol_boats.remove(ship)
                    break
        if len(patrol_boats) == 0:
            patrol_boats = [()]


def remove_ship_by_type(ship_name):
    global carriers, battleships, destroyers, submarines, patrol_boats

    if ship_name == "carriers":
        carriers = [()]
    elif ship_name == "battleships":
        battleships = [()]
    elif ship_name == "destroyers":
        destroyers = [()]
    elif ship_name == "submarines":
        submarines = [()]
    elif ship_name == "patrol_boats":
        patrol_boats = [()]


def check_overlap(new_ship, *old_ships):
    """Assume all old ships do not overlap. Check each old ship against new ship. If anything overlaps, return True,
    otherwise return False."""
    if new_ship == [()]:
        return False

    for ship in old_ships:
        if ship == [()]:
            continue
        for coordinate in ship:
            if coordinate in new_ship:
                return True
    return False


def generate_configurations():
    x = 0
    start = time()

    for carrier in carriers:
        for battleship in battleships:
            if check_overlap(battleship, carrier):
                continue
            for destroyer in destroyers:
                if check_overlap(destroyer, carrier, battleship):
                    continue
                for submarine in submarines:
                    if check_overlap(submarine, carrier, battleship, destroyer):
                        continue
                    for patrol_boat in patrol_boats:
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

                        if time() - start > 60:  # stop after # seconds
                            print("timed out")
                            # print(time() - start)
                            # print(x)
                            return


if __name__ == "__main__":
    for _ in generate_configurations():
        pass
