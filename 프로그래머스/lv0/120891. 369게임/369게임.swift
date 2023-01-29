import Foundation

func solution(_ order:Int) -> Int {
    var answer = 0
    for i in Array(String(order)) {
        if ["3", "6", "9"].contains(i) {
            answer += 1
        }
    }
    return answer
}