function solution(s) {
    const first = s.substring(0, 1);
    if (first === "-" | first === "+") {
        const num = parseInt(s.substring(1))
        return first === "-" ? num * -1 : num;
    }
    return parseInt(s);
}