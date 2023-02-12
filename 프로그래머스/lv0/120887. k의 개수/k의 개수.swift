import Foundation

func solution(_ i:Int, _ j:Int, _ k:Int) -> Int {
    var count = 0
    for num in i...j {
        let array = Array(String(num))
        let char = Character(String(k))
        if array.contains(char) {
            for n in array {
                if (n == char) {
                    count += 1
                }
            }
        }
    }
    return count
}