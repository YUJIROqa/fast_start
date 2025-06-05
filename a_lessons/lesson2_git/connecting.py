Пошаговое руководство: Git + GitHub через SSH

1. Создание SSH-ключа
# Генерация SSH-ключа (замените email на тот, что используете в GitHub)
ssh-keygen -t ed25519 -C "ваш_email@example.com"
# Нажмите Enter для сохранения по умолчанию (обычно ~/.ssh/id_ed25519)
# Введите пароль или нажмите Enter дважды, чтобы не использовать пароль

2. Добавление ключа в SSH-агент
# Запуск SSH-агента в фоне
eval "$(ssh-agent -s)"

# Добавление ключа
ssh-add ~/.ssh/id_ed25519

3. Копирование публичного ключа
# Linux/macOS
cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard
# или просто вывести на экран для копирования
cat ~/.ssh/id_ed25519.pub

## 4. Добавление ключа в GitHub

1. Войдите в свой аккаунт на GitHub
2. Нажмите на аватар → Settings
3. В левом меню выберите "SSH and GPG keys"
4. Нажмите "New SSH key"
5. Дайте ключу название (например, "My Laptop")
6. Вставьте скопированный публичный ключ в поле "Key"
7. Нажмите "Add SSH key"

## 5. Проверка SSH-соединения
ssh -T git@github.com

Если всё правильно, вы увидите:
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
## 6. Варианты создания и синхронизации репозитория

### Вариант A: Сначала создаём репозиторий на GitHub, потом клонируем

1. **На GitHub**: создайте новый репозиторий
   - Нажмите "+" → "New repository"
   - Введите имя, описание
   - Нажмите "Create repository"

2. **На локальном компьютере**: клонируйте репозиторий
   git clone git@github.com:username/repo-name.git
   cd repo-name
   # Добавляйте файлы, делайте коммиты, пушите
   touch README.md
   git add README.md
   git commit -m "Initial commit"
   git push
   ```

### Вариант B: Сначала создаём репозиторий локально, потом связываем с GitHub

1. **На локальном компьютере**: создайте репозиторий
   mkdir project-name
   cd project-name
   git init
   
   # Добавьте файлы и сделайте первый коммит
   touch README.md
   git add README.md
   git commit -m "Initial commit"

2. **На GitHub**: создайте пустой репозиторий
   - Нажмите "+" → "New repository"
   - Введите то же имя
   - **НЕ** инициализируйте с README, .gitignore или лицензией
   - Нажмите "Create repository"

3. **На локальном компьютере**: свяжите и отправьте
   git remote add origin git@github.com:username/project-name.git
   git branch -M main  # Переименовать главную ветку в main, если нужно
   git push -u origin main

## 7. Пуш и пулл: в чём разница
- **git push** — отправляет ваши локальные коммиты на GitHub
  git push  # Отправить текущую ветку

- **git pull** — получает изменения с GitHub и применяет их к вашему локальному репозиторию
  git pull  # Получить изменения из текущей ветки

## Что создавать первым?

- **Если у вас уже есть код**: сначала локальный репозиторий, потом GitHub (Вариант B)
- **Если вы начинаете с нуля**: лучше сначала GitHub, потом клонировать (Вариант A)

## Ключевые моменты
1. SSH-ключ настраивается один раз для компьютера
2. Всегда делайте `git pull` перед началом работы
3. Всегда делайте `git push` после завершения блока работы
4. Используйте осмысленные сообщения коммитов

Теперь у вас есть всё необходимое для работы с Git и GitHub через SSH!
