class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return (f"{self.sender} says to {self.receiver}: "
                f"{self.content}. Sent: {self.is_sent}")


emails = []

while True:
    command = input()
    if command == "Stop":
        break
    new_command = command.split(" ")
    email_sender = new_command[0]
    email_receiver = new_command[1]
    email_content = new_command[2]
    email = Email(email_sender, email_receiver, email_content)
    emails.append(email)

sent_emails_indexes = list(map(int, input().split(", ")))

for i in range(len(emails)):
    if i in sent_emails_indexes:
        emails[i].send()

for y in range(len(emails)):
    print(emails[y].get_info())
