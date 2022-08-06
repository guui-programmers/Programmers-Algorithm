function solution(nums) {
  let answer = 0;
  let max = nums.length;

  // 3개의 수를 더했을떄 나오는 모든 경우의 수를 구함
  for (let i = 0; i < max - 2; i++) {
    let number = 0;
    for (let j = i + 1; j < max - 1; j++) {
      for (let k = j + 1; k < max; k++) {
        number = nums[i] + nums[j] + nums[k];

        // sosu인지 판별하는 함수를 호출했을 때의 결과값이 true 라면
        if (sosu(number)) answer++;
      }
    }
  }

  function sosu(number) {
    for (let i = 2; i <= Math.floor(Math.sqrt(number)); i++) {
      // 1 과 자기자신이 아닌 다른 수로 나누었을 떄 나머지가 없다면 소수가 아니다.
      if (number % i === 0) return false;
    }
    return true;
  }
  return answer;
}
