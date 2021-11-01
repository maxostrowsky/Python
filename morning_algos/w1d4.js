// pseudo code
// 1. create a function that takes in a string
// 2. create a new string
// 2.1 create count
// 3. loop through the string
// 4. determine if next character is the same as current index
// 5. create a count


// const str1 = "aabb";
//     const expected1 = "a4b2c1d3";

//     function encodeStr(str) {
//     var newstring = ""
//     var count = 1
//     if(str.length <= 1){
//         return str
//     }
//     for (var i = 0; i<str.length;i++){
//         if(str[i]== str[i+1]){
//             count += 1;
//         }
//         if(str[i]!= str[i+1]){
//             newstring += str[i] + count;
//             count = 1
//             }
//     }
//     if(newstring.length>=str.length){
//         return str
//     }
//     return newstring
// }

// console.log(encodeStr(str1));
/* 
    Given in an alumni interview in 2021.
    String Encode
    You are given a string that may contain sequences of consecutive characters.
    Create a function to shorten a string by including the character,
    then the number of times it appears. 
    
    
    If final result is not shorter (such as "bb" => "b2" ),
    return the original string.
  */

    // const str1 = "aaaabbcddd";
    // const expected1 = "a4b2c1d3";
    
    
    // const str2 = "";
    // const expected2 = "";
    
    // const str3 = "a";
    // const expected3 = "a";
    
    // const str4 = "bbcc";
    // const expected4 = "bbcc";
    
    // const str5 = "aaaabbaaacddd";
    // const expected5 = "a4b2a3c1d3";
//     // /**
//    * Encodes the given string such that duplicate characters appear once followed
//    * by a number representing how many times the char occurs only if the
//    * character occurs more than two time.
//    * - Time: O(?).
//    * - Space: O(?).
//    * @param {string} str The string to encode.
//    * @returns {string} The given string encoded.
// //    */
//     function encodeStr(str) {}
    
  // ***********************************************
    
    /* 
    String Decode  
  */
    
const two_str1 = "a3b2c1d3";
const two_expected1 = "aaabbcddd";

const two_str2 = "a3b2c12d10";
const two_expected2 = "aaabbccccccccccccdddddddddd";
    
    /**
   * Decodes the given string by duplicating each character by the following int
   * amount if there is an int after the character.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str An encoded string with characters that may have an int
   *    after indicating how many times the character occurs.
   * @returns {string} The given str decoded / expanded.
   */
function decodeStr(str) {}
    let decode = ""
    let i = 0
    while (i < str.length){
        let char = str[i++]
        let numstr = ""

        while(i < str.length && !isNaN(str[i])){
            numstr += str[i++]
        }
        decode += char.
    }
decode(two_str2)