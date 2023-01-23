import Foundation

func solution(_ my_string:String) -> String {
    return my_string.reduce("", { String($1) + String($0) } )
}