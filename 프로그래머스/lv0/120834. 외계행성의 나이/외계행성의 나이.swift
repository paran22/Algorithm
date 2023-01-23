import Foundation

func solution(_ age:Int) -> String {
    let asciiA: Int = Int(Character("a").asciiValue!)
    return String(age).reduce("", { $0 + String(UnicodeScalar(asciiA + Int(String($1))!)!) })
}