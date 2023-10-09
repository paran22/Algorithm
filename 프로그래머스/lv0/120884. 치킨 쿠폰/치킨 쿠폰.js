function solution(chicken) {
    let answer = 0;
    let coupon = chicken;
    while (coupon > 9) {
        const service = Math.floor(coupon / 10);
        answer += service
        coupon = Math.floor(coupon % 10);
        coupon += service;
    }
    return answer;
}