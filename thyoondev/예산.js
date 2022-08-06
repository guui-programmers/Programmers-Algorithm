function solution(d, budget) {
  var answer = 0;
  let idx = 0;
  d.sort((a, b) => a - b);
  while (budget >= d[idx]) {
    budget = budget - d[idx];
    idx++;
  }
  return idx;
}
