import Foundation

func solution(_ num_list:[Int]) -> Int {
    var a = 1
    var b = 0
    for num in num_list {
        a *= num
        b += num
    }
    return a < b * b ? 1 : 0
}
