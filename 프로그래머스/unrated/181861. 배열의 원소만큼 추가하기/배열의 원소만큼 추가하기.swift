import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var answer : [Int] = []
    for num in arr {
        for _ in 0..<num {
            answer.append(num)
        }
    }
    return answer
}