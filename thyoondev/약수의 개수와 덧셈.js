const countMea = (num) => {
  let count = 0;
  for (let i = 1; i <= num + 1; i++) {
    if (num % i === 0) {
      count++;
    }
  }
  return count;
};

function solution(left, right) {
  var answer = 0;
  for (let i = left; i <= right; i++) {
    countMea(i) % 2 === 0 ? (answer += i) : (answer -= i);
  }
  return answer;
}
