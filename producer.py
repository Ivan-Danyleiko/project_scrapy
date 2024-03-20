import pika
import json
from faker import Faker
from models import Contact

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='contact_queue')


def send_contacts_to_queue(num_contacts):
    fake = Faker()
    for _ in range(num_contacts):
        fullname = fake.name()
        email = fake.email()
        contact = Contact(fullname=fullname, email=email)
        contact.save()
        message = {'contact_id': str(contact.id)}
        channel.basic_publish(exchange='', routing_key='contact_queue', body=json.dumps(message))
        print(f"Contact {fullname} with email {email} sent to queue")


send_contacts_to_queue(5)

connection.close()
