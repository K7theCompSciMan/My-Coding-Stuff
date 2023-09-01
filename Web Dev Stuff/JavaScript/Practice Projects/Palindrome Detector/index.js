document.getElementById("btn").onclick = function() {

    let word = document.getElementById("word").value;

    word = word.toLowerCase();

    var reverseWord = word.split("").reverse().join("");
    
    if(reverseWord == word)  {
        document.getElementById("Output").innerHTML = "That word is a palindrome";``
    }

    else {
        document.getElementById("Output").innerHTML = "That word is not a palindrome";
    }
}