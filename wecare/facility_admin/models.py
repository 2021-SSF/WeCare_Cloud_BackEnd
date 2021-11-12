from django.db import models

# Create your models here.


class Facility(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.name # name 추가 해야 할듯..?!


class Adminster(models.Model):
    facility_id = models.ForeignKey(Facility, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

class Room(models.Model):
    facility_id = models.ForeignKey(Facility, on_delete=models.CASCADE)
    room_loc = models.CharField(max_length=300)

    def __str__(self):
        return self.room_loc # name 추가 해야 할듯..?!

class Bed(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    # camera_id

    def __str__(self):
        return str(self.id)