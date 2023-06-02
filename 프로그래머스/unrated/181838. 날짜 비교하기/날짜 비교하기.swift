import Foundation

func solution(_ date1:[Int], _ date2:[Int]) -> Int {
    var same = true
    for i in 0..<date1.count {
        if date1[i] < date2[i] && same {
            return 1
        }
        if date1[i] > date2[i] {
            same = false
        }
    }
    return 0
}