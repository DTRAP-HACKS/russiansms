# AresBomb 2.0

AresBomb - это SMS/Call бомбер с приятными фичами и автообновлениями

##### Список фич
 - Кастомные списки бомбинга
 - Управление частотой SMS и Call бомбинга процентным соотношением
 - Отправление определённого количества сообщений и звонков
 - Интервалы между отправкой
 - Список избранных номеров

# Установка

#### Для Termux
```sh
pkg install git
pkg install python
pip install requests
git clone https://github.com/MaksPV/AresBomb/tree/new-version
```
Вам надо ещё найти базы данных с расширением .arsdat

# Запуск
```sh
cd AresBomb
python ui.py
```

# API
Запуск бомбина из консоли
```sh
python core.py <выбор режима работы> <номер телефона в формате 79000000000> <количество сообщений> <интервал между их отправкой в секундах>

Режимы запуска бомбера:
-g - печатать отчёт в консоль

Пример:
python core.py -g 79104342719 100 1.5
python core.py - 79058625419 98 0
```
Генерация файлов .arsdat в удобоваримый для спамера формат
```sh
python generate.py <режим> <имя файла>

-s - генерация сервисов для СМС
-c - генерация сервисов для звонков

Пример:
python generate.py -s database
python generate.py -c callsdata
```

# Ссылочки
* [t.me/AresBomb](telete.in/AresBomb) - Телеграм канал на котором новости проекта
* [t.me/Maksimushka](telete.in/Maksimushka) - Автор бомбера
