import Foundation

func solution(_ start:Int, _ end:Int) -> [Int] {
    return Array(end...start).sorted(by: >)
}