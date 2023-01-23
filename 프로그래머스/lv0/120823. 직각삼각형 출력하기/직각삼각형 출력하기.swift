import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }

func solution(n: Int) -> String {
    var answer = ""
    for i in 0..<n {
        for j in 0..<n {
            if j <= i {
                answer += "*"
            }
        }
        answer += "\n"
    }
    return answer
}

print(solution(n: n[0]))

