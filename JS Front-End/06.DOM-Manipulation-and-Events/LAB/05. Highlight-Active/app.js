function focused() {
    const inputs = document.querySelectorAll('input[type="text"]');

    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            input.closest('div').classList.add('focused');
        });

        input.addEventListener('blur', function() {
            input.closest('div').classList.remove('focused');
        });
    });
}
