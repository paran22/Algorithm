import Foundation

func solution(_ n:Int) -> Int {
    let num : Int = Int(sqrt(Double(n)))
    if (num * num == n) {
        return 1
    }
    return 2
}