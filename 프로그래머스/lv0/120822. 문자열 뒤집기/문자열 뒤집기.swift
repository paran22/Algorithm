import Foundation

func solution(_ my_string:String) -> String {
    var reverseds : [Character] = []
    for i in 0..<my_string.count {
        reverseds.append(my_string[my_string.index(my_string.startIndex, offsetBy: i)])
    }
    return String(reverseds.reversed())
}