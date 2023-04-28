import Foundation

func solution(_ a:Int, _ d:Int, _ included:[Bool]) -> Int {
    var answer = 0
    for i in 0..<included.count {
        if included[i] {
            answer += d * i + a
        }
    }
    return answer
}