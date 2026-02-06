document.addEventListener('DOMContentLoaded', function() {
    const telefonInput = document.querySelector('#telefon');
    if (telefonInput) {
        telefonInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length > 9) {
                value = value.slice(0, 9);
            }
            e.target.value = value;
            const formatted = formatPhoneNumber(value);
            e.target.dataset.formatted = formatted;
        });

        telefonInput.addEventListener('blur', function() {
            const form = telefonInput.closest('form');
            const hiddenInput = document.createElement('input');
            hiddenInput.type = 'hidden';
            hiddenInput.name = 'telefon';
            hiddenInput.value = telefonInput.dataset.formatted ? telefonInput.dataset.formatted.replace(/\s/g, '') : '';
            form.appendChild(hiddenInput);
        });
    }

    function formatPhoneNumber(value) {
        if (value.length === 9) {
            return `+420 ${value.slice(0, 3)} ${value.slice(3, 6)} ${value.slice(6)}`;
        }
        return value ? `+420 ${value}` : '';
    }
});