import Foundation

func solution(_ n:Int, _ t:Int) -> Int {
    var answer = n
    for _ in 0..<t {
        answer = answer * 2
    }
    return answer
}