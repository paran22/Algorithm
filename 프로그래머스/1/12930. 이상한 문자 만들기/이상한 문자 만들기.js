function solution(s) {
    const toWeirdWord = (word) => word.split('').map((str, index) => index % 2 === 0 ? str.toUpperCase() : str.toLowerCase()).join('');
    return s.split(' ').map(word => toWeirdWord(word)).join(' ');
}