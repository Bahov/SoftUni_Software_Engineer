class Email:
    def __init__(self, sender, receiver, content, is_sent = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True
    
    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'
    
all_emails = []

while True:
    email = input()
    if email == 'Stop':
        break
    sender, receiver, content = email.split(' ')
    current_email = Email(sender, receiver, content)
    all_emails.append(current_email)

sent_emails = list(map(int, input().split(', ')))

for index in sent_emails:
    all_emails[index].send()

for element in all_emails:
    print(element.get_info())