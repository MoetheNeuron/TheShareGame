# Generated by Django 3.0.4 on 2020-03-07 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fonds', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FondThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('slug', models.SlugField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('locked', models.BooleanField(default=False)),
                ('pinned', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'fond_thread',
            },
        ),
        migrations.CreateModel(
            name='InvestmentFond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('slug', models.SlugField()),
                ('day_time', models.DateTimeField(auto_now_add=True)),
                ('founder', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fond',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader', models.BooleanField(default=False)),
                ('fond', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fonds.InvestmentFond')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fond_member',
            },
        ),
        migrations.CreateModel(
            name='FondThreadPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fonds.FondThread')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fond_thread_post',
            },
        ),
        migrations.AddField(
            model_name='fondthread',
            name='fond',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fonds.InvestmentFond'),
        ),
        migrations.AddField(
            model_name='fondthread',
            name='read_by',
            field=models.ManyToManyField(related_name='read_fond_threads', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fondthread',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FondProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='Description of the Fond')),
                ('open_for_application', models.BooleanField(default=True)),
                ('fond', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fonds.InvestmentFond')),
            ],
            options={
                'db_table': 'fond_profile',
            },
        ),
        migrations.CreateModel(
            name='FondNotification',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Notification')),
                ('fond', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fonds.InvestmentFond')),
            ],
            options={
                'db_table': 'fond_notification',
            },
            bases=('users.notification',),
        ),
        migrations.CreateModel(
            name='FondLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, null=True, upload_to='logo/fond')),
                ('production_ready', models.BooleanField(default=False)),
                ('fond', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fonds.InvestmentFond')),
            ],
            options={
                'db_table': 'fond_logo',
            },
        ),
        migrations.CreateModel(
            name='FondComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Comment')),
                ('fond', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fonds.InvestmentFond')),
            ],
            options={
                'db_table': 'fond_comment',
            },
            bases=('users.comment',),
        ),
        migrations.CreateModel(
            name='FondChatRoom',
            fields=[
                ('chatroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.ChatRoom')),
                ('fond', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fonds.InvestmentFond')),
            ],
            options={
                'db_table': 'fond_chat_room',
            },
            bases=('users.chatroom',),
        ),
        migrations.CreateModel(
            name='FondArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Article')),
                ('fond', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fonds.InvestmentFond')),
            ],
            options={
                'db_table': 'fond_article',
            },
            bases=('users.article',),
        ),
        migrations.AddField(
            model_name='fondapplication',
            name='fond',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fonds.InvestmentFond'),
        ),
        migrations.AddField(
            model_name='fondapplication',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_time', models.DateTimeField(auto_now_add=True)),
                ('fond', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fonds.InvestmentFond')),
                ('invited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fonds.Member')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fond_invitation',
                'unique_together': {('user', 'fond')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='fondapplication',
            unique_together={('fond', 'user')},
        ),
    ]