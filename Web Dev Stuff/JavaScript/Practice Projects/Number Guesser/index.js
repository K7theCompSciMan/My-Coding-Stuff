const answer = Math.floor(Math.random()*100 +1)
let guesses = 0;

document.getElementById("submitButton").onclick = function(){
    let guess =document.getElementById("guessField").value
    guesses+=1
    if(guess==answer && guesses ==1) {
        alert(`${answer} is the number. It took you ${guesses} guess.`)
    }
    else if(guess==answer && guesses >1) {
        alert(`${answer} is the number. It took you ${guesses} guesses.`)
    }
    else if(guess>answer) {
        alert("Too large")
    }
    else if(guess<answer) {
        alert("Too small")
    }
}