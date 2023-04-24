import Foundation

func solution(_ numbers:[Int], _ n:Int) -> Int {
    var answer = 0
    for num in numbers {
        if answer > n {
            return answer
        }
        answer += num
    }
    return answer
}