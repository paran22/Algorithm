import Foundation

func solution(_ numbers:[Int], _ direction:String) -> [Int] {
    var answer = numbers
    if direction == "right" {
        answer.insert(numbers[numbers.count - 1], at: 0)
        answer.remove(at: numbers.count)
    }
    if direction == "left" {
        answer.append(numbers[0])
        answer.remove(at: 0)
    }
    return answer
}