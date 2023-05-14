""" 

Here is a sketch to start getting to work

"""
# project 'app'
# app 'users'
 
from django.db import models
from django.contrib.auth.models import AbstractUser

from PIL import Image


    
class Profile(models.Model):
    about = models.CharField(blank=True, null=True)
    avatar = models.ImageField(upload_to='profiles/', null=True, blank=True)
    
    ###### social media links. like 
    # linkedin
    # fb
    # etc

        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        
        # prevent collapse bd with images and bad display
        if self.avatar:
            image = Image.open(self.avatar.path)
            output_size = (300, 300)
            image.thumbnail(output_size)
            if image.width < output_size[0] or image.height < output_size[1]:
                background = Image.new('RGB', output_size, (255, 255, 255))
                offset = ((output_size[0] - image.width) // 2, (output_size[1] - image.height) // 2)
                background.paste(image, offset)
                image = background
            image.save(self.avatar.path)
            
            
            
            
            
            
class BaseUser(AbstractUser):
    
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField(blank=False)
    nationality = models.CharField(max_length=100) # make some select with js
    
    
    
    ###### CONTACT
    # phone_number =
    # email =
    
    
    ###### LOCATION 
    # address
    # city/locality               # make some select with js            
    # state                         # make some select with js
    # postal_code
    # country                        # make some select with js
    
    
    
    ###### DOCS
    # identification - driver's licence - passport
    
    
    ##### CREDIT CARD AND WOP DATA
    
    
    
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    class Meta:
        abstract = True
    
    
    
            
class Family(BaseUser):
     
    pass

    
            
class Children(models.Model):
    family = models.ForeignKey(Family, related_name="childrens", on_delete=models.CASCADE)

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    name = models.CharField(max_length=100)
    dietary_requirements = models.TextField(blank=True)            
    notes =  models.TextField(blank=True)   
    
    


class Nanny(BaseUser): # do we allow them upload their resume or a maybe a url to it?
    # abailable_hours =
    
    def __str__ (self):
        return self.get_full_name

class NannyData(models.Model):
    name = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField(blank=True) 

    class Meta:
        abstract = True 

class NannyEducation(NannyData):
    nanny = models.ForeignKey(Nanny, on_delete=models.CASCADE, related_name="education")
   # place = models.CharField()
    
    
class NannyExperience(NannyData):
    nanny = models.ForeignKey(Nanny, on_delete=models.CASCADE, related_name="experiences")
    detail = models.TextField()
    # ref_name = models.CharField()
    # ref_contact =
    
    
    
        
    
