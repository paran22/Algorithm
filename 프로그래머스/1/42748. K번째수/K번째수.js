function solution(array, commands) {
    const toCommand = (array, command) => {
        const sliced = array.slice(command[0] - 1, command[1]);
        const sorted = sliced.sort((a, b) => a - b);
        return sorted[command[2] - 1];
    }
    return commands.map(command => toCommand(array, command));
}