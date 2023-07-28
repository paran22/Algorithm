function solution(rsp) {
    let answer = {
        '2' : '0',
        '0' : '5',
        '5' : '2',
    }
    return rsp.split('').map((e) => answer[e]).join('');
}