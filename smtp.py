import smtplib
import getpass

# SMTP服务器设置
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your_email@gmail.com"
password1 = "your_password"  # 或者使用应用程序密码
receiver_email = "receiver@example.com"

smtp_obj =smtplib.SMTP(smtp_server, smtp_port)

smtp_obj.ehlo()
smtp_obj.starttls()

email = input("Enter your email: ")
password2 = getpass.getpass("Enter your  password: ")
smtp_obj.login(email, password1)

smtp_obj.login(sender_email, password2)

From_address =sender_email
To_address = receiver_email
subject = "Test email"
message = "This is a test email from Python"
full_email = f"Subject: {subject}\n\n{message}"
print(smtp_obj.send_message(From_address, To_address, full_email))
smtp_obj.quit()
