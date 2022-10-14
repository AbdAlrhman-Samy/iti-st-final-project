let CART_ITEMS = [];

const cartBtn = document.getElementById("cart");
const cartItemsCount = document.getElementById("cart-items-count");
const addToCartBtn = document.getElementById("add-btn");
const cartBackdrop = document.getElementById("cart-backdrop");
const cartDrawer = document.getElementById("cart-drawer");
const cartItems = document.getElementById("cart-items");
const cartTotal = document.getElementById("total");


window.addEventListener("load", () => {
	if (!localStorage.getItem("cart")) {
		localStorage.setItem("cart", JSON.stringify(CART_ITEMS));
	} else {
		CART_ITEMS = JSON.parse(localStorage.getItem("cart"));
		cartItemsCount.innerText = CART_ITEMS.length;
	}

	
});

if (addToCartBtn) {
	addToCartBtn.addEventListener("click", (e) => {
		const productDetails = {
			name: e.target.getAttribute("data-product-name"),
			price: e.target.getAttribute("data-product-price"),
			amount: 1,
		};

		if (CART_ITEMS.find((item) => item.name === productDetails.name)) {
			CART_ITEMS[
				CART_ITEMS.findIndex((i) => i.name === productDetails.name)
			].amount += 1;
		} else {
			CART_ITEMS.push(productDetails);
			cartItemsCount.innerText = Number(cartItemsCount.innerText) + 1;
		}

		localStorage.setItem("cart", JSON.stringify(CART_ITEMS));
	});
}

cartBtn.addEventListener("click", () => {
	console.log(CART_ITEMS);

	let total = 0

	CART_ITEMS.forEach(item => {
		total = total + item.price*item.amount
		const prod = document.createElement("div")
		prod.classList.add("item-card")
		prod.innerHTML = `
			<h2> ${item.name} </h2>
			<h4> ${item.amount} Pieces - ${item.price * item.amount}$ </h4>
		`
		cartItems.appendChild(prod)
	})

	cartBackdrop.style.display = "block";
	cartDrawer.style.display = "flex";

	cartTotal.innerText = `TOTAL: ${total}$`

});

cartBackdrop.addEventListener("click", () => {
	cartBackdrop.style.display = "none";
	cartDrawer.style.display = "none";
	cartItems.innerHTML = ""
});

