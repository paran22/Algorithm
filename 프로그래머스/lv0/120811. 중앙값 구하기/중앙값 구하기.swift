import Foundation

func solution(_ array:[Int]) -> Int {
    let sorted : [Int] = array.sorted()
    return sorted[sorted.count / 2]
}