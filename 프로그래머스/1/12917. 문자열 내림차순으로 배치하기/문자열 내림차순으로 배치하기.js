function solution(s) {
    return s.split('').sort((a, b) => a.toLowerCase() === a.toUpperCase() || a < b ? 1 : -1).join('');
}