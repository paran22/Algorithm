function solution(array, commands) {
    const toCommand = (array, command) => {
        const [startPosition, endPosition, index] = command;
        const sliced = array.slice(startPosition - 1, endPosition);
        const sorted = sliced.sort((a, b) => a - b);
        return sorted[index - 1];
    }
    return commands.map(command => toCommand(array, command));
}