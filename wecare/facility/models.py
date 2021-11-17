from django.db import models


# Create your models here.

class Room(models.Model):
    objects = models.Manager()

    room_loc = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id)


class Bed(models.Model):
    objects = models.Manager()

    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Elder(models.Model):
    objects = models.Manager()

    GENDER_CHOICES = (
        ('여자', '여'),
        ('남자', '남'),
    )

    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_id = models.ForeignKey(Bed, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    sickness = models.TextField(max_length=300)
    recent_problem = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class ElderStatus(models.Model):
    objects = models.Manager()

    elder_id = models.ForeignKey(Elder, on_delete=models.CASCADE)
    time = models.DateTimeField()
    lay = models.IntegerField()
    sit = models.IntegerField()
    empty = models.IntegerField()
    recent_status = models.CharField(max_length=10)
    today_status = models.CharField(max_length=10)
    max_status = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)


class Violence(models.Model):
    objects = models.Manager()

    bed_id = models.ForeignKey(Bed, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class OccupancyGraph(models.Model):
    objects = models.Manager()

    elder_id = models.ForeignKey(Elder, on_delete=models.CASCADE)
    image = models.CharField(max_length=500)

    def __str__(self):
        return str(self.id)
