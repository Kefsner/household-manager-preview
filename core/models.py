from django.db import models

class DB(models.Model):
    id = models.AutoField(primary_key=True)

class LogSystem(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    exception = models.CharField(max_length=255)
    request = models.TextField()
    traceback = models.TextField()

class MetaData(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    db = models.ForeignKey(DB, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True

    def save(self, request=None, *args, **kwargs):
        if self._state.adding and request:
            self.created_by = request.user
            self.db = request.user.db
        super().save(*args, **kwargs)