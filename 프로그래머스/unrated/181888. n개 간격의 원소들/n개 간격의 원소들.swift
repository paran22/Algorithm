import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    return stride(from: 0, through: num_list.count - 1, by: n).map { num_list[$0] }
}
