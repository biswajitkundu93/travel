from TravelingSite.settings import SECRET_KEY
from os import link
from django.contrib import admin
from . import models
from django.contrib.auth.models import Group


# Register your models here.
img_tag = "image_tag"
dec = "description"
img = "image"


class TourByRegionAdmin(admin.ModelAdmin):
    list_display = (img_tag, "region", dec, img)
    search_fields = ("region", dec)
    list_editable = (img,)
    list_filter = ("region",)
    list_display_links = ("region", dec, img_tag)


class TourByInterestAdmin(admin.ModelAdmin):
    list_display = (img_tag, "title", dec, img)
    list_display_links = (dec, img_tag)


class DestinationAdmin(admin.ModelAdmin):
    list_display = list_display_links = list_filter = (
        "country_Name", "city_Name", "region")
    search_fields = ("country_Name", "city_Name", "region")


class DestinationAboutCityAdmin(admin.ModelAdmin):
    list_display = list_display_links = (img_tag, "city", "about", img)
    search_fields = ("city", "about")


class DestinationAboutCountryAdmin(admin.ModelAdmin):
    list_display = list_display_links = (img_tag, "country", "about", img)
    search_fields = ("country", "about")


class DestinationAboutCityAttractionAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        img_tag, "city", "name_place", dec, img)

    search_fields = ("city", "name_place", dec)

    list_filter = ("city", "name_place")


class NewsAdmin(admin.ModelAdmin):
    list_display = list_display_links = (img_tag, "title", img)
    search_fields = ("title",)


class HomeBlogAdmin(admin.ModelAdmin):
    list_display = list_display_links = (img_tag, "title", dec, img,)
    search_fields = ("title", dec,)


class HomeBannerAdmin(admin.ModelAdmin):
    list_display = list_display_links = (img_tag, "name_of_image", img)
    search_fields = ("name_of_image",)


class AwardsAdmin(admin.ModelAdmin):
    list_display = list_display_links = (img_tag, "title", img)
    search_fields = ("title",)

# class NewOffersAdmin(admin.ModelAdmin):


class ServiceTourPackageAdmin(admin.ModelAdmin):
    list_display = search_fields = list_display_links = ("service",)


class ServiceElementaryServicesAdmin(admin.ModelAdmin):
    list_display = search_fields = list_display_links = ("service",)


class MiceAdmin(admin.ModelAdmin):
    list_display = list_display_links = (img_tag, "title", dec, img)
    search_fields = ("title", dec,)


class GalleryAdmin(admin.ModelAdmin):
    list_display = list_display_links = (img_tag, "title", img)


class GuestAdmin(admin.ModelAdmin):
    list_display = list_display_links = search_fields = ("name", "email", dec)


class contectUsAdmin(admin.ModelAdmin):
    list_display = list_display_links = search_fields = (
        "name", "email", "number", "comment")


class HotelListAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        img_tag, "city", "name", "star", "adress", dec, img)
    list_filter = ("city",)
    search_fields = ("city", "name", "star", "adress", dec,)


class AllpackagesAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        img_tag, "packages_name", "interest_name", "region", "day", "night", "route", img)
    list_filter = ("interest_name",)
    search_fields = ("packages_name", "interest_name",
                     "region", "day", "night", "route",)


class ALLPackageDetailsAdmin(admin.ModelAdmin):
    list_display = list_display_links = search_fields = (
        "title", "packages_name", "day_number", dec)


class EnquiryAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        "name", "email", "contect", "country", "arrivalDate", "departureDate", "adult", "child", "accomodation", "remark")


admin.site.unregister(Group)

admin.site.site_header = "Admin"
admin.site.site_title = "Admin"
admin.site.index_title = "Travel"

admin.site.register(models.Intro)
admin.site.register(models.TourByRegion, TourByRegionAdmin)
admin.site.register(models.TourByInterest, TourByInterestAdmin)
admin.site.register(models.Destination, DestinationAdmin)
admin.site.register(models.DestinationAboutCity, DestinationAboutCityAdmin)
admin.site.register(models.DestinationAboutCountry,
                    DestinationAboutCountryAdmin)
admin.site.register(models.DestinationAboutCityAttraction,
                    DestinationAboutCityAttractionAdmin)
admin.site.register(models.News, NewsAdmin)
admin.site.register(models.AboutSite)
admin.site.register(models.HomeBlog, HomeBlogAdmin)
admin.site.register(models.HomeBanner, HomeBannerAdmin)
admin.site.register(models.Awards, AwardsAdmin)
admin.site.register(models.NewOffers)
admin.site.register(models.ServiceTourPackage, ServiceTourPackageAdmin)
admin.site.register(models.ServiceElementaryServices,
                    ServiceElementaryServicesAdmin)
admin.site.register(models.Mice, MiceAdmin)
admin.site.register(models.Gallery, GalleryAdmin)
admin.site.register(models.Guest, GuestAdmin)
admin.site.register(models.contectUs, contectUsAdmin)
admin.site.register(models.HotelList, HotelListAdmin)
admin.site.register(models.Allpackages, AllpackagesAdmin)
admin.site.register(models.ALLPackageDetails, ALLPackageDetailsAdmin)
admin.site.register(models.Enquiry, EnquiryAdmin)
admin.site.register(models.Management)

