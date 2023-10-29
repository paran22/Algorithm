function solution(polynomial) {
    const arr = polynomial.split(' + ');
    let x = 0;
    let number = 0;
    for (num of arr) {
        if (num.includes('x')) {
            const n = num.length > 1 ? Number(num.split('x')[0]) : 1;
            x += n;
            continue;
        }
        number += Number(num);
    }
    let answer = '';
    if (x > 0) answer += `${x === 1 ? '' : x}x`;
    if (x > 0 && number > 0) answer += ' + ';
    if (number > 0) answer += `${number}`;
    return answer;
}