import Foundation

func solution(_ numbers:[Int]) -> Int {
    var sortedNumbers = numbers.sorted(by: >)
    return sortedNumbers[0] * sortedNumbers[1]
}