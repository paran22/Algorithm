function solution(s) {
    const words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    let answer = '';
    while (s.length > 0) {
        const firstStr = s.substring(0, 1);
        if (!isNaN(firstStr)) {
            answer += firstStr;
            s = s.substring(1);
            continue;
        }
        for (let i = 0; i < words.length; i++) {
            const word = words[i];
            if (s.startsWith(word)) {
                answer += i;
                s = s.substring(word.length);
                break;
            }
        }
    }
    return Number(answer);
}