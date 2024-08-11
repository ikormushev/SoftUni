function solve() {
    const correctAnswers = ["onclick", "JSON.stringify()", "A programming API for HTML and XML documents"];
    let userCorrectAnswers = [];

    let allQuestionsSections = document.querySelectorAll('section');

    for (let i = 0; i < allQuestionsSections.length; i++) {
        let currSection = allQuestionsSections[i].querySelectorAll('ul .quiz-answer .answer-wrap .answer-text');

        currSection.forEach(x => x.addEventListener('click', () => {
            if (x.textContent === correctAnswers[i]) {
                console.log(x.textContent);
                userCorrectAnswers.push(x.textContent);
            }
            allQuestionsSections[i].style.display = "none";

            let nextSection = allQuestionsSections[i + 1];

            if (nextSection !== undefined) {
                nextSection.style.display = "block";
            } else {
                let resultEL = document.querySelector('#results');
                let resultH1 = resultEL.querySelector('h1');
        
                console.log(resultEL);
                resultH1.textContent = (userCorrectAnswers.length === correctAnswers.length) ? 
                "You are recognized as top JavaScript fan!": `You have ${userCorrectAnswers.length} right answers`;
                resultEL.style.display = "block";
            }
        }));
    }
}
