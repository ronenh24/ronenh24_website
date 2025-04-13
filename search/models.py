from django.db import models

# Create your models here.
class Chapter(models.Model):
    chapter_name = models.CharField(max_length=20)
    preview = models.TextField()

    def __str__(self):
        return self.chapter_name

class Verse(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    verse_number = models.IntegerField()
    verse_text = models.TextField()

    def __str__(self):
        return str(self.chapter) + ":" + str(self.verse_number)