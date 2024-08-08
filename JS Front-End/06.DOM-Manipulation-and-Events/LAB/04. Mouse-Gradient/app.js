function attachGradientEvents() {
    let hoverEl = document.getElementById('gradient');
    let resultEL = document.getElementById('result');

    hoverEl.addEventListener('mousemove', gradientMove);
    hoverEl.addEventListener('mouseout', gradientOut);

    function gradientMove(event) {
        let resultGradient = event.offsetX / (event.target.clientWidth - 1);
        resultGradient = Math.trunc(resultGradient * 100);
        resultEL.textContent = resultGradient + "%";
    }

    function gradientOut(event) {
        resultEL.textContent = '';
    }
}
