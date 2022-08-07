(function () {
  console.log(1);
  setTimeout(function () { console.log(2) }, 0);
  
  //process.nextTick(() => {
  //    process.nextTick(console.log.bind(console, 3));
  //});
  
  Promise.resolve().then(() => console.log(3));
  
  setTimeout(function () { console.log(4) }, 100);
  process.nextTick(function () { console.log(5) });
  console.log(6);
})();
