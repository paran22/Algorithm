import Foundation

func solution(_ s:String) -> String {
    var answer: [Character] = []
    var duplicated: [Character] = []
    for i in Array(s) {
        if !answer.contains(i) {
            answer.append(i)
            continue
        }
        duplicated.append(i)
    }
    for i in duplicated {
        if answer.contains(i) {
            answer.remove(at: answer.firstIndex(of: i)!)
        }
    }
    return String(answer.sorted())
}