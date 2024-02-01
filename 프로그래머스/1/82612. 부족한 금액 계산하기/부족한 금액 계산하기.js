function solution(price, money, count) {
    let totalPrice = 0;
    for (let i = 0; i < count; i++) {
        totalPrice += price * (i + 1);
    }
    const diff = totalPrice - money;
    return diff > 0 ? diff : 0; 
}