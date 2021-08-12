function abbrevName(userString)
{
userString=userString.split(' ');
return userString[0]+" "+userString[1].charAt(0).toUpperCase()+'.';
}