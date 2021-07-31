//1
document.getElementsByClassName('list')[0].lastElementChild.textContent="Richard";
//2+3
let uls = document.getElementsByTagName("ul");
for (ul of uls) {
    ul.firstElementChild.innerText = "Ofer";
    ul.classList.add("student_list");//5
    let heystudentsli = document.createElement("li");
    heystudentsli.innerText = "hey students.";
    ul.appendChild(heystudentsli);
}
//4
let list = document.getElementsByClassName('list')[1];
list.removeChild(list.children[1]);
//5
document.getElementsByClassName('list')[0].classList.add("university");
document.getElementsByClassName('list')[0].classList.add("attendance");