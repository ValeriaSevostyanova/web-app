document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Здесь можно добавить код для отправки данных на сервер

    // Для примера просто выводим сообщение
    // document.getElementById('message').innerText = `Регистрация успешна! Добро пожаловать, ${username}!`;
    
    // Очистка формы
    this.reset();
});
