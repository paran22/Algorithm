import Foundation

func solution(_ num_list:[Int]) -> Int {
    var odd = ""
    var even = ""
    for num in num_list {
        if num % 2 == 1 {
            odd += String(num)
            continue
        }
        even += String(num)
    }
    return Int(odd)! + Int(even)!
}
