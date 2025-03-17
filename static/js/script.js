// Example: Add client-side validation (optional, but good practice)
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            //Basic validation example
            const principal = parseFloat(document.getElementById('principal').value);
            const rate = parseFloat(document.getElementById('rate').value);
            const time = parseFloat(document.getElementById('time').value);

            if (isNaN(principal) || principal <= 0) {
                alert('Please enter a valid positive principal amount.');
                event.preventDefault();
                return;
            }

            if (isNaN(rate) || rate < 0) {
                alert('Please enter a valid non-negative interest rate.');
                event.preventDefault();
                return;
            }
            if (isNaN(time) || time <= 0) {
                alert('Please enter a valid positive time in years.');
                event.preventDefault();
                return;
            }

        });
    }
});