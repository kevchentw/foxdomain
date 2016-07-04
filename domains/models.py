from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

Record_Type = (
    ('A', 'A'),
    ('CNAME', 'CNAME'),
    ('MX', 'MX'),
    ('TXT', 'TXT'),
    ('ALIAS', 'ALIAS'),
    ('SPF', 'SPF'),
    ('URL', 'URL'),
    ('SRV', 'SRV'),
    ('NAPTR', 'NAPTR'),
    ('PTR', 'PTR'),
    ('AAAA', 'AAAA'),
    ('SSHFP', 'SSHFP'),
    ('HINFO', 'POOL'),
)

TTL_TYPE = (
    (60, '一分鐘'),
    (600, '十分鐘'),
    (3600, '一小時'),
    (7200, '兩小時'),
    (14400, '四小時'),
    (28800, '八小時'),
    (43200, '十二小時'),
    (86400, '一天'),
    (259200, '三天'),
)


class Domain(models.Model):
    name = models.CharField(max_length=200)
    expire = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SubDomain(models.Model):
    domain = models.ForeignKey(Domain, related_name="domain_subdomain")
    owner = models.ForeignKey(User, related_name="user_subdomain")
    share = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Record(models.Model):
    subdomain = models.ForeignKey(SubDomain, related_name="subdomain_record")
    full_domain = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=100, blank=True, validators=[RegexValidator(regex="^[a-z\d]+([-_][a-z\d]+)*$", message="subdomain must be valid")])
    record_type = models.CharField(max_length=10, choices=Record_Type)
    content = models.CharField(max_length=500)
    ttl = models.IntegerField(blank=True, default=3600, choices=TTL_TYPE)
    priority = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    record_id = models.IntegerField(default=0, blank=True)
