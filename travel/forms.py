from django import forms
from travel.models import (
    Category,
    SubCategory,
    AllCategory,
    Inclusion,
)


# forms for category
class AddCategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=True,
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Please enter category title'
        })
    )
    class Meta:
        model = Category
        fields =['title',]

#froms for subcategory 
class AddSubCategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=True,
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Please enter subcategory title ',
            'required': 'required',
        })
    )
    class Meta:
        model = SubCategory
        fields =['category','title']


#froms for All category
class AddAllCategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=True,
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Please enter all category title'
        })
    )
   
    class Meta:
        model = AllCategory
        fields =['category','sub_category','title']


#froms for inclusion
class AddInclusionForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=True,
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Please enter inclusion for different packages'
        })
    )
   
    class Meta:
        model = Inclusion
        fields =['title',]