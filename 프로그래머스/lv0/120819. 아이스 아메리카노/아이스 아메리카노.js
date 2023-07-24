function solution(money) {
  const coffeePrice = 5500;
  return [parseInt(money / coffeePrice), money % coffeePrice];
}