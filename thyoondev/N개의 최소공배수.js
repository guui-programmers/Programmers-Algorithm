function solution(arr) {
  //최대공약수 -> 유클리드 호제법으로 구하기
  //최소공배수 -> 두 자연수를 곱하고 최대 공약수로 나누기
  const greatest = (a, b) => (b === 0 ? a : greatest(b, a % b));
  const least = arr.reduce((acc, cur) => (acc * cur) / greatest(acc, cur));
  return least;
}
