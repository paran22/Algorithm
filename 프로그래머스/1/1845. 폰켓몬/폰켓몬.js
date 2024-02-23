function solution(nums) {
    const quantity = nums.length / 2;
    const numsSet = new Set(nums);
    return numsSet.size > quantity ? quantity : numsSet.size;
}