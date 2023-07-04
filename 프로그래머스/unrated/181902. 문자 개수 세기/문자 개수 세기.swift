import Foundation

func solution(_ my_string:String) -> [Int] {
    var answer: [Int] = []
    for i in Int(UnicodeScalar("A").value)...Int(UnicodeScalar("Z").value) {
        answer.append(my_string.filter { String($0) == String(UnicodeScalar(i)!) }.count )
    }
    for i in Int(UnicodeScalar("a").value)...Int(UnicodeScalar("z").value) {
        answer.append(my_string.filter { String($0) == String(UnicodeScalar(i)!) }.count )
    }
    return answer
}