import Foundation

func solution(_ my_string:String) -> String {
    var answer = ""
    for char in my_string {
        answer += char.isUppercase ? char.lowercased() : char.uppercased()
    }
    return answer
}