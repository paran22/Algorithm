function solution(age) {
    return String(age).split('').map((str) => String.fromCharCode('a'.charCodeAt() + Number(str))).join('');
}