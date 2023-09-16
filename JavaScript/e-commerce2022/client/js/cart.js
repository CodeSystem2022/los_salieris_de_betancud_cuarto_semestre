const $cartModal = document.getElementById("modal-container");
const $cartOverlay = document.getElementById("modal-overlay");
const $cartButton = document.getElementById("cart-btn");


function clearCart() {
  $cartModal.innerHTML = "";
};

function increseItemCart (productContainer, product, totalPriceContainer) {
  const $quantityInput = productContainer.querySelector(".quantity-input");
  const quantity = parseInt($quantityInput.textContent);
  const itemCartIndex = cart.findIndex(item => item.id === product.id);
  const newQuantity = quantity + 1;
  $quantityInput.textContent = newQuantity;
  cart[itemCartIndex].quantity = newQuantity;
  setTotalPrice(totalPriceContainer);
};

function decreseItemCart(productContainer, product, totalPriceContainer) {
  const $quantityInput = productContainer.querySelector(".quantity-input");
  const quantity = parseInt($quantityInput.textContent);
  const itemCartIndex = cart.findIndex(item => item.id === product.id);
  if (quantity > 1) {
    const newQuantity = quantity - 1;
    $quantityInput.textContent = newQuantity;
    cart[itemCartIndex].quantity = newQuantity;
  } else {
    productContainer.remove();
    cart.splice(itemCartIndex, 1);
  }
  setTotalPrice(totalPriceContainer);
};

function deleteItemCart(productContainer, product, totalPriceContainer) {
  const itemCartIndex = cart.findIndex(item => item.id === product.id);
  productContainer.remove();
  cart.splice(itemCartIndex, 1);
  setTotalPrice(totalPriceContainer);
}

function getTotalPrice() {
  const totalPrice = cart.reduce((acc, item) => {
    return acc + item.price * item.quantity;
  }, 0);
  return totalPrice;
}

function setTotalPrice(footer) {
  const totalPrice = getTotalPrice();
  footer.textContent = `Total: $ ${totalPrice}`;
}

function createProductCartElement(productContainer, product, totalPriceContainer) {
  const $modalBody = document.createElement("div");
  // Configura el contenido del modal
  $modalBody.className = "modal-body";
  $modalBody.innerHTML = `
    <div class="product">
      <img src="${product.img}" alt="${
  product.productName}" class="product-img" />
      <div class="product-info">
        <h4>${product.productName}</h4>
      </div>
      <div class="quantity">
        <span class="quantity-btn-decrese">-</span>
        <span class="quantity-input">${product.quantity}</span>
        <span class="quantity-btn-increse">+</span>
      </div>
      <div class="price">$ ${product.price * product.quantity}</div>
      <div class="delete-product">❌</div>
    </div>
    `;

  productContainer.append($modalBody);

  const $decreseButton = $modalBody.querySelector(".quantity-btn-decrese");
  const $increseButton = $modalBody.querySelector(".quantity-btn-increse");
  const $deleteButton = $modalBody.querySelector(".delete-product");

  $modalBody.addEventListener("click", event => {
    event.preventDefault()
    switch (event.target) {
      case $decreseButton:
        return decreseItemCart($modalBody, product, totalPriceContainer);
      case $increseButton:
        return increseItemCart($modalBody, product, totalPriceContainer);
      case $deleteButton:
        return deleteItemCart($modalBody, product, totalPriceContainer);
      default:
        break;
    }
  })
};



const displayCart = () => {
  $cartModal.style.display = "block";
  $cartOverlay.style.display = "block";
  const $modalHeader = document.createElement("header");
  const $modalClose = document.createElement("button");
  const $modalTitle = document.createElement("h3");
  const $modalFooter = document.createElement("div");

  // Configura el boton de cierre del header
  $modalClose.textContent = "❌";
  $modalClose.className = "modal-close";
  // Configura el título del modal
  $modalTitle.textContent = "Cart";
  $modalTitle.className = "modal-title";
  // Configura el footer del modal
  $modalFooter.className = "modal-footer";
  $modalFooter.innerHTML = `
  <div className="total-price">Total: ${getTotalPrice()}</div>
  `;
  // Agrega elementos al header del modal
  $modalHeader.append($modalTitle, $modalClose);
  // Agrega elementos al contenedor del modal
  $cartModal.append($modalHeader);
  // Carga los productos al contenedor del modal
  cart.forEach(product => createProductCartElement($cartModal, product, $modalFooter));
  // Agrega el footer al contenedor del modal
  $cartModal.append($modalFooter);

  $modalClose.addEventListener("click", event => {
    event.preventDefault();
    $cartModal.removeChild($modalHeader)
    $cartModal.style.display = 'none'
    $cartOverlay.style.display = 'none'
  });
};

$cartButton.addEventListener("click", event => {
  event.preventDefault();
  clearCart();
  displayCart();
});
