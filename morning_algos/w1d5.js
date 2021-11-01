// pseudo code
// 1. create a funtion that takes in a string
// 2. create a new variable
// 3. loop through the given string backwards
// 4. push into new variable
// 5. compare both strings



/* 
String: Is Palindrome
Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
Do not ignore spaces, punctuation and capitalization
 */

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

//   /**
//    * Determines if the given str is a palindrome (same forwards and backwards).
//    * - Time: O(?).
//    * - Space: O(?).
//    * @param {string} str
//    * @returns {boolean} Whether the given str is a palindrome or not.
//    */
function isPalindrome(str){
    newString = ""
    for(var x = str.length-1; x >= 0; x--){
        newString += str[x]
    }
    
    if(newString == str){
        return true
    }
    else{
        return false
    }
}
isPalindrome(str1)
isPalindrome(str2)
isPalindrome(str3)
isPalindrome(str4)



  /* 
  Longest Palindrome

  For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 

  Strings longer or shorter than complete words are OK.

  All the substrings of "abc" are:
  a, ab, abc, b, bc, c
*/

// pseudo code
// 1. create a function that takes a in string
// 2. create a new variable
// 3. loop through string 
// 4. 

// const str1 = "what up, daddy-o?";
// const expected1 = "dad";

// const str2 = "uh, not much";
// const expected2 = "u";

// const str3 = "Yikes! my favorite racecar erupted!";
// const expected3 = "e racecar e";

// const str4 = "a1001x20002y5677765z";
// const expected4 = "5677765";

// const str5 = "a1001x20002y567765z";
// const expected5 = "567765";

// /**
//  * Finds the longest palindromic substring in the given string.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str
//  * @returns {string} The longest palindromic substring from the given string.
//  */
// function longestPalindromicSubstring(str) {
//     newString = ""
//     newString2 = ""
//     for(var i = str.length-1; i >= 0; i--){
//         newString += str[i]
//     }
//     newString2 = str.slice(newString[i] == str[i])
//     console.log(newString2)
//     return newString2
// }
// longestPalindromicSubstring(str1)