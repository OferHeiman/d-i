
let addressNumber = "5 ";
let addressStreet = "Hamagen ";
let country = "Israel";
let global_address = addressNumber.concat(addressStreet).concat(country);
let global_address1= addressNumber + "" + addressStreet + "" + country;
console.log(global_address)
console.log(global_address1)

let birthyear = 1996;
let futureyear = 2026;
let age1 = futureyear - birthyear;
console.log("I will be " + (futureyear - birthyear) + " In " + futureyear);
console.log("I will be " + age1 + " In " + futureyear);

let op = Boolean(10 > 9)
console.log(op)

let pets = ['cat','dog','fish','rabbit','cow'];
console.log(pets[1])
pets.push("horse")
console.log(pets)
pets.splice(3,1)
console.log(pets)
console.log(pets.length)

