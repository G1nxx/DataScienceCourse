def filter_by_category(products: list[dict], category: str) -> list[dict]:
    new_products = []
    for prod in products:
        if 'category' in prod:
            if prod['category'] == category:
                new_products.append(prod)
    return new_products

def get_expensive_products(products: list[dict], min_price: int) -> list[dict]:
    new_products = []
    for prod in products:
        if 'price' in prod:
            if prod['price'] > min_price:
                new_products.append(prod)
    return new_products

def calculate_total_price(products: list[dict]) -> int:
    sum = 0
    for prod in products:
        if 'price' in prod:
            sum += prod['price'];
    return sum

def main():
    products = [
        {"name": "Ноутбук", "price": 50000, "category": "Электроника"},
        {"name": "Книга", "price": 500, "category": "Книги"},
        {"name": "Кофе", "price": 300, "category": "Продукты"},
        {"name": "Телефон", "price": 30000, "category": "Электроника"},
        {"name": "Ручка", "price": 50, "category": "Канцтовары"}
    ]
    print(products)
    print(filter_by_category(products, 'Электроника'))
    print(get_expensive_products(products, 400))
    print(calculate_total_price(products))

if __name__ == '__main__':
    main()