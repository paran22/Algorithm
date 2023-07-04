import Foundation

func solution(_ arr:[Int]) -> Int {
    var before = arr
    var after: [Int] = []
    var count = 0
    repeat {
        if !after.isEmpty { before = after }
        after = before.map {
            if $0 >= 50 {
                return $0 % 2 == 0 ? $0 / 2 : $0
            }
            return $0 % 2 == 0 ? $0 : $0 * 2 + 1
        }
        count += 1
    } while before != after
    return count - 1
}