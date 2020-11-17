from django.http import request
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from . import models, serializers, forms
from .serializers import Footer

# Create your views here.


# def DoseNotExist(func):
#     def wrap(request):
#         try:
#             return func(request)
#         except:
#             return HttpResponse("<h1>Page Not Found 404</h2>")
#     return wrap


def index(request):
    serializeData = serializers.IndexSerializer()
    return render(request, "index.html", serializeData.data())


def blogApi(request):
    serializeData = serializers.BlogApiSerializer()
    return JsonResponse({"data": serializeData.data()}, safe=False)


def bannerApi(request):
    serializeData = serializers.BannerApiSerializer()
    return JsonResponse({"data": serializeData.data()}, safe=False)


def clientApi(request):
    serializeData = serializers.ClientSerializer()
    return JsonResponse(serializeData.data(), safe=False)


def destination(request):
    serializerData = serializers.DestinationSerializer()
    return render(request, "destination.html", {"data": serializerData.data(), "footer": Footer()})


def city(request, cityId):
    serializerData = serializers.DestinationSerializer()
    return render(request, "city.html", serializerData.allCity(cityId))


def serviceTourPackage(request):
    serializerData = serializers.ServiceTourPackageSerializer()
    return render(request, "service.html", serializerData.data())


def serviceElementaryService(request):
    serializerData = serializers.ServiceElementaryServiceSerializer()
    return render(request, "service.html", serializerData.data())


def mice(request):
    serializerData = serializers.MiceSerializer()
    return render(request, "mice.html", serializerData.data())


def toursByInterest(request):
    serializerData = serializers.ToursByInterestSerializer()
    return render(request, "tourbyinterest.html", serializerData.data())


def packages(request, interestId):
    serializerData = serializers.PackagesSerializer()
    return render(request, "package.html", serializerData.data(interestId))


def packageItem(request, packageId):
    serializerData = serializers.PackageItemSerializer()
    return render(request, "packageItem.html", serializerData.data(packageId))


def toursByRegion(request):
    serializerData = serializers.ToursByRegionSerializer()
    return render(request, "region.html", serializerData.data())


def allRegion(request, regionId):
    serializerData = serializers.AllRegionSerializer()
    return render(request, "regionedetails.html", serializerData.data(regionId))


def news(request):
    serializerData = serializers.NewsSerializer()
    return render(request, "news.html", serializerData.data())


def gallary(request):
    serializerData = serializers.GallerySerializer()
    return render(request, "gallary.html", serializerData.data())


def guest(request):
    if request.method == "POST":
        form = forms.guestForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request, "guest.html", {"msg": "Success", "footer": Footer()})
        else:
            return render(request, "guest.html", {"msg": "Failed", "footer": Footer()})
    return render(request, "guest.html", {"footer": Footer()})


def contectUs(request):
    if request.method == "POST":
        form = forms.contactForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request, "contect.html", {"msg": "Success", "footer": Footer()})
        else:
            return render(request, "contect.html", {"msg": "Failed", "footer": Footer()})
    return render(request, "contect.html", {"footer": Footer()})


def about(request):
    serializerData = serializers.AboutSerializer()
    return render(request, "about.html", serializerData.data())


def management(request):
    serializerData = serializers.Management()
    return render(request, "management.html", serializerData.data())


def hotel(request):
    serializerData = serializers.HotelSerializer()
    return render(request, "hotel.html", serializerData.data())


def hotelList(request, countryId, cityId):
    serializerData = serializers.HotelListSerializer()
    return render(request, "hotelDetails.html", serializerData.data(countryId, cityId))


def enquiry(request):
    if request.method == "POST":
        form = forms.enquiryForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request, "enquiry.html", {"msg": "Success", "footer": Footer()})
        else:
            return render(request, "enquiry.html", {"msg": "Failed", "footer": Footer()})
    return render(request, "enquiry.html", {"footer": Footer()})
