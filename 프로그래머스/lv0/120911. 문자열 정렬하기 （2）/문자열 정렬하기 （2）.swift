import Foundation

func solution(_ my_string:String) -> String {
    return String(Array(my_string.lowercased()).sorted())
}