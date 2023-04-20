import Foundation

func solution(_ dots:[[Int]]) -> Int {
    var targetA: Int?
    var targetB: Int?
    var a: Int?
    var b: Int?
    var length1 = 0
    var length2 = 0
    for i in dots {
        if targetA == nil {
            targetA = i[0]
            a = i[1]
            continue
        }
        if i[0] == targetA! {
            length1 = a! - i[1]
        }
        if targetB == nil {
            targetB = i[1]
            b = i[0]
            continue
        }
        length2 = b! - i[0]
    }
    return abs(length1 * length2)
}