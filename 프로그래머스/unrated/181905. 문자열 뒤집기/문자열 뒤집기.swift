import Foundation

func solution(_ my_string:String, _ s:Int, _ e:Int) -> String {
    var answer = String(my_string[my_string.startIndex..<my_string.index(my_string.startIndex, offsetBy: s)])
    for i in stride(from: e, through: s, by: -1) {
        answer += String(my_string[my_string.index(my_string.startIndex, offsetBy: i)])
    }
    
    answer += String(my_string[my_string.index(my_string.startIndex, offsetBy: e + 1)...])
    return answer
}
