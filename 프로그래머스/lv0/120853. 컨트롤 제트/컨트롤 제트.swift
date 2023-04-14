import Foundation

func solution(_ s:String) -> Int {
    let array = s.components(separatedBy: " ")
    var lastInputNum = 0
    var answer = 0
    for i in array {
        if let num = Int(i) {
            lastInputNum = num
            answer += num
            continue
        }
        answer -= lastInputNum
    }
    return answer
}
