import Foundation

func solution(_ dots:[[Int]]) -> Int {
    let groupX = Dictionary(grouping: dots, by: { $0[0] } )
    let groupY = Dictionary(grouping: dots, by: { $0[1] } )
    let x = groupX[groupX.keys.first!]!.map { $0[1] }
    let y = groupY[groupY.keys.first!]!.map { $0[0] }
    
    return (x.max()! - x.min()!) * (y.max()! - y.min()!)
}