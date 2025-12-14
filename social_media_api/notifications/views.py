from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Notification
from .serializers import NotificationSerializer


class NotificationListView(ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(
            recipient=self.request.user
        )

from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

if target_user != request.user:
    Notification.objects.create(
        recipient=target_user,
        actor=request.user,
        verb='started following you'
    )


from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

comment = serializer.save(author=self.request.user)

if comment.post.author != self.request.user:
    Notification.objects.create(
        recipient=comment.post.author,
        actor=self.request.user,
        verb='commented on your post',
        content_type=ContentType.objects.get_for_model(comment.post),
        object_id=comment.post.id,
    )
