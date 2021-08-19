let people = ["Greg", "Mary", "Devon", "James"]
people.shift(); //1
people.splice(2,1,'Jason') //2
people.push("Ofer") //3
for(i=0;i<people.length;i++){ //4
console.log(people[i]);
}
for(i=0;i<people.length;i++){ //5
    console.log(people[i]);
    if(people[i] == 'Jason'){
        break
    }
}
let newPeopleArray = people.slice(1,3) //6
console.log(people.indexOf('Mary'));//7
console.log(people.indexOf('Foo'));//8,returns -1 because string 'Foo' doesn't exist in the array
let last = people[people.length-1]; //9