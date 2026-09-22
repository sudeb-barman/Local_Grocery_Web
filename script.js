// ==========================================
// LOAD PRODUCTS - DASHBOARD
// ==========================================
function loadProducts() {

    fetch("/api/products")           // 1. Get the raw network response

        .then(response => response.json())      // 2. Use the fully parsed data

        .then(products => {                          // You can now read properties directly

            const table =
                document.getElementById("productTable");

            table.innerHTML = "";

            document.getElementById("totalProducts").innerText =
                products.length;


            products.forEach(product => {

                table.innerHTML += `

                    <tr>

                        <td>${product.product_id}</td>

                        <td>${product.name}</td>

                        <td>${product.uom_name}</td>

                        <td>₹${product.price_per_unit}</td>

                        <td>
                            <button
                                class="delete-btn"
                                onclick="deleteProduct(${product.product_id})">

                                Delete

                            </button>
                        </td>

                    </tr>

                `;

            });

        })

        .catch(error => {

            console.log("Error:", error);

        });
}


// Load products when Dashboard opens
document.addEventListener("DOMContentLoaded", loadProducts);


// ==========================================
// DELETE PRODUCT
// ==========================================

function deleteProduct(productId) {

    const confirmDelete = confirm(
        "THINK AGAIN MAMU "
    );


    if (!confirmDelete) {
        return;
    }


    fetch(
        "/api/products/" + productId,
        {
            method: "DELETE"
        }
    )

        .then(response => {

            if (!response.ok) {
                throw new Error("Delete failed");
            }

            return response.json();

        })

        .then(result => {

            alert(
                result.message || "Product deleted successfully"
            );
            loadProducts(); //RELOAD THE PAGE

        })

        .catch(error => {

            console.error(
                "Error deleting product:",
                error
            );

            alert(
                "Unable to delete product"
            );

        });

}



// ==========================================
// ADD PRODUCT - NEW ORDER PAGE
// ==========================================

function addProduct() {

    const name = document.getElementById("product_name").value.trim(); //value=user typed value,trim = cutting the extra space beginning of value or last
    const uom = document.getElementById("unit").value;
    const price = document.getElementById("price").value;

    if (name === "") {
        alert("Please enter product name");
        return;
    }

    if (uom === "") {
        alert("Please select a unit");
        return;
    }

    if (price === "") {
        alert("Please enter price");
        return;
    }

    fetch("/api/products", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            product_name: name,
            unit: Number(uom),
            price: Number(price)
        })
    })

    .then(response => {
        if (!response.ok) {
            throw new Error("Add product failed");
        }

        return response.json();
    })

.then(result => {
    console.log("Server response:", result);

    alert(result.message || "Product added successfully");

    document.getElementById("product_name").value = "";
    document.getElementById("unit").value = "";
    document.getElementById("price").value = "";
})

    .catch(error => {
        console.error(error);
        alert("Unable to add product");
    });
}



// ==========================================
// RUN WHEN DASHBOARD OPENS
// ==========================================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        // Only runs on dashboard
        // because dashboard has productTable

        if (
            document.getElementById(
                "productTable"
            )
        ) {

            loadProducts();

        }

    }
);