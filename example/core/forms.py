from django import forms
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'reg_number')