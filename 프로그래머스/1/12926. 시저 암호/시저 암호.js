function solution(s, n) {
    const encrypt = (str) => {
        if (str === ' ') return str;
        const code = str.codePointAt();
        let newCode = code + n;
        const lowerZCode = 'z'.codePointAt();
        const upperZCode = 'Z'.codePointAt();
        if ((str === str.toUpperCase() && newCode > upperZCode) || (str === str.toLowerCase() && newCode > lowerZCode)) {
            newCode -= 26;
        }
        return String.fromCharCode(newCode);
    }
    return s.split('').map(encrypt).join('');
}