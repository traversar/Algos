function isAnagram(strA, strB) {

    function createCharMap(text) {
        let charMap = {}

        for (let char of text) {
            if (charMap.hasOwnProperty(char)) {
                charMap[char]++
            } else {
                charMap[char] = 1
            }
        }

        return charMap
    }

    if (strA.length === strB.length) {
        let strAMap = createCharMap(strA)
        let strBMap = createCharMap(strB)
        for (let char in strAMap) {
            if (strAMap[char] !== strBMap[char]) {
                return false
            }
        }
        return true
    } else {
        return false
    }
}
