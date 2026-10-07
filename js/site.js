// The HTML keeps a readable year when JavaScript is unavailable.
const year = String(new Date().getFullYear());
document.querySelectorAll('[data-current-year]').forEach((element) => {
  element.textContent = year;
  element.setAttribute('datetime', year);
});
