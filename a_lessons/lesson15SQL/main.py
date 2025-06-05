import psycopg2

try:
    db = psycopg2.connect(
        host="192.168.10.51",
        user="studybay",
        password="oa1loh5The",
        database="studybay_test",
        port=5433
    )
    print("✅ Подключение к PostgreSQL успешно!")
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
    except psycopg2.Error as e:
        print(f"❌ Ошибка выполнения запроса: {e}")
    
    print(f"📊 Найдено записей: {len(result)}")
    print(f"📋 Данные: {result}")
    
except psycopg2.Error as e:
    print(f"❌ Ошибка подключения: {e}")


 







db.close()