import re

url = input("Twitter URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

# if matches:
#     print("Username:", matches.group(2))

# if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print("Username:", matches.group(2))

# if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print("Username:", matches.group(1))

# if matches := re.search(r"^https?://(?:www\.)?twitter\.(?:com|org)/(.+)$", url, re.IGNORECASE):
#     print("Username:", matches.group(1))

if matches := re.search(r"^https?://(?:www\.)?twitter\.(?:com|org)/(\w)$", url, re.IGNORECASE):
    print("Username:", matches.group(1))
