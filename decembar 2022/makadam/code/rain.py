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

print('10 je očekivani rezultat')
voda(makadam=[3, 0, 0, 2, 0, 4])

print('10 je očekivani rezultat')
voda(makadam=[7, 4, 0, 9])

print('0 je očekivani rezultat')
voda(makadam=[6, 9, 9])

print('6 je očekivani rezultat')
voda(makadam=[0, 1, 0, 2, 1, 0, 1,  3, 2, 1, 2, 1])

print('3 je očekivani rezultat')
voda(makadam=[3, 0, 3])

print('0 je očekivani rezultat')
voda(makadam=[0, 4, 5, 1])

print('10 je očekivani rezultat')
voda(makadam=[1, 4, 2, 5, 0, 6, 2, 3, 4])
