// By considering the terms in the Fibonacci sequence whose values do not exceed four million,
// find the sum of the even-valued terms.

function solution(limit = 4000000) {
  let [a, b] = [0, 1];
  let sm = 0;

  while (b < limit) {
    [a, b] = [b, a + b];
    if (!(b & 1)) {
      sm += b;
    }
  }

  return sm
}

console.log(solution())
