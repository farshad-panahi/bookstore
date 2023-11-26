from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from django.contrib.auth import get_user_model

class ThisUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = (
            'username',
            'email',
        )

class ThisUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
        )


