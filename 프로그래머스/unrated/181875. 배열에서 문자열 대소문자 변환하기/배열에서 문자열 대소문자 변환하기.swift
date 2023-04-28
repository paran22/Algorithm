import Foundation

func solution(_ strArr:[String]) -> [String] {
    return strArr.enumerated().map { $0.offset % 2 == 1 ? $0.element.uppercased() : $0.element.lowercased() }
}