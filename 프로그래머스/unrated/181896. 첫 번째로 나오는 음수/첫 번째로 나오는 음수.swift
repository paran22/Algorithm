import Foundation

func solution(_ num_list:[Int]) -> Int {
    return Int(num_list.firstIndex { $0 < 0 } ?? -1 )
}