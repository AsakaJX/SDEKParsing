# Info
> [!IMPORTANT]
> Before using this script install python v.3.xx and `bs4, requests` libraries.

**Python for Windows:** https://www.python.org/downloads/<br />
**Python for Linux:** 
- **Ubuntu:** `sudo apt -y upgrade;sudo apt install -y python3-pip`
- **Arch:** `sudo pacman -Syy python;sudo pacman -Syy python-pip`

**Installing libraries:** `pip install bs4 requests`

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
> There could be more than 5 information about package, **BUT** this's not guaranteed

# Example
Example below parses `status` for package with id `1238742112`
```powershell
python sdek_parse.py 1238742112 1
```
