import Foundation

func solution(_ num:Int, _ k:Int) -> Int {
    let array = Array(String(num))
    for i in 0..<array.count {
        if array[i] == Character(String(k)) {
            return i + 1
        }
    }
    return -1
}