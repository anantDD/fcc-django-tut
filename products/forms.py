from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    # cant do TextField here
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder": 'your title'}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "class": 'new-classname',
            "rows": 20,
            "cols": 150,
            "id": 'my_id',
            "placeholder": "your description"
        }))
    price = forms.DecimalField(initial=199.99)
