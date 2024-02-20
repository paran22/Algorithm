function solution(n, arr1, arr2) {
    const decodeds = [];
    const toBinary = (str, n) => str.toString(2).padStart(n, '0').split('');
    const decode = (strArr1, strArr2) => strArr1.map((str, i) => (str === '0' && strArr2[i] === '0') ? '0' : '1').join('');
    for (let i = 0; i < n; i++) {
        const binary1 = toBinary(arr1[i], n);
        const binary2 = toBinary(arr2[i], n);
        const decoded = decode(binary1, binary2);
        decodeds.push(decoded);
    }
    return decodeds.map(decoded => decoded.split('').map(str => str === '0' ? " " : "#").join(''));
}