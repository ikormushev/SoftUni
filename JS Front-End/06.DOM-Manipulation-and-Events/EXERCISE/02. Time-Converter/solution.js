function attachEventsListeners() {
    let daysInput = document.getElementById('days');
    let daysButton = document.getElementById('daysBtn');

    let hoursInput = document.getElementById('hours');
    let hoursButton = document.getElementById('hoursBtn');

    let minutesInput = document.getElementById('minutes');
    let minutesButton = document.getElementById('minutesBtn');

    let secondsInput = document.getElementById('seconds');
    let secondsButton = document.getElementById('secondsBtn');

    daysButton.addEventListener('click', () => {
        hoursInput.value = Number(daysInput.value) * 24;
        minutesInput.value = Number(daysInput.value) * 24 * 60;
        secondsInput.value = Number(daysInput.value) * 24 * 60 * 60;
    });

    hoursButton.addEventListener('click', () => {
        daysInput.value = Number(hoursInput.value) / 24;
        minutesInput.value = Number(hoursInput.value) * 60;
        secondsInput.value = Number(hoursInput.value) * 60 * 60;
    });

    minutesButton.addEventListener('click', () => {
        daysInput.value = Number(minutesInput.value) / (24 * 60);
        hoursInput.value = Number(minutesInput.value) / 60;
        secondsInput.value = Number(minutesInput.value) * 60;
    });

    secondsButton.addEventListener('click', () => {
        daysInput.value = Number(secondsInput.value) / (24 * 60 * 60);
        hoursInput.value = Number(secondsInput.value) / (60 * 60);
        minutesInput.value = Number(secondsInput.value) / 60;
    });
}
