// Элементы
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const emailError = document.getElementById('emailError');
const passwordError = document.getElementById('passwordError');
const submitBtn = document.getElementById('submitBtn');
const togglePassword = document.getElementById('togglePassword');
const strengthBar = document.getElementById('strengthBar');

// Валидация email
const validateEmail = (email) => {
    if (!email) return { isValid: false, error: 'Email обязателен' };
    if (!email.includes('@')) return { isValid: false, error: 'Должен быть @' };
    if (email.split('@')[0].length < 3) return { isValid: false, error: 'Минимум 3 символа до @' };
    if (!email.split('@')[1].includes('.')) return { isValid: false, error: 'После @ должна быть точка' };
    return { isValid: true, error: '' };
};

// Валидация пароля
const validatePassword = (password) => {
    if (!password) return { isValid: false, error: 'Пароль обязателен' };
    if (password.length < 6) return { isValid: false, error: 'Минимум 6 символов' };
    if (password.length > 20) return { isValid: false, error: 'Максимум 20 символов' };
    if (!/\d/.test(password)) return { isValid: false, error: 'Нужна хотя бы одна цифра' };
    if (!/[a-zA-Z]/.test(password)) return { isValid: false, error: 'Нужна хотя бы одна буква' };
    return { isValid: true, error: '' };
};

// Обновление интерфейса
const updateUI = () => {
    const emailValid = validateEmail(emailInput.value);
    const passwordValid = validatePassword(passwordInput.value);

    emailError.textContent = emailValid.error;
    emailInput.classList.toggle('error', !emailValid.isValid);

    passwordError.textContent = passwordValid.error;
    passwordInput.classList.toggle('error', !passwordValid.isValid);

    submitBtn.disabled = !(emailValid.isValid && passwordValid.isValid);

    // Счётчик надёжности
    let strength = 0;
    const pwd = passwordInput.value;
    if (pwd.length >= 6) strength++;
    if (pwd.length >= 8) strength++;
    if (/[a-z]/.test(pwd)) strength++;
    if (/[A-Z]/.test(pwd)) strength++;
    if (/\d/.test(pwd)) strength++;
    if (/[!@#$%^&*]/.test(pwd)) strength++;

    const percent = (strength / 6) * 100;
    strengthBar.style.width = percent + '%';
    strengthBar.style.backgroundColor = 
        percent < 30 ? '#e74c3c' :
        percent < 60 ? '#f39c12' :
        percent < 80 ? '#3498db' : '#2ecc71';
};

// Отправка формы
document.getElementById('loginForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const emailValid = validateEmail(emailInput.value);
    const passwordValid = validatePassword(passwordInput.value);
    if (emailValid.isValid && passwordValid.isValid) {
        alert('Успешный вход!');
    }
});

// Глазик
togglePassword.addEventListener('click', () => {
    const type = passwordInput.type === 'password' ? 'text' : 'password';
    passwordInput.type = type;
    togglePassword.textContent = type === 'password' ? '👁️' : '🙈';
});

// Слушатели ввода
emailInput.addEventListener('input', updateUI);
passwordInput.addEventListener('input', updateUI);

// Запуск
updateUI();