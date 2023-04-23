from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        ("NEW", "New"),
        ("IN_PROCESS", "In Process"),
        ("COMPLETED", "Completed"),
    ]
    
    name = models.CharField(max_length=200)
    status = models.CharField(
        choices = STATUS_CHOICES,
        max_length = 15,
        default = "NEW",
    )
    
    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"
        