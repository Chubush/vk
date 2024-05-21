# şifre resetleme token üreticisi
from django.contrib.auth.tokens import PasswordResetTokenGenerator

#şifre resetleme token üretici method

class UserVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        user_id = str(user.pk)
        ts = str(timestamp)
        is_active = str(user.is_active)
        
        return f"{user_id}{ts}{is_active}"
    
    
user_tokenizer_generate = UserVerificationTokenGenerator()