import Foundation

func solution(_ numbers:[Int]) -> Int {
    if numbers.count == 2 {
        return numbers[0] * numbers[1]
    }
    let sorted = numbers.sorted(by: >)
    return max(sorted[0] * sorted[1], sorted[numbers.count - 2] * sorted[numbers.count - 1])
}