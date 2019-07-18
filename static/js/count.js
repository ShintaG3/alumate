const DUR = 3.6;
let isAnimating = false;

document.addEventListener('DOMContentLoaded', () => {
  if (isAnimating) {
    return;
  }

  isAnimating = true;
  document.querySelectorAll('.count').forEach(h2 => {

    const from = parseInt(h2.dataset.from, 10);
    const to = parseInt(h2.dataset.to, 10);
    let obj = { count: from };

    TweenMax.to(obj, DUR, {
      count: to,
      ease: Power3.easeInOut,
      onUpdate: () => {
        h2.textContent = Math.floor(obj.count);
      },
      onComplete: () => {
        isAnimating = false;
      } });

  })

});
