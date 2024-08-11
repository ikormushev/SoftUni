// Simulating a Database
let products = {};
let checkoutProducts = {};
let totalCheckoutPrice = 0;

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

// Create a product
function createProduct() {
    let productTitle = document.getElementById('productTitle');
    let productPrice = document.getElementById('productPrice');
    let productDescriptionValue = document.getElementById('productDescription').value;
    let productsCount = document.querySelectorAll('.product').length;

    if (!validateInput(productTitle, 'name') || !validateInput(productPrice, 'price') ) return;

    if (Object.keys(products).includes(productTitle.value)) return;


    products[productTitle.value] = {};
    products[productTitle.value]["price"] = Number(productPrice.value);

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
    let totalPriceEl = document.querySelector('.totalPrice span');

    let productTitle = wantedProduct.querySelector('.product-title').textContent;
    let productPrice = Number(wantedProduct.querySelector('.product-line-price').textContent);

    productAddToCheckoutButton.addEventListener('click', () => {
        if (checkoutProducts.hasOwnProperty(productTitle)) {
            let increaseButton = document.querySelector('.increaseButton');
            increaseButton.click();
            return;
        }

        checkoutProducts[productTitle] = {};
        checkoutProducts[productTitle]["count"] = 1;
        checkoutProducts[productTitle]["price"] = productPrice;
        totalCheckoutPrice += productPrice;
        totalPriceEl.textContent = totalCheckoutPrice.toFixed(2);

        let checkoutTableBody = document.querySelector(".tableDiv table tbody");
        let newRow = document.createElement('tr');

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
        productCountSpanEl.textContent = checkoutProducts[productTitle]["count"];

        let productCountButtonIncrease = document.createElement('button');
        productCountButtonIncrease.classList.add('increaseButton');
        productCountButtonIncrease.textContent = "+";


        productCountCol.appendChild(productCountButtonDecrease);
        productCountCol.appendChild(productCountSpanEl);
        productCountCol.appendChild(productCountButtonIncrease);

        productCountButtonDecrease.addEventListener('click', () => {
            let currCount = checkoutProducts[productTitle]["count"];
        
            let currCountEl = document.querySelector('.countCol span');
            let currPriceEl = document.querySelector('.productPriceCol');

            if (currCount > 1) {
                checkoutProducts[productTitle]["count"]--;
                checkoutProducts[productTitle]["price"] -= productPrice;
                totalCheckoutPrice -= productPrice;

                currCountEl.textContent = checkoutProducts[productTitle]["count"];
                currPriceEl.textContent = checkoutProducts[productTitle]["price"].toFixed(2);

                totalPriceEl.textContent = totalCheckoutPrice.toFixed(2);
            }
        });

        productCountButtonIncrease.addEventListener('click', () => {
            let currCount = checkoutProducts[productTitle]["count"];
        
            let currCountEl = document.querySelector('.countCol span');
            let currPriceEl = document.querySelector('.productPriceCol');

            if (currCount < 100) {
                checkoutProducts[productTitle]["count"]++;
                checkoutProducts[productTitle]["price"] += productPrice;
                totalCheckoutPrice += productPrice;

                currCountEl.textContent = checkoutProducts[productTitle]["count"];
                currPriceEl.textContent = checkoutProducts[productTitle]["price"].toFixed(2);

                totalPriceEl.textContent = totalCheckoutPrice.toFixed(2);
            }
        });

        // Delete Button Col
        let productDelButtonDiv = document.createElement('td');
        productDelButtonDiv.classList.add('delButton');
        let productDelButton = document.createElement('button');
        productDelButton.textContent = "X";
        productDelButton.addEventListener('click', () => {
            totalCheckoutPrice -= checkoutProducts[productTitle]["price"];
            totalPriceEl.textContent = totalCheckoutPrice.toFixed(2);
            delete checkoutProducts[productTitle];
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
    if (totalCheckoutPrice === 0.00) {
        return;
    }

    let resultString = Object.entries(checkoutProducts).map(x => `${x[0]} x${x[1]['count']}`).join(', ');

    let result = `You have successfully purchased ${resultString} for $${totalCheckoutPrice.toFixed(2)}.`;

    // Empty old values
    totalCheckoutPrice = 0;
    let checkoutTableBody = document.querySelectorAll(".tableDiv table tbody tr");
    checkoutTableBody.forEach(x => x.remove());
    checkoutProducts = {};
    let totalPriceEl = document.querySelector('.totalPrice span');
    totalPriceEl.textContent = 0;

    // Add the checkout
    let shoppingCartEl = document.querySelector('.checkout');
    let resultEl = document.createElement('h3');
    resultEl.textContent = result;

    shoppingCartEl.appendChild(resultEl);
}
