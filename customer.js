let products = [];

// ===============================
// LOAD PRODUCTS FROM DATABASE
// ===============================

function loadProducts() {

    fetch("/api/products")
        .then(response => {

            if (!response.ok) {
                throw new Error("API error: " + response.status);
            }

            return response.json();
        })

        .then(data => {

            console.log("Products from database:", data);

            products = data;

            loadDropdowns();

        })

        .catch(error => {

            console.error("Product loading error:", error);

            alert("Products cannot be loaded");

        });
}


// ===============================
// PUT PRODUCTS IN DROPDOWN
// ===============================

function loadDropdowns() {

    const dropdowns =
        document.querySelectorAll(".product");

    dropdowns.forEach(dropdown => {

        dropdown.innerHTML =
            '<option value="">Select Product</option>';

        products.forEach(product => {

            const option =
                document.createElement("option");

            option.value = product.product_id;

            option.textContent = product.name;

            dropdown.appendChild(option);

        });

        dropdown.addEventListener(
            "change",
            productSelected
        );

    });
}


// ===============================
// WHEN PRODUCT IS SELECTED
// ===============================

function productSelected(event) {

    const dropdown = event.target;

    const row =
        dropdown.closest(".product-row");

    const productId =
        Number(dropdown.value);

    const product =
        products.find(
            p => Number(p.product_id) === productId
        );

    if (product) {

        row.querySelector(".price").value =
            product.price_per_unit;

    }
    else {

        row.querySelector(".price").value = "";

    }

    calculateTotal();
}


// ===============================
// CALCULATE TOTAL
// ===============================

function calculateTotal(row) {

    let price = Number(
        row.querySelector(".price").value
    );

    let quantity = Number(
        row.querySelector(".quantity").value
    );

    let total = price * quantity;

    row.querySelector(".row-total").innerText = total;

    calculateGrandTotal();
}


function calculateGrandTotal() {

    let total = 0;

    document.querySelectorAll(".row-total").forEach(function(item) {

        total = total + Number(item.innerText);

    });

    document.getElementById("grandTotal").innerText = total;
}


// When quantity changes
document.addEventListener("input", function(event) {

    if (event.target.classList.contains("quantity")) {

        let row = event.target.closest(".product-row");

        calculateTotal(row);
    }

});


// ===============================
// ADD MORE PRODUCT
// ===============================

function addProductRow() {

    const container =
        document.getElementById("productRows");

    const row =
        document.createElement("div");

    row.className = "product-row";

    row.innerHTML = `

        <select class="product">
            <option value="">Select Product</option>
        </select>

        <input
            type="number"
            class="price"
            placeholder="Price"
            readonly>

        <input
            type="number"
            class="quantity"
            value="1"
            min="1">

        <div class="total">
            ₹<span class="row-total">0.00</span>
        </div>

        <button
            class="remove-btn"
            onclick="removeProduct(this)">
            Delete
        </button>
    `;

    container.appendChild(row);

    // Fill the new dropdown
    loadDropdowns();

    calculateTotal();
}


// ===============================
// REMOVE PRODUCT
// ===============================

function removeProduct(button) {

    const rows =
        document.querySelectorAll(".product-row");

    if (rows.length === 1) {

        alert("At least one product is required");

        return;
    }

    button.closest(".product-row").remove();

    calculateTotal();
}
// PLACE ORDER

function saveOrder() {

    let customerName = document.getElementById("customerName").value;  //the value of which we write in page ,,,, also customerName is Id (html)

    let rows = document.querySelectorAll(".product-row");     // Selects the all products Row that's use to get total value  

    let orderDetails = [];  // its a dictionary where store the all list of the product in a row 

    rows.forEach(function(row) {                  //Go through each product row one by one.  like this( Row 1 → Rice, Row 2 → Sugar, Row 3 → Oil )



        let productId = row.querySelector(".product").value;    // id's in html
        let quantity = row.querySelector(".quantity").value;  // id's in html
        let totalPrice = row.querySelector(".row-total").innerText; // id's in html

        if (productId !== "") {

            orderDetails.push({
                product_id: productId,
                quantity: quantity,
                total_price: totalPrice.replace("₹", "")
            });

        }
    });

    let grandTotal = document.getElementById("grandTotal").innerText;      // It shows the total price ex. 700 

    let order = {                            // Its fatching all the data like in order.py . line no. (42 - 53).
        customer_name: customerName,
        grand_total: grandTotal,
        order_details: orderDetails
    };

    fetch("/api/orders", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"                    // Tell Flask that the data is JSON
        },

        body: JSON.stringify(order)                  //Convert JavaScript object to JSON  like   {
                                                                    //    customer_name: "Sourabh",
                                                                    //    grand_total: "700",
                                                                    //    order_details: [...]
                                                                    //}

    })
    .then(response => response.json())
    .then(data => {

        alert("Order saved successfully! Order ID: " + data.order_id);

    })
    .catch(error => {

        console.error(error);
        alert("Order could not be saved");

    });
}



// ===============================
// PAGE LOAD
// ===============================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        console.log("Customer JS loaded");

        loadProducts();

    }
);