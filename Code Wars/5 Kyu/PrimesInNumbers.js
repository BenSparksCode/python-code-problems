// https://www.codewars.com/kata/54d512e62a5e54c96200019e

// TIME: O(sqrt(n))
// SPACE: O(1)

function primeFactors(n) {

    let div = 2
    let divCnt = 0
    let output = ""

    while (n > 1) {
        if (n % div == 0) {
            divCnt = 0
            while (n % div == 0) {
                n = n / div
                divCnt += 1
            }
            output += divCnt > 1 ? "(" + div + "**" + divCnt + ")" : "(" + div + ")"
        }
        div++
    }

    return output
}