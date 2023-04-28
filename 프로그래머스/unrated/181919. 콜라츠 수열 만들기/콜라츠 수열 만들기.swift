import Foundation

func solution(_ n:Int) -> [Int] {
    var answer: [Int] = [n]
    var varN = n
    while varN > 1 {
        if varN % 2 == 0 {
            var num = varN / 2
            answer.append(num)
            varN = num
        } else {
            var num = 3 * varN + 1
            answer.append(num)
            varN = num
        }
    }
    return answer
}