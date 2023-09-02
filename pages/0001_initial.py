# Generated by Django 3.0.7 on 2021-04-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

        initial = True

            dependencies = [
                        ]

                operations = [
                                migrations.CreateModel(
                                                name='Teams',
                                                            fields=[
                                                                                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                                                                                                ('first_name', models.CharField(max_length=255)),
                                                                                                                ('last_name', models.CharField(max_length=255)),
                                                                                                                                ('desigantion', models.CharField(max_length=255)),
                                                                                                                                                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                                                                                                                                                                ('twitter_link', models.URLField(max_length=255)),
                                                                                                                                                                                ('github_link', models.URLField(max_length=255)),
                                                                                                                                                                                                ('created_data', models.DateTimeField(auto_now_add=True)),
                                                                                                                                                                                                            ],
                                                                    ),
                                    ]
