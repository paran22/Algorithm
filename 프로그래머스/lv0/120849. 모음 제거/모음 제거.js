function solution(my_string) {
    const vowels = ['a', 'i', 'u', 'e', 'o'];
    return my_string.split('').filter((str) => !vowels.includes(str)).join('');
}