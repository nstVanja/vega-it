### Vega IT izazov

#### Prvi zadatak

Uzgajali ste biljku i, posle tri meseca, došlo je vreme da poberete plodove (cveće). Tokom faze rasta ste dodavali vodu, đubrivo i održavali ste idealnu temperaturu.
Vreme je da proverite koliko je biljka porasla.

Biljka je predstavljena horizontalno, s leva na desno: ---@---@---@

Stabljiku sačinjavaju crtice, a cvetovi su predstavljeni simbolima. Biljka uvek počinje stabljikom i završava se cvetovima.

- Seme daje tip cveta na stabljici (@, #, a,...)
- Onoliko puta koliko ste zalili biljku, te dužine joj je stabljika i sastoji se od isto toliko segmenata
- Đubrivo povećava broj cvetova na kraju jednog segmenta
- Ukoliko temperatura nije u opsegu između 20 i 30 stepeni, svo cveće na stabljici se suši, osim jednog - poslednjeg na stabljici.

Primer 1:
Cvet: @
Voda: 3
Đubrivo: 3
Temperatura: 25
Rezultat: ---@@@---@@@---@@@

Primer 2:
Cvet: #
Voda: 3
Đubrivo: 3
Temperatura: 15
Rezultat: ---------#

Zadatak: 

Napisati algoritam koji prikazuje biljku na osnovu 4 zadata parametra: cvet, voda, đubrivo i temperatura.
