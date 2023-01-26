import Foundation

func solution(_ n:Int) -> [Int] {
    var answer: [Int] = []
    for i in 0..<n + 1 {
        if (i % 2 != 0) {
            answer.append(i)
        }
    }
    return answer
}