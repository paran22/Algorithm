import Foundation

func solution(_ my_strings:[String], _ parts:[[Int]]) -> String {
    var answer = ""
    for i in 0..<my_strings.count {
        let startIndex = my_strings[i].index(my_strings[i].startIndex, offsetBy: parts[i][0])
        let endIndex = my_strings[i].index(my_strings[i].startIndex, offsetBy: parts[i][1])
        answer += String(my_strings[i][startIndex...endIndex])
    }
    return answer
}