import Foundation

func solution(_ my_string:String, _ s:Int, _ e:Int) -> String {
    let prefix = my_string.prefix(s)
    let suffix = my_string.suffix(my_string.count - e - 1)
    let middle = Array(my_string)[s...e].reversed().map{ String($0) }.joined()
    return prefix + middle + suffix
}
