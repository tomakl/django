from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from datetime import date, datetime


class Regulatory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, verbose_name="Nazwa")
    content = RichTextField(verbose_name="Treść regulaminu", )
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name="Utworzono")
    published_date = models.DateTimeField(
        blank=True, null=True, verbose_name="Opublikowno")

    class Meta:
        verbose_name = ("Regulamin")
        verbose_name_plural = ("Regulaminy")
        ordering = ('published_date',)

    def __str__(self):
        return "{} ({})".format(self.name, self.published_date)




class Competition(models.Model):
    STATUS_CHOICES = (
        (1, 'Aktywny'),
        (0, 'Nieaktywny'),
    )
    TYPE_CHOICES = (
    (1, 'Zawody sportowe'),
    (2, 'Inne wydarzenie'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nazwa zawodów")
    date = models.DateTimeField(default=timezone.now, verbose_name="Data rozpoczęcia")
    distance = models.IntegerField(verbose_name="Dystans")
    reg_name = models.ForeignKey('Regulatory', on_delete=models.CASCADE, verbose_name="Regulamin", blank=True, null=True)
    price = models.IntegerField(verbose_name="Cena", blank=True, null=True)
    image = models.ImageField(upload_to='events', blank='True', verbose_name="Zdjęcie")
    place = models.CharField(max_length=200, blank=True, null=True, verbose_name='Miejsce zawodów')
    info = models.TextField(verbose_name="Info", blank=True, null=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES)
    allowed = models.IntegerField(verbose_name='Limit', default='0')
    reported = models.IntegerField(verbose_name='Zgłoszonych', null=True, blank='True', default='0')



    class Meta:
        verbose_name = ("Zawody")
        verbose_name_plural = ("Zawody")
        ordering = ('-id',)

    def __str__(self):
        return "{} ({} km)".format(self.name, self.distance)


class Competitor(models.Model):
    GENDER_CHOICES = (
        (1, 'Mężczyzna'),
        (2, 'Kobieta'),
    )
    PAYMENT_CHOICES = (
        (0, 'BRAK'),
        (1, 'OK'),
    )
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200, verbose_name="Imię")
    lastname = models.CharField(max_length=200, verbose_name="Nazwisko")
    birth = models.DateField(verbose_name="Data urodzenia")
    gender = models.IntegerField(verbose_name='Płeć', blank=True, choices=GENDER_CHOICES, default=0)
    city = models.CharField(verbose_name='Miasto', max_length=200)
    club = models.CharField(max_length=200, verbose_name="Klub/Drużyna")
    email = models.EmailField(max_length=70, blank=True, verbose_name="Email")
    comp_name = models.ForeignKey('Competition', blank=True, null=True, on_delete=models.CASCADE, verbose_name="Zawody")
    payment = models.SmallIntegerField(choices= PAYMENT_CHOICES, default=0, verbose_name="Płatność")
    payment_date = models.DateTimeField(null=True, blank=True, verbose_name="Data płatności")
    start_number = models.IntegerField(verbose_name="Numer startowy", null=True, blank=True)

    class Meta:
        verbose_name = ("Zawodnik")
        verbose_name_plural = ("Zawodnicy")
        ordering = ['-id']

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)
        ordering = ('self.lastname')

    def age(self):
        today = date.today()
        age = today.year - self.birth.year - (
                (today.month, today.day) < (self.birth.month, self.birth.day))
        return "{} lat".format(age)
    age.short_description = 'Wiek'











# Create your models here.
