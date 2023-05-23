import Foundation

func solution(_ num_list:[Int]) -> Int {
    var answer = 0;
    for num in num_list {
        var n = num
        while n > 1 {
            if n % 2 == 0 {
                n /= 2
            } else {
                n = (n - 1) / 2
            }
            answer += 1
        }
    }
    return answer
}