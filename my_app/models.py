from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subtopics')

    def __str__(self):
        return self.title

# class Subtopic(models.Model):
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.title