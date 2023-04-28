import Foundation

func solution(_ arr:[[Int]]) -> Int {
    for i in 0..<arr.count {
        for j in i..<arr[0].count {
            if i == j { continue }
            if arr[i][j] != arr[j][i] { return 0 }
        }
    }
    return 1
}