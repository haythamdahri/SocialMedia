# Generated by Django 2.0.4 on 2018-05-06 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20180507_0038'),
        ('SocialMedia', '0010_responseconversation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=300)),
                ('date_creation', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil')),
            ],
        ),
    ]
