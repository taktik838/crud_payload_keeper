# crud_payload_keeper
Сервер имеет 5 endpoint'ов:

- POST /api/add. Все что находится в request -> payload кладется в базу данных, в ответ возвращает ключ, по которому можно получить назад этот payload
- GET /api/get?key=key. Возвращает payload и счетчик дубликатов
- PUT /api/update. Обнуляет счетчик дубликатов у старого payload, и добавляет новый payload. В request -> payload должны быть переданы два параметра: "key", "newPayload"
- DELETE /api/remove. Удаляет payload по ключу. В request -> payload должен передаваться "key"
- GET /api/statistic. Возвращает процент дубликатов

Есть [postman коллекция](payload_keeper.postman_collection.json)

[Само ТЗ](%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20(backend).pdf)
