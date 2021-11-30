from django.db import models
import datetime as dt


class Editor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    @classmethod
    def get_editors(cls):
        editors = cls.objects.all()
        return editors

    def save_e(self):
        self.save()

    def delete_e(self):
        self.delete()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = [
            'first_name'
        ]


class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=40)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    Tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articles/')

    @classmethod
    def today_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date=today)
        return news

    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_date__date=date)
        return news

    @classmethod
    def search_by_title(cls, search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
