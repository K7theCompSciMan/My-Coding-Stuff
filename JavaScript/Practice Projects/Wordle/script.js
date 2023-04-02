const words = ['hello'];
let word = words[Math.floor(Math.random() * words.length)];
let currentGuess = 1
let letter = 1
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
let isLetter = (str) => {
    return str.length === 1 && str.match(/[a-z]/i);
}

// Determine if the Word is a word
document.addEventListener('keydown',(e)=>{
    if(letter==5 && e.key=="Enter"){
        letter=1;
        currentGuess++;
    }
})