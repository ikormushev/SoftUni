function solve() {
   let resultArea = document.querySelector('textarea');
   let products = document.querySelectorAll('.shopping-cart .product');
   let checkoutButton = document.querySelector('.checkout');
   let productsAdded = {};

   products.forEach(product => {
      let productButton = product.querySelector('.product-add .add-product');
      let productName = product.querySelector('.product-details .product-title').textContent;
      let productPrice = Number(product.querySelector('.product-line-price').textContent);
   
      productButton.addEventListener('click', () => {
         resultArea.value += `Added ${productName} for ${productPrice.toFixed(2)} to the cart.\n`;

         if (!productsAdded.hasOwnProperty(productName)) {
            productsAdded[productName] = 0;
         }
         productsAdded[productName] += productPrice;
      });
   });

   checkoutButton.addEventListener('click', () => {
      let totalPrice = Object.values(productsAdded).reduce((x, y) => x + y, 0);
      let finalProducts = Object.keys(productsAdded).join(', ');

      resultArea.value += `You bought ${finalProducts} for ${totalPrice.toFixed(2)}.`;

      let allButtons = document.querySelectorAll('button');
      allButtons.forEach(button => button.disabled = true);
   });
}
