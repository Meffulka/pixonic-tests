# тестовые задания для Pixonic

## 1

### Условие

Напиши на python скрипт, который проверяет запущенный локально процесс nginx на 80 порту. Скрипт должен выводить один из статусов: OK, Warning, Error - придумай по каким критериям назначить тот или иной статус.

### Результат

файл first.py

Статусы:

* `OK` - если сервис запушен и конфиг валидный
* `Warning` - если сервис запущен и конфиг невалидный или используется не 80 порт
* `Error` - если сервис не запущен

*** Update 13:05 - проверка порта

## 2

### Условие

Напиши командную утилиту на python аргументом которой передается лог-файл access.log. Нужно вывести ТОП-5 самых часто встречаемых IP-адресов с которых заходили на сайт и количество запросов с этого IP. Образец лога можно взять здесь https://drive.google.com/file/d/1bg1_DU5qwn3bMLOKH0Zq-PxNC_rfbsF1/view?usp=sharing

### Результат

файл second.py

аргумент передается через ключ `--file`
