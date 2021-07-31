//1
document.getElementsByClassName('list')[0].lastElementChild.textContent="Richard";
//2
document.getElementsByClassName('list')[0].firstElementChild.textContent="Ofer";
document.getElementsByClassName('list')[1].firstElementChild.textContent="Ofer";
//3
let li=document.createElement("li");
li.appendChild(document.createTextNode("Hey students"));
let li2=document.createElement("li");
li2.appendChild(document.createTextNode("Hey students"));
document.getElementsByClassName('list')[0].appendChild(li);
document.getElementsByClassName('list')[1].appendChild(li2);
//4
let list = document.getElementsByClassName('list')[1];
list.removeChild(document.getElementsByClassName('list')[1].children[1]);
//5
document.getElementsByClassName('list')[0].classList.add("student_list");
document.getElementsByClassName('list')[1].classList.add("student_list");
document.getElementsByClassName('list')[0].classList.add("university");
document.getElementsByClassName('list')[0].classList.add("attendance");