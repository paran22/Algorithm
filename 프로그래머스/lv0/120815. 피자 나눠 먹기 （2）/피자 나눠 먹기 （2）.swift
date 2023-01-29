import Foundation

func solution(_ n:Int) -> Int {
    let piecesOfPizza = 6
    var answer = 1
    while answer * piecesOfPizza % n != 0 {
        answer += 1
    }
    return answer
}