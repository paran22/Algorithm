import Foundation

func solution(_ numLog:[Int]) -> String {
    var dict : [Int:String] = [1:"w", -1:"s", 10:"d", -10:"a"]
    var answer = ""
    for i in 1..<numLog.count {
        let distance = numLog[i] - numLog[i-1]
        answer += dict[distance]!
    }
    return answer
}