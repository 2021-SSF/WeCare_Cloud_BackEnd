from django.db import models


# Create your models here.


class Hospital(models.Model):
    location = models.CharField(max_length=300)
    number = models.CharField(max_length=100)


class Adminster(models.Model):
    hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)


class Room(models.Model):
    hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    room_loc = models.CharField(max_length=300)


class Bed(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    # camera_id
