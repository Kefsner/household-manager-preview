from core.models import LogSystem

class Logger:
    def log(self, exception, request, data=None, traceback=None):
        LogSystem.objects.create(
            exception=exception,
            request=request,
            data=request.POST,
            traceback=traceback
        )