import re

title_pattern = r"<title>(?P<title>.*)</title>"
body_pattern = r"<body>(?P<body>.*)</body>"
ignore_pattern = r"<.*?>"

text = input()

title = re.search(title_pattern, text).group()
# the easiest way to ignore the tags is to replace them with an empty string
title_without_tags = re.sub(ignore_pattern, "", title)
# because we cannot use \n in the regex, we just use a simple replace string method
title_without_special_tag = "".join(title_without_tags).replace("\\n", "")

body = re.search(body_pattern, text).group()
body_without_tags = re.sub(ignore_pattern, "", body)
body_without_special_tag = "".join(body_without_tags).replace("\\n", "")

print(f"Title: {title_without_special_tag}")
print(f"Content: {body_without_special_tag}")
