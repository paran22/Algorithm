function solution(s) {
    const middleIndex = Math.floor(s.length / 2);
    return s.length % 2 === 1 ? s[middleIndex] : s.slice(middleIndex - 1, middleIndex + 1);
}