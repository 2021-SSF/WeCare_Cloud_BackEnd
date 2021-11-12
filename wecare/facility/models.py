from django.db import models

# Create your models here.
from facility_admin.models import Adminster, Bed, Room


class Nurse(models.Model):
    objects = models.Manager()

    admin_id = models.ForeignKey(Adminster, on_delete=models.CASCADE)  # admin model ?!
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Elders(models.Model):
    objects = models.Manager()

    GENDER_CHOICES = (
        ('여', '남'),
        ('남자', '여'),
    )

    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    nurse_id = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    bed_id = models.ForeignKey(Bed, on_delete=models.CASCADE)  # bed model ?!
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES)  # gender속성은 choices를 통해서 남,여 중에서 고를 수 있다. 추후 수정 할꺼면 하기
    note = models.TextField(max_length=300, blank=True, null=True)
    companion_num = models.CharField(max_length=50, blank=True)  # 대표 보호자 번호
    companion_relation = models.CharField(max_length=20, blank=True)  # 환자와의 관계

    def __str__(self):
        return self.name


class Diet(models.Model):
    objects = models.Manager()
    nurse_id = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    image = models.CharField(max_length=300)
    time = models.DateTimeField()

    def __str__(self):
        return self.time  # 추후 다른것으로 변경하는거 고려
