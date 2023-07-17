import Foundation

func solution(_ ineq:String, _ eq:String, _ n:Int, _ m:Int) -> Int {
    var answer = false
    if ineq == ">", eq == "=" { answer = n >= m }
    if ineq == "<", eq == "=" { answer = n <= m }
    if ineq == ">", eq == "!" { answer = n > m }
    if ineq == "<", eq == "!" { answer = n < m }
    return answer ? 1 : 0
}