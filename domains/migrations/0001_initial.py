# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('expire', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(related_name='user_domain', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('full_domain', models.CharField(max_length=200, blank=True)),
                ('name', models.CharField(validators=[django.core.validators.RegexValidator(regex='^[a-z\\d]+([-_][a-z\\d]+)*$', message='subdomain must be valid')], max_length=100, blank=True)),
                ('record_type', models.CharField(max_length=10, choices=[('A', 'A'), ('CNAME', 'CNAME'), ('MX', 'MX'), ('TXT', 'TXT'), ('ALIAS', 'ALIAS'), ('SPF', 'SPF'), ('URL', 'URL'), ('SRV', 'SRV'), ('NAPTR', 'NAPTR'), ('PTR', 'PTR'), ('AAAA', 'AAAA'), ('SSHFP', 'SSHFP'), ('HINFO', 'POOL')])),
                ('content', models.CharField(max_length=500)),
                ('ttl', models.IntegerField(blank=True, choices=[(60, '一分鐘'), (600, '十分鐘'), (3600, '一小時'), (7200, '兩小時'), (14400, '四小時'), (28800, '八小時'), (43200, '十二小時'), (86400, '一天'), (259200, '三天')], default=3600)),
                ('priority', models.IntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('record_id', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SubDomain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('domain', models.ForeignKey(related_name='domain_subdomain', to='domains.Domain')),
                ('owner', models.ForeignKey(related_name='user_subdomain', to=settings.AUTH_USER_MODEL)),
                ('share', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='subdomain',
            field=models.ForeignKey(related_name='subdomain_record', to='domains.SubDomain'),
        ),
    ]
