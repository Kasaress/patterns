# Адаптация паттернов программирования из книги head first "Паттерны программирования" на python

![Обложка книги](img/book_img.jpg)

1. [x] [Стратегия](chapter_1_strategy/main.py)

**Паттерн Стратегия определяет семейство алгоритмов, инкапсулирует каждый из них и обеспечивает их взаимозаменяемость. Он позволяет модифицировать алгоритмы независимо от их использования на стороне клиента.**

Вместо джавовских интерфейсов использовала наследование от абстрактного класса и от протокола (для разнообразия и практики). Разницы пока не заметила.

2. [x] [Наблюдатель](chapter_2_observer/main.py)

**Паттерн Наблюдатель определяет отношение «один ко многим» между объектами таким образом, что при изменении состояния одного объекта происходит автоматическое оповещение и обновление всех зависимых объектов.**

Реализовано два типа наблюдателей:

- пассивный, который принимает все данные при обновлении, сохраняет себе только необходимые;
- активный, который принимает сигнал о наличии обновлений, запрашивает только необходимые данные.

3. [x] [Декоратор](chapter_3_decorator/main.py)

**Паттерн Декоратор динамически наделяет объект новыми возможностями и является гибкой альтернативой субклассированию в области расширения функциональности.**

Реализация без синтаксического сахара, классы-декораторы изменяют поведение основных классов.

4. [x] [Фабрика](chapter_4_factory/main.py)

**Абстрактная фабрика предоставляет интерфейс для создания семейств взаимосвязанных объектов без указания их конкретных классов.**

**Фабричный метод определяет интерфейс создания объекта, но позволяет субклассам выбрать создаваемый экземпляр.**


5. [x] [Одиночка](chapter_5_singleton/main.py)

**Паттерн Одиночка гарантирует, что класс имеет только один экземпляр, и предоставляет глобальную точку доступа к этому экземпляру.**

Выбран вариант с декоратором, позволяет создавать единственный экземпляр класса тогда, когда он потребуется.

Реализация подходит для выполнения в однопоточном режиме, с одним инстансом приложения.

6. [x] [Команда](chapter_6_command/main.py)

**Паттерн Команда инкапсулирует запрос в виде объекта, делая возможной параметризацию клиентских объектов с другими запросами, организацию очереди или регистрацию запросов, а также поддержку отмены операций.**

Текущаая реализация страдает многословностью, неряшливостью и запутанностью. Но я подумаю о этом после написания всех паттернов (или нет).

7.1. [x] [Адаптер](chapter_7_adapter/main.py)

**Адаптер преобразует интерфейс класса к другому интерфейсу, на который рассчитан клиент. Адаптер обеспечивает совместную работую классов, невозможную в обынчх условиях из-за несовместимых интерфейсов.**

7.2. [x] [Фасад](chapter_7_facade/main.py)

**Фасад предоставляет унифицированный интерфейс к группе интерфейсов подсистемы. Фасад определяет высокоуровневый интерфейс, упрощающий работу с подсистемой.**

8. [x] [Шаблонный метод](chapter_8_template_method/main.py)

**Шаблонный метод определяет скелет алгоритма в методе, оставляя определение реализации некоторых шагов субклассам. Субклассы могут переопределять некоторые части алгоритма без изменения его структуры.**

9.1. [x] [Итератор](chapter_9_iterator/main.py)

**Паттерн итератор предоставляет механизм последовательного перебора элементов коллекции без раскрытия ее внутреннего представления.**

9.2. [ ] [Компоновщик]()

**.**

10. [ ] [ ]()

**.**

11. [ ] [ ]()

**.**

12. [ ] [ ]()

**.**

13. [ ] [ ]()

**.**

14. [ ] [ ]()

**.**