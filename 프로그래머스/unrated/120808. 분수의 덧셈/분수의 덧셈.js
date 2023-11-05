function solution(numer1, denom1, numer2, denom2) {
    let denom = lcm(denom1, denom2);
    let numer = (denom / denom1 * numer1) + (denom / denom2 * numer2);
    const num = gcd(denom, numer);
    if (num > 1) {
        numer /= num;
        denom /= num;
    }
    return [numer, denom];
}

function lcm(a, b) {
  return (a * b) / gcd(a, b)
}

function gcd(a, b) {
  let r
  while (b != 0) {
    r = a % b
    a = b
    b = r
  }
  return a
}