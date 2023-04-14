import Foundation

func solution(_ numbers:[Int], _ k:Int) -> Int {
    var shotter = 0
    for _ in 0..<k - 1 {
        shotter += 2
        if shotter > numbers.count - 1 {
            shotter -= numbers.count
        }
    }
    return shotter + 1
}
