import Foundation

func solution(_ n:Int) -> Int {
    var result = 0
    var idx = 0
    while result <= n {
        idx += 1
        result = factorial(idx)
    }
    return idx - 1
}

func factorial(_ n: Int) -> Int {
    if n == 1 {
        return 1
    }
    return factorial(n - 1) * n
}