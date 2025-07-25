# Системный Монитор — Информация о компьютере

Простой Python-скрипт, который выводит основную системную информацию о вашем компьютере в виде отформатированной таблицы.  
С вероятностью 50% выводит случайное сообщение с помощью cowsay.

---

## Основные возможности

- Отображение имени компьютера
- Определение домена (если компьютер в домене)
- MAC-адрес сетевого адаптера
- Полное имя пользователя (из Windows)
- IP-адреса (все, привязанные к хосту)
- Имя учётной записи (логин)
- Случайная фраза от коровы (в 50% случаев)

---

getNameMashin()
Возвращает имя компьютера
getDomainName()
Определяет доменное имя или сообщает, что ПК не в домене
getMacAddress()
Получает MAC-адрес через uuid
get_display_name()
Получает полное имя пользователя (Windows)
getIPAddress()
Получает все IP-адреса машины
getAccountName()
Получает имя учётной записи (логин)
getChans()
Возвращает True с 50% вероятностью — для случайного вывода коровы
__randomInscription()
Возвращает случайную фразу из списка

Особенности
Использует PrettyTable для красивого форматирования таблицы.
cowsay добавляет элемент случайности и юмора.
Поддержка кириллицы (указано # -*- coding: utf-8 -*-).
Автоматическое определение сетевых и системных параметров.
## Лицензия
Этот проект распространяется под лицензией MIT. См. файл LICENSE для подробностей.

Автор Sniaper
Скрипт написан для быстрой диагностики системы и поднятия настроения.
