# Generated by Django 4.2.3 on 2023-08-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("author", models.CharField(max_length=100)),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-pub_date"],},
        ),
        migrations.AlterModelOptions(name="event", options={"ordering": ["-time"]},),
    ]
