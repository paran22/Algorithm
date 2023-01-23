import Foundation

func solution(_ cipher:String, _ code:Int) -> String {
    var answer = ""
    for i in 1...cipher.count {
        if i % code == 0 {
            answer += String(cipher[cipher.index(cipher.startIndex, offsetBy: i - 1)])
        }
    }
    return answer
}