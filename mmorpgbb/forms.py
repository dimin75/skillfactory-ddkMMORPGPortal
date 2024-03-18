from django import forms

from .models import MmoRPGAdv, Response


class CreateAdvForm(forms.ModelForm):
    id_category = forms.ChoiceField(label="Категория", choices=MmoRPGAdv.CATEGORY,
                                    widget=forms.Select(attrs={"style": "width:100%"}))
    text = forms.CharField(label="Текст", widget=forms.Textarea(attrs={"style": "width:100%"}))
    file = forms.FileField(label="", required=False)

    class Meta:
        model = MmoRPGAdv
        fields = ['id_category', 'text', 'file']

    id_category = forms.ChoiceField(choices=MmoRPGAdv.CATEGORY)
    # id_category = forms.ModelChoiceField(queryset=id_category.choices)

class CreateResponseForm(forms.ModelForm):

    text = forms.CharField(label="Текст", widget=forms.Textarea(attrs={"style": "width:100%"}))
    file = forms.FileField(label="", required=False)

    class Meta:
        model = Response
        fields = ['text', 'file']
