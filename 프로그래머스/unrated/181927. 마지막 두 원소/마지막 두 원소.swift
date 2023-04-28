import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    let last = num_list[num_list.count - 1]
    let beforeLast = num_list[num_list.count - 2]
    return last > beforeLast ? num_list + [last - beforeLast] :  num_list + [last * 2]
}