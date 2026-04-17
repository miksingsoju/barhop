from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('review_user__username','review_bar__name','review_description', 'review_date_created', 'review_rating')

    def review_user__username(self, obj):
        return obj.review_user.username

    def review_bar__name(self, obj):
        if obj.review_bar:
            return obj.review_bar.bar_name
        else:
            return "No bar"


admin.site.register(Review, ReviewAdmin)
    