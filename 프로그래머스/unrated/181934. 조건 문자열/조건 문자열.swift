import Foundation

func solution(_ ineq:String, _ eq:String, _ n:Int, _ m:Int) -> Int {
    var answer = false
    switch (ineq, eq) {
        case (">", "=") : answer = n >= m
        case ("<", "=") : answer = n <= m
        case (">", "!") : answer = n > m
        case ("<", "!") :  answer = n < m
        default: answer = false
    }
    return answer ? 1 : 0
}