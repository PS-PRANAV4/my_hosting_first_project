from django.core.mail import send_mail,EmailMessage


def send_email(otp,email):
    subject = 'OTP VERIFICATION!'
    message = f'YOUR OTP FOR VERIFICATION IS {otp} '
    from_email = 'pranavpranab@gmail.com'

    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list) 
