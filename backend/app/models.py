import uuid

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class AIAnalyse(models.Model):
    MONTHS = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]


    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        blank=False,
        null=False
    )

    estimated_price = models.PositiveIntegerField(
        blank=False,
        null=False
    )

    analyse = models.TextField(
        blank=False,
        null=False
    )

    evaluated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.estimated_price}"


    def format_price(self):
        """
            Custom method for formating the price "500 | 1,000 | 18,500 | 100,545 | 1,800,945"
        """

        return f"{self.estimated_price:,}"


    def format_date(self):
        """
            Custom method for formating the date "11 June, 2025"
        """

        raw_date = str(self.evaluated_at).split(" ") # ["2025-06-11", "15:42:00"]
        date = raw_date[0].split("-") # ["2025", "06", "11"]
        formated_date = f"{date[2]} {self.MONTHS[int(date[1]) - 1]}, {date[0]}" # "11 June, 2025"

        return formated_date


class CarImage(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        blank=False,
        null=False
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="car_images"
    )

    analysis = models.ForeignKey(
        AIAnalyse,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="car_images/"
    )


    def __str__(self):
        return f"{self.id}"