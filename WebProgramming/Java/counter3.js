
let counter = 0;

// Funcion que incrementa en uno el valor counter
function count() {
  counter++;
  document.querySelector('#counter').innerHTML = counter;

  //Si el valor counter es divisor de 10
  //se nos mostrará un mensaje pop up in
  if (counter % 10 === 0) {
    // Con (% 10 ===0) indicamos que si el residuo de la división counter/10 es igual  a 0
    //se ejecute el código.
    alert (`Counter is at ${counter}!/s`)
  }
}
