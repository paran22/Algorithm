function solution(numer1, denom1, numer2, denom2) {
    let denom = denom1 * denom2;
    let numer = denom1 * numer2 + denom2 * numer1;
    const num = gcd(denom, numer);
    return [numer / num, denom / num];
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