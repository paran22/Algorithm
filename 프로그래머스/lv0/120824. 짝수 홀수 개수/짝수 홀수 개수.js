function solution(num_list) {
  let evenCnt = 0;
  for (num of num_list) {
    if (num % 2 == 0) {
      evenCnt += 1;
    }
  }
  return [evenCnt, num_list.length - evenCnt]
}