import Foundation

func solution(_ numbers:String) -> Int64 {
    let array = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    var answer = numbers
    for i in 0..<array.count {
        answer = answer.replacingOccurrences(of: array[i], with: String(i))
    }
    return Int64(answer)!
}