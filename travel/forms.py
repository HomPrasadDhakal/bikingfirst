from django import forms
from travel.models import (
    Category,
    SubCategory,
    AllCategory,
    Inclusion,
    Blogs,
    SliderImage,
    AboutusDetail,
    ContactDetail,
    Packages,
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
    

# forms for contactus
class ContactUsForm(forms.ModelForm):
    sub_title = forms.CharField(max_length=255, required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Please enter your slogon here.'
        })
    )

    address = forms.CharField( max_length=255, required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Please enter your address here.'
        })
    )

    phone = forms.CharField(required=True, max_length=15,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter your Phone number'
        })
    )

    mobile = forms.CharField(required=True, max_length=15,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter your mobile number'
            
        })
    )

    email = forms.EmailField( max_length=255, required=True,
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Enter your email here',
            
        })
    )

    website = forms.URLField( max_length=255, required=True,
        widget=forms.URLInput(attrs={
            'class':'form-control',
            'placeholder':'Enter your website'
        })
    )

    class Meta:
        model = ContactDetail
        fields =['sub_title','address','phone','mobile','email','website']




# forms for packages
class DateInput(forms.DateInput):
    input_type = 'date'

class AddPackagesForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=True,
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Please add package name here.'
        })
    )

    description = forms.CharField(required= True, 
        widget=CKEditorWidget()),

    gallary = forms.FileField(required=True,
        widget=forms.FileInput( attrs={
            'class':'form-control',
            'multiple': True,
        })
    )

    # category = [(Category.id, Category.title) for Category in Category.objects.all()]
    # category = forms.MultipleChoiceField(
    #     required=True, widget=forms.Select, choices=category
    # )

    # category = [(Category.id, Category.title) for Category in Category.objects.all()]
    # sub_category = forms.MultipleChoiceField(required=True,
    # widget=forms.Select, choices=category
    
    

    Itinerary = forms.CharField(required= True, 
        widget=CKEditorWidget()),

    region = forms.CharField(max_length=255, required=True,
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Please add package name here.'
        })
    )

    duration = forms.CharField(max_length=255, required=True,
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Please add package name here.'
        })
    )

    starting_date = forms.DateTimeField(required=True,
        widget = DateInput(attrs={
            'class':'form-control',
        })
    )

    ending_date = forms.DateTimeField(required=True,
        widget = DateInput(attrs={
            'class':'form-control',
        })
    )

    Availability = forms.BooleanField(required=False)

    inclusion = [(Inclusion.id, Inclusion.title) for Inclusion in Inclusion.objects.all()]
    inclusion = forms.MultipleChoiceField(
        required=True, widget=forms.CheckboxSelectMultiple, choices=inclusion,
    )

    price = forms.CharField(max_length=255, required=True,
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Please enter the price of package here.'
        })
    )

    class Meta:
        model = Packages
        fields= '__all__'