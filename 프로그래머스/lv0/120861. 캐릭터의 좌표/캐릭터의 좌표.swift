import Foundation

func solution(_ keyinput:[String], _ board:[Int]) -> [Int] {
    var vertical = 0
    var horizontal = 0
    let verticalLimit = (board[1] - 1) / 2
    let horizontalLimit = (board[0] - 1) / 2

    for i in keyinput {
        if i == "up" && vertical < verticalLimit {
            vertical += 1
        }
        if i == "down" && vertical > -verticalLimit {
            vertical -= 1
        }
        if i == "left" && horizontal > -horizontalLimit {
            horizontal -= 1
        }
        if i == "right" && horizontal < horizontalLimit {
            horizontal += 1
        }
    }
    return [horizontal, vertical]
}