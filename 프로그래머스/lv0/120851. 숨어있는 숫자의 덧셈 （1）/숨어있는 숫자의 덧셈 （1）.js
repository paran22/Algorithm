function solution(my_string) {
    return my_string.split('').filter((str) => Number(str)).reduce((a, b) => a + Number(b), 0);
}