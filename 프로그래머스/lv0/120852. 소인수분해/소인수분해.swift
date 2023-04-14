import Foundation

func solution(_ n:Int) -> [Int] {
    if n < 4 {
        return [n]
    }
    var array : [Int] = []
    for i in 2...n/2 {
        if n % i == 0, !array.contains(where: { i % $0 == 0}) {
            array.append(i)
        }
    }
    return array.isEmpty ? [n] : array
}
