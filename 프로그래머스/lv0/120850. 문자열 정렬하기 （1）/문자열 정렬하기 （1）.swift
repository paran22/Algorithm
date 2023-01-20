import Foundation

func solution(_ my_string:String) -> [Int] {
    var answer: [Int] = []
    for char in my_string {
        if char.isNumber, let num = Int(String(char)) {
            answer.append(num)
        }
    }
    return answer.sorted()
}