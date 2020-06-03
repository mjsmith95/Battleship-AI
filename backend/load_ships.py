from random import shuffle


def load_carriers():
    carriers = []
    for i in range(10):
        for j in range(6):
            h_start = i*10 + j
            v_start = j*10 + i
            carriers.append((h_start, h_start+1, h_start+2, h_start+3, h_start+4))
            carriers.append((v_start, v_start+10, v_start+20, v_start+30, v_start+40))

    return shuffle(carriers)


def load_battleships():
    battleships = []
    for i in range(10):
        for j in range(7):
            h_start = i*10 + j
            v_start = j*10 + i
            battleships.append((h_start, h_start+1, h_start+2, h_start+3))
            battleships.append((v_start, v_start+10, v_start+20, v_start+30))

    return shuffle(battleships)


def load_destroyers():
    destroyers = []
    for i in range(10):
        for j in range(8):
            h_start = i*10 + j
            v_start = j*10 + i
            destroyers.append((h_start, h_start+1, h_start+2))
            destroyers.append((v_start, v_start+10, v_start+20))

    return shuffle(destroyers)


def load_submarines():
    submarines = []
    for i in range(10):
        for j in range(8):
            h_start = i*10 + j
            v_start = j*10 + i
            submarines.append((h_start, h_start+1, h_start+2))
            submarines.append((v_start, v_start+10, v_start+20))

    return shuffle(submarines)


def load_patrol_boats():
    patrol_boats = []
    for i in range(10):
        for j in range(9):
            h_start = i*10 + j
            v_start = j*10 + i
            patrol_boats.append((h_start, h_start+1))
            patrol_boats.append((v_start, v_start+10))

    return shuffle(patrol_boats)
