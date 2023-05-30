
from pathlib import Path
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives

recipient = "dbpillai@gmail.com"
sender = "collabozartek@gmail.com" #
image_path = '/Users/divyarahchand/PycharmProjects/EventCollabo/CE/444fde54-aa48-4539-96cf-6852718aecab.png'
image_name = Path(image_path).name

subject = "I am sending you nice image."
text_message = f"Email with embedded image {image_name}."

html_message = f"""
<!doctype html>
  <html lang=en>
    <head>
       <meta charset=utf-8>
       <title>Some title.</title>
    </head>
    <body>
      <h1>{subject}</h1>
      <p>
         <img src='cid:{image_name}'/>
      </p>
    </body>
</html>
"""


# define function for sending email
def send_email(subject, text_content, html_content=None, sender=sender, recipient=recipient, image_path=None, image_name=None):
    email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sender, to=recipient if isinstance(recipient, list) else [recipient])

    if all([html_content,image_path,image_name]):
        email.attach_alternative(html_content, "text/html")
        email.content_subtype = 'html'  # set primary content to be text/html
        email.mixed_subtype = 'related' # it is important part that ensures embedding of image

        with open(image_path, mode='rb') as f:
            image = MIMEImage(f.read())
            email.attach(image)
            image.add_header('Content-ID', f'<{image_name}>')

    email.send()


# send test email
send_email(subject="TEST", text_content=text_message, html_content=html_message, sender=sender, recipient=recipient, image_path=image_path, image_name=image_name)
