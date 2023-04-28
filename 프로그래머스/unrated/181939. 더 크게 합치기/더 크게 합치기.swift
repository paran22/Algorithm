import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let case1 = Int(String(a) + String(b))!
    let case2 = Int(String(b) + String(a))!
    return case1 > case2 ? case1 : case2
}