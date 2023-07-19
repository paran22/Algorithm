import Foundation

func solution(_ arr:[[Int]]) -> [[Int]] {
    var answer: [[Int]] = []
    var rowCnt = arr[0].count
    var columnCnt = arr.count
    if rowCnt > columnCnt {
        answer = arr
        for _ in 0..<rowCnt - columnCnt {
            answer.append(Array(repeating: 0, count: rowCnt))
        }
        return answer
    }
    for array in arr {
        answer.append(array + Array(repeating: 0, count: columnCnt - rowCnt))
    }
    return answer
}