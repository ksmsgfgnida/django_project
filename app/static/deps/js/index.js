document.addEventListener('DOMContentLoaded', function() {
    const subscribeButton = document.getElementById('subscribe-button');
    const emailInput = document.getElementById('form5Example22');

    subscribeButton.addEventListener('click', function(event) {
        // Предотвращаем отправку формы
        event.preventDefault();
        // Очищаем значение поля ввода
        emailInput.value = '';
    });
});
