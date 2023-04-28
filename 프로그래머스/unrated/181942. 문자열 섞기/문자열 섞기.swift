import Foundation

func solution(_ str1:String, _ str2:String) -> String {
    var answer = ""
    for i in 0..<str1.count {
        answer += String(str1[str1.index(str1.startIndex, offsetBy: i)])
        answer += String(str2[str2.index(str2.startIndex, offsetBy: i)])
    }
    return answer
}