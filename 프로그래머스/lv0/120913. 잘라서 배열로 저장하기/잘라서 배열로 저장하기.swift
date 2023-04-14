import Foundation

func solution(_ my_str:String, _ n:Int) -> [String] {
    var answer : [String] = []
    var temp = my_str
    while !temp.isEmpty {
        if (temp.count < n) {
            answer.append(temp)
            break
        }
        let index = temp.index(temp.startIndex, offsetBy: n)
        answer.append(String(temp[temp.startIndex..<index]))
        temp.removeSubrange(temp.startIndex..<index)
    }
    return answer
}