# character class works for a particular pattern only

import re

pattern = r"[A-Z][A-Z][0-9]"      # 1st and 2nd position for alphabets, 3rd position for numerical values

if re.search(pattern, "AB4"):
    print("Match found")
else:
    print("Match not found")