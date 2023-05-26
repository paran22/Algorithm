import Foundation

func solution(_ my_string:String, _ m:Int, _ c:Int) -> String {
    return my_string.map { String($0) } .enumerated().filter { $0.offset % m == c - 1 }.reduce("") { $0 + $1.element }
}