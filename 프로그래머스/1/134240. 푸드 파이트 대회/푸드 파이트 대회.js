function solution(food) {
    let order = '';
    for (i = 1; i < food.length; i++) {
        const half = Math.floor(food[i] / 2)
        order += String(i).repeat(half);
    }
    return order + "0" + [...order].reverse().join('');
}