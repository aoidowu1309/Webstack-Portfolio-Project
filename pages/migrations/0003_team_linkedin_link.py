# Generated by Django 3.0.7 on 2023-09-02 21:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

        dependencies = [
                        ('pages', '0002_auto_20210426_2008'),
                            ]

            operations = [
                            migrations.AddField(
                                            model_name='team',
                                                        name='linkedin_link',
                                                                    field=models.URLField(default=django.utils.timezone.now, max_length=255),
                                                                                preserve_default=False,
                                                                                        ),
                                ]
