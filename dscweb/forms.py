from django import forms


class MemberForm(forms.Form):
    username    = forms.CharField()
    first_name  = forms.CharField()
    last_name   = forms.CharField()
    mobile      = forms.CharField(widget=forms.NumberInput)
    email       = forms.EmailField()
    password    = forms.CharField(widget=forms.PasswordInput)
    confirm     = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(MemberForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm")
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
    
