# Generated by Django 4.2.13 on 2024-06-28 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('affiche', '0049_theater'),
    ]

    operations = [
        migrations.AddField(
            model_name='backstage',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backstageblock',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conductor',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='creatives',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainimages',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performanceconductor',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performancecreatives',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performancefiles',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performanceperformers',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performers',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='row',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seat',
            name='theater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affiche.theater'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='performance',
            name='image_carousel',
            field=models.ManyToManyField(blank=True, to='affiche.performancefiles'),
        ),
    ]
