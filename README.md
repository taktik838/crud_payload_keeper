# crud_payload_keeper
Сервер имеет 5 endpoint'ов:

- POST /api/add. Все что находится в request -> payload кладется в базу данных, в ответ возвращает ключ, по которому можно получить назад этот payload
- GET /api/get?key=key. Возвращает payload и счетчик дубликатов
- PUT /api/update. Обнуляет счетчик дубликатов у старого payload, и добавляет новый payload. В request -> payload должны быть переданы два параметра: "key", "newPayload"
- DELETE /api/remove. Удаляет payload по ключу. В request -> payload должен передаваться "key"
- GET /api/statistic. Возвращает процент дубликатов

Есть [postman коллекция](payload_keeper.postman_collection.json)
