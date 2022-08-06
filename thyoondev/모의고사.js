function repeatStr(str, maxLength) {
  return str.repeat(maxLength).substr(0, maxLength);
}

function makePattern(str, maxLength) {
  return [...repeatStr(str, maxLength)].map(Number);
}

function solution(answers) {
  var answer = [];
  //찍는 패턴 배열로 만들기
  let one = makePattern('12345', answers.length);
  let two = makePattern('21232425', answers.length);
  let three = makePattern('3311224455', answers.length);

  //정답 수 체크
  let oneAnswersCount = answers.filter((e, i) => e === one[i]).length;
  let twoAnswersCount = answers.filter((e, i) => e === two[i]).length;
  let threeAnswersCount = answers.filter((e, i) => e === three[i]).length;
  let max = Math.max(oneAnswersCount, twoAnswersCount, threeAnswersCount);

  //정답 넣기
  if (oneAnswersCount === max) {
    answer.push(1);
  }
  if (twoAnswersCount === max) {
    answer.push(2);
  }
  if (threeAnswersCount === max) {
    answer.push(3);
  }

  return answer;
}
