import ships_manager as sm

# names of the SQL table containing the ship type
CARRIER = "carriers"
BATTLESHIP = "battleships"
DESTROYER = "destroyers"
SUBMARINE = "submarines"
PATROL_BOAT = "patrol_boats"


def update_heatmap(configuration, heatmap):
    for ship in configuration:
        if ship == [()]:
            continue
        for coordinate in ship:
            heatmap[coordinate] += 1


def log_hit(coordinate):
    heatmap = [0 for _ in range(100)]
    num_configurations = 0

    sm.non_sunk_hits.append(coordinate)

    for configuration in sm.generate_configurations():
        update_heatmap(configuration, heatmap)
        num_configurations += 1

    return heatmap, num_configurations


def log_miss(coordinate):
    heatmap = [0 for _ in range(100)]
    num_configurations = 0

    sm.remove_ship_by_coordinate(coordinate)

    for configuration in sm.generate_configurations():
        update_heatmap(configuration, heatmap)
        num_configurations += 1

    return heatmap, num_configurations


def log_sunk_ship(ship_type, *coordinates):
    heatmap = [0 for _ in range(100)]
    num_configurations = 0

    sm.remove_ship_by_type(ship_type)
    for coordinate in coordinates:
        if coordinate in sm.non_sunk_hits:
            sm.non_sunk_hits.remove(coordinate)
        sm.remove_ship_by_coordinate(coordinate)

    for configuration in sm.generate_configurations():
        update_heatmap(configuration, heatmap)
        num_configurations += 1

    return heatmap, num_configurations


def test():
    heatmap, num_configurations = log_miss(0)
    print(heatmap)
    print(num_configurations)
    print()

    heatmap, num_configurations = log_hit(55)
    print(heatmap)
    print(num_configurations)
    print()

    heatmap, num_configurations = log_sunk_ship(PATROL_BOAT, 45, 55)
    print(heatmap)
    print(num_configurations)
    print()


if __name__ == "__main__":
    test()
