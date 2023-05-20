from django.contrib import admin
from .models import Search,Contact,Subscriber

# Register your models here.
@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('query','user',)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone',)
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display=('email',)
class FeedbackAdmin(admin.ModelAdmin):
    list_display  = ('mail',)