const words = ['hello'];
let word = words[Math.floor(Math.random() * words.length)];
let currentGuess = 1
let letter = 1
let guess = "";
let endgame = false;
while(!endgame){
    document.addEventListener('keydown', (e)=>{
        if(isLetter(e.key)){
            if (currentGuess == 1){
                if (letter == 1){
                    document.querySelector('.guess1 .letter1').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 2){
                    document.querySelector('.guess1 .letter2').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 3){
                    document.querySelector('.guess1 .letter3').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 4){
                    document.querySelector('.guess1 .letter4').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 5){
                    document.querySelector('.guess1 .letter5').innerHTML = e.key.toUpperCase()
                    letter++;
                }
            }
            else if (currentGuess == 2){
                if (letter == 1){
                    document.querySelector('.guess2 .letter1').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 2){
                    document.querySelector('.guess2 .letter2').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 3){
                    document.querySelector('.guess2 .letter3').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 4){
                    document.querySelector('.guess2 .letter4').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 5){
                    document.querySelector('.guess2 .letter5').innerHTML = e.key.toUpperCase()
                    letter++;
                }
            }
            else if (currentGuess == 3){
                if (letter == 1){
                    document.querySelector('.guess3 .letter1').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 2){
                    document.querySelector('.guess3 .letter2').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 3){
                    document.querySelector('.guess3 .letter3').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 4){
                    document.querySelector('.guess3 .letter4').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 5){
                    document.querySelector('.guess3 .letter5').innerHTML = e.key.toUpperCase()
                    letter++;
                }
            }
            else if (currentGuess == 4){
                if (letter == 1){
                    document.querySelector('.guess4 .letter1').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 2){
                    document.querySelector('.guess4 .letter2').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 3){
                    document.querySelector('.guess4 .letter3').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 4){
                    document.querySelector('.guess4 .letter4').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 5){
                    document.querySelector('.guess4 .letter5').innerHTML = e.key.toUpperCase()
                    letter++;
                }
            }
            else if (currentGuess == 5){
                if (letter == 1){
                    document.querySelector('.guess5 .letter1').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 2){
                    document.querySelector('.guess5 .letter2').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 3){
                    document.querySelector('.guess5 .letter3').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 4){
                    document.querySelector('.guess5 .letter4').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 5){
                    document.querySelector('.guess5 .letter5').innerHTML = e.key.toUpperCase()
                    letter++;
                }
            }
            else if (currentGuess == 6){
                if (letter == 1){
                    document.querySelector('.guess6 .letter1').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 2){
                    document.querySelector('.guess6 .letter2').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 3){
                    document.querySelector('.guess6 .letter3').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 4){
                    document.querySelector('.guess6 .letter4').innerHTML = e.key.toUpperCase()
                    letter++;
                }
                else if (letter == 5){
                    document.querySelector('.guess6 .letter5').innerHTML = e.key.toUpperCase()
                    letter++;
                }
            }
        }
        if(e.key == 'Backspace'){
            if(letter!=1){
                document.querySelector(`.guess${currentGuess} .letter${letter-1}`).innerHTML = '';
                letter--;
            }
        }
    })

    document.addEventListener('keydown',async(e)=>{
        if(letter==6 && e.key=="Enter"){
            console.log('Pressed Enter')
            guess = '';
            guess += (document.querySelector(`.guess${currentGuess} .letter1`).innerHTML);
            guess += (document.querySelector(`.guess${currentGuess} .letter2`).innerHTML);
            guess += (document.querySelector(`.guess${currentGuess} .letter3`).innerHTML);
            guess += (document.querySelector(`.guess${currentGuess} .letter4`).innerHTML);
            guess += (document.querySelector(`.guess${currentGuess} .letter5`).innerHTML);
            guess = guess.toLowerCase();
            
            if(await isWord(guess)){
                if(currentGuess >=7){
                    endgame = true;
                }
                console.log(`Guess ${currentGuess}: ${guess}`)
                let count = 0
                for(var i = 0; i < guess.length; i++){
                    for(var j = 0; j < word.length; j++){
                        if(guess.charAt(i)==word.charAt(j)){
                            isThere(i)
                        }
                    }
                }

                for(var i =0; i < word.length; i++){
                    if(guess.charAt(i)==word.charAt(i)){
                        isCorrect(i)
                        count++;
                    }
                }
                if(count == 5){
                    alert('Correct')
                    endgame = true;
                }
                
                
                letter=1;
                currentGuess++;
            }
            else{
                notWord(guess)
                guess =''
            }
        }
    })
}
if(currentGuess >=  7){
    lost()
}
else{
    won()
}
const lost = () =>{
    document.querySelector('.game').style += 'background-color: red;'

}
const won = () =>{
    document.querySelector('.game').style += 'background-color: #0f0;'
    document.querySelector('.winner-screen') += 'display: flex;'
}
const isWord = async(guess) => {

    const response = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${guess}`);
    var data = await response.json();
    console.log(data);
    if(data.title == "No Definitions Found"){
        return false;
    }
    return true;
    
}
const notWord = (guess) => {
    alert(`${guess} is not a word. Please enter an actual word.`);
}
const isCorrect = (location) => {
    document.querySelector(`.guess${currentGuess} .letter${location+1}`).style = 'background-color: #0f0;'
}
const isThere = (location) => {
    document.querySelector(`.guess${currentGuess} .letter${location+1}`).style = 'background-color: yellow;'
}
const isLetter = (str) => {
    return str.length === 1 && str.match(/[a-z]/i);
}