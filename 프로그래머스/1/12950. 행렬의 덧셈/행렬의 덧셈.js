function solution(arr1, arr2) {
    return arr1.map((e, index) => e.map((value, index2) => value + arr2[index][index2]))
}