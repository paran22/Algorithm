function solution(n, k) {
  const priceOfFood = 12000;
  const priceOfDrink = 2000;
  return priceOfFood * n + priceOfDrink * (k - parseInt(n / 10));
}