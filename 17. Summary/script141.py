"""
The Client class is implemented.

Create the following four instances of the Client class:

    client1 = Client('Tom', 'sample@gmail.com')
    client2 = Client('Donald', 'sales@gmail.com')
    client3 = Client('Mike', 'sales@yahoo.com')
    client4 = Client('Lisa', 'info@gmail.com')

Then search for all customers who have a gmail account ('gmail' in email address).

In response, print result to the console as shown below.
"""

class ClientList(list):
    def search_email(self, value):
        result = [client for client in self if value in client.email]
        return result

class Client:
    all_clients = ClientList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    def __repr__(self):
        return f"Client(name='{self.name}', email='{self.email}')"

client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@gmail.com')
client3 = Client('Mike', 'sales@yahoo.com')
client4 = Client('Lisa', 'info@gmail.com')

for client in Client.all_clients.search_email("gmail"):
    print(client)
