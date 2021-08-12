function isOmnipresent(Array, val) {
    return Array.every(ar => ar.includes(val));
}

// function isOmniPresent(arr, val) {
//     for (i = 0; i < arr.length; i++) {
//         for (n = 0; n < arr[n].length; n++) {
//             if (arr[n].includes(val) == false) {
//                 return false;
//             }
//         }
//     }
//     return true;
// }