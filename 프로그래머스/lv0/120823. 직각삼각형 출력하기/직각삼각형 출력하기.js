const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    const n = Number(input[0]);
    let answer = '';
    for (let i = 0; i < n; i++) {
        answer += '*'.repeat(i + 1)
        answer += '\n'
    }
    console.log(answer);
});