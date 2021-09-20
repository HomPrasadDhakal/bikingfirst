from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import DateField
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
    PackagesGallary,
    BookPackages,
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

    class Meta:
        model = SubCategory
        fields =['category','title']

        widgets ={
            'category':forms.Select(attrs={
                'class':'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter sub category title'
            })
        }


#froms for All category
class AddAllCategoryForm(forms.ModelForm):

    class Meta:
        model = AllCategory
        fields =['category','sub_category','title']

        widgets ={
            'category':forms.Select(attrs={
                'class':'form-control'
            }),
            'sub_category':forms.Select(attrs={
                'class':'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter sub category title'
            })
        }


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
        widget=forms.ClearableFileInput(attrs={
            'class':'form-control'
            }
        )
    )

    class Meta:
        model = Blogs
        fields = ['title','content','cover_image']

# froms for sliderimage
class SliderImgForm(forms.ModelForm):
    
    class Meta:
        model = SliderImage
        fields = ['title','image']
        widgets={
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter slider image title here'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class':'form-control',
            }),
        }


# forms for aboutus
class AboutUsForm(forms.ModelForm):
    
    class Meta:
        model = AboutusDetail
        fields = ['title','content','about_cover']
        widgets={
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter about us  title here'
            }),
            'content': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter about us detail here'
            }),
            'about_cover': forms.ClearableFileInput(attrs={
                'class':'form-control',
            }),
        }
    

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
    inclusion = [(Inclusion.id, Inclusion.title) for Inclusion in Inclusion.objects.all()]
    inclusion = forms.MultipleChoiceField(
        required=True, widget=forms.CheckboxSelectMultiple, choices=inclusion,
    )
    class Meta:
        model = Packages
        fields= ['title','description','image','category','sub_category','all_category','Itinerary',
        'region','duration','starting_date','ending_date','Availability','inclusion','price']

        widgets ={
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter packages title here'
            }),
            'description': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter pacakge description',
                'rows':'8',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class':'form-control',
            }),
            'category':forms.Select(attrs={
                'class':'form-control'
            }),
            'sub_category':forms.Select(attrs={
                'class':'form-control'
            }),
            'all_category':forms.Select(attrs={
                'class':'form-control'
            }),
            'Itinerary': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter pacakge description',
                'rows':'8',
            }),
            'region': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter packages region here'
            }),
            'duration': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter packages title here'
            }),
            'starting_date': DateInput(attrs={
                'class':'form-control',
            }),
            'ending_date': DateInput(attrs={
                'class':'form-control',
            }),
            'Availability':forms.CheckboxInput(attrs={
               'help-text':'please tick in the field'
            }),
           'price': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter packages price here'
            }),
            
        }

# forms for packages images gallary

class AddPackagesImagesFrom(forms.ModelForm):
    class Meta:
        model = PackagesGallary
        fields  = ['packages','image']



#forms for booking packing
class BookingPackages(forms.ModelForm):
    class Meta:
        model = BookPackages
        fields = ['name','phone','email','country','package','arrival_date','depature_date','no_of_adults','no_of_children']

        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter your name',
            }),
            'phone':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter your contact number',
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Enter your email address',
            }),
            'country':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter your country name',
            }),
            'package':forms.Select(attrs={
                'class':'form-control',
            }),
            'arrival_date':DateField(attrs={
                'class':'form-control',
            }),
            'depature_date':DateField(attrs={
                'class':'form-control',
            }),
            'no_of_adults':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter total number of adult want to booked'
            }),
            'no_of_children':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Please enter total number of children want to booked'
            }),
        }