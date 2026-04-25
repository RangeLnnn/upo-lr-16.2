function loadProducts() {
    const container = document.getElementById('product-list');
    
    container.innerHTML = `
        <div class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Загрузка...</span>
            </div>
            <p>Загружаем товары...</p>
        </div>
    `;
    
    fetch('/shop/api/product/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка загрузки');
            }
            return response.json();
        })
        .then(products => {
            container.innerHTML = '';
            
            if (products.length === 0) {
                container.innerHTML = '<p class="text-center">Товары не найдены</p>';
                return;
            }
            
            products.forEach(product => {
                const card = `
                    <div class="col-sm-6 col-md-4 col-lg-4 mb-4">
                        <div class="card h-100">
                            <div class="card-body">
                                <h5 class="card-title">${product.name}</h5>
                                <p class="fw-bold">${product.price} BYN</p>
                            </div>
                            <div class="card-footer bg-white border-0">
                                <button class="btn btn-outline-primary w-100" onclick="showDetail(${product.id})">Подробнее</button>
                                <button class="btn btn-success w-100 mt-2" onclick="addToCart(${product.id})">🛒 В корзину</button>
                            </div>
                        </div>
                    </div>
                `;
                container.innerHTML += card;
            });
        })
        .catch(error => {
            container.innerHTML = '<div class="alert alert-danger">Не удалось загрузить товары. Попробуйте позже.</div>';
        });
}

function addToCart(productId) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    fetch('/shop/api/cart/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
            product_id: productId,
            quantity: 1
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Ошибка');
        }
        return response.json();
    })
    .then(data => {
        showAlert('Товар добавлен в корзину!', 'success');
    })
    .catch(error => {
        showAlert('Не удалось добавить товар', 'danger');
    });
}

function showAlert(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 end-0 m-3`;
    alertDiv.role = 'alert';
    alertDiv.innerHTML = `${message}<button type="button" class="btn-close" data-bs-dismiss="alert"></button>`;
    document.body.appendChild(alertDiv);
    
    setTimeout(() => {
        alertDiv.remove();
    }, 3000);
}

document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('product-list')) {
        loadProducts();
    }
});