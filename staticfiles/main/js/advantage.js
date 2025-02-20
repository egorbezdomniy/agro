document.querySelectorAll('.advantages').forEach(advantage => {
  advantage.addEventListener('mouseover', () => {
    advantage.style.backgroundColor = '#e8f0fe';
  });
  advantage.addEventListener('mouseout', () => {
    advantage.style.backgroundColor = '#fff';
  });
});