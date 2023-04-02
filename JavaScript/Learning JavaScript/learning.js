// initial

// console.log("I like puri!");
// console.log("Its really goooooood!!!")
// window.alert("I LOVE PURI") //this creates a popup

// variables

// let age = 14;
// let name = "K7"
// document.getElementById("p1").innerHTML = "Hello "+ name; //edits HTML document based off id



//user input (window prompt) ALWAYS A STRING

// let userName = window.prompt("What's your name?")
// console.log(userName)

//HTML Textbox

// let username;

// document.getElementById("myButton").onclick = function(){

//     username = document.getElementById("myText").value

//     console.log(username)
//     document.getElementById("myLabel").innerHTML = "Hello "+username
// }

// let age = window.prompt("How old are you? ");
// age = Number(age);
// age +=1;
// console.log(age)

// String Convertion is done through constructors. Ex=Number, String, Boolean(if string is empty ==false; else ==true)

//const is a var that cannot change ex. final

// const PI = 3.14159265358979; //cannot change generally all uppercase
// let r = window.prompt("Enter the radius of a circle: ");
// r = Number(r)
// c = 2 * PI * r
// console.log("The circumference is "+c)



// MATH WOOOOO

// let x = 134.1234561
// x = Math.round(x)
// //general math functions
// console.log(x)


// hypotenuse calculation 
// let a = window.prompt("Enter side a: ");
// a=Number(a);
// let b = window.prompt("Enter side b: ");
// b=Number(b);
// let c = Math.sqrt(Math.pow(a,2) + Math.pow(b,2));

// console.log("Side c is " +c)

// document.getElementById("submitbutton").onclick = function(){
//     let a = document.getElementById("aTB").value;
//     a=Number(a);
//     let b = document.getElementById("bTB").value;
//     b=Number(b);
//     let c = Math.sqrt(Math.pow(a,2) + Math.pow(b,2));

//     document.getElementById("cLabel").innerHTML = "Side C: "+c;
// }


// ---------------------Counter------------------//

// let count = 0;

// document.getElementById("decreaseBtn").onclick= function(){
//     count -=1;
//     document.getElementById("countLabel").innerHTML = count;
// }

// document.getElementById("resetBtn").onclick= function(){
//     count =0;
//     document.getElementById("countLabel").innerHTML = count;
// }

// document.getElementById("increaseBtn").onclick= function(){
//     count +=1;
//     document.getElementById("countLabel").innerHTML = count;
// }


//------------String slicing---------//
// let fullname ="Kesavan Rangarajan";
// let firstName;
// let lastName;
// // lastName=fullname.slice(3);
// // console.log(lastName);
// // firstName = fullname.slice(0,2);
// // console.log(firstName);
// firstName = fullname.slice(0,fullname.indexOf(" ")+1);
// console.log(firstName);
// lastName = fullname.slice(fullname.indexOf(" ")+1);
// console.log(lastName);

//------Method Chaining-----//
// let username = "k7";
// let letter = username.charAt(0).toUpperCase();
// console.log(letter);

//-----Checked-----//

// document.getElementById("checkboxBTN").onclick = function(){
//     const checkbox = document.getElementById("checkboxA");

//     const visaBTN = document.getElementById("visa");
//     const mastercardBTN = document.getElementById("mastercard");
//     const paypalBTN = document.getElementById("paypal");

//     if(checkbox.checked){
//         console.log("You are subscribed!")
//     }
//     else {
//         console.log("You are not subscribed!!")
//     }
//     if(visaBTN.checked){
//         console.log("You are paying with Visa.")
//     }
//     else if(mastercardBTN.checked){
//         console.log("You are paying with MasterCard.")
//     }
//     else if(paypalBTN.checked){
//         console.log("You are paying with PayPal.")
//     }
//     else {
//         console.log("You must select a payment type!")
//     }
// }

// -----Template Literals-----//

// let username ="K7";
// let items = 3;
// let total = 154;

// // console.log("Hello", username,", you have", items, "items in your cart. Your total is $",total)

// // console.log(`Hello ${username}`)
// // console.log(`You have ${items} items in your cart`)
// // console.log(`Your total $${total}`) ///////lot easier

// let text =`Hello ${username},
// you have ${items} items in your cart.
// Your total $${total}`
// document.getElementById("myLabel").innerHTML = text

//-----Arrays-----//
// let fruits = ["apple","orange","banana"];
// fruits[0] = "coconut";
// fruits.push("lemon");
// fruits.pop(); //removes last element
// fruits.unshift("mango"); //adds to the beginning
// fruits.shift(); //removes from beginning
// let length = fruits.length;
// let index = fruits.indexOf("banana")

// console.log(fruits, length, index);

//-----Spread Operator-----//
// ... is the spread operator
// let userName = "Kesavan Rangarajan";
// let numbers = [1,2,3,4,5,6,7,8,9];
// console.log(...numbers)
// let maximum = Math.max(...numbers);
// console.log(maximum)
// let class1 = ["Spongebob", "Patric", "Sandy"];
// let class2 = ["Squidward", "Mr.Krabs", "Plankton"];
// class1.push(class2); //DON'T DO THIS!!!!!!!!
// class1.push(...class2)
// console.log(...class1);

//-----Rest Parameters-----//
// let a = 1;
// let b = 2;
// let c = 3;
// let d = 4;
// let e = 5;

// console.log(sum(a,b,c,d,e))

// function sum(...numbers){
//     let total = 0;
//     for(let number of numbers){
//         total+=number
//     }
//     return total
// }

//-----Callbacks-----//
// sum(2,3, displayConsole)
// sum(2,3, displayDom)

// function sum(x,y,myfunction){
//     myfunction((x+y))
// }

// function displayConsole(output){
//     console.log(output)
// }

// function displayDom(output){
//     document.getElementById("myLabel").innerHTML=output
// }
