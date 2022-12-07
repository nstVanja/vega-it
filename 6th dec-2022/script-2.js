Array
  .from(document.getElementsByTagName("input"))
  .forEach((inputPolje, i) => {
    inputPolje.addEventListener("click", () => {
      console.log("This is element #" + (i + 1));
    });
});


