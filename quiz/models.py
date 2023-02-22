from django.db import models

class MetaData(models.Model):
    title = models.CharField(
        max_length=50,
    )

    description = models.CharField(
        max_length=255,
    )

    published = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.title

class Question(models.Model):
    metaDataId = models.ForeignKey(
        'quiz.MetaData',
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=50,
    )
    
    description = models.CharField(
        max_length=255,
    )
    
    mandatory = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.title

class Answer(models.Model):
    questionId = models.ForeignKey(
        'quiz.Question',
        on_delete=models.CASCADE,
    )

    reply = models.CharField(
        max_length=255,
    )

    rightAnswer = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.reply

