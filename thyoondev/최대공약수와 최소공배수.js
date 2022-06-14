function solution(n, m) {
  //최대공약수 -> 유클리드 호제법으로 구하기
  //최소공배수 -> 두 자연수를 곱하고 최대 공약수로 나누기
  const greatest = (a, b) => (b === 0 ? a : greatest(b, a % b));
  const least = (a, b) => (a * b) / greatest(a, b);
  return [greatest(n, m), least(n, m)];
}
