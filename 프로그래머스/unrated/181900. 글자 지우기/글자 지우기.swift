import Foundation

func solution(_ my_string:String, _ indices:[Int]) -> String {
    return my_string.map { String($0) }.enumerated().filter { !indices.contains($0.offset) }.reduce("") { $0 + $1.element }
}