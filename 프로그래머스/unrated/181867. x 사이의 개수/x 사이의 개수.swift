import Foundation

func solution(_ myString:String) -> [Int] {
    var answer : [Int] = []
    var count = 0
    for i in myString {
        if i == "x" {
            answer.append(count)
            count = 0
            continue
        }
        count += 1
    }
    answer.append(count)
    return answer;
}