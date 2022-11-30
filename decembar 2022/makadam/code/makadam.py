def voda(makadam):
    total = 0
    levo = 0
    desno = len(makadam)-1
    nivo = 0

    while levo < desno:
        if makadam[levo] < makadam[desno]:
            manji = makadam[levo]
            levo += 1
        else:
            manji = makadam[desno]
            desno -= 1
        nivo = max(nivo, manji)
        total += nivo - manji
    print(total)

print('8 je očekivani rezultat')
voda(makadam=[5, 2, 2, 4, 3, 2, 3, 4])

print('16 je očekivani rezultat')
voda(makadam=[5, 2, 3, 4, 1, 1, 3, 5])
