function solution(x) {
  let strArr = String(x).split("");
  let result = 0;

  for (let i of strArr) {
    result += Number(i);
  }

  if (x % result === 0) {
    return true;
  } else {
    return false;
  }
}
