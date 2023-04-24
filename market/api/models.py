import uuid
from django.db import models


class Order(models.Model):
    NEW = 'new'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    status = models.CharField(
        choices = STATUS_CHOICES,
        max_length = 15,
        default = NEW,
    )
    
    def __str__(self):
        return f"{self.name} ({self.get_status_display()}) #{self.id}"
