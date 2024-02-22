function solution(a, b) {
    const dayOfWeek = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];
    const daysOfMonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const days = daysOfMonth.slice(0, a).reduce((a, b) => a + b) + b;
    return dayOfWeek[days % dayOfWeek.length]
}