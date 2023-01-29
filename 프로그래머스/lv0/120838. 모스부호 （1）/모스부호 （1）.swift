import Foundation

let morse = [
    ".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f",
    "--.":"g","....":"h","..":"i",".---":"j","-.-":"k",".-..":"l",
    "--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r",
    "...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x",
    "-.--":"y","--..":"z"
]

func solution(_ letter:String) -> String {
    var answer = ""
    for i in letter.split(separator: " ") {
        answer += morse[String(i)]!
    }
    return answer
}