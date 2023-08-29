function solution(balls, share) {
    const factorial = (num) => {
        if (num === 1) return 1;
        var result = 1;
        for (let i = 2; i < num + 1; i ++) {
            result *= i;
        }
        return result;
    }
    return Math.round(factorial(balls) / (factorial(balls - share) * factorial(share)));
}