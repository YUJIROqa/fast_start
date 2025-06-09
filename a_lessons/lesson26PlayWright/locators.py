# 🎯 **ВСЕ ТИПЫ ЛОКАТОРОВ**

## **1️⃣ ПО ID**

### **🔍 Поиск в Elements:**
html
<button id="submit-btn">Отправить</button>

// В поиске Elements вводим:
#submit-btn

### **🎭 В Playwright:**
javascript
// Способ 1 - через CSS селектор
await page.locator('#submit-btn').click();

// Способ 2 - через getByRole с именем
await page.get_by_role('button', { name: 'Отправить' }).click();

// Способ 3 - прямой поиск по ID
await page.locator('[id="submit-btn"]').click();

## **2️⃣ ПО CLASS**

### **🔍 Поиск в Elements:**
html
<!-- HTML -->
<div class="error-message active">Ошибка!</div>

javascript
// В поиске Elements:
.error-message          // Найдет все с классом error-message
.error-message.active    // Найдет только с обоими классами
.active                  // Найдет все с классом active

### **🎭 В Playwright:**
javascript
// По одному классу
await page.locator('.error-message').textContent();

// По нескольким классам
await page.locator('.error-message.active').textContent();

// Через атрибут class
await page.locator('[class*="error-message"]').textContent();

## **3️⃣ ПО ТЕГУ**

### **🔍 Поиск в Elements:**
html
<!-- HTML -->
<input type="email" placeholder="Email">
<button>Войти</button>
<h1>Заголовок</h1>
```

javascript
// В поиске Elements:
input           // Все input элементы
button          // Все кнопки  
h1              // Все заголовки h1

### **🎭 В Playwright:**
javascript
// Простой поиск по тегу
await page.locator('input').fill('test@mail.ru');
await page.locator('button').click();
await page.locator('h1').textContent();

// Лучше использовать более специфичные методы
await page.getByRole('textbox').fill('test@mail.ru');
await page.getByRole('button').click();
await page.getByRole('heading', { level: 1 }).textContent();

## **4️⃣ ПО АТРИБУТАМ**

### **🔍 Поиск в Elements:**
html
<!-- HTML -->
<input type="password" name="password" placeholder="Пароль">
<button data-testid="login-btn" disabled>Войти</button>
<a href="/profile" title="Профиль пользователя">Профиль</a>

javascript
// В поиске Elements:
[type="password"]                    // По атрибуту type
[name="password"]                    // По атрибуту name  
[data-testid="login-btn"]           // По data-testid
[disabled]                          // Элементы с атрибутом disabled
[href="/profile"]                   // По точному значению href
[title*="Профиль"]                  // Содержит "Профиль" в title
[placeholder^="Пар"]                // Начинается с "Пар"
[href$=".pdf"]                      // Заканчивается на ".pdf"


### **🎭 В Playwright:**
javascript
// По data-testid (рекомендуемый способ)
await page.getByTestId('login-btn').click();

// По различным атрибутам
await page.locator('[type="password"]').fill('123456');
await page.locator('[name="password"]').fill('123456');
await page.locator('[placeholder="Пароль"]').fill('123456');

// По частичному совпадению
await page.locator('[title*="Профиль"]').click();
await page.locator('[href^="/user"]').click();
await page.locator('[class$="-button"]').click();

## **5️⃣ ПО ТЕКСТУ**

### **🔍 Поиск в Elements:**
html
<!-- HTML -->
<button>Сохранить изменения</button>
<span>Добро пожаловать, Иван!</span>
<a>Подробнее</a>

javascript
// В Elements нельзя искать по тексту напрямую
// Нужно визуально найти элемент и посмотреть его селекторы

### **🎭 В Playwright:**
javascript
// По точному тексту
await page.getByText('Сохранить изменения').click();
await page.getByText('Добро пожаловать, Иван!').textContent();

// По частичному тексту
await page.getByText('Добро пожаловать').textContent();
await page.getByText(/Добро.*Иван/).textContent(); // Регулярное выражение

// По роли и тексту (лучший способ)
await page.getByRole('button', { name: 'Сохранить изменения' }).click();
await page.getByRole('link', { name: 'Подробнее' }).click();

## **6️⃣ ПО PLACEHOLDER**

### **🔍 Поиск в Elements:**
html
<!-- HTML -->
<input placeholder="Введите email">
<textarea placeholder="Ваш комментарий"></textarea>

javascript
// В поиске Elements:
[placeholder="Введите email"]
[placeholder*="email"]
```

### **🎭 В Playwright:**
javascript
// Специальный метод для placeholder
await page.getByPlaceholder('Введите email').fill('test@mail.ru');
await page.getByPlaceholder('Ваш комментарий').fill('Отличный сервис!');

// Через атрибут
await page.locator('[placeholder="Введите email"]').fill('test@mail.ru');

## **7️⃣ ПО LABEL**

### **🔍 Поиск в Elements:**
html
<!-- HTML -->
<label for="email">Email адрес:</label>
<input id="email" type="email">

<label>
  Пароль:
  <input type="password">
</label>

javascript
// В поиске Elements ищем input:
#email                    // По связанному ID
label[for="email"]       // Сам label


### **🎭 В Playwright:**
// По связанному label (лучший способ)
await page.getByLabel('Email адрес:').fill('test@mail.ru');
await page.getByLabel('Пароль:').fill('123456');

// Альтернативные способы
await page.locator('#email').fill('test@mail.ru');
await page.locator('input[type="email"]').fill('test@mail.ru');

## **8️⃣ ПО ROLE (РОЛИ)**

### **🔍 Поиск в Elements:**
html
<!-- HTML -->
<button>Отправить</button>
<input type="text">
<a href="/home">Главная</a>
<h1>Заголовок</h1>
<img alt="Логотип" src="logo.png">

javascript
// В Elements роли не видны напрямую, но можно понять по тегам:
button          // role="button"
input           // role="textbox" 
a               // role="link"
h1              // role="heading"
img             // role="img"

### **🎭 В Playwright:**
javascript
// По роли (семантический подход)
await page.getByRole('button').click();
await page.getByRole('textbox').fill('текст');
await page.getByRole('link').click();
await page.getByRole('heading').textContent();
await page.getByRole('img').getAttribute('alt');

// С дополнительными параметрами
await page.getByRole('button', { name: 'Отправить' }).click();
await page.getByRole('heading', { level: 1 }).textContent();
await page.getByRole('link', { name: 'Главная' }).click();
```

---

## **9️⃣ ПО ALT (для изображений)**

### **🔍 Поиск в Elements:**
```html
<!-- HTML -->
<img src="avatar.jpg" alt="Аватар пользователя">
<img src="logo.png" alt="Логотип компании">
```

```javascript
// В поиске Elements:
[alt="Аватар пользователя"]
[alt*="Аватар"]
img[alt]                    // Все img с атрибутом alt
```

### **🎭 В Playwright:**
```javascript
// По alt тексту
await page.getByAltText('Аватар пользователя').click();
await page.getByAltText('Логотип компании').getAttribute('src');

// Через атрибут
await page.locator('[alt="Аватар пользователя"]').click();
```

---

## **🔟 ПО TITLE**

### **🔍 Поиск в Elements:**
```html
<!-- HTML -->
<button title="Сохранить документ">💾</button>
<a href="/help" title="Справочная информация">?</a>
```

```javascript
// В поиске Elements:
[title="Сохранить документ"]
[title*="Сохранить"]
```

### **🎭 В Playwright:**
```javascript
// По title атрибуту
await page.getByTitle('Сохранить документ').click();
await page.getByTitle('Справочная информация').click();

// Через локатор
await page.locator('[title="Сохранить документ"]').click();


## **✅ РЕКОМЕНДУЕМЫЙ ПОРЯДОК ПРИОРИТЕТОВ:**

### **1️⃣ Семантические локаторы (лучше всего):**
```javascript
page.getByRole('button', { name: 'Отправить' })
page.getByLabel('Email:')
page.getByPlaceholder('Введите текст')
page.getByText('Добро пожаловать')
page.getByAltText('Логотип')
page.getByTitle('Подсказка')
```

### **2️⃣ Data-testid (для тестирования):**
```javascript
page.getByTestId('submit-button')
page.getByTestId('user-profile')
```

### **3️⃣ ID (если есть):**
```javascript
page.locator('#submit-btn')
page.locator('#user-email')
```

### **4️⃣ CSS селекторы (в крайнем случае):**
```javascript
page.locator('.btn.btn-primary')
page.locator('[name="password"]')
```

---

## **❌ ИЗБЕГАТЬ:**

### **🚫 Слишком хрупкие селекторы:**
```javascript
// Плохо - зависит от структуры
page.locator('div > div > button:nth-child(3)')

// Плохо - зависит от позиции
page.locator('button:nth-of-type(2)')

// Плохо - слишком длинный путь
page.locator('html > body > div.container > form > div.form-group > button')
```

# 🏆 **ИТОГОВЫЙ ЧЕКЛИСТ**

## **📋 Алгоритм поиска локатора:**

### **1️⃣ Открыть DevTools (F12)**
### **2️⃣ Найти элемент в Elements**
### **3️⃣ Проверить селектор в поиске (Ctrl+F)**
### **4️⃣ Убедиться, что найден именно нужный элемент**
### **5️⃣ Выбрать лучший тип локатора**
### **6️⃣ Написать код в Playwright**
### **7️⃣ Протестировать локатор**

**Главное: сначала проверяем в Elements, потом используем в коде!** 🎯
