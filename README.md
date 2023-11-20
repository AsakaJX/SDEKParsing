# Requirements
> [!IMPORTANT]
> Before using this script install python v.3.xx and `bs4, requests` libraries.

**Python for Windows:** https://www.python.org/downloads/<br />
**Python for Linux:** 
- **Ubuntu:** `sudo apt -y upgrade;sudo apt install -y python3-pip`
- **Arch:** `sudo pacman -Syy python python-pip`

**Installing libraries:** `pip install bs4 requests`

# sdek_parse_json.py - version that dumps every parsed element into json format
> [!NOTE]
> This script accepts *one* argument: `package_id`

`package_id` - package number given to be able to track it's status

# sdek_parse_json.py - Example
Example below parses everything for package with id `1238742112`
```powershell
python sdek_parse_json.py 1238742112
```
Output:
```json
{
    "package_id": "1238742112",
    "data": [
        {
            "Идентификатор": "1238742112",
            "Текущий статус": "Вручен (Лениногорск)",
            "Город-отправитель": "Казань",
            "Город-получатель": "Лениногорск",
            "Отправитель": "Побережная Евгения Анатольевна",
            "Дата создания накладной": "20.03.2021",
            "Адрес получения": "ул. Ленинградская, 53",
            "График работы ПВЗ": "Пн-Пт: 08:00 - 20:00 Сб-Вс: 10:00 - 18:00",
            "Телефон ПВЗ": "+74954451900",
            "Вес": "0.38 кг",
            "Количество мест": "1 место"
        }
    ]
}
```

# sdek_parse.py - simple version, that just outputs one element at the time
> [!NOTE]
> This script accepts *two* arguments: `package_id` and `element_id`

`package_id` - package number given to be able to track it's status

`element_id` - choses what you want to output:

**0 - package id<br />
1 - status<br />
2 - shipped from (city)<br />
3 - shipped to (city)<br />
4 - package sender**

> [!WARNING]
> There could be more than 5 information about package, **BUT** this is not guaranteed

## sdek_parse.py - Example
Example below parses `status` for package with id `1238742112`
```powershell
python sdek_parse.py 1238742112 1
```
Output:
```powershell
Вручен (Лениногорск)
```
