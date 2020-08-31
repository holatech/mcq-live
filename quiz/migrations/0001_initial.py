# Generated by Django 3.0.5 on 2020-08-30 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, null=True)),
                ('a', models.CharField(max_length=100, null=True)),
                ('b', models.CharField(max_length=100, null=True)),
                ('c', models.CharField(max_length=100, null=True)),
                ('d', models.CharField(max_length=100, null=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Answer')),
            ],
        ),
    ]