function solution(s) {
    const array = s.toLowerCase().split('');
    const pCount = array.filter(str => str === "p").length;
    const yCount = array.filter(str => str === "y").length;
    return pCount === yCount ? true : false;
 }