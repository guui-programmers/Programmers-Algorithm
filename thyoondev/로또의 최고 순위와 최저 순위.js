function solution(lottos, win_nums) {
  const rank = { 6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6 };
  let total = 0;
  let zero = 0;
  lottos.map((n) => (win_nums.includes(n) ? total++ : n === 0 ? zero++ : n));
  return [rank[total + zero], rank[total]];
}
