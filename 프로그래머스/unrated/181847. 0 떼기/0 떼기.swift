import Foundation

func solution(_ n_str:String) -> String {
    var answer = n_str
    for n in n_str {
        if n == "0" {
            answer.remove(at: answer.startIndex)
            continue
        }
        return answer
    }
    return answer
}