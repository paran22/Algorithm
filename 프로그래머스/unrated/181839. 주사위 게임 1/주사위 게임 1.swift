import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    func isOdd(_ num:Int) -> Bool {
        return num % 2 == 1
    }
    
    let isAOdd = isOdd(a)
    let isBOdd = isOdd(b)
    if (isAOdd && isBOdd) {
        return a * a + b * b
    }
    if (!isAOdd && !isBOdd) {
        return abs(a - b)
    }
    return 2 * (a + b)
}