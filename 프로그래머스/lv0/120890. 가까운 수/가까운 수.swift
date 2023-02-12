import Foundation

func solution(_ array:[Int], _ n:Int) -> Int {
    var distance: [Int] = []
    let sorted = array.sorted()
    for i in sorted {
        distance.append(abs(i - n))
    }
    return sorted[distance.firstIndex(of: distance.min()!)!]
}
