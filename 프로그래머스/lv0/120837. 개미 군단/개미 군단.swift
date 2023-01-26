import Foundation

func solution(_ hp:Int) -> Int {
    var answer : Int = 0
    answer += hp / 5
    let left : Int = hp % 5
    if (left != 0) {
        answer += left / 3
        answer += left % 3
    }
    return answer
}