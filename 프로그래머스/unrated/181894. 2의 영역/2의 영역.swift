import Foundation

func solution(_ arr:[Int]) -> [Int] {
    if !arr.contains(2) { return [-1] }
    let firstIndex = arr.firstIndex(of: 2)
    let lastIndex = arr.lastIndex(of: 2)
    return Array(arr[firstIndex!...lastIndex!])
}