from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib import auth

from jobapp.models import *
from ckeditor.widgets import CKEditorWidget

from django import forms
from .models import Job

from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    job_type = forms.ChoiceField(choices=JOB_TYPE, widget=forms.Select(attrs={
        'class': 'form-select',
        'id': 'job-type'
    }), label="Job Type")

    class Meta:
        model = Job
        fields = [
            "title",
            "location",
            "job_type",
            "category",
            "salary",
            "description",
            "tags",
            "last_date",
            "company_name",
            "company_description",
            "url"
        ]
        widgets = {
            'last_date': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'datepicker',  # Important for jQuery selector
            }),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'company_description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)

        # Add placeholders explicitly
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Job Title'
        })
        self.fields['location'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Job Location'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Job Category'
        })
        self.fields['salary'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '$ Enter Job Salary'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Job Description'
        })
        self.fields['tags'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Job Tags (comma separated)'
        })
        self.fields['company_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Company Name'
        })
        self.fields['company_description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Company Description'
        })
        self.fields['url'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Company Website URL'
        })
        self.fields['last_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'yyyy-mm-dd'
        })

        for field_name, field in self.fields.items():
            if field_name != 'last_date':
                field.widget.attrs['class'] = 'form-control'



    

# class JobForm(forms.ModelForm):
    
#     def __init__(self, *args, **kwargs):
#         forms.ModelForm.__init__(self, *args, **kwargs)
#         self.fields['title'].label = "Job Title :"
#         self.fields['location'].label = "Job Location :"
#         self.fields['salary'].label = "Salary :"
#         self.fields['description'].label = "Job Description :"
#         self.fields['tags'].label = "Tags :"
#         self.fields['last_date'].label = "Submission Deadline :"
#         self.fields['company_name'].label = "Company Name :"
#         self.fields['url'].label = "Website :"


#         self.fields['title'].widget.attrs.update(
#             {
#                 'placeholder': 'eg : Software Developer',
#             }
#         )        
#         self.fields['location'].widget.attrs.update(
#             {
#                 'placeholder': 'eg : Bangladesh',
#             }
#         )
#         self.fields['salary'].widget.attrs.update(
#             {
#                 'placeholder': '$800 - $1200',
#             }
#         )
#         self.fields['tags'].widget.attrs.update(
#             {
#                 'placeholder': 'Use comma separated. eg: Python, JavaScript ',
#             }
#         )                        
#         self.fields['last_date'].widget.attrs.update(
#             {
#                 'placeholder': 'YYYY-MM-DD ',
                
#             }
#         )        
#         self.fields['company_name'].widget.attrs.update(
#             {
#                 'placeholder': 'Company Name',
#             }
#         )           
#         self.fields['url'].widget.attrs.update(
#             {
#                 'placeholder': 'https://example.com',
#             }
#         )    


    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "job_type",
            "category",
            "salary",
            "description",
            "tags",
            "last_date",
            "company_name",
            "company_description",
            "url"
            ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Service is required")
        return job_type

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("category is required")
        return category


    def save(self, commit=True):
        job = super(JobForm, self).save(commit=False)
        if commit:
            
            job.save()
        return job




class JobApplyForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['job']

class JobBookmarkForm(forms.ModelForm):
    class Meta:
        model = BookmarkJob
        fields = ['job']




class JobEditForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Job Title :"
        self.fields['location'].label = "Job Location :"
        self.fields['salary'].label = "Salary :"
        self.fields['description'].label = "Job Description :"
        # self.fields['tags'].label = "Tags :"
        self.fields['last_date'].label = "Dead Line :"
        self.fields['company_name'].label = "Company Name :"
        self.fields['url'].label = "Website :"


        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Software Developer',
            }
        )        
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg : Bangladesh',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': '$800 - $1200',
            }
        )
        # self.fields['tags'].widget.attrs.update(
        #     {
        #         'placeholder': 'Use comma separated. eg: Python, JavaScript ',
        #     }
        # )                        
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-MM-DD ',
            }
        )        
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'Company Name',
            }
        )           
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'https://example.com',
            }
        )    

    
        last_date = forms.CharField(widget=forms.TextInput(attrs={
                    'placeholder': 'Service Name',
                    'class' : 'datetimepicker1'
                }))

    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "job_type",
            "category",
            "salary",
            "description",
            "last_date",
            "company_name",
            "company_description",
            "url"
            ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Job Type is required")
        return job_type

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("Category is required")
        return category


    def save(self, commit=True):
        job = super(JobEditForm, self).save(commit=False)
      
        if commit:
            job.save()
        return job

