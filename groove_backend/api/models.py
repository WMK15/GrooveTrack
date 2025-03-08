from django.db import models
from django.contrib.auth.models import User

class DanceMove(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dance_move = models.ForeignKey(DanceMove, on_delete=models.CASCADE)
    progress = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.dance_move.name}"

class RecommendedExercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

# Dance Style model
class DanceStyle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# Move model
class Move(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    media_url = models.URLField()  # URL for video/image/media related to the move
    style = models.ForeignKey(DanceStyle, related_name='moves', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Progress Tracker model
class Progress(models.Model):
    user_id = models.IntegerField()  # You could relate this to the User model if necessary
    move = models.ForeignKey(Move, on_delete=models.CASCADE)
    progress_status = models.CharField(max_length=50, choices=[('In Progress', 'In Progress'), ('Mastered', 'Mastered')])

    def __str__(self):
        return f"{self.move.name} - {self.progress_status} for User {self.user_id}"