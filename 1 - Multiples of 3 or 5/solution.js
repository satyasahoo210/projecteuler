// Find the sum of all the multiples of 3 or 5 below 1000.
function mutiples(below=1000) {
  return new Array(below-1)
    .fill(0)
    .map((_,i) => i+1)
    .filter(i => i%3 == 0 || i%5 == 0)
    .reduce((a,c) => a+c, 0);
}

sm = mutiples(10)
console.log(sm)
