from django import forms
from .models import Recipient, Message, Mailing


class BootstrapFormStylesMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, (forms.Select, forms.SelectMultiple)):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

class RecipientForm(BootstrapFormStylesMixin, forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ["email", "full_name", "comment"]



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["topic", "text"]




class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = (
            "message",
            "recipients",
        )

