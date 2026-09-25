let cart = [];

function toggleCartDrawer() {
    document.getElementById('cart-drawer').classList.toggle('open');
    document.getElementById('cart-overlay').classList.toggle('open');
}

function addToCart(id, name, price) {
    const existingItem = cart.find(item => item.id === id);
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({ id, name, price, quantity: 1 });
    }
    updateCartUI();
    // Automatically open drawer on item addition for quick review
    if (!document.getElementById('cart-drawer').classList.contains('open')) {
        toggleCartDrawer();
    }
}

function updateCartUI() {
    const cartItemsList = document.getElementById('cart-items');
    const cartTotalSpan = document.getElementById('cart-total');
    const cartBadge = document.getElementById('cart-badge');
    
    let totalItemsCount = cart.reduce((sum, item) => sum + item.quantity, 0);
    cartBadge.textContent = totalItemsCount;

    if (cart.length === 0) {
        cartItemsList.innerHTML = '<li class="list-group-item text-muted text-center border-0">Your cart is empty</li>';
        cartTotalSpan.textContent = '0.00';
        return;
    }

    cartItemsList.innerHTML = '';
    let total = 0;
    
    cart.forEach(item => {
        total += item.price * item.quantity;
        const li = document.createElement('li');
        li.className = 'list-group-item d-flex justify-content-between align-items-center px-0 border-bottom';
        li.innerHTML = `
            <div>
                <h6 class="my-0 fw-semibold">${item.name}</h6>
                <small class="text-muted">Qty: ${item.quantity}</small>
            </div>
            <span class="text-danger fw-bold">₹${(item.price * item.quantity).toFixed(2)}</span>
        `;
        cartItemsList.appendChild(li);
    });
    
    cartTotalSpan.textContent = total.toFixed(2);
}

function submitOrder() {
    if (cart.length === 0) {
        alert('Your order is empty!');
        return;
    }

    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);

    fetch('/api/order', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ items: cart, total: total })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        cart = [];
        updateCartUI();
        toggleCartDrawer();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to place order.');
    });
}