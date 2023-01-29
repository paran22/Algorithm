import Foundation

func solution(_ n:Int) -> Int {
    let piecesOfPizza = 6
    for i in 1...100 {
        if piecesOfPizza * i % n == 0 {
            return i
        }
    }
    return 0
}