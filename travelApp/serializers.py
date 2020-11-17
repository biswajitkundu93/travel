from django.http import request
from . import models
import json


def Footer():
    interest = models.TourByInterest.objects.all()
    interestTitleList = [{"name": i.title, "id": i.id} for i in interest]
    region = models.TourByRegion.objects.all()
    regionTitleList = [{"name": i.region, "id": i.id} for i in region]
    data_set = {
        "interestTitleList": interestTitleList,
        "regionTitleList": regionTitleList

    }
    return data_set


class DestinationSerializer:
    def __init__(self, *args, **kwargs):
        self.data_set = []

    def data(self):
        destination = models.DestinationAboutCountry.objects.all()
        for item in destination:
            temp = models.Destination.objects.filter(country_Name=item.country)
            city = [{"id": i.id, "cityName": i.city_Name} for i in temp]
            temp_data = {
                "name": item.country,
                "description": item.about,
                "city": city
            }
            self.data_set.append(temp_data)
        return self.data_set

    def allCity(self, cityId):
        destination = models.Destination.objects.get(id=cityId)
        about = models.DestinationAboutCity.objects.get(
            city=destination.city_Name)
        attraction = models.DestinationAboutCityAttraction.objects.filter(
            city=destination.city_Name)

        temp = models.Destination.objects.filter(
            country_Name=destination.country_Name)
        city = [{"id": i.id, "cityName": i.city_Name} for i in temp]

        data = {
            "name": destination.city_Name,
            "about": about.about,
            "image": about.image,
            "attraction": attraction,
            "country": destination.country_Name,
            "cities": city,
            "footer": Footer()
        }

        return data


class IndexSerializer:
    def __init__(self):
        self.data_set = {}

    def data(self):
        intro = models.Intro.objects.all()
        intro = intro[0]
        award = models.Awards.objects.all()
        if len(award) > 3:
            hotels = award[:3]
        offers = models.NewOffers.objects.all()
        new_offer = [models.Allpackages.objects.get(
            packages_name=i.package_name) for i in offers]
        gallery = models.Gallery.objects.all()
        interest = models.TourByInterest.objects.all()
        interest = [
            {
                "id": i.id,
                "title": i.title,
                "image": i.image,
                "description": i.description[:100]
            } for i in interest
        ]
        if len(interest) > 6:
            hotels = interest[:6]
        news = models.News.objects.all()
        if len(news) > 3:
            hotels = news[:3]
        hotels = models.HotelList.objects.all()
        hotels = [
            {
                "id": i.id,
                "city": i.city,
                "name": i.name,
                "star": i.star,
                "adress": i.adress,
                "description": i.description[:100],
                "image": i.image,
                "country":models.Destination.objects.get(city_Name=i.city)
            } for i in hotels
        ]
        if len(hotels) > 6:
            hotels = hotels[:6]

        self.data_set = {
            "desciption": intro.description,
            "award": award,
            "offers": new_offer,
            "interest": interest,
            "news": news,
            "hotels": hotels,
            "gallary": gallery,
            "footer": Footer()
        }
        return self.data_set


class BlogApiSerializer:
    def __init__(self):
        self.data_set = []

    def data(self):
        blog = models.HomeBlog.objects.all()
        for item in blog:
            temp = {
                "title":  item.title,
                "image": json.loads(json.dumps(str(item.image.url))),
                "description": item.description,
            }
            self.data_set.append(temp)
        return self.data_set


class BannerApiSerializer:
    def __init__(self):
        self.data_set = []

    def data(self):
        bannars = models.HomeBanner.objects.all()
        for item in bannars:
            temp = {
                "name": item.name_of_image,
                "image": json.loads(json.dumps(str(item.image)))
            }
            self.data_set.append(temp)
        return self.data_set


class ServiceTourPackageSerializer:
    def __init__(self):
        self.data_set = {}

    def data(self):
        services = models.ServiceTourPackage.objects.all()
        self.data_set = {
            "services": services,
            "fristName": "tour",
            "lastName": "packages",
            "name": "services",
            "footer": Footer()
        }
        return self.data_set


class ServiceElementaryServiceSerializer:
    def __init__(self):
        self.data_set = {}

    def data(self):
        services = models.ServiceElementaryServices.objects.all()
        self.data_set = {
            "services": services,
            "fristName": "elementary",
            "lastName": "services",
            "name": "services",
            "footer": Footer()
        }
        return self.data_set


class MiceSerializer:
    def __init__(self):
        self.data_set = {}

    def data(self):
        mice = models.Mice.objects.all()
        self.data_set = {
            "mices": mice,
            "footer": Footer()
        }
        return self.data_set


class ToursByInterestSerializer:
    def __init__(self):
        self.data_set = {}

    def data(self):
        interest = models.TourByInterest.objects.all()

        self.data_set = {
            'interest': interest,
            "footer": Footer()
        }
        return self.data_set


class PackagesSerializer:
    def __init__(self):
        self.data_set = {}

    def data(self, interestId):
        item = models.TourByInterest.objects.get(id=interestId)
        interestList = models.TourByInterest.objects.all()
        interestItems = models.Allpackages.objects.filter(
            interest_name=item.title)
        self.data_set = {
            "name": item.title,
            "description": item.description,
            "image": item.image,
            "list_of_intrest": interestList,
            "allitems": interestItems,
            "footer": Footer()
        }
        return self.data_set


class PackageItemSerializer:
    def __init__(self):
        self.data_set = {}

    def custSort(self, arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j].day_number > arr[j+1].day_number:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr

    def data(self, packageId):
        packageItem = models.Allpackages.objects.get(id=packageId)
        route = packageItem.route.split(',')
        interestList = models.TourByInterest.objects.all()
        details = self.custSort([i for i in models.ALLPackageDetails.objects.filter(
            packages_name=packageItem.packages_name)])
        self.data_set = {
            "item": packageItem,
            "route": route,
            "list_of_intrest": interestList,
            "details": details,
            "fristRoute": route[0],
            "footer": Footer()
        }
        return self.data_set


class ToursByRegionSerializer:
    def __init__(self):
        self.data_set = {}

    def data(self):
        region = models.TourByRegion.objects.all()
        self.data_set = {
            "regions": region,
            "footer": Footer()
        }
        return self.data_set


class AllRegionSerializer:
    def __init__(self):
        self.data_set = []

    def data(self, regionId):
        region = models.TourByRegion.objects.get(id=regionId)
        filterpackage = models.Allpackages.objects.filter(region=region.region)
        self.data_set = {
            "packages": filterpackage,
            "allRegion": models.TourByRegion.objects.all(),
            "currentRegion": region,
            "footer": Footer()
        }
        return self.data_set


class NewsSerializer:
    def __init__(self):
        self.data_set = {}

    def data(self):
        news = models.News.objects.all()
        self.data_set = {
            "news": news,
            "footer": Footer()
        }
        return self.data_set


class GallerySerializer:
    def __init__(self):
        self.data_set = {}

    def data(self):
        gallary = models.Gallery.objects.all()
        self.data_set = {
            "gallary": gallary,
            "footer": Footer()
        }
        return self.data_set


class AboutSerializer:
    def __init__(self):
        self.data_set = {}

    def data(self):
        about = models.AboutSite.objects.get(id=1)
        self.data_set = {
            "about": about.about,
            "footer": Footer()
        }
        return self.data_set


class HotelSerializer:
    def __init__(self):
        self.data_set = {}

    def data(self):
        country = models.DestinationAboutCountry.objects.all()
        temp  = []
        for i in country:
            temp.append({
                "id":i.id,
                "image":i.image,
                "country":i.country,
                "default":models.Destination.objects.filter(
            country_Name=i.country.lower()).first()
            })
        self.data_set = {
            "country": temp,
            "footer": Footer()
        }
        return self.data_set


class HotelListSerializer:
    def __init__(self):
        self.data_set = {}

    def data(self, countryId, cityId):
        country = models.DestinationAboutCountry.objects.get(id=countryId)
        cityList = models.Destination.objects.filter(
            country_Name=country.country.lower())

        city_name = models.Destination.objects.get(id=cityId)

        self.data_set = {
            "city": cityList,
            "hotels": models.HotelList.objects.filter(city=city_name.city_Name),
            "footer": Footer(),
            "name": city_name.city_Name
        }
        return self.data_set


class ClientSerializer:
    def __init__(self):
        self.data_set = {}

    def data(self):
        clientList = models.Guest.objects.all()
        fliterData = [{"name": i.name, "text": i.description}
                      for i in clientList]
        self.data_set = {
            "clients": fliterData
        }
        return self.data_set
        
class Management:
    def __init__(self):
        self.data_set = {}
        
    def data(self):
        self.data_set = {
            "management":models.Management.objects.get(id=1),
            "footer": Footer()
        }
        return self.data_set
