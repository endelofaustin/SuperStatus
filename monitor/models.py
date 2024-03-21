from django.db import models

class URLStatus(models.Model):
    url = models.URLField(unique=True)
    status = models.BooleanField(default=False)  # True for Up, False for Down
    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.url} - {'Up' if self.status else 'Down'}"

