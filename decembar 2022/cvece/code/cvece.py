def basta(cvet, voda, djubrivo, temp):
    rezultat = ''
    segment = ''
    crta = '-'
    j = 0
   
    i=0
    while i < voda:
        segment += crta
        i += 1
    
    i = 0
    while i < voda:
        rezultat += segment 
        i += 1

        if temp > 20 and temp < 30:

            j = 0
            while j < djubrivo:
                rezultat += cvet
                j += 1
        
    if (temp < 20 or temp > 30) or djubrivo == 0:
            rezultat += cvet

    print(rezultat)

basta(cvet = '@', voda = 3, djubrivo = 3, temp = 25)
print('---@@@---@@@---@@@               cvet = @, voda = 3, djubrivo = 3, temp = 25')

basta(cvet = '#', voda = 3, djubrivo = 3, temp = 15)
print('---------#                       cvet = #, voda = 3, djubrivo = 3, temp = 15')

basta(cvet = '?', voda = 5, djubrivo = 0, temp = 28)
print('-------------------------?       cvet = ?, voda = 5, djubrivo = 0, temp = 25')

basta(cvet = '*', voda = 5, djubrivo = 0, temp = 10)
print('-------------------------*       cvet = *, voda = 5, djubrivo = 0, temp = 10')