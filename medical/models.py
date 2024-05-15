from django.db import models


FEMALE, MALE = ('ayol', 'erkak')
ORDINARY, DOCTOR = ('ordinary', 'doctor')


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Family(BaseModel, models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Oila'
        verbose_name_plural = 'Oilalar'


class Person(BaseModel, models.Model):
    GENDER_CHOICES = (
        (FEMALE, FEMALE),
        (MALE, MALE)
    )
    PERSON_ROLES = (
        (ORDINARY, ORDINARY),
        (DOCTOR, DOCTOR)
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=70)
    birth_of_date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=13, unique=True)
    image = models.ImageField(upload_to='person_images/', null=True, blank=True, default='default.jpg')
    profession = models.CharField(max_length=50)
    person_role = models.CharField(max_length=10, choices=PERSON_ROLES, default=ORDINARY)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='persons')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"

    class Meta:
        verbose_name = 'Odam'
        verbose_name_plural = 'Odamlar'


class Register(BaseModel, models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name} registered"

    class Meta:
        verbose_name = "Ro'yxat"
        verbose_name_plural = "Ro'yxatlar"
