from django import forms

class CreateTask(forms.Form) :
    judul = forms.CharField(label='judul', max_length=100)
    deskripsi = forms.CharField(label = 'deskripsi', widget=forms.Textarea)