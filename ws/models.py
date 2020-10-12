import uuid

from django.contrib.auth.models import User
from django.db import models


class Session(models.Model):
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1_session", null=True, blank=True)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2_session", null=True, blank=True)

    def __str__(self):
        return f"Session({self.session_id}) {self.user1} vs {self.user2}"
