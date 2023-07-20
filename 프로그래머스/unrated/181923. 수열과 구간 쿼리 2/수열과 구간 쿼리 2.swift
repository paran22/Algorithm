import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var answer: [Int] = []
    for i in 0..<queries.count {
        let s = queries[i][0]
        let e = queries[i][1]
        let k = queries[i][2]
        var temp: [Int] = []
        for i in s...e {
            if arr[i] > k {
                temp.append(arr[i])
            }
        }
        answer.append(temp.min() ?? -1)
    }
    return answer
}