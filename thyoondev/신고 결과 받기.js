function solution(id_list, report, k) {
  //이용자의 id배열 id_list
  //이용자가 신고한 사람 배열 report
  //정지 기준 수 k
  var answer = [];
  let report_list = {};
  //불량 이용자를 신고하고 처리 결과를 메일로 발송
  //유저별로  한번에  한 명 신고 가능, 신고 무제한, 중복x
  //k번 이상 신고 당하면 이용 정지 -> 신고한 사람에게 메일로 전송

  id_list.map((user) => {
    report_list[user] = [];
    //key로 userid를 value로 빈 배열을 가지는 객체
  });

  //report의 중복을 제거하고,
  let set = new Set(report);
  let dup_report = [...set];
  //이후 신고자 별로 누구를 신고하고 몇 번 했는지 기록해야된다.
  //신고 당한사람 별로 신고 횟수를 누적하면 될 듯
  let list = [];
  dup_report.map((log) => {
    list = log.split(' ');
    report_list[list[1]].push(list[0]);
  });

  //report_list의 키별로 배열 길이 담아서 리턴
  let success_reporter = [];
  for (key in report_list) {
    k <= report_list[key].length && success_reporter.push(...report_list[key]);
  }

  //유저 별로 카운터 담을 객체 생성
  let mail_list = {};
  id_list.map((user) => {
    mail_list[user] = 0;
  });

  //유저 별로 카운트 반환
  id_list.map((user) => {
    success_reporter.map((s_user) => {
      user === s_user ? mail_list[user]++ : mail_list[user];
    });
  });

  for (key in mail_list) {
    answer.push(mail_list[key]);
  }

  return answer;
  //유저별로 처리 결과 메일을 받은 횟수의 배열
}
