import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    var array : [Character] = []
    for i in 0..<my_string.count {
        array.append(my_string[my_string.index(my_string.startIndex, offsetBy: i)])
    }
    
    var converted : [String] = []
    for i in 0..<array.count {
        var word : String = ""
        for _ in 0..<n {
            word += "\(array[i])"
        }
        converted.append(word)
    }
    return converted.joined(separator: "")
}