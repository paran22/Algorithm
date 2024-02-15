function solution(s) {
    return s.split('').map((str, currentIndex) => {
        const word = s.substring(0, currentIndex);
        const priorIndex = word.lastIndexOf(str);
        const hasPriorStr = priorIndex < 0;
        return hasPriorStr ? -1 : currentIndex - priorIndex;
    });
}