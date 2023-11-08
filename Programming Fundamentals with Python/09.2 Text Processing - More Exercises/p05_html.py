def printing_title(title):
    print("<h1>")
    print(f"    {title}")
    print("</h1>")


def printing_content(content):
    print("<article>")
    print(f"    {content}")
    print("</article>")


def printing_comment(comment):
    print(f"<div>")
    print(f"    {comment}")
    print(f"</div>")


article_title = input()
article_content = input()

comments = []

while True:
    command = input()
    if command == "end of comments":
        break
    article_comments = command
    comments.append(article_comments)

printing_title(article_title)
printing_content(article_content)
[printing_comment(com) for com in comments]
