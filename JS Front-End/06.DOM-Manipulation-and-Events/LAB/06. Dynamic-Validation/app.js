function validate() {
    let emailInput = document.getElementById('email');
    let emailPattern = /^[a-z]+@[a-z]+\.[a-z]+$/;

    emailInput.addEventListener('change', emailChange);

    function emailChange(event) {
        if (!emailPattern.test(emailInput.value)) {
            emailInput.classList.add('error');
        } else {
            emailInput.classList.remove('error');
        }
    }
}
