from django import forms
from travel.models import (
    Category,
    SubCategory,
    AllCategory,
    Inclusion,
    Blogs,
    SliderImage,
    AboutusDetail,
)
from ckeditor.widgets import CKEditorWidget

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


# froms for blogs
class AddBlogsForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=True,
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Please enter blog title'
        })
    )
    content = forms.CharField(required=True,
        widget=CKEditorWidget()
    )
    
    cover_image = forms.FileField(required=True,
        widget=forms.FileInput(attrs={
            'class':'form-control'
            }
        )
    )

    class Meta:
        model = Blogs
        fields = ['title','content','cover_image']

# froms for sliderimage
class SliderImgForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=True,
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Please enter blog title'
        })
    )
    image = forms.FileField(required=True,
        widget=forms.FileInput(attrs={
            'class':'form-control'
            }
        )
    )
    
    class Meta:
        model = SliderImage
        fields = ['title','image']


# forms for aboutus
class AboutUsForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=True,
        widget=forms.TextInput(attrs={'class':'form-control',
          'placeholder':'Please enter about us title'}))

    content = forms.CharField(required= True, 
        widget=CKEditorWidget()
    )
    about_cover = forms.FileField(required=True,
        widget=forms.FileInput( attrs={
            'class':'form-control',
        })
    )

    class Meta:
        model = AboutusDetail
        fields = ['title','content','about_cover']
    