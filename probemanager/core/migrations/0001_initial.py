# Generated by Django 2.0.3 on 2018-03-22 12:06

import core.modelsmixins
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_beat', '0006_auto_20180210_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True)),
                ('value', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('probe', models.CharField(max_length=255, verbose_name='Probe / URL')),
                ('status', models.CharField(choices=[('In progress', 'In progress'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Error', 'Error')], max_length=255)),
                ('result', models.TextField(default=None, editable=False, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(core.modelsmixins.CommonMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OsSupported',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            bases=(core.modelsmixins.CommonMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Probe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, unique=True)),
                ('description', models.CharField(blank=True, default='', max_length=400)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('rules_updated_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('type', models.CharField(blank=True, default='', editable=False, max_length=400)),
                ('subtype', models.CharField(blank=True, editable=False, max_length=400, null=True)),
                ('secure_deployment', models.BooleanField(default=True)),
                ('scheduled_rules_deployment_enabled', models.BooleanField(default=False)),
                ('scheduled_check_enabled', models.BooleanField(default=True)),
                ('installed', models.BooleanField(default=False, verbose_name='Probe Already installed ?')),
                ('scheduled_check_crontab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crontabschedule_check', to='django_celery_beat.CrontabSchedule')),
                ('scheduled_rules_deployment_crontab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crontabschedule_rules', to='django_celery_beat.CrontabSchedule')),
            ],
            bases=(core.modelsmixins.CommonMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProbeConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            bases=(core.modelsmixins.CommonMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=400, unique=True)),
                ('host', models.CharField(default='localhost', max_length=400, unique=True)),
                ('remote_user', models.CharField(blank=True, default='admin', max_length=400)),
                ('remote_port', models.IntegerField(blank=True, default=22)),
                ('become', models.BooleanField(default=False)),
                ('become_method', models.CharField(blank=True, default='sudo', max_length=400)),
                ('become_user', models.CharField(blank=True, default='root', max_length=400)),
                ('become_pass', models.CharField(blank=True, max_length=400, null=True)),
                ('os', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.OsSupported')),
            ],
            bases=(core.modelsmixins.CommonMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SshKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, unique=True)),
                ('file', models.FileField(upload_to='ssh_keys/')),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='ssh_private_key_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SshKey'),
        ),
        migrations.AddField(
            model_name='probe',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Server'),
        ),
    ]
