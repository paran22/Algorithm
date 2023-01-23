import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    let odd = num_list.filter({ $0 % 2 == 0}).count
    return [odd, num_list.count - odd]
}