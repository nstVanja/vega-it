document.querySelector("#numBtn").addEventListener("click", (e) => {
  e.preventDefault();

  let number = document.querySelector("#brojStudenata").value;

  let counter = brojStudenata(number);

  let podaci = document.querySelector("#podaci");

  podaci.innerHTML = `<p>Ukupan broj studenata koji sede je <b>${counter}.</b></p>
                      <p>___________________________________</p>`;
});

function brojStudenata(n) {
  // n => broj studenata
  var arr = [];
  // var element;
  var counter = 0;

  for (let i = 0; i < n; i++) {
    arr[i] = false; // false => student stoji, true => student sedi
  }

  // element = arr;
  // counter = element.filter((x) => x === true).length;
  console.log("-------------------------------------------");
  console.log("Inicijalno stanje - broj studenata:", arr.length);
  console.log("-------------------------------------------");

  for (let prolaz = 1; prolaz <= n; prolaz++) {
    arr.reverse();

    for (let i = prolaz - 1; i < arr.length; i = i + prolaz) {
      arr[i] = !arr[i];
    }
    // element = arr;
    counter = arr.filter((x) => x === true).length;
    // console.log("Raspored", element.reverse());
    console.log("Prolaz nastavnika:", prolaz);
    console.log("Ukupan broj studenata koji sede je", counter);
    console.log("-------------------------------------------");
  }

  return counter;
}
