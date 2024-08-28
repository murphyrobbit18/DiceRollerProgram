function receiveRoll(){
    const diceOptions = document.getElementById("dice");
    let selectedDice;

    for (let die of dice){
      if (die.checked){
        selectedDice = die.value;
        break;
      }
    }

    if (!selectedDice){
      alert("Please select at least one option.");
      return;
    }
    else if (selectedDice > 1){
        alert("Please select only one dice at a time.");
        return;
    }

    let diceRoll;
    switch (selectedDice) {
        case "d4":
            diceRoll = Math.floor(Math.random() * 4) + 1;
            break;
        case "d6":
            diceRoll = Math.floor(Math.random() * 6) + 1;
            break;
        case "d8":
            diceRoll = Math.floor(Math.random() * 8) + 1;
            break;
        case "d10":
            diceRoll = Math.floor(Math.random() * 10) + 1;
            break;
        case "d12":
            diceRoll = Math.floor(Math.random() * 12) + 1;
            break;
        case "d20":
            diceRoll = Math.floor(Math.random() * 20) + 1;
            break;
        case "d100":
            diceRoll =  Math.floor(Math.random() * 100) + 1;
            break;
        default:
            alert("Please select at least one option.");
            return;
    }

    const resultDiv = document.getElementById("result");
    resultDiv.textContent = `You rolled a ${diceRoll}`;
    resultDiv.style.display = 'block';

  }


function clearPage(){
    const questions = document.querySelectorAll('input[type = "checkbox"]')
    questions.forEach((question) => {
        question.checked = false;

    });
    
    const resultDiv = document.getElementById('result');
    resultDiv.style.display = 'none'; 
  }