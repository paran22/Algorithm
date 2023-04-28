import Foundation

func solution(_ n:Int) -> [[Int]] {
    var answer : [[Int]] = []
    for i in 0..<n {
        var arr : [Int] = []
        for j in 0..<n {
            arr.append(i == j ? 1 : 0)
        }
        answer.append(arr)
    }
    return answer
}