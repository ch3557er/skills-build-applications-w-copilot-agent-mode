# Generated by Django 4.1 on 2025-04-09 09:35

from django.db import migrations
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("octofit_tracker", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="team",
            name="members",
        ),
        migrations.AddField(
            model_name="team",
            name="members",
            field=djongo.models.fields.ArrayReferenceField(
                default=list,
                on_delete=django.db.models.deletion.CASCADE,
                to="octofit_tracker.user",
            ),
        ),
    ]
