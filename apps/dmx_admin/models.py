from django.db import models


class MfiSsaRmlException(models.Model):
    universe_date = models.DateField(blank=True, null=True, verbose_name='Universe Date')
    source = models.CharField(max_length=6, blank=True, null=True, verbose_name='Source')
    bond_id = models.CharField(max_length=20, blank=True, null=True, verbose_name='Bond ID')
    mds_uid = models.CharField(max_length=30, blank=True, null=True, verbose_name='MDS UID')
    error_descr = models.CharField(max_length=400, blank=True, null=True, verbose_name='Error Description')
    tstp = models.DateTimeField(blank=True, null=True, verbose_name='Timestamp')
    error_code = models.IntegerField(blank=True, null=True, verbose_name='Error Code')

    @classmethod
    def get_verbose_field_names(cls):
        return [field.verbose_name for field in cls._meta.fields if field.verbose_name not in {'ID', 'Error Code'}]

    @classmethod
    def get_field_names(cls):
        return [field.name for field in cls._meta.fields if field.verbose_name not in {'ID', 'Error Code'}]