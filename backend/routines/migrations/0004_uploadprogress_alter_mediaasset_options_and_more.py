# Generated by Django 5.0.2 on 2025-05-21 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("routines", "0003_achievement_remove_breathingexercise_media_url_and_more"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadProgress",
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
                ("upload_id", models.UUIDField(unique=True)),
                ("file_name", models.CharField(max_length=255)),
                ("file_path", models.CharField(blank=True, max_length=512, null=True)),
                (
                    "asset_type",
                    models.CharField(
                        choices=[
                            ("image", "Image"),
                            ("video", "Video"),
                            ("audio", "Audio"),
                            ("animation", "Animation"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "total_size",
                    models.PositiveIntegerField(help_text="Total file size in bytes"),
                ),
                (
                    "uploaded_size",
                    models.PositiveIntegerField(
                        default=0, help_text="Uploaded bytes so far"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("uploading", "Uploading"),
                            ("verifying", "Verifying"),
                            ("completed", "Completed"),
                            ("failed", "Failed"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("error_message", models.TextField(blank=True, null=True)),
                (
                    "metadata",
                    models.JSONField(
                        default=dict, help_text="Additional upload metadata"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.AlterModelOptions(
            name="mediaasset",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="mediaasset",
            name="file_path",
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name="mediaasset",
            name="asset_type",
            field=models.CharField(
                choices=[
                    ("image", "Image"),
                    ("video", "Video"),
                    ("audio", "Audio"),
                    ("animation", "Animation"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="mediaasset",
            name="duration_seconds",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="mediaasset",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="mediaasset",
            name="thumbnail_url",
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name="mediaasset",
            name="url",
            field=models.URLField(max_length=1024),
        ),
        migrations.AddIndex(
            model_name="mediaasset",
            index=models.Index(
                fields=["asset_type"], name="routines_me_asset_t_198172_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="mediaasset",
            index=models.Index(
                fields=["instructor", "asset_type"],
                name="routines_me_instruc_308978_idx",
            ),
        ),
        migrations.AddField(
            model_name="uploadprogress",
            name="instructor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="upload_progress",
                to="users.userprofile",
            ),
        ),
        migrations.AddIndex(
            model_name="uploadprogress",
            index=models.Index(
                fields=["upload_id"], name="routines_up_upload__8dff74_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="uploadprogress",
            index=models.Index(fields=["status"], name="routines_up_status_d3d01a_idx"),
        ),
        migrations.AddIndex(
            model_name="uploadprogress",
            index=models.Index(
                fields=["instructor", "status"], name="routines_up_instruc_e59392_idx"
            ),
        ),
    ]
