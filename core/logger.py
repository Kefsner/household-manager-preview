from core.models import LogSystem

class Logger:
    def log(self, exception, request, traceback):
        LogSystem.objects.create(
            exception=exception,
            request=request,
            traceback=traceback
        )