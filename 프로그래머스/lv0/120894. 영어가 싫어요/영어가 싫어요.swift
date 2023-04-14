import Foundation

func solution(_ numbers:String) -> Int64 {
    let array = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    var temp = numbers
    var answer = "0"
    while !temp.isEmpty {
        for i in 0..<array.count {
            let number = array[i]
            if temp.starts(with: number) {
                answer += String(i)
                let index = temp.index(temp.startIndex, offsetBy: number.count)
                temp.removeSubrange(temp.startIndex..<index)
            }
        }
    }
    return Int64(answer)!
}