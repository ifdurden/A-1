import re

url = input("Enter your URL : ")
#() in search means to capture the value which will be inputed or whatever
#(?:) so it's doesn't capture the group of what ever
#
#
#
#
if username := re.search(r"^https?:/(?:www\.)?twitter\.(?:com|xyz|edu)/(.+)$", url):
#if username := re.sub("https:/twitter.com/" , "" , url)..............group().....yeal all that
    print(f"USERNAME: {username.group(1)}")




