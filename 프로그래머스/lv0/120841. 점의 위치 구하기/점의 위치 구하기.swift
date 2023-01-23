import Foundation

func solution(_ dot:[Int]) -> Int {
    let x = dot[0]
    let y = dot[1]
    if x > 0 {
        return y > 0 ? 1 : 4
    } else {
        return y > 0 ?  2 : 3
    }
    return 0
}