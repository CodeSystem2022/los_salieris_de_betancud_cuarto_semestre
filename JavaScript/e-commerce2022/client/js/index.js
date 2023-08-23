const $shopContent = document.querySelector('#shopContent')

products.forEach(product => {
    const $product = document.createElement('div')
    const $productName = document.createElement('h3')
    const $productPrice = document.createElement('p')
    const $productImage = document.createElement('img')
    $productName.textContent = product.productName
    $productPrice.textContent = `$${product.price}`
    $productImage.setAttribute('src', product.img)
    $product.append($productImage, $productName, $productPrice)
    $shopContent.append($product)
})