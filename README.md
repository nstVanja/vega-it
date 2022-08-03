# Vega IT izazov za avgust 2022 
#

(function () {
  console.log(1);
  setTimeout(function () { console.log(2) }, 0);
  _function_to_invoke(console.log(3));
  setTimeout(function () { console.log(4) }, 100);
  process.nextTick(function () { console.log(5) });
  console.log(6);
})();

Napiši poziv funkcije umesto '_function_to_invoke' koji će pozvati 'console.log(3)' kako bi osigurali sledeći redosled izvršavanja logova u konzoli: 1,6,5,3,2,4.
Ne bi trebali menjati redosled poziva funkcija.
