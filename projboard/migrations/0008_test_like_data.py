# Generated by Django 4.1.3 on 2022-11-23 11:48

from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('projboard', '0007_test_view_article_data'),
    ]

    def generate_like_data(apps, schema_editor):
        from projboard.models.article import Article, User, Like

        user1 = User.get_user_by_nickname("User1")
        user2 = User.get_user_by_nickname("User2")

        article1 = Article.get_article_by_user(user1)
        article2 = Article.get_article_by_user(user2)

        test_data = [
            (user1, article1),
            (user2, article2),
        ]

        with transaction.atomic():
            for user, article in test_data:
                Like(user_id=user, article_id=article).save()

    operations = [
        migrations.RunPython(generate_like_data),
    ]
