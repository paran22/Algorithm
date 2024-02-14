function solution(sizes) {
    let max1 = 0;
    let max2 = 0;
    for (size of sizes) {
        size.sort((a, b) => b - a);
        max1 = Math.max(max1, size[0]);
        max2 = Math.max(max2, size[1]);
    }
    return max1 * max2;
}