import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(name, ingredients, email="ijzepeda@duck.com"):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Use 465 for SSL/TLS connections
    sender_email = "foodier.planner@gmail.com"
    sender_password = "Qwerty1234!@#$"
    receiver_email = email 

    subject = "Your Shopping List for this week"
    body = f"Hello {name},\n This are the ingredients for this week meal plan:\n{ingredients}\n\nWe want you healthy,\nFoodier Team"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, "plain"))


    try:
        print("Creating smtplib server")
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        print("1")
        # Start TLS (Transport Layer Security) encryption
        server.starttls()
        print("2")

        # Log in to the SMTP server
        server.login(sender_email, sender_password)
        print("3")

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("4")

        print("Email sent successfully!")

    except Exception as e:
        print("An error occurred while sending the email:", e)

    finally:
        # Close the connection to the SMTP server
        server.quit()
