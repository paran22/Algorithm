function solution(order) {
    const threeSixNine = ['3', '6', '9'];
    return Array.from(String(order)).filter((e) => threeSixNine.includes(e)).length;
}