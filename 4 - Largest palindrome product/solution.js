function isPalindrome(n) {
  s = n + '';
  return s === s.split('').reverse().join('');
}

let largest = 0;
for (let num1 = 1; num1 < 1000; num1++) {
  for (let num2 = 1; num2 < 1000; num2++) {
    if (isPalindrome(num1 * num2)) {
      largest = num1 * num2;
      console.log(num1, num2)
    }
  }
}

console.log(largest);
