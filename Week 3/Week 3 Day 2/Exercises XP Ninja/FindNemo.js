let sentence = prompt("Type a sentence with the word 'Nemo'.");
let Nemo=sentence.split(" ").indexOf("Nemo");
Nemo === -1 ?  console.log("I can't fine Nemo") : console.log("I found Nemo at "+Nemo);