import Foundation

func solution(_ array:[Int]) -> [Int] {
    if let max = array.max() {
        if let maxIndex = array.firstIndex(of: max) {
            return [max, maxIndex]
        }
    }
    return []
}