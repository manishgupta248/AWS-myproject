from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Notice(models.Model):
    subject = models.CharField(verbose_name= _("Notice Subject"), max_length=50, default="")
    notice_date = models.DateField(verbose_name= _("Notice Date"), auto_now=False, auto_now_add=False)
    upload_on = models.DateTimeField(verbose_name= _("Notice Upload Date"), auto_now_add=True)
    notice_copy = models.FileField(verbose_name= _("Notice Copy"), upload_to='Notices/', max_length=100,)
    upload_by = models.ForeignKey(get_user_model(), verbose_name=_("Uploaded By"), on_delete=models.CASCADE,)

    def __str__(self):
        return self.subject[0:20]
    
    def get_absolute_url(self):
        return reverse("notice", args=[str(self.id)])
    
    def path(self):
        return self.url
    class Meta:
        ordering = ['-notice_date']
    