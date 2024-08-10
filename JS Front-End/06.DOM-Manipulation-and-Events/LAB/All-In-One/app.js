// Validate & Check Functions
function validateInput(inputEl, inputType) {
    let productTitlePattern = /^[a-zA-Z]+$/;
    let productPricePattern = /^(0|[1-9]+[0-9]*)(\.[0-9]+)*$/;

    let patternToUse = "";

    if (inputType === "name") {
        patternToUse = productTitlePattern;
    } else if (inputType === "price") {
        patternToUse = productPricePattern;
    }

    return patternToUse.test(inputEl.value);
}

function changeBorderDependingOnValue(inputEl, inputType) {
    if (!validateInput(inputEl, inputType)) {
        inputEl.style.border = '2px solid red';
    } else {
        inputEl.style.border = '2px solid gray';
    }
}

function validate() {
    let productTitleInput = document.getElementById('productTitle');

    productTitleInput.addEventListener('change', () => {
        changeBorderDependingOnValue(productTitleInput, 'name')
    });

    let productPriceInput = document.getElementById('productPrice');

    productPriceInput.addEventListener('change',() => {
        changeBorderDependingOnValue(productPriceInput, 'price')
    });
}

function doesProductExist(productTitle) {
    let products = document.querySelectorAll('.product .product-details .product-title');

    for (let productT of products) {
        if (productT.textContent === productTitle) return true;
    }

    return false;
}

// Create a product
function createProduct() {
    let productTitle = document.getElementById('productTitle');
    let productPrice = document.getElementById('productPrice');
    let productDescriptionValue = document.getElementById('productDescription').value;
    let productsCount = document.querySelectorAll('.product').length;

    if (!validateInput(productTitle, 'name') || !validateInput(productPrice, 'price') ) {
        return;
    }

    if (doesProductExist(productTitle.value)) return;

    // Product Element
    let productEl = document.createElement('div');
    productEl.classList.add('product');
    productEl.id = `productN${productsCount+1}`;

    // Product Image
    let productImage = document.createElement('div');
    productImage.classList.add('product-image');
    let image = document.createElement('img');
    image.src = 'productTemplate.jpg';
    productImage.appendChild(image);

    // Product Details - Title & Description
    let productDetails = document.createElement('div');
    productDetails.classList.add('product-details');

    let productTitleDiv = document.createElement('div');
    productTitleDiv.classList.add('product-title');
    productTitleDiv.textContent = productTitle.value;

    let productDescriptionDiv = document.createElement('div');
    productDescriptionDiv.classList.add('product-description');
    productDescriptionDiv.textContent = (productDescriptionValue === "") ? "No description.": productDescriptionValue;
    
    productDetails.appendChild(productTitleDiv);
    productDetails.appendChild(productDescriptionDiv);

    // Product Add-to-Checkout button
    let productAddToCheckoutDiv = document.createElement('div');
    productAddToCheckoutDiv.classList.add('product-add');

    let productAddToCheckoutButton = document.createElement('button');
    productAddToCheckoutButton.classList.add('add-product');
    productAddToCheckoutButton.textContent = 'Add to checkout';
    productAddToCheckoutDiv.appendChild(productAddToCheckoutButton);

    // Product Price
    let prodcutPriceDiv = document.createElement('div');
    prodcutPriceDiv.classList.add('product-line-price');
    prodcutPriceDiv.textContent = Number(productPrice.value).toFixed(2);

    // Delete Button
    let productDelButtonDiv = document.createElement('div');
    productDelButtonDiv.classList.add('delButton');
    let productDelButton = document.createElement('button');
    productDelButton.textContent = "X";
    productDelButton.addEventListener('click', () => productEl.remove());
    productDelButtonDiv.appendChild(productDelButton);
    
    // Add all to Product Element
    productEl.appendChild(productImage);
    productEl.appendChild(productDetails);
    productEl.appendChild(productAddToCheckoutDiv);
    productEl.appendChild(prodcutPriceDiv);
    productEl.appendChild(productDelButtonDiv);

    // Add to ShoppingCart
    let shoppingCartEl = document.getElementById('products');
    shoppingCartEl.appendChild(productEl);

    addToCheckout(productEl.id);
}

// Add-to-Checkout Button Function
function addToCheckout(productId) {
    let wantedProduct = document.getElementById(productId);
    let productAddToCheckoutButton = wantedProduct.querySelector('.add-product');

    let productTitle = wantedProduct.querySelector('.product-title').textContent;
    let productPrice = Number(wantedProduct.querySelector('.product-line-price').textContent);

    productAddToCheckoutButton.addEventListener('click', () => {
        let checkoutTableBody = document.querySelector(".tableDiv table tbody");

        let productsAdded = checkoutTableBody.querySelectorAll('tr');

        for (let product of productsAdded) {
            let currProductName = product.querySelector('td.productNameCol');
            if (currProductName.textContent === productTitle) {
                let productIncreaseButton = product.querySelector('td button.increaseButton');
                productIncreaseButton.click();
                return;
            }
        }

        let newRow = document.createElement('tr');
        let totalPriceEl = document.querySelector('.totalPrice span');
        totalPriceEl.textContent = (Number(totalPriceEl.textContent) + productPrice).toFixed(2);

        // Create the columns
        // Name Column
        let productNameCol = document.createElement('td');
        productNameCol.classList.add('productNameCol');
        productNameCol.textContent = productTitle;

        // Price Column
        let productPriceCol = document.createElement('td');
        productPriceCol.classList.add('productPriceCol');
        productPriceCol.textContent = productPrice;

        // Count Column
        let productCountCol = document.createElement('td');
        productCountCol.classList.add('countCol');

        let productCountButtonDecrease = document.createElement('button');
        productCountButtonDecrease.textContent = "-";

        let productCountSpanEl = document.createElement('span');
        productCountSpanEl.textContent = "1";

        let productCountButtonIncrease = document.createElement('button');
        productCountButtonIncrease.classList.add('increaseButton');
        productCountButtonIncrease.textContent = "+";

        productCountButtonDecrease.addEventListener('click', () => {
            let currentValue = Number(productCountSpanEl.textContent);

            if (currentValue > 1) {
                let startPrice = Number(productPriceCol.textContent) / currentValue;
                currentValue--;
                productCountSpanEl.textContent = currentValue;

                let newPrice = currentValue * startPrice;
                productPriceCol.textContent = (newPrice).toFixed(2);
                totalPriceEl.textContent = (Number(totalPriceEl.textContent) - startPrice).toFixed(2);
            }
        });

        productCountButtonIncrease.addEventListener('click', () => {
            let currentValue = Number(productCountSpanEl.textContent);

            if (currentValue < 100) {
                let startPrice = Number(productPriceCol.textContent) / currentValue;
                currentValue++;
                productCountSpanEl.textContent = currentValue;

                let newPrice = currentValue * startPrice;
                productPriceCol.textContent = (newPrice).toFixed(2);
                totalPriceEl.textContent = (Number(totalPriceEl.textContent) + startPrice).toFixed(2);
            }
        });

        productCountCol.appendChild(productCountButtonDecrease);
        productCountCol.appendChild(productCountSpanEl);
        productCountCol.appendChild(productCountButtonIncrease);

        // Delete Button Col
        let productDelButtonDiv = document.createElement('td');
        productDelButtonDiv.classList.add('delButton');
        let productDelButton = document.createElement('button');
        productDelButton.textContent = "X";
        productDelButton.addEventListener('click', () => {
            totalPriceEl.textContent = (Number(totalPriceEl.textContent) - Number(productPriceCol.textContent)).toFixed(2);
            newRow.remove();
        });
        productDelButtonDiv.appendChild(productDelButton);

        // Add them to the row
        newRow.appendChild(productNameCol);
        newRow.appendChild(productPriceCol);
        newRow.appendChild(productCountCol);
        newRow.appendChild(productDelButtonDiv);

        // Add row to table
        checkoutTableBody.appendChild(newRow);
    });
}

// Checkout Button Function
function checkout() {
    let checkoutTableBody = document.querySelectorAll(".tableDiv table tbody tr");
    let products = {};
    let totalPrice = document.querySelector('.totalPrice span').textContent;

    if (Number(totalPrice) === 0.00) {
        return;
    }

    for (let row of checkoutTableBody) {
        let productNameEl = row.querySelector('td.productNameCol');
        let productCountEl = row.querySelector('td.countCol span');

        let productName = productNameEl.textContent;
        let productCount = Number(productCountEl.textContent);

        products[productName] = productCount;
    }
    console.log(Object.entries(products));
    let resultString = Object.entries(products).map(x => `${x[0]} x${x[1]}`).join(', ');

    let result = `You have successfully purchased ${resultString} for $${totalPrice}.`;

    let shoppingCartEl = document.querySelector('.checkout');
    let resultEl = document.createElement('h3');
    resultEl.textContent = result;

    shoppingCartEl.appendChild(resultEl);
}
