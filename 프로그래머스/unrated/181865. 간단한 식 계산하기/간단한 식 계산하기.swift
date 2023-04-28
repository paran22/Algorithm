import Foundation

func solution(_ binomial:String) -> Int {
    let array = binomial.components(separatedBy: " ")
    let operators = array[1]
    if (operators == "+") { return Int(array[0])! + Int(array[2])! }
    if (operators == "-") { return Int(array[0])! - Int(array[2])! }
    if (operators == "*") { return Int(array[0])! * Int(array[2])! }
    if (operators == "/") { return Int(array[0])! / Int(array[2])! }
    return 0
}