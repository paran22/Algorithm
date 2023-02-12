import Foundation

func solution(_ emergency:[Int]) -> [Int] {
    let sorted = emergency.sorted(by: >)
    var answer: [Int] = []
    for i in emergency {
        answer.append(sorted.firstIndex(of: i)! + 1)
    }
    return answer
}