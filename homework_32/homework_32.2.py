from datetime import datetime


class Email:
    def __init__(self, sender: str, recipient: str, subject: str, body: str, date: str):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = self.convert_str_date_to_date_object(date)

    def convert_str_date_to_date_object(self, date):
        if isinstance(date, str):
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            return date_obj
        return None

    def __lt__(self, other):
        if isinstance(other, Email):
            return self.date < other.date
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Email):
            return self.date <= other.date
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Email):
            return self.date > other.date
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Email):
            return self.date >= other.date
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Email):
            return self.date == other.date
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Email):
            return self.date != other.date
        return NotImplemented

    def __str__(self):
        return (f"From: {self.sender}\nTo: {self.recipient}\n"
                f"Subject: {self.subject}\nDate: {self.date}\n{self.body}")

    def __len__(self):
        return len(self.body)

    def __hash__(self):
        return hash((self.sender, self.recipient, self.subject, self.date))

    def __bool__(self):
        return len(self.body) == 0


email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", 2022)
email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
email3 = Email("alice@example.com", "bob@example.com", "Hello", "", "2022-05-09")

print(email1)
print(len(email2))
print(hash(email3))
print(bool(email3))
print(email2 > email3)
