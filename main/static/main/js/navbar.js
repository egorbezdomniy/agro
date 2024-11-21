document.addEventListener("DOMContentLoaded", () => {
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    navToggle.addEventListener('click', () => {
        if (navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
            setTimeout(() => {
                navLinks.style.display = 'none';
            }, 300);
        } else {
            navLinks.style.display = 'flex';
            setTimeout(() => {
                navLinks.classList.add('active');
            }, 10);
        }
    });

    // Обработчик события для изменения размера окна
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            navLinks.style.display = 'flex'; // Обеспечиваем отображение навбара на десктопах
            navLinks.classList.remove('active');
        } else if (!navLinks.classList.contains('active')) {
            navLinks.style.display = 'none'; // Скрываем для мобильного вида, если неактивно
        }
    });
});