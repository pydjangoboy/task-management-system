from django import forms
from .models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Task Information',
                'title',
                'description',
                'due_date',
                'status'
            ),
            Submit('submit', 'Save')
        )

        # Add the crispy date picker class to the due_date field
        self.fields['due_date'].widget.attrs['class'] = 'datepicker'
        # Set the date format for the due_date field
        self.fields['due_date'].widget.input_type = 'text'
        self.fields['due_date'].widget.format = '%Y-%m-%d'  # Adjust the format as needed
        self.fields['due_date'].widget.attrs['placeholder'] = 'YYYY-MM-DD'

        # Add placeholders for other fields
        self.fields['title'].widget.attrs['placeholder'] = 'Enter title'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter description'
        self.fields['status'].widget.attrs['placeholder'] = 'Enter status'
