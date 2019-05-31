from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000,help_text='The max length of the text is 4000')
                #'placeholder' attribute can be added
    # this field isnt available in Topic model:;okay its created here

    class Meta:
        model = Topic
        fields = ['subject', 'message']
        # fields = '__all__'
