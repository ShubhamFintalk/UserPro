from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=33)
    password = models.CharField(max_length=22)
    userName = models.CharField(max_length=33)

    def __str__(self):
        return "{0}, firstName: {2}, lastName: {1}, email: {2}, userName:{3}".format(self.first_name, self.last_name,
                                                                                     self.email, self.userName)


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=33)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "User: {0}, text: {1}, Created: {2}, Updated: {3}" \
            .format(self.user, self.text, self.created_at, self.updated_at)

    # class Meta:
    #     db_table = 'myuser'
