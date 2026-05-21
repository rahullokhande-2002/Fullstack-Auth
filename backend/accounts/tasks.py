from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    try:
        send_mail(
            subject="Welcome to our App ✅",
            message=f"Hello {email}, welcome to our system 🚀",
            from_email="lokhanderahul960@gmail.com",   # ✅ your gmail
            recipient_list=[email],
            fail_silently=False,
        )

        print(f"✅ REAL EMAIL SENT TO: {email}")

    except Exception as e:
        print(f"❌ ERROR SENDING EMAIL: {e}")
