import Foundation

func solution(_ rsp:String) -> String {
    var answer = ""
    for char in rsp {
        answer += windCase(char)
    }
    return answer
}

func windCase(_ rsp: Character) -> String {
    if rsp == "2" {
        return "0"
    }
    if rsp == "0" {
        return "5"
    }
    if rsp == "5" {
        return "2"
    }
    return ""
}