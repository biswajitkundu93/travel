from django.db import models
from django.utils.html import mark_safe

# Create your models here.


class Intro(models.Model):
    description = models.TextField()

    def __str__(self):
        return "Introduction"

    class Meta:
        db_table = verbose_name_plural = "Introduction"


class TourByRegion (models.Model):
    region = models.CharField(max_length=255)
    image = models.ImageField(
        blank=False, upload_to="image/TourByRegion/", null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.region

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    class Meta:
        db_table = "TourByRegion"
        verbose_name_plural = "Tour By Region"


class TourByInterest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(
        blank=False, upload_to="image/TourByInterest", null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    class Meta:
        db_table = "TourByInterest"
        verbose_name_plural = "Tour By Interest"


class Destination(models.Model):
    country_Name = models.CharField(max_length=255)
    city_Name = models.CharField(max_length=255)
    region = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.country_Name

    class Meta:
        db_table =verbose_name_plural = "Destination"


class DestinationAboutCity(models.Model):
    city = models.CharField(max_length=255)
    about = models.TextField()
    image = models.ImageField(
        blank=False, upload_to="image/DestinationAboutCity/", null=True)

    def __str__(self):
        return self.city

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    class Meta:
        db_table = "AboutCity"
        verbose_name_plural = "Destination About City"


class DestinationAboutCityAttraction(models.Model):
    city = models.CharField(max_length=255)
    name_place = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(
        blank=True, upload_to="image/DestinationAboutCityAttraction/", null=True)

    def __str__(self):
        return self.name_place

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    class Meta:
        db_table = "CityAttraction"
        verbose_name_plural = "Destination About City Attraction"


class DestinationAboutCountry(models.Model):
    country = models.CharField(max_length=255)
    about = models.TextField()
    image = models.ImageField(blank=True, upload_to="image/country", null=True)

    def __str__(self):
        return self.country

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    class Meta:
        db_table = "AboutCountry"
        verbose_name_plural = "Destination About Country "


class AboutSite(models.Model):
    about = models.TextField()

    def __str__(self):
        return "About Website"

    class Meta:
        db_table = "AboutSite"


class HomeBlog(models.Model):
    image = models.ImageField(
        blank=False, upload_to="image/HomeBlog/", null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    class Meta:
        db_table = "HomeBlog"


class HomeBanner(models.Model):
    image = models.ImageField(
        blank=False, upload_to="image/HomeBanner/", null=True)
    name_of_image = models.CharField(max_length=255)

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    def __str__(self):
        return self.name_of_image

    class Meta:
        db_table = "HomeBanner"
        verbose_name_plural = "Home Banner"


class Awards(models.Model):
    image = models.ImageField(blank=False, upload_to="image/awerd/", null=True)
    title = models.CharField(max_length=255)

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    def __str__(self):
        return self.title

    class Meta:
        db_table= "Awerd"
        verbose_name_plural  = "Awards"

class NewOffers(models.Model):
    package_name = models.CharField(max_length=255)

    def __str__(self):
        return self.package_name

    class Meta:
        db_table = "NewOffers"
        verbose_name_plural = "New Offers"


class News(models.Model):
    image = models.ImageField(blank=False, upload_to="image/news/", null=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    class Meta:
        db_table =  "New"
        verbose_name_plural = "News"


class ServiceTourPackage(models.Model):
    service = models.TextField()

    def __str__(self):
        return "service"

    class Meta:
        db_table = "ServiceTourPackage"
        verbose_name_plural = "Service Tour Package"

class ServiceElementaryServices(models.Model):
    service = models.TextField()

    def __str__(self):
        return "service"

    class Meta:
        db_table = "ServiceElementaryServices"
        verbose_name_plural = "Service Elementary Services"


class Mice(models.Model):
    image = models.ImageField(blank=False, upload_to="image/mice/", null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    def __str__(self):
        return self.title

    class Meta:
        db_table= "Mice"
        verbose_name_plural ="TakeMyTrip - Happenings"


class Allpackages(models.Model):
    image = models.ImageField(
        blank=True, upload_to="image/allpackages/", null=True)
    packages_name = models.CharField(max_length=255)
    interest_name = models.CharField(max_length=255, blank=False)
    region = models.CharField(max_length=255, null=True)
    day = models.IntegerField()
    night = models.IntegerField()
    route = models.TextField()

    def __str__(self):
        return self.packages_name

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    class Meta:
        db_table = 'Allpackages'
        verbose_name_plural = "All packages"

class ALLPackageDetails(models.Model):
    day_number = models.IntegerField()
    title = models.CharField(max_length=255, null=True)
    packages_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.packages_name

    class Meta:
        db_table = "PackageDetails"
        verbose_name_plural = "All Package Details"


class Gallery(models.Model):
    image = models.ImageField(
        blank=True, upload_to="image/gallary/", null=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    class Meta:
        db_table= "Gallary"
        verbose_name_plural = "Gallery"

class Guest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table=verbose_name_plural = "Guest Review"


class contectUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=False, null=True)
    number = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table= "Contect Us"
        verbose_name_plural = "Contact Us"

class HotelList(models.Model):
    city = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    star = models.IntegerField()
    adress = models.TextField()
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to="image/hotels/", null=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')

    class Meta:
        db_table = "HotelList"
        verbose_name_plural = "Hotel List"


class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contect = models.IntegerField()
    country = models.CharField(max_length=255)
    arrivalDate = models.DateField()
    departureDate = models.DateField()
    adult = models.IntegerField()
    child = models.IntegerField()
    accomodation = models.CharField(max_length=255)
    remark = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table =verbose_name_plural = "Enquiry"


class Management(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to="image/Management/", null=True)
    
    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" width="150" height="100" />')
    class Meta:
        db_table = "Management"
        verbose_name_plural = "Management"