import Foundation

func solution(_ n:Int) -> Int {
    var answer : Int = 0
    let root : Int = Int(sqrt(Double(n)))
    for i in 1...root {
        if (n % i == 0) {
            answer += 2
        }
    }
    return root * root == n ? answer - 1 : answer
}