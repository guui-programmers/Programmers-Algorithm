function solution(n) {
  let result = 0;
  Array.from(String(n), (x) => (result += +x));
  return result;
}
