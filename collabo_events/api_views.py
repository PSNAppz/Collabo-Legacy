from rest_framework import generics
from rest_framework.exceptions import APIException

from collabo_events.models import Seller,Event,City,Venue1,Artist,HomeFeatureArtist,HomeFeatureVenue,HomeFeatureEvent,HomeBanner,EventCategory,Host,Type,ArtistGenre
from collabo_events.serializers import  SellerSerializerDet,EventDetailSerializer,EventsListWebSerializer, EventSerializer,Venue1Serializer,CitySerializer,ArtistSerializer,EventSerializerWeb,BannerFeatureSerializer,ArtistEventSerializer,VenueListWebSerializer,ArtistListWebSerializer,VenueEventSerializer
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from django.db.models import Q
from rest_framework.generics import get_object_or_404

from rest_framework import exceptions

from rest_framework_social_oauth2.views import ConvertTokenView
from oauth2_provider.models import AccessToken
from rest_framework.response import Response
import datetime as dtime
from datetime import datetime as DateTime, timedelta as TimeDelta
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import IsAuthenticated,AllowAny
import sys
sys.path.append("..")

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets
from collections import namedtuple
from datetime import datetime
import pytz

ArtistDetail = namedtuple('ArtistDetail',('upcomingEvents','pastEvents','artist','context'))

Timeline = namedtuple('Timeline', ('banner', 'category', 'featureevent','featurevenue','featureartist','context'))
VenueWeb = namedtuple('VenueWeb', ('banner', 'category', 'venuelist','context'))
ArtistWeb = namedtuple('ArtistWeb', ('banner', 'category', 'artistlist','context'))
EventWeb = namedtuple('EventWeb', ('banner', 'category', 'eventlist','context'))
EventSer = namedtuple('EventSer', ('event',))
SellerDet = namedtuple('SellerDet', ('seller','context'))

VenueDetail= namedtuple('VenueDetail',('upcomingEvents','pastEvents','venue','context'))






class testResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10



class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class CityResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 30



class EventDetails(generics.ListAPIView):
    permission_classes = (AllowAny,)

    serializer_class = EventSerializer
    pagination_class = LargeResultsSetPagination
    lookup_url_kwarg = "id"



    def get_queryset(self,):
        """
        This view should return a details of saloo
        for the currently authenticated user.
        """



        print("sdfd")
        id = self.kwargs.get(self.lookup_url_kwarg)
        print(id)
        queryset=Event.objects.filter(id=id)
        print(queryset)

        return (queryset)

class EventDetailsSlug(generics.ListAPIView):
    permission_classes = (AllowAny,)

    #serializer_class = EventSerializer
    pagination_class = LargeResultsSetPagination
    lookup_url_kwarg = "slug"

    def list(self, request,*args, **kwargs):

        slug = self.kwargs.get(self.lookup_url_kwarg)


        eventdetail = self.filter_queryset(self.get_queryset())
        print("in list")
        print(eventdetail)



        serializer = EventDetailSerializer(eventdetail,context={'slug': slug,"request":request})
        return Response(serializer.data)



    def get_queryset(self,):

        """
        This view should return a details of saloo
        for the currently authenticated user.
        """
        print("slug")
        slug = self.kwargs.get(self.lookup_url_kwarg)
        print(slug)


        domain =self.request.GET.get('domain')
        print(domain)
        #domain="in"
        if(domain=='in'):
            default='kochi'
        else:
            default='jaddah'
        #city =self.request.GET.get('city', default)
        event = get_object_or_404(Event,slug=slug)
        city=event.city.slug
        print(city)
        city_domain=event.city.state.country.domain
        print(city_domain)
        if(domain!=city_domain):


            resp = {"status":"False","message":"Requested url not found"}
            print(resp)
            raise exceptions.NotFound(resp)
        else:
            eventser=EventSer(
                event=Event.objects.filter(slug=slug))
            return eventser



class SellerEventDetailsSlug(generics.ListAPIView):
    permission_classes = (AllowAny,)

    #serializer_class = EventSerializer
    pagination_class = LargeResultsSetPagination
    lookup_url_kwarg = "slug"

    def list(self, request,*args, **kwargs):

        slug = self.kwargs.get(self.lookup_url_kwarg)


        eventdetail = self.filter_queryset(self.get_queryset())
        print("in list")
        print(eventdetail)



        serializer = EventDetailSerializer(eventdetail,context={'slug': slug,'request':request})
        return Response(serializer.data)



    def get_queryset(self,):

        """
        This view should return a details of saloo
        for the currently authenticated user.
        """
        print("slug")
        slug = self.kwargs.get(self.lookup_url_kwarg)


        eventser=EventSer(
            event=Event.objects.filter(slug=slug))
        return eventser



class EventFilter(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)


    serializer_class = EventSerializerWeb
    pagination_class = LimitOffsetPagination
    def get_queryset(self,):
        """
        This view should return  list of all categories and its details
        """
        print("SLUG")
        city =self.request.GET.get('city', 'None')
        category =self.request.GET.get('category', 'None')
        date =self.request.GET.get('date', 'None')
        print(city)
        print(category)
        print(date)

        #today = datetime.datetime.today()
        city_1 = get_object_or_404(City,slug=city)
        tz_city = pytz.timezone(str(city_1.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)


        queryset=Event.objects.filter(Q(city__slug=city)).filter(Q(end_time__gte =today)).filter(Q(category__slug__in =category.split(','))).filter(Q(start_time__gte =date))
        return (queryset)


class EventListWeb(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)


    serializer_class = EventSerializerWeb
    pagination_class = LimitOffsetPagination
    def get_queryset(self,):
        """
        This view should return  list of all categories and its details
        """
        print("SLUG")
        slug =self.request.GET.get('city', 'kochi')
        domain =self.request.GET.get('domain')
        city =self.request.GET.get('city', None)
        # to check the current city domain
        city = get_object_or_404(City,slug=city)
        print(city.state.country.domain)
        print("USER INFO")
        print(self.request.user)

        city_domain=city.state.country.domain
        if(domain!=city_domain):


            resp = {"status":"False","message":"Requested url not found"}
            print(resp)
            raise exceptions.NotFound(resp)
        else:
            pass


        tz_city = pytz.timezone(str(city.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)
        #print("Riyadh time:", today.strftime("%H:%M:%S"))


        queryset=Event.objects.filter(city__slug=slug).filter(Q(end_time__gte =today)).order_by('category__weight')
        return (queryset)

class HomeWeb1(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)


    serializer_class = EventSerializerWeb
    pagination_class = LimitOffsetPagination
    def get_queryset(self,):
        """
        This view should return  list of all categories and its details
        """
        print("SLUG")
        slug =self.request.GET.get('city', 'kochi')
        queryset=Event.objects.filter(city__slug=slug)
        return (queryset)

from rest_framework import exceptions


class IntergrityError(object):
    pass


class EventList(generics.ListAPIView):
    permission_classes = (AllowAny,)


    serializer_class = EventSerializer
    pagination_class = LargeResultsSetPagination
    def get_queryset(self,):

        """
        This view should return  list of all categories and its details
        """
        print("SLUG")


        domain =self.request.GET.get('domain')
        city1 =self.request.GET.get('city', None)
        # to check the current city domain
        city = get_object_or_404(City,slug=city1)
        print(city.state.country.domain)
        city_domain=city.state.country.domain
        if(domain!=city_domain):


            resp = {"status":"False","message":"Requested url not found"}
            print(resp)
            raise exceptions.NotFound(resp)
        else:
            print("PASS")

            #today = datetime.datetime.today()

            tz_city = pytz.timezone(str(city.timezone1))
            today = datetime.now(tz_city).replace(tzinfo=None)

            try:

                queryset=Event.objects.filter(city__slug=city1).filter(Q(end_time__gte =today)).order_by('category__weight')
            except ValueError:
                raise APIException(detail='Custom message')
        return (queryset)


    # def list(self, request):
    #     print(self.request)
    #
    #     #id = self.kwargs.get(self.lookup_url_kwarg)
    #     #print(id)
    #     saloondetail = Saloondetail(
    #         saloon=Saloons.objects.filter(id_s=1),
    #         context={'status': "ok"}
    #
    #     )
    #     # timeline.append(context={'status': "ok"})
    #     # print(serializers..status_code)
    #     # print(status.data)
    #     serializer = SaloonsSerializer(saloondetail, context={'status': Response.status_code})
    #
    #     print(Response(serializer.context['status']))
    #
    #     # Response(serializer.data['status'])= Response.status_code
    #     print(Response(serializer.data['status']))
    #     print(Response.status_code)
    #
    #     return Response(serializer.data)


class VenueDetails(generics.ListAPIView):
    permission_classes = (AllowAny,)

    serializer_class = Venue1Serializer
    pagination_class = LargeResultsSetPagination
    lookup_url_kwarg = "id"



    def get_queryset(self,):
        """
        This view should return a details of saloo
        for the currently authenticated user.
        """
        print("sdfd")
        id = self.kwargs.get(self.lookup_url_kwarg)
        print(id)
        queryset=Venue1.objects.filter(venue_id=id)
        print(queryset)

        return (queryset)


class VenueDetailsSlug1(generics.ListAPIView):
    permission_classes = (AllowAny,)

    serializer_class = Venue1Serializer
    pagination_class = LargeResultsSetPagination
    lookup_url_kwarg = "slug"



    def get_queryset(self,):
        """
        This view should return a details of saloo
        for the currently authenticated user.
        """
        print("slug")
        slug = self.kwargs.get(self.lookup_url_kwarg)
        print(slug)
        queryset=Venue1.objects.filter(slug=slug)
        print(queryset)

        return (queryset)



class VenueDetailsPFVenue(generics.ListAPIView):
    permission_classes = (AllowAny,)

    serializer_class = Venue1Serializer
    pagination_class = LargeResultsSetPagination
    lookup_url_kwarg = "slug"



    # def get_queryset(self,):
    #     """
    #     This view should return a details of saloo
    #     for the currently authenticated user.
    #     """
    #     print("slug")
    #     slug = self.kwargs.get(self.lookup_url_kwarg)
    #     print(slug)
    #     city =self.request.GET.get('city', 'kochi')
    #     queryset=Venue1.objects.filter(slug=slug)
    #     print(queryset)
    #
    #     return (queryset)



    def list(self, request,*args, **kwargs):
        print("TEST")


        venuedetail = self.filter_queryset(self.get_queryset())



        serializer = VenueEventSerializer(venuedetail,context={'status': Response.status_code,"request": request})
        return Response(serializer.data)


    def get_queryset(self):
        print("wSDF")
        slug = self.kwargs.get(self.lookup_url_kwarg)
        print("venue")
        print(slug)
        city =self.request.GET.get('city', 'kochi')
        print(city)

        #today = datetime.datetime.today()
        city = get_object_or_404(City,slug=city)

        tz_city = pytz.timezone(str(city.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)

        print(today)
        venuedetail = VenueDetail(
            upcomingEvents=Event.objects.filter(Q(end_time__gte =today)&Q(address_venue__slug=slug)),
            pastEvents=Event.objects.filter(Q(end_time__lte =today)&Q(address_venue__slug=slug)),
            venue=Venue1.objects.filter(Q(slug=slug)),
            context={'status': "ok"}


        )
        return venuedetail





class VenueDetailsSlug(generics.ListAPIView):
    permission_classes = (AllowAny,)

    serializer_class = Venue1Serializer
    pagination_class = LargeResultsSetPagination
    lookup_url_kwarg = "slug"



    def get_queryset(self,):
        """
        This view should return a details of saloo
        for the currently authenticated user.
        """
        print("slug")
        slug = self.kwargs.get(self.lookup_url_kwarg)
        print(slug)
        city =self.request.GET.get('city', 'kochi')
        queryset=Venue1.objects.filter(slug=slug)
        print(queryset)

        return (queryset)



    def list(self, request,*args, **kwargs):
        print("TEST")


        venuedetail = self.filter_queryset(self.get_queryset())



        serializer = VenueEventSerializer(venuedetail,context={'status': Response.status_code,"request": request})
        return Response(serializer.data)


    def get_queryset(self):
        print("wSDF")
        slug = self.kwargs.get(self.lookup_url_kwarg)
        print(slug)
        city =self.request.GET.get('city', 'kochi')
        print(city)

        #today = datetime.datetime.today()
        city_1 = get_object_or_404(City,slug=city)
        tz_city = pytz.timezone(str(city_1.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)

        print(today)
        venuedetail = VenueDetail(
            upcomingEvents=Event.objects.filter(Q(end_time__gte =today)&Q(city__slug=city)),
            pastEvents=Event.objects.filter(Q(end_time__lte =today)&Q(city__slug=city)),
            venue=Venue1.objects.filter(Q(slug=slug)),
            context={'status': "ok"}


        )
        return venuedetail





class ArtistDetailsPFArtist(generics.ListAPIView):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = "slug"


    def list(self, request,*args, **kwargs):
        print("TEST")


        artistdetail = self.filter_queryset(self.get_queryset())

        for  i in artistdetail:
            print(i)

        serializer = ArtistEventSerializer(artistdetail,context={'status': Response.status_code,"request": request})
        print(Response(serializer.context['status']))
        print(Response(serializer.data['status']))
        print(Response.status_code)
        return Response(serializer.data)


    def get_queryset(self):
        print("wSDF")
        slug = self.kwargs.get(self.lookup_url_kwarg)
        print(slug)
        city =self.request.GET.get('city', 'kochi')

        #today = datetime.datetime.today()
        city_1 = get_object_or_404(City,slug=city)
        tz_city = pytz.timezone(str(city_1.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)

        print(today)
        artistdetail = ArtistDetail(
            upcomingEvents=Event.objects.filter(Q(end_time__gte =today)&Q(artists__slug__in=[slug])),
            pastEvents=Event.objects.filter(Q(end_time__lte =today)&Q(artists__slug__in=[slug])),
            artist=Artist.objects.filter(Q(slug=slug)),
            context={'status': "ok"}


        )
        return artistdetail



class ArtistDetailsSlugUserApp(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = "slug"
    authentication_classes = (TokenAuthentication,)



    def list(self, request,*args, **kwargs):
        print("TEST")


        artistdetail = self.filter_queryset(self.get_queryset())

        for  i in artistdetail:
            print(i)

        serializer = ArtistEventSerializer(artistdetail,context={'status': Response.status_code,"request": request})
        print(Response(serializer.context['status']))
        print(Response(serializer.data['status']))
        print(Response.status_code)
        return Response(serializer.data)


    def get_queryset(self):
        print("wSDF")
        slug = self.kwargs.get(self.lookup_url_kwarg)
        print(slug)
        city =self.request.GET.get('city', 'kochi')

        #today = datetime.datetime.today()
        city_1 = get_object_or_404(City,slug=city)
        tz_city = pytz.timezone(str(city_1.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)

        print(today)
        artistdetail = ArtistDetail(
            upcomingEvents=Event.objects.filter(Q(end_time__gte =today)&Q(city__slug=city)),
            pastEvents=Event.objects.filter(Q(end_time__lte =today)&Q(city__slug=city)),
            artist=Artist.objects.filter(Q(slug=slug)),
            context={'status': "ok"}


        )
        return artistdetail





class ArtistDetailsSlug(generics.ListAPIView):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = "slug"
    authentication_classes = (TokenAuthentication,)




    def list(self, request,*args, **kwargs):
        print("TEST")


        artistdetail = self.filter_queryset(self.get_queryset())

        for  i in artistdetail:
            print(i)

        serializer = ArtistEventSerializer(artistdetail,context={'status': Response.status_code,"request": request})
        print(Response(serializer.context['status']))
        print(Response(serializer.data['status']))
        print(Response.status_code)
        return Response(serializer.data)


    def get_queryset(self):
        print("wSDF")
        slug = self.kwargs.get(self.lookup_url_kwarg)
        print(slug)
        city =self.request.GET.get('city', 'kochi')

        #today = datetime.datetime.today()
        city_1 = get_object_or_404(City,slug=city)
        tz_city = pytz.timezone(str(city_1.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)

        print(today)
        artistdetail = ArtistDetail(
            upcomingEvents=Event.objects.filter(Q(end_time__gte =today)&Q(city__slug=city)),
            pastEvents=Event.objects.filter(Q(end_time__lte =today)&Q(city__slug=city)),
            artist=Artist.objects.filter(Q(slug=slug)),
            context={'status': "ok"}


        )
        return artistdetail






class VenueListWeb(generics.ListAPIView):
    permission_classes = (AllowAny,)


    serializer_class = VenueListWebSerializer
    pagination_class = LargeResultsSetPagination
    def get_queryset1(self,):
        """
        This view should return  list of all categories and its details
        """
        slug =self.request.GET.get('city', 'kochi')
        queryset=Venue1.objects.filter(city__slug=slug)
        print(queryset)
        return (queryset)

    def list(self, request):
        slug =self.request.GET.get('city', 'kochi')
        domain =self.request.GET.get('domain')
        # to check the current city domain
        city = get_object_or_404(City,slug=slug)
        print(city.state.country.domain)
        city_domain=city.state.country.domain
        if(domain!=city_domain):


            resp = {"status":"False","message":"Requested url not found"}
            print(resp)
            raise exceptions.NotFound(resp)
        else:
            pass



        print("SLUG")
        print(slug)
        #today = datetime.datetime.today()
        #city = get_object_or_404(City,slug=city)
        tz_city = pytz.timezone(str(city.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)


        timeline = self.filter_queryset(self.get_queryset(slug,today))
        print("TIMELINE")

        #timeline.append(context={'status': "ok"})
        #print(serializers..status_code)
        #print(status.data)
        #request="http://localhost:8000"
        serializer = VenueListWebSerializer(timeline,context={'status': Response.status_code,"request": request,'city':slug})



        print(Response(serializer.context['status']))

        #Response(serializer.data['status'])= Response.status_code
        print(Response(serializer.data['status']))
        qs=Venue1.objects.filter(city__slug=slug).count()
        type={"type":{"name":"All","count":qs,"id":0}}
        serializer.data['category'].append(type)
        print(serializer.data['category'])
        print(Response.status_code)




        return Response(serializer.data)


    def get_queryset(self,slug,today):

        venueweb = VenueWeb(
            banner=HomeBanner.objects.all(),
            category=Type.objects.filter(venue1__city__slug=slug).distinct(),
            venuelist=Venue1.objects.filter(Q(city__slug=slug))[:9],

            context={'status': "ok"}


        )
        print("VENUEWEB CATEGORY")
        print(venueweb.category)
        return venueweb




class EventsListWeb(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EventsListWebSerializer
    pagination_class = LargeResultsSetPagination
    def list(self, request):
        slug =self.request.GET.get('city', 'kochi')

        domain =self.request.GET.get('domain', 'in')
        city = get_object_or_404(City, slug=slug)
        city_domain=city.state.country.domain
        print(city_domain)
        if(domain!=city_domain):

            resp = {"status":"False","message":"Requested url not found"}
            return Response(resp)

        #today = datetime.datetime.today()
        tz_city = pytz.timezone(str(city.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)


        timeline = self.filter_queryset(self.get_queryset(slug,today))
        print("TIMELINE")
        serializer = EventsListWebSerializer(timeline,context={'status': Response.status_code,"request": request,"city":slug,"today":today})
        print(Response(serializer.context['status']))

        #Response(serializer.data['status'])= Response.status_code
        print(Response(serializer.data['status']))
        print(Response.status_code)
        #qs=Artist.objects.filter(city__slug=obj.pk).count()

        qs=Event.objects.filter(city__slug=slug).count()
        type={"type":{"name":"All","count":qs,"id":0}}
        serializer.data['category'].append(type)






        return Response(serializer.data)


    def get_queryset(self,slug,today):
        print(slug)

        eventweb = EventWeb(
            banner=HomeBanner.objects.all(),
            category=EventCategory.objects.filter(events__city__slug=slug).distinct(),
            eventlist=Event.objects.filter(Q(city__slug=slug)).filter(Q(end_time__gte =today))[:9],
            context={'status': "ok"}
        )
        return eventweb








class ArtistListWeb(generics.ListAPIView):
    permission_classes = (AllowAny,)


    serializer_class = ArtistListWebSerializer
    pagination_class = LargeResultsSetPagination


    def list(self, request):
        slug =self.request.GET.get('city', 'kochi')



        #today = datetime.datetime.today()
        city = get_object_or_404(City,slug=slug)
        tz_city = pytz.timezone(str(city.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)

        timeline = self.filter_queryset(self.get_queryset(slug,today))
        print("TIMELINE")

        #timeline.append(context={'status': "ok"})
        #print(serializers..status_code)
        #print(status.data)
        #request="http://localhost:8000"
        serializer = ArtistListWebSerializer(timeline,context={'status': Response.status_code,"request": request})



        print(Response(serializer.context['status']))

        #Response(serializer.data['status'])= Response.status_code
        print(Response(serializer.data['status']))
        print(Response.status_code)
        #qs=Artist.objects.filter(city__slug=obj.pk).count()

        qs=Artist.objects.filter(city__slug=slug).count()
        type={"genre":{"name":"All","count":qs,"id":0}}
        serializer.data['category'].append(type)





        return Response(serializer.data)


    def get_queryset(self,slug,today):

        artistweb = ArtistWeb(
            banner=HomeBanner.objects.all(),
            category=ArtistGenre.objects.all(),
            artistlist=Artist.objects.all(),
            context={'status': "ok"}


        )
        return artistweb








class ArtistDetailsSlug1(generics.ListAPIView):
    permission_classes = (AllowAny,)

    serializer_class = ArtistSerializer
    pagination_class = LargeResultsSetPagination
    lookup_url_kwarg = "slug"



    def get_queryset(self,):
        """
        This view should return a details of saloo
        for the currently authenticated user.
        """
        print("slug")
        slug = self.kwargs.get(self.lookup_url_kwarg)
        print(slug)
        queryset=Artist.objects.filter(slug=slug)
        print(queryset)

        return (queryset)



class CityListCC(generics.ListAPIView):
    permission_classes = (AllowAny,)


    serializer_class = CitySerializer
    pagination_class = CityResultsSetPagination
    def get_queryset(self,):
        """
        This view should return  list of all categories and its details
        """




        cc =self.request.GET.get('cc')



        queryset=City.objects.filter(state__country__country_code=cc)
        print(queryset)

        return (queryset)



class CityList(generics.ListAPIView):
    permission_classes = (AllowAny,)


    serializer_class = CitySerializer
    pagination_class = CityResultsSetPagination
    def get_queryset(self,):
        """
        This view should return  list of all categories and its details
        """




        domain =self.request.GET.get('domain')



        queryset=City.objects.filter(state__country__domain=domain)
        print(queryset)

        return (queryset)

class EventListType(generics.ListAPIView):
    permission_classes = (AllowAny,)


    serializer_class = EventSerializer
    pagination_class = LargeResultsSetPagination
    def get_queryset(self,):
        """
        This view should return  list of all categories and its details
        """
        slug =self.request.GET.get('city', 'kochi')
        type =self.request.GET.get('type', 1)
        domain =self.request.GET.get('domain')
        # to check the current city domain
        city = get_object_or_404(City,slug=slug)

        print(city.state.country.domain)
        city_domain=city.state.country.domain
        if(domain!=city_domain):


            resp = {"status":"False","message":"Requested url not found"}
            print(resp)
            raise exceptions.NotFound(resp)
        else:
            pass

        print(slug)
        print(type)
        #today = datetime.datetime.today()
        #city = get_object_or_404(City,slug=city)
        tz_city = pytz.timezone(str(city.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)

        queryset=Event.objects.filter(Q(city__slug=slug)&Q(category_id=type)&Q(end_time__gte =today))
        print(queryset)

        return (queryset)


class VenueListType(generics.ListAPIView):
    permission_classes = (AllowAny,)


    serializer_class = Venue1Serializer
    pagination_class = LargeResultsSetPagination
    def get_queryset(self,):
        """
        This view should return  list of all categories and its details
        """
        slug =self.request.GET.get('city', 'kochi')
        type =self.request.GET.get('type', 3)
        domain =self.request.GET.get('domain')
        # to check the current city domain
        city = get_object_or_404(City,slug=slug)

        print(city.state.country.domain)
        city_domain=city.state.country.domain
        if(domain!=city_domain):


            resp = {"status":"False","message":"Requested url not found"}
            print(resp)
            raise exceptions.NotFound(resp)
        else:
            pass


        queryset=Venue1.objects.filter(Q(city__slug=slug)&Q(type__id=type))
        print(queryset)

        return (queryset)

class VenueList(generics.ListAPIView):
    permission_classes = (AllowAny,)


    serializer_class = Venue1Serializer
    pagination_class = LargeResultsSetPagination
    def get_queryset(self,):
        """
        This view should return  list of all categories and its details
        """
        slug =self.request.GET.get('city', 'kochi')
        domain =self.request.GET.get('domain')
        # to check the current city domain
        city = get_object_or_404(City,slug=slug)
        print(city.state.country.domain)
        city_domain=city.state.country.domain
        if(domain!=city_domain):


            resp = {"status":"False","message":"Requested url not found"}
            print(resp)
            raise exceptions.NotFound(resp)
        else:
            pass


        queryset=Venue1.objects.filter(city__slug=slug)
        print(queryset)

        return (queryset)


class ArtistListGenre(generics.ListAPIView):
    permission_classes = (AllowAny,)


    serializer_class = ArtistSerializer
    pagination_class = LargeResultsSetPagination
    def get_queryset(self,):
        """
        This view should return  list of all categories and its details
        """
        genre =self.request.GET.get('genre', None)
        domain =self.request.GET.get('domain', 'in')





        #queryset=Artist.objects.filter(city__slug=slug)
        queryset=Artist.objects.filter(city__state__country__domain=domain).filter(Q(genre__id=genre))

        print(queryset)

        return (queryset)

class ArtistList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ArtistSerializer
    authentication_classes = (TokenAuthentication,)


    pagination_class = LargeResultsSetPagination






    def get_queryset(self,):
        """
        This view should return  list of all categories and its details
        """
        slug =self.request.GET.get('city', 'kochi')
        domain =self.request.GET.get('domain', 'in')

        city = get_object_or_404(City, slug=slug)
        city_domain=city.state.country.domain
        print(city_domain)
        # if(domain!=city_domain):
        #
        #     resp = {"status":"False","message":"Requested url not found"}
        #     print(resp)
        #
        #     return (queryset)

        #queryset=Artist.objects.filter(city__slug=slug)
        print("USER info")
        print(self.request.user)
        queryset=Artist.objects.filter(city__state__country__domain=domain)
        print(queryset)

        return (queryset)


#from compression_middleware.decorators import compress_page




class HomeWeb(generics.ListAPIView):
    permission_classes = (AllowAny,)


    """
    """


    def list(self, request):
        domain =self.request.GET.get('domain')
        print(domain)
        #domain="in"
        if(domain=='in'):
            default='kochi'
        else:
            default='jaddah'
        slug =self.request.GET.get('city', default)
        city = get_object_or_404(City, slug=slug)
        city_domain=city.state.country.domain
        print(city_domain)
        if(domain!=city_domain):

            resp = {"status":"False","message":"Requested url not found"}
            print(resp)
            #resp= gzip_middleware.process_response(request, resp)

            return Response(resp)





        print("SLUG")
        print(slug)
        #today = datetime.datetime.today()
        #city = get_object_or_404(City,slug=city)
        tz_city = pytz.timezone(str(city.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)

        print(today)
        print(today)
        timeline = self.filter_queryset(self.get_queryset(slug,today))


        # timeline = Timeline(
        #     banner=HomeBanner.objects.all(),
        #     category=EventCategory.objects.all(),
        #     #featureevent=HomeFeatureEvent.objects.filter(Q(city__slug=slug)&Q(event__city__slug__in=[slug]) & Q(event__end_time__gte =today)).distinct(),
        #     featureevent=HomeFeatureEvent.objects.filter(Q(city__slug=slug)).distinct(),
        #     featurevenue=HomeFeatureVenue.objects.filter(city__slug=slug),
        #     featureartist=HomeFeatureArtist.objects.filter(city__slug=slug),
        #     context={'status': "ok"}
        #
        #
        # )
        print("TIMELINE")
        for  i in timeline.featureevent:
            print(i.event.all())

        print("TIMELINE")

        #timeline.append(context={'status': "ok"})
        #print(serializers..status_code)
        #print(status.data)
        #request="http://localhost:8000"
        serializer = BannerFeatureSerializer(timeline,context={'status': Response.status_code,"request": request,"city":slug,"today":today})
        print(type(serializer.data))
        def Remove(tuples):
            tuples = [t for t in tuples if t]
            print("TUPLE")
            print(tuples)
            return tuples

        # for (i) in serializer.data['category'][:]:
        #     d=i
        #     print(d)
        #     if(i['category'] is None):
        #         #print(i['category'])
        #         del(i['category'])
                #pass

        # for i, val in enumerate(serializer.data['category'][:]):
        #     if val['category'] is  None:
        #         l: list = serializer.data['category']
        #         l.remove(l[i])
        #         #l.pop(i)

        return Response(serializer.data)

    def get_serializer_context(self):
        return {"city": "COCHIN"}



    def get_queryset(self,slug,today):
        print("CITY")
        print(slug)
        timeline = Timeline(
            banner=HomeBanner.objects.filter(Q(event__city__slug=slug)),
            category=EventCategory.objects.all(),
            #featureevent=HomeFeatureEvent.objects.filter(Q(city__slug=slug)),

            featureevent=HomeFeatureEvent.objects.filter(Q(event__city__slug=slug)&Q(event__end_time__gte =today)&Q(city__slug =slug)).distinct(),
            #featureevent=HomeFeatureEvent.objects.filter(event__city__slug=slug).filter(Q(event__end_time__gte=today)),

            #featureevent=HomeFeatureEvent.objects.filter(Q(city__slug=slug)).distinct(),
            featurevenue=HomeFeatureVenue.objects.filter(city__slug=slug),
            featureartist=HomeFeatureArtist.objects.filter(city__slug=slug),
            context={'status': "ok","city":slug}


        )
        return timeline





class Subscribe(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
            #host = request.data['host']
            host =self.request.GET.get('host', '')
            print(host)

            user = self.request.user.customer
            self.request.user.customer.subscription.add(host)
            qs=Host.objects.filter(id__exact=host)
            for i in qs:
                i.cust.add(user)


        #self.request.user.customer.save()

            resp = {"status":"True","message":"Subscribed to the event"}
            return Response(resp)

        except Exception as e:
            resp = {"status":False,"message": str(e)}
            return Response(resp)


class UnfollowVenue(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
            venue =self.request.GET.get('venue', None)
            print(venue)

            user = self.request.user.customer
            print(user)
            #
            venue= get_object_or_404(Venue1, slug=venue)
            self.request.user.customer.follow_venue.remove(venue.id)
            resp = {"status":"True","message":"UnFollowed venue"}
            return Response(resp)

        except Exception as e:
            resp = {"status":False,"message": str(e)}
            return Response(resp)

class FollowVenue(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
            venue =self.request.GET.get('venue', None)
            print(venue)

            user = self.request.user.customer
            print(user)
            #
            venue= get_object_or_404(Venue1, slug=venue)
            self.request.user.customer.follow_venue.add(venue.id)
            resp = {"status":"True","message":"Followed venue"}
            return Response(resp)

        except Exception as e:
            resp = {"status":False,"message": str(e)}
            return Response(resp)

class FollowArtist(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
            artist =self.request.GET.get('artist', None)
            print(artist)

            user = self.request.user.customer
            print(user)
            #
            artist = get_object_or_404(Artist, slug=artist)
            self.request.user.customer.follow_artist.add(artist.id)
            resp = {"status":"True","message":"Followed artist"}
            return Response(resp)

        except Exception as e:
            resp = {"status":False,"message": str(e)}
            return Response(resp)

class UnFollowArtist(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
            artist =self.request.GET.get('artist', None)
            print(artist)

            user = self.request.user.customer
            print(user)
            #
            artist = get_object_or_404(Artist, slug=artist)
            self.request.user.customer.follow_artist.remove(artist.id)
            resp = {"status":"True","message":"unfollowed artist"}
            return Response(resp)

        except Exception as e:
            resp = {"status":False,"message": str(e)}
            return Response(resp)


class Unsubscribe(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
            host =self.request.GET.get('host', '')
            print(host)

            user = self.request.user.customer

            self.request.user.customer.subscription.remove(host)
            qs=Host.objects.filter(id__exact=host)
            for i in qs:
                i.cust.remove(user)


            resp = {"status": "True", "message": "Unsubscribed"}
            return Response(resp)

        except Exception as e:
            resp = {"status": False, "message": str(e)}
            return Response(resp)


class EventListSeller(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    #permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)



    serializer_class = SellerSerializerDet
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        slug =self.request.GET.get('city', 'kochi')
        city = get_object_or_404(City,slug=slug)
        tz_city = pytz.timezone(str(city.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)
        timeline = self.filter_queryset(self.get_queryset(slug,today))
        serializer = SellerSerializerDet(timeline,context={'status': Response.status_code,"request": request,'city':slug})
        return Response(serializer.data)

    def get_queryset(self,slug,today):
        user=self.request.user

        sellerdet = SellerDet(
            #seller=Seller.objects.filter(Q(user=user)&Q(event__event__end_time__gte =today)&Q(event__event__city__slug =slug)),
            seller=Seller.objects.filter(Q(user=user)&Q(event__eventdetail__end_time__gte =today)).distinct(),
            context={'status': "ok"}
        )
        return sellerdet


class EventListSeller1(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    #permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)


    serializer_class = SellerSerializerDet
    #pagination_class = LimitOffsetPagination
    def get_queryset(self,):
        """
        This view should return  list of all categories and its details
        """
        print("SLUG")
        user=self.request.user
        print(user)

        slug =self.request.GET.get('city', 'kochi')
        domain =self.request.GET.get('domain')
        city =self.request.GET.get('city', None)
        # to check the current city domain
        city = get_object_or_404(City,slug=city)
        print(city.state.country.domain)
        city_domain=city.state.country.domain
        if(domain!=city_domain):


            resp = {"status":"False","message":"Requested url not found"}
            print(resp)
            raise exceptions.NotFound(resp)
        else:
            pass


        tz_city = pytz.timezone(str(city.timezone1))
        today = datetime.now(tz_city).replace(tzinfo=None)
        #print("Riyadh time:", today.strftime("%H:%M:%S"))


        queryset=Seller.objects.filter(Q(user=user)&Q(event__event__end_time__gte =today)&Q(event__event__city__slug =city))
        return (queryset)



