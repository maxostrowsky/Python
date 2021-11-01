// pseudo code
// 1. Create a function that takes in a list 
// 2. create empty dictionary
// 3. loop thru list 
// 4. add to dictionary





/* 
Zip Arrays into Map


Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

// const keys1 = ["abc", 3, "yo"];
// const vals1 = [42, "wassup", true];
// const expected1 = {
//     abc: 42,
//     3: "wassup",
//     yo: true,
// };

// const keys2 = ["abc", 3, "yo", "bro"];
// const vals2 = [42, "wassup", true];
// const expected2 = {
//     abc: 42,
//     3: "wassup",
//     yo: true,
//     bro: null
// };

// const keys3 = ["abc", 3, "yo"];
// const vals3 = [42, "wassup", true, 'bro'];
// const expected3 = {
//     abc: 42,
//     3: "wassup",
//     yo: true,
//     "?":"?"
// };

// /**
//    * Converts the given arrays of keys and values into an object.
//    * - Time: O(?).
//    * - Space: O(?).
//    * @param {Array<string>} keys
//    * @param {Array<any>} values
//    * @returns {Object} The object with the given keys and values.
//    */
// function zipArraysIntoMap(keys, values) {
//     if (values.length > keys.lenth){
//         return false
//     }
//         var new_dict = {}
//         for (var i=0; i < keys.length; i++){
//             if (values[i] === undefined){
//                 new_dict[keys[i]] = null
//             }
//             else{
//                 new_dict[keys[i]] = values[i]
//             }
//         }
//         return new_dict
// }
// console.log(zipArraysIntoMap(keys1, vals1))
// console.log(zipArraysIntoMap(keys2, vals2))
// console.log(zipArraysIntoMap(keys3, vals3))



/* 
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const two_expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

const two_obj2 = { name: "Zaphod", charm: "high", morals: "dicey", something: "dicey" };
// const expected1 = { Zaphod: "name", high: "charm", dicey: ["morals","something"] };
// const expected1 = { Zaphod: "name", high: "charm", dicey: "something" };
// const expected1 = { Zaphod: "name", high: "charm", dicey: "morals", dicey1: "something" };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, string>} obj An object with string keys and string values.
 * @return The given object with key value pairs inverted.
 */
function invertObj(obj) {
    let dict = {}
    for (let key in obj){
        let value = obj[key]
        if (dict.hasOwnProperty(value)){
            if (typeof dict[value] === 'string'){
                arr = [dict[value]]
            } else if (typeof dict[value] === 'object'){
                dcit[value].push(key)
            }
            dict[value] = arr
        } else{
            dict[value] = key
        }
    }
    return dict
} 

console.log(invertObj(two_obj2))