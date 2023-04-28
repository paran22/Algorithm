import Foundation

func solution(_ n_str:String) -> String {
    return String(n_str.suffix(from: n_str.firstIndex { $0 != "0"}! ))
}