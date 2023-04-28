import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var answer = arr
    for query in queries {
        answer.swapAt(query[0], query[1])
    }
    return answer
}