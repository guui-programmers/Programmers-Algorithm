function solution(n, lost, reserve) {
  //n 전체 학생의 수
  //lost 체육복을 도난당한 학생들의 번호가 담긴 배열
  //reserve 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
  //return 체육수업을 들을 수 있는 학생의 최댓값

  let answer = n - lost.length;

  //여벌 체육복 가진 사람이 도난 당한 경우
  let realReserve = reserve.filter((r) => !lost.includes(r));
  let realLost = lost.filter((l) => !reserve.includes(l));
  answer += lost.length - realLost.length;

  realLost.sort((a, b) => a - b);
  // realReserve.sort((a,b) => a - b);

  realLost.forEach((l) => {
    if (realReserve.length === 0) {
      return;
    }

    if (realReserve.includes(l - 1)) {
      realReserve = realReserve.filter((r) => r !== l - 1);
      answer++;
    } else if (realReserve.includes(l + 1)) {
      realReserve = realReserve.filter((r) => r !== l + 1);
      answer++;
    }
  });

  return answer;
}
