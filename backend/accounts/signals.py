from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from accounts.tasks import send_welcome_email


@receiver(user_logged_in)
def on_user_login(sender, request, user, **kwargs):
    print("✅ SIGNAL TRIGGERED:", user.email)

    if user.email:
          print(" check ✅ EMAIL FOUND:", user.email)
          send_welcome_email.delay(user.email)
      
    else:
        print("❌ NO EMAIL FOUND")