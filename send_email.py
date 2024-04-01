import smtplib, ssl

def send_email(message, receiver):
    host = "smtp.gmail.com"
    port = 465

    username = "saleemesha04@gmail.com"
    password = "icmr ymev sgqb wxaw"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)