import Foundation

func solution(_ my_string:String) -> [String] {
    var answer : [String] = []
    for i in 0..<my_string.count {
        let index = my_string.index(my_string.startIndex, offsetBy: i)
        answer.append(String(my_string[index...]))
    }
    return answer.sorted()
}