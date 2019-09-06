from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
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
    email = forms.EmailField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "anant" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email


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
