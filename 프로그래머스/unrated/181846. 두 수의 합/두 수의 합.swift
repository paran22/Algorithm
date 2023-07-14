import Foundation

func solution(_ a:String, _ b:String) -> String {
    var a = a, b = b
    var answer = ""
    var temp = 0
    var i = 1
    while !a.isEmpty || !b.isEmpty {
        if !a.isEmpty {
            temp += Int(String(a.last!))!
            a.removeLast()
        }
        if !b.isEmpty {
            temp += Int(String(b.last!))!
            b.removeLast()
        }
        i += 1
        answer = String(temp % 10) + answer
        temp /= 10
    }
    if temp != 0 {
        answer = String(temp) + answer
    }
    return answer
}