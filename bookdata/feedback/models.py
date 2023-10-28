from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import Book,Category

class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    message = models.CharField(max_length=100, blank=True,null=True)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user} - {self.title}"
    

# class Recommendation(models.Model):
#     personality = models.ForeignKey(Book, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, null=True, blank=True)

#     def __str__(self):
#         return f"Recommendation for {self.personality}"

# def recommend():
#     recommendation = Recommendation.objects.get(id=1)
#     author_name = recommendation.personality.category
#     print(author_name)


     
