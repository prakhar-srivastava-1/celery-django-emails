from django import forms

class ReviewForm(forms.Form):
    name = forms.CharField(
        label='Name',
        mine_length=4,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control-mb-3',
                'placeholder': 'Name',
                'id': 'name-field'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control-mb-3',
                'placeholder': 'Email',
                'id': 'email-field'
            }
        )
    )
    review = forms.CharField(
        label='Review',
        mine_length=4,
        max_length=200,
        widget=forms.TextArea(
            attrs={
                'class': 'form-control',
                'rows': '5',
            }
        )
    )