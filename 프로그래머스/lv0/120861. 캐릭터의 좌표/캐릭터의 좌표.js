function solution(keyinput, board) {
    const firstMax = Math.floor(board[0] / 2);
    const secondMax = Math.floor(board[1] / 2);
    let first = 0;
    let second = 0;
    for (key of keyinput) {
        switch(key) {
            case "left":
                first = first === -firstMax ? -firstMax : first - 1;
                break;
            case "right":
                first = first === firstMax ? firstMax : first + 1;
                break;
            case "up":
                second = second === secondMax ? secondMax : second + 1;
                break;
            case "down":
                second =  second === -secondMax ? -secondMax : second - 1;
                break;
        }
    }
    return [first, second];
}