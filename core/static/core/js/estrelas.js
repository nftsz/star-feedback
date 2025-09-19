document.querySelectorAll('.estrelas').forEach(starDiv => {
    const rating = parseFloat(starDiv.dataset.rating);
    const stars = starDiv.querySelectorAll('span');

    stars.forEach((star, index) => {
        const fill = Math.min(Math.max(rating - index, 0), 1);
        star.style.setProperty('--fill', fill);
        star.style.background = `linear-gradient(90deg, gold ${fill * 100}%, #444 ${fill * 100}%)`;
        star.style.webkitBackgroundClip = 'text';
        star.style.color = 'transparent';
    });
});