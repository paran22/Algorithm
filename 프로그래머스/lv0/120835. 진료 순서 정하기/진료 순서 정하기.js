function solution(emergency) {
    var sorted = [...emergency].sort((a, b) => b - a);
    return emergency.map(e => sorted.indexOf(e) + 1);
}