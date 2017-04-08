from django.db import models
from django.utils.timezone import now

class Member(models.Model):
    employee_id = models.DecimalField(max_digits=6, decimal_places=0, default=0) 
    level = models.DecimalField(max_digits=2, decimal_places=0, default=10) 
    department = models.CharField(max_length=256, default='')
    name = models.CharField(max_length=256, default='Hello World')
    ch_name = models.CharField(max_length=256, default='None')
    extension = models.DecimalField(max_digits=5, decimal_places=0, default=0) 
    group_name = models.CharField(max_length=256, default='NCTU')
    drawn = models.BooleanField(default=False)
    def __str__(self):
        return '%d, %s - %s (%s), ext=%d, pick=%r' % (self.employee_id, self.group_name, self.ch_name, self.name, self.extension, self.drawn)

class History(models.Model):
    member = models.ForeignKey(Member, related_name="draw_histories")
    time = models.DateTimeField(default=now)

    def __str__(self):
        return '%d, %s (%s), %s' % (self.member.employee_id, self.member.ch_name, self.member.name, self.time)
