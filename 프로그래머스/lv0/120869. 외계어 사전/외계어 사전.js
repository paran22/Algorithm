function solution(spell, dic) {
    for (str of dic) {
        if (str.length != spell.length) continue;
        let word = str;
        for (char of spell) {
            word = word.replace(char, '');
        }
        if (!word) return 1;
    }
    return 2;
}