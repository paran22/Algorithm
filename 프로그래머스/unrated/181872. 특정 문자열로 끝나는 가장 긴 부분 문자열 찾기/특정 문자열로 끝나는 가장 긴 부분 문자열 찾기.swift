import Foundation

func solution(_ myString:String, _ pat:String) -> String {
    var str = ""
    var answer = ""
    for char in myString {
        str += String(char)
        if str.hasSuffix(pat) {
            answer = str
        }
    }
    return answer
}
