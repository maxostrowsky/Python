// pseudo code
// 1. create a function that takes in an array that gives a string
// 2. create newString
// 3. loop through array
// 4. add each number to new string
// 5. console.log  string
// 6. repeat
// 7. 

/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

// edge case
const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

function newString(arr){
    var string = ""
    for (var x=0; x<arr.length; x++){
        if(x === arr.length-1){
            string += arr[x]
        }
        else{
            string += arr[x] + ","
        }
    }
    console.log(string)
    var string2 = ""
    for (var x=0; x<arr.length; x++){
        if(x === arr.length-1){
            string2 += arr[x]
        }
        else{
            string2 += arr[x] + "-"
        }
    }
    console.log(string2)
    var string3 = ""
    for (var x=0; x<arr.length; x++){
        if(x === arr.length-1){
            string3 += arr[x]
        }
        else{
            string3 += arr[x] + " - "
        }
    }
    console.log(string3)
    return string, string2, string3
}

newString(arr1)

// console.log(newString(arr1, arr2, arr3))

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */

// ****************************************************

/* 
Book Index
Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums span a consecutive range
*/

// pseudo code
// 1. create a function that takes in an array and a separator
// 2. create a newString
// 3. loop thru array
// 4. conditional for separators
// 5. array in to the string



const two_nums1 = [1, 13, 14, 15, 37, 38, 70];
const two_expected1 = "1, 13-15, 37-38, 70";

const two_nums2 = [1, 13, 14, 15, 16,17,18, 37, 38, 70, 71, 72, 73, 74, 75];
const two_expected2 = "1, 13-18, 37-38, 70-75";

function join(arr, separator) {
    var newerString = ""
    for (var i=0; i < arr.length; i++){
        if (arr[i + 1] === arr[i] + 1){
            
        }
    }
}

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @returns {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */

function bookIndex(nums) {}