document.addEventListener('DOMContentLoaded', function() {
    const editButton = document.getElementById('edit-button');
    const editForm = document.getElementById('edit-form');
    const profileInfo = document.querySelector('.profile-data');

    editButton.addEventListener('click', function() {
        // Показываем форму для редактирования
        editForm.classList.remove('hidden');
        // Скрываем информацию о профиле
        profileInfo.style.display = 'none';
        // Скрываем кнопку "Изменить"
        editButton.style.display = 'none';
    });

    // Добавляем обработчик для отмены редактирования
    const cancelButton = document.createElement('button');
    cancelButton.classList.add('btn', 'btn-secondary', 'mt-3');
    cancelButton.textContent = 'Отменить';
    editForm.appendChild(cancelButton);

    cancelButton.addEventListener('click', function() {
        // Скрываем форму для редактирования
        editForm.classList.add('hidden');
        // Показываем информацию о профиле
        profileInfo.style.display = 'block';
        // Показываем кнопку "Изменить"
        editButton.style.display = 'block';
    });
});
