// pseudo code
// 1. create a function that with a given STRING iterated in reverse
// 2. make a newString
// 3. for loop through string 


const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";



function creature(string){
    let newString = ""
    for(let x = string.length-1; x >= 0; x--){
        newString += string[x];
    }
    return newString
}

console.log(creature(str1))
console.log(creature(str2))


/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {}

module.exports = { reverseString };

