import Foundation

func solution(_ strArr:[String]) -> [String] {
    var answer : [String] = []
    for i in 0..<strArr.count {
        if i % 2 == 1 {
            answer.append(strArr[i].uppercased())
            continue
        }
        answer.append(strArr[i].lowercased())
    }
    return answer
}