"""
Абстрактный тип данных (АТД) -- это неявное определение некоторого типа данных
в нашей системе, которое формально задаёт некоторое множество объектов и
набор допустимых операций над ними.
Класс -- это реализация АТД.

Добавление нового класса в программу определяется исключительно наличием в
проекте определяющего этот класс АТД.

Правила проектирования программы:
-- Система типов основана только на классах.
-- Вычислительная модель ООП -- это набор равноправных классов.
-- Методы -- это единственная форма общения между классами.
-- Активно применяем обобщённые типы.
-- По возможности применяем статическую типизацию.
-- Отказываемся от явных структур данных в классах (отвязываемся от конкретной
реализации).
При проектировании АТД надо обязательно учитывать и эффективность его реализации.
В процессе проектирования очень важно делать акцент на возможности повторного
использования всех компонентов.

В спецификацию АТД добавляем предусловия и постусловия.
Придерживаемся принципа достаточной полноты АТД.
Все методы делим на конструкторы, запросы и команды.
Конструкторы всегда создают объекты в согласованном формате.
Полностью исключаем все абстрактные побочные эффекты.
По возможности избегаем явной обработкой исключений в коде.

Класс -- это базовая строительная единица в нашей программе, она сочетает
свойства и типа данных как семантической единицы, и модуля, объединяющего
данные и вычисления, и выделяющего код в отдельную синтаксическую единицу.

Придерживаемся единой нотации.
Единственной модульной единицей в проекте всегда остаётся только класс.
Классы обычно группируются в кластеры.
Частично реализованные классы играют важную роль в конструировании системы,
фиксируя общее поведение некоторой группы объектов.
"""

start_url = 'https://api.hh.ru/resumes?all_folders=True&page={}&per_page=50'
page_number = 0
ids_to_upload = []
while true:
    url = start_url.format(page_number)
    response = connector.get_response(url=url)
    data = response.json()
    items = data['items']
    ids = loader.get_ids(
        items=items,
        action='upload',
        )
    ids_to_upload.extend(ids)
    page_number += 1
    if page_number >= data['pages']:
        break

resumes = []
for id in ids_to_upload:
    url = f'https://api.hh.ru/resumes/{id}'
    response = connector.get_records(url=url)
    resume: List[dict] = response.json()
    resumes.extend(resume)
        
records = parser.get_records(resumes)
loader.save(records)
    
    
    
    
    
    
    