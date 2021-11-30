from django.test import TestCase
import datetime as dt
from .models import Editor, Articles, Tags


class EditorTestClass(TestCase):
    def setUp(self):
        self.charles = Editor(id=1, first_name='charles', last_name='mikey', email='info@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.charles, Editor))

    def test_verbose_name_plural(self):
        self.assertEqual(str(Editor._meta.verbose_name_plural), 'editors')

    def test_save_method(self):
        self.charles.save_e()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_get_editors(self):
        editors = Editor.get_editors()
        self.assertTrue(len(editors) == 1)

    def test_delete_method(self):
        self.charles.delete_e()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) < 1)


class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.charles = Editor(first_name='charles', last_name='mikey', email='mikey@gmail.com')
        self.charles.save_e()

        # Creating a new tag and saving it
        self.new_tag = Tags(name='testing')
        self.new_tag.save()

        self.new_article = Articles(title='Test Article', post='This is a random test Post', editor=self.charles)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Articles.objects.all().delete()

    def test_get_news_today(self):
        today_news = Articles.today_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2019-09-30'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Articles.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
