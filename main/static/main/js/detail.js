function changeImage(element) {
    const mainImage = document.getElementById('displayed-image');
    mainImage.src = element.src;
    mainImage.style.width = "500px";  // Фиксированная ширина
    mainImage.style.height = "500px";  // Автоматическая высота для сохранения пропорций
}
