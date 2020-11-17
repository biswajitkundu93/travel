from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("api/blog", views.blogApi, name="blog"),
    path("api/bannar", views.bannerApi, name="bannar"),
    path("api/client", views.clientApi, name="clients"),
    path("destination", views.destination, name="destination"),
    path("destination/city/<int:cityId>", views.city, name="city"),
    path("service/tourpackage", views.serviceTourPackage, name="tourpackage"),
    path("service/elementaryservice",
         views.serviceElementaryService, name="elementaryservice"),
    path("service/mice", views.mice, name="mice"),
    path("tour/interest", views.toursByInterest, name="tourByinterest"),
    path("tour/region", views.toursByRegion, name="region"),
    path("packages/<int:interestId>", views.packages, name="interest"),
    path("package/items/<int:packageId>",
         views.packageItem, name="packageItem"),
    path("region/<int:regionId>", views.allRegion, name="allRegion"),
    path("news", views.news, name="news"),
    path("gallary", views.gallary, name="gallary"),
    path("guest", views.guest, name="guest"),
    path("contect", views.contectUs, name="contactUs"),
    path("about", views.about, name="about"),
    path("management", views.management, name="management"),
    path("hotel", views.hotel, name="hotel"),
    path("hoteldetails/<int:countryId>/<int:cityId>",
         views.hotelList, name="hotelDetails"),
    path("enquiry", views.enquiry, name="enquiey")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
