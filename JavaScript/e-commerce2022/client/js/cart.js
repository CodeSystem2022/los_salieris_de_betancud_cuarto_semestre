const $cartModal = document.getElementById("modal-container");
const $cartOverlay = document.getElementById("modal-overlay");
const $cartButton = document.getElementById("cart-btn");

const displayCart = () => {
  $cartModal.style.display = "block";
  $cartOverlay.style.display = "block";
  const $modalHeader = document.createElement("header");
  const $modalClose = document.createElement("button");
  const $modalTitle = document.createElement("h3");
  // Configura el boton de cierre del header
  $modalClose.textContent = "❌";
  $modalClose.className = "modal-close";
  // Configura el título del modal
  $modalTitle.textContent = "Cart";
  $modalTitle.className = "modal-title";
  // Agrega elementos al header del modal
  $modalHeader.append($modalTitle, $modalClose);
  // Agrega elementos al contenedor del modal
  $cartModal.append($modalHeader);

  $modalClose.addEventListener("click", event => {
    event.preventDefault();
    $cartModal.removeChild($modalHeader)
    $cartModal.style.display = 'none'
    $cartOverlay.style.display = 'none'
  });
};

$cartButton.addEventListener("click", event => {
  event.preventDefault();
  displayCart();
});
