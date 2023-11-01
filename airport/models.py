from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=255)
    closest_big_city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.closest_big_city}"


class Route(models.Model):
    source = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="sources"
    )
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="destinations"
    )
    distance = models.IntegerField()

    def __str__(self):
        return f"From {self.source} to {self.destination}"
