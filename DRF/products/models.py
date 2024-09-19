from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2,default=00.00)


class Follow(models.Model):
    #user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    follower = models.ForeignKey(User,related_name='following',on_delete=models.CASCADE,blank=True,null=True)
    following = models.ForeignKey(User,related_name='followers',on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower', 'following'], name='unique_follow')
        ]


    def __str__(self):
        return f'{self.follower} follows {self.following}'