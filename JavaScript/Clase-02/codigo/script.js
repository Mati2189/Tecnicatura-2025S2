// Clase 02 — JavaScript (demo)
function h(t) {
  console.log("\n==============================");
  console.log(t);
  console.log("==============================");
}

h("Variables");
let nombre = "Matías";
const anio = 2025;
console.log({ nombre, anio });

h("Arreglos");
const nums = [1, 2, 3, 4, 5];
console.log("nums:", nums);
console.log("map x2:", nums.map(n => n * 2));
console.log("filter pares:", nums.filter(n => n % 2 === 0));
console.log("reduce suma:", nums.reduce((a, b) => a + b, 0));

h("Funciones");
function saludar(n) { return `Hola, ${n}!`; }
console.log(saludar(nombre));

h("DOM");
document.getElementById("app").textContent = "Salida también en consola ✔";
