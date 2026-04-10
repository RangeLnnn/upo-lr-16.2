import os
import django

# ============================================================
# НАСТРОЙКА DJANGO
# ============================================================
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  # ← поменяй myproject
django.setup()

# ============================================================
# ИМПОРТ ВСЕХ МОДЕЛЕЙ
# ============================================================
from shop.models import ProductCategory, Manufacter, Product, Cart, CartsElement
from django.contrib.auth.models import User

# ============================================================
# ОЧИСТКА СТАРЫХ ДАННЫХ (в правильном порядке из-за связей)
# ============================================================
print("🧹 Очищаю старые данные...")

CartsElement.objects.all().delete()   # сначала удаляем зависимые
Cart.objects.all().delete()           # потом корзины
Product.objects.all().delete()        # потом товары
ProductCategory.objects.all().delete()# потом категории
Manufacter.objects.all().delete()     # потом производителей

print("   ✅ Старые данные удалены\n")

# ============================================================
# 1. СОЗДАНИЕ КАТЕГОРИЙ ТОВАРОВ (ProductCategory)
# ============================================================
print("📁 Создаю категории товаров...")

cat_ballons_montana = ProductCategory.objects.create(
    name="Баллончики Montana",
    description="Профессиональная краска Montana для граффити, 400 мл"
)

cat_ballons_molotow = ProductCategory.objects.create(
    name="Баллончики Molotow",
    description="Премиум краска Molotow, высокая пигментация"
)

cat_trafarety = ProductCategory.objects.create(
    name="Трафареты",
    description="Многоразовые трафареты для граффити и стрит-арта"
)

cat_maski = ProductCategory.objects.create(
    name="Защитные маски",
    description="Респираторы и маски для защиты при работе с краской"
)

cat_nabory = ProductCategory.objects.create(
    name="Наборы Старт",
    description="Готовые наборы для начинающих граффити-художников"
)

print(f"   ✅ Создано категорий: 5\n")

# ============================================================
# 2. СОЗДАНИЕ ПРОИЗВОДИТЕЛЕЙ (Manufacter)
# ============================================================
print("🏭 Создаю производителей...")

man_montana = Manufacter.objects.create(
    name="Montana Cans",
    country="Германия",
    description="Немецкий производитель профессиональных аэрозольных красок"
)

man_molotow = Manufacter.objects.create(
    name="Molotow",
    country="Германия",
    description="Премиум бренд красок и маркеров для граффити"
)

man_traf = Manufacter.objects.create(
    name="StencilPro",
    country="Россия",
    description="Производитель многоразовых трафаретов"
)

man_3m = Manufacter.objects.create(
    name="3M",
    country="США",
    description="Мировой лидер в производстве средств защиты"
)

man_jetasafety = Manufacter.objects.create(
    name="Jeta Safety",
    country="Китай",
    description="Производитель доступных средств защиты"
)

man_start = Manufacter.objects.create(
    name="GraffitiStart",
    country="Россия",
    description="Отечественный производитель наборов для начинающих"
)

print(f"   ✅ Создано производителей: 6\n")

# ============================================================
# 3. СОЗДАНИЕ ТОВАРОВ (Product)
# ============================================================
print("🛒 Создаю товары...")

# Для товаров нужно фото. Если у тебя нет реальных файлов,
# можно оставить поле пустым или указать заглушку.
# Я укажу пустую строку, но в админке это будет выглядеть как "нет фото".

# -------------------- Montana --------------------
Product.objects.create(
    name="Montana Black 400мл",
    description="Профессиональная краска, 400 мл, матовая поверхность",
    products_photo="",  # ← потом добавишь через админку
    price=350.00,
    quantity=25,
    category=cat_ballons_montana,
    manufacter=man_montana
)

Product.objects.create(
    name="Montana Gold 400мл",
    description="Акриловая краска, 400 мл, глянцевая поверхность",
    products_photo="",
    price=450.00,
    quantity=18,
    category=cat_ballons_montana,
    manufacter=man_montana
)

Product.objects.create(
    name="Montana White 400мл",
    description="Белая краска повышенной укрывистости",
    products_photo="",
    price=500.00,
    quantity=12,
    category=cat_ballons_montana,
    manufacter=man_montana
)

# -------------------- Molotow --------------------
Product.objects.create(
    name="Molotow Premium 400мл",
    description="Премиум качество, высокая пигментация",
    products_photo="",
    price=400.00,
    quantity=20,
    category=cat_ballons_molotow,
    manufacter=man_molotow
)

Product.objects.create(
    name="Molotow Burner Chrome",
    description="Хромированная краска, зеркальный эффект",
    products_photo="",
    price=600.00,
    quantity=8,
    category=cat_ballons_molotow,
    manufacter=man_molotow
)

Product.objects.create(
    name="Molotow CoversAll",
    description="Супер-укрывистая краска для любых поверхностей",
    products_photo="",
    price=550.00,
    quantity=0,  # нет в наличии
    category=cat_ballons_molotow,
    manufacter=man_molotow
)

# -------------------- Трафареты --------------------
Product.objects.create(
    name='Трафарет "Буквы"',
    description="Набор букв русского алфавита, 10 см",
    products_photo="",
    price=100.00,
    quantity=30,
    category=cat_trafarety,
    manufacter=man_traf
)

Product.objects.create(
    name='Трафарет "Цифры"',
    description="Цифры от 0 до 9, 15 см",
    products_photo="",
    price=120.00,
    quantity=25,
    category=cat_trafarety,
    manufacter=man_traf
)

Product.objects.create(
    name='Трафарет "Орнамент"',
    description="Сложные геометрические узоры, многоразовый",
    products_photo="",
    price=250.00,
    quantity=15,
    category=cat_trafarety,
    manufacter=man_traf
)

Product.objects.create(
    name='Трафарет "Граффити-шрифт"',
    description="Стилизованные буквы для граффити",
    products_photo="",
    price=300.00,
    quantity=0,  # нет в наличии
    category=cat_trafarety,
    manufacter=man_traf
)

# -------------------- Защитные маски --------------------
Product.objects.create(
    name="Респиратор 3M 6200",
    description="Полумаска с фильтрами от паров краски",
    products_photo="",
    price=800.00,
    quantity=10,
    category=cat_maski,
    manufacter=man_3m
)

Product.objects.create(
    name="Маска одноразовая FFP3",
    description="Защита от аэрозолей и пыли, 10 шт в упаковке",
    products_photo="",
    price=200.00,
    quantity=50,
    category=cat_maski,
    manufacter=man_3m
)

Product.objects.create(
    name="Респиратор Jeta Safety",
    description="Многоразовый с угольным фильтром",
    products_photo="",
    price=500.00,
    quantity=15,
    category=cat_maski,
    manufacter=man_jetasafety
)

# -------------------- Наборы Старт --------------------
Product.objects.create(
    name='Набор "Новичок"',
    description="3 баллончика Montana + трафарет + перчатки",
    products_photo="",
    price=1200.00,
    quantity=8,
    category=cat_nabory,
    manufacter=man_start
)

Product.objects.create(
    name='Набор "Продвинутый"',
    description="6 баллончиков + 2 трафарета + маска + перчатки",
    products_photo="",
    price=2500.00,
    quantity=5,
    category=cat_nabory,
    manufacter=man_start
)

Product.objects.create(
    name='Набор "Профи"',
    description="10 баллончиков + 5 трафаретов + респиратор + кэпы",
    products_photo="",
    price=4500.00,
    quantity=0,  # нет в наличии
    category=cat_nabory,
    manufacter=man_start
)

print(f"   ✅ Создано товаров: 16\n")

# ============================================================
# 4. СОЗДАНИЕ КОРЗИН (Cart) - опционально
# ============================================================
print("🛒 Создаю корзины для пользователей...")

# Получаем всех пользователей
users = User.objects.all()

if users.exists():
    for user in users:
        # Создаём корзину только если её ещё нет
        cart, created = Cart.objects.get_or_create(user=user)
        if created:
            print(f"   ✅ Корзина для {user.username} создана")
        else:
            print(f"   ℹ️ Корзина для {user.username} уже существует")
else:
    print("   ⚠️ Нет пользователей в системе. Создайте суперпользователя:")
    print("      python manage.py createsuperuser")

print(f"\n   📊 Всего корзин: {Cart.objects.count()}\n")

# ============================================================
# 5. ДОБАВЛЕНИЕ ТОВАРОВ В КОРЗИНУ (CartsElement) - опционально
# ============================================================
print("➕ Добавляю тестовые товары в корзины...")

# Берём первую корзину для примера
first_cart = Cart.objects.first()

if first_cart:
    # Берём несколько товаров которые есть в наличии
    products_in_stock = Product.objects.filter(quantity__gt=0)[:3]
    
    for product in products_in_stock:
        # Проверяем нет ли уже такого товара в корзине
        element, created = CartsElement.objects.get_or_create(
            cart=first_cart,
            product=product,
            defaults={'quantity': 1}
        )
        if created:
            print(f"   ✅ Добавлен: {product.name}")
        else:
            print(f"   ℹ️ {product.name} уже в корзине")
    
    print(f"\n   📊 Товаров в первой корзине: {first_cart.cartselement_set.count()}")
else:
    print("   ⚠️ Нет корзин для добавления товаров")

# ============================================================
# ПРОВЕРКА РЕЗУЛЬТАТА
# ============================================================
print("\n" + "=" * 50)
print("📊 ИТОГОВАЯ СТАТИСТИКА")
print("=" * 50)

print(f"📁 Категорий товаров: {ProductCategory.objects.count()}")
print(f"🏭 Производителей: {Manufacter.objects.count()}")
print(f"🛒 Товаров: {Product.objects.count()}")
print(f"   ✅ В наличии: {Product.objects.filter(quantity__gt=0).count()}")
print(f"   ❌ Нет в наличии: {Product.objects.filter(quantity=0).count()}")
print(f"👤 Пользователей: {User.objects.count()}")
print(f"🛍️ Корзин: {Cart.objects.count()}")
print(f"📦 Элементов в корзинах: {CartsElement.objects.count()}")

print("\n📋 Товары по категориям:")
for cat in ProductCategory.objects.all():
    count = Product.objects.filter(category=cat).count()
    print(f"   - {cat.name}: {count} шт.")

print("\n📋 Товары по производителям:")
for man in Manufacter.objects.all():
    count = Product.objects.filter(manufacter=man).count()
    print(f"   - {man.name} ({man.country}): {count} шт.")

print("\n" + "=" * 50)
print("✅ База данных успешно заполнена!")
print("💡 Зайди в админку: http://127.0.0.1:8000/admin/")
print("=" * 50)