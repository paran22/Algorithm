import Foundation

func solution(_ n:Int, _ k:Int) -> Int {
    let service = n / 10
    return 12000 * n + 2000 * (k - service)
}