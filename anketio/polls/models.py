from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def get_total_votes(self):
        return sum(choice.votes for choice in self.choice_set.all())

    def __str__(self):
        return self.question_text

    # Toplam oy sayısını veren yardımcı fonksiyon
    def get_total_votes(self):
        return sum(choice.votes for choice in self.choice_set.all())

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    def get_percent(self):
        total = self.question.get_total_votes()
        if total == 0:
            return 0
        return round((self.votes / total) * 100, 1)

    
    # Bu seçeneğin yüzdesini hesaplayan fonksiyon
    def get_percentage(self):
        total = self.question.get_total_votes()
        if total == 0:
            return 0
        return round((self.votes / total) * 100, 1)