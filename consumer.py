import pika
import json
from models import Contact

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='contact_queue')


def send_email(contact_id):
    contact = Contact.objects.get(id=contact_id)
    print(f"Sending email to {contact.fullname} at {contact.email}")
    contact.message_sent = True
    contact.save()
    print("Email sent")


def callback(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message['contact_id']
    send_email(contact_id)


channel.basic_consume(queue='contact_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
