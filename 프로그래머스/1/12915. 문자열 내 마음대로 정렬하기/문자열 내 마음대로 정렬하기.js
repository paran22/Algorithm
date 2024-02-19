function solution(strings, n) {
    return strings.sort((a, b) => a[n] === b[n] ? a.localeCompare(b) : a[n].charCodeAt() - b[n].charCodeAt());
}