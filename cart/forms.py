from django import forms


class AddToCartForm(forms.Form):
    quantity_choices = [(i, str(i)) for i in range(1, 30)]
    
    quantity = forms.TypedChoiceField(choices=quantity_choices, coerce=int)
