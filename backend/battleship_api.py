import database_manager as db

CARRIER = "carrier"
BATTLESHIP = "battleship"
DESTROYER = "destroyer"
SUBMARINE = "submarine"
PATROL_BOAT = "patrol_boat"


def update_heatmap(configuration, heatmap):
    for ship in configuration:
        for coordinate in ship:
            heatmap[coordinate] += 1


def log_hit(coordinate):
    heatmap = [0 for _ in range(100)]
    num_configurations = 0

    db.non_sunk_hits.append(coordinate)

    for configuration in db.generate_configurations():
        update_heatmap(configuration, heatmap)
        num_configurations += 1

    return heatmap, num_configurations


def log_miss(coordinate):
    heatmap = [0 for _ in range(100)]
    num_configurations = 0

    db.remove_ship_by_coordinate(coordinate)

    for configuration in db.generate_configurations():
        update_heatmap(configuration, heatmap)
        num_configurations += 1

    return heatmap, num_configurations


def log_sunk_ship(ship_type, *coordinates):
    heatmap = [0 for _ in range(100)]
    num_configurations = 0

    db.remove_ship_by_type(ship_type)
    for coordinate in coordinates:
        db.non_sunk_hits.remove(coordinate)
        db.remove_ship_by_coordinate(coordinate)

    for configuration in db.generate_configurations():
        update_heatmap(configuration, heatmap)
        num_configurations += 1

    return heatmap, num_configurations
