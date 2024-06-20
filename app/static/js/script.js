document.addEventListener('DOMContentLoaded', function () {
    // Начало обработчика события DOMContentLoaded

    // Выбираем все элементы с классом 'add-to-cart' и для каждого добавляем обработчик события клика
    document.querySelectorAll('.add-to-cart').forEach(function (button) {
        button.onclick = function () {
            // При клике на кнопку получаем значение атрибута data-product-id
            const productId = this.dataset.productId;

            // Выполняем запрос fetch для добавления продукта в корзину
            fetch(`/add_to_cart/${productId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // Добавляем CSRF токен для защиты от CSRF атак
                    'X-CSRFToken': '{{ csrf_token() }}'
                }
            }).then(response => response.json()).then(data => {
                // Обрабатываем ответ от сервера
                if (data.success) {
                    alert('Product added to cart'); // Выводим сообщение об успешном добавлении продукта
                } else {
                    alert('Error adding product to cart'); // Выводим сообщение об ошибке при добавлении продукта
                }
            });
        };
    });
});
