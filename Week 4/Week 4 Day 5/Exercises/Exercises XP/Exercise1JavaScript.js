//1
let element=document.getElementById("navBar")
element.setAttribute("id","socialNetworkNavigation")
//2
let li=document.createElement("li");
li.appendChild(document.createTextNode("Logout"));
element.firstElementChild.appendChild(li);
//3
element.firstElementChild.firstElementChild.textContent;
element.firstElementChild.lastElementChild.textContent;