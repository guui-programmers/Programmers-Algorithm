function solution(x, n) {
  //x부터 시작해 x씩 증가 -> x의 배수
  //n개
  var answer = [];
  let result = x;
  for (let i = 0; i < n; i++) {
    answer.push(result);
    result += x;
  }
  return answer;
}
