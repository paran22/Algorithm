import Foundation

func solution(_ intStrs:[String], _ k:Int, _ s:Int, _ l:Int) -> [Int] {
    return intStrs.map { str in
        let startIndex = str.index(str.startIndex, offsetBy: s)
        let endIndex = str.index(str.startIndex, offsetBy: s + l - 1)
        return Int(String(str[startIndex...endIndex]))!
    }.filter { $0 > k }
}
