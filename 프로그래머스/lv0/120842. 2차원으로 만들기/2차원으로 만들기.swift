import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [[Int]] {
    var answer: [[Int]] = []
    for i in stride(from: 0, to: num_list.count, by: n) {
        var list: [Int] = []
        for j in 0..<n {
            list.append(num_list[i + j])
        }
        answer.append(list)
    }
    return answer
}