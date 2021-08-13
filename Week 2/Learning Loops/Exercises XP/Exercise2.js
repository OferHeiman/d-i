let people = ["Greg", "Mary", "Devon", "James"];
people.splice(0, 1);
people.splice(2, 1, "Jason")
people.push("Ofer")
for (i in people) {
    console.log(people[i]);
    if (people[i] == 'Jason') {
        break
    }
}
let people_Copy = people.slice(1, 3)
console.log(people.indexOf('Mary'));
console.log(people.indexOf('Foo')); // returns -1 because it 'Foo' doesnt exist in the array
let last = people[people.length-1];
console.log(last);