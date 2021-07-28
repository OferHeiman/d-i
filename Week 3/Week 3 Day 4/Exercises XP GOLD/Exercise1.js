let language = prompt("Which language do you speak?","") //1
language = language.toLowerCase() //2
switch(language) //3
{
    case 'french': //4
        console.log("Bonjour")
      break;
    case 'english': //5
        console.log("Hello")
      break;
      case 'hebrew': //6
        console.log("Shalom")
        break;
    default: //7
        console.log("01110011 01101111 01110010 01110010 01111001")
  }