from djongo import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Cambiar ArrayReferenceField a ManyToManyField para manejar relaciones correctamente
class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)  # Usar ManyToManyField en lugar de ArrayReferenceField

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return f"{self.activity_type} - {self.user.username}"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}: {self.score}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
