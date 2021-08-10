let num = parseInt(prompt("Type a number"));
let boom = ['B', 'o', 'o', 'm'];
if (num < 2) {
    return "boom";
}
if (num >= 2) {
    for (i = 0; i < num - 2; i++) {
        boom.splice(1, 0, 'o')
    }
}
if (num % 5 === 0 && num % 2 === 0) {
    boom.push("!");
    return boom.join('').toUpperCase();
}
else if (num % 2 === 0) {
    boom.push("!");
    return boom.join('');
}
else if (num % 5 === 0) {
    return boom.join('').toUpperCase();
}
