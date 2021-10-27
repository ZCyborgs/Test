# -*- coding: utf-8 -*-

import re
text = "Abcd 4 computer 765 Python 687 computer"
pattern = r"[\d\w]+"
email = "sitamzeus@gmail.com"
phone = "670065835"
phone1 = "670 065 835"
phone2 = "670-065-835"
phone3 = "670.065.835"
phone_pattern = r"[0-9]{9,}"
phone_cmr_patern = r"^2[0-9]{2}[\s\-]?[0-9]{3}[\s\-]?[0-9]{3}$"
phone1_pattern = r"^6[0-9]{3}\s[0-9]{3}\s[0-9]{3}$"
email_pattern = r"[a-z]+[0-9]*[a-z]*@[a-z]+.[a-z]+$"
email_pattern = r"[a-z]+[0-9\.\-_]*[a-z]*[0-9\.\-_]*[a-z]*@[a-z]+[a-z]*[\.\-_]?.[a-z]{2,4}"
password_pattern = r"[a-z]+"
password_pattern = r"[A-Z]+"
password_pattern1 = r"[/\"':!^&-_à}{)(+=µ%]+"
password_pattern1 = r"[a-zA-Z0-9/\"':!^&-_à}{)(+=µ%]{8,}"
match = re.findall(pattern, text)
print(re.match(email_pattern, email))
print(match)