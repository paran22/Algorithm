import Foundation

func solution(_ myString:String) -> String {
    return myString.map( { $0 < "l" ? String("l") : String($0) } ).joined()
}
