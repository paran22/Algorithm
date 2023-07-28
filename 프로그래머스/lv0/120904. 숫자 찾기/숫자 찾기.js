function solution(num, k) {
    const index = Array.from(String(num)).indexOf(String(k));
    return index >= 0 ? index + 1 : index;
}