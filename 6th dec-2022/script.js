var elements = document.getElementsByTagName("input");
var n = elements.length;

var brojInputa = function (broj) {
  return function () {
    console.log("This is element #" + broj);
  };
};

for (var i = 0; i < n; i++) {
  elements[i].onclick = brojInputa(i + 1);
}


