from django.urls import include, path

from django.urls import re_path as url

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import include 
from qr_code import urls as qr_code_urls
from . import api_views
from .views import collabo_events, operators, owners
from django_filters.views import FilterView
from .filters import UserFilter
from . import views
urlpatterns = [
    path('', collabo_events.home, name='home'),
    path('sellerslist/',collabo_events.sellerslist, name='sellerslist'),
    #path('sellerslist/<int:id>',collabo_events.sellerslist, name='sellerslistid'),
    #path('sellerseventlist/(?P<event_title>\w+)/$',collabo_events.sellerseventlist, name='sellerseventlist'),
    #path('sellerslist/(?P<event_title>\w+)/$',collabo_events.sellerslist, name='sellerslist'),

    path('userslist/',collabo_events.userslist, name='userslist'),
    path('subscribers/',collabo_events.subscribers, name='subscribers'),


    path('addseller/',collabo_events.addseller, name='addseller'),
    path('editseller/',collabo_events.editseller, name='editseller'),
    path('addsellertoevent/',collabo_events.addsellertoevent, name='addsellertoevent'),
    path('signup/', collabo_events.signup, name='signup'),



    path('operators/', include(([
                                    path('', operators.QuizListView.as_view(), name='event_list'),
                                    path('edit', operators.SaloonEditView.as_view(), name='edit'),


                                    #path('interests/', operators.StudentInterestsView.as_view(), name='student_interests'),
                                    #path('taken/', operators.TakenQuizListView.as_view(), name='taken_quiz_list'),
                                    #path('quiz/<int:pk>/', classmethod.take_quiz, name='take_quiz'),
                                ], 'collabo_events'), namespace='operators')),

    path('owners/', include(([
                                 path('', owners.QuizListView.as_view(), name='quiz_change_list'),
                                 path('', owners.AdminView.as_view(), name='admin_view'),
                                 #path('sellerslistview',owners.SellerListView.as_view(), name='sellerslistview'),

                                 path('sellerslistview/?P<event_title>\w+/',owners.SellerListView.as_view(), name='sellerslistview'),
                                 path('sellersaddlistview/?P<event_title>\w+/',owners.SellerAddListView.as_view(), name='sellersaddlistview'),
                                 path('sellersaddeventview/?P<event_title>\w+/',owners.SellerAddEventView.as_view(), name='sellersaddeventview'),

                                 path('sellerseditlistview/?P<id>\d+/',owners.SellerEditListView.as_view(), name='sellerseditlistview'),
                                 path('userslistview',owners.UserListView.as_view(), name='userslistview'),
                                 path('subscribersview',owners.SubscribersView.as_view(), name='subscribersview'),


                                 # path('quiz/add/', owners.QuizCreateView.as_view(), name='quiz_add'),
                                 # path('quiz/<int:pk>/', owners.QuizUpdateView.as_view(), name='quiz_change'),
                                 # path('quiz/<int:pk>/delete/', owners.QuizDeleteView.as_view(), name='quiz_delete'),
                                 #  path('quiz/<int:pk>/results/', owners.QuizResultsView.as_view(), name='quiz_results'),
                                 #  path('quiz/<int:pk>/question/add/', owners.question_add, name='question_add'),
                                 #  path('quiz/<int:quiz_pk>/question/<int:question_pk>/', owners.question_change, name='question_change'),
                                 #  path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', owners.QuestionDeleteView.as_view(), name='question_delete'),
                             ], 'collabo_events'), namespace='owners')),



    url(r'^api/event/(?P<id>[0-9]+)/$', api_views.EventDetails.as_view()),
    #url(r'^api/eventlists/(?P<slug>[A-Za-z-]+)/$', api_views.EventList.as_view()),
    url(r'^api/eventlists/$', api_views.EventList.as_view()),
    url(r'^api/venue/(?P<id>[0-9]+)/$', api_views.VenueDetails.as_view()),
    url(r'^api/venuelists/$', api_views.VenueList.as_view()),
    url(r'^api/artistlists/$', api_views.ArtistList.as_view()),
    url(r'^api/cities/', api_views.CityList.as_view()),
    url(r'^api/citylist/', api_views.CityListCC.as_view()),
    #slug-fields

    url(r'^api/event/(?P<slug>[0-9A-Za-z_-]+)/$', api_views.EventDetailsSlug.as_view()),
    url(r'^api/sellerevent/(?P<slug>[0-9A-Za-z_-]+)/$', api_views.SellerEventDetailsSlug.as_view()),


    url(r'^api/venue/(?P<slug>[0-9A-Za-z_-]+)/$', api_views.VenueDetailsSlug.as_view()),
    url(r'^api/artist/(?P<slug>[0-9A-Za-z_-]+)/$', api_views.ArtistDetailsSlug.as_view()),
    url(r'^api/artistdetail/(?P<slug>[0-9A-Za-z_-]+)/$', api_views.ArtistDetailsSlugUserApp.as_view()),


    #artist filter for past and future based on particualar venue and artist
    url(r'^api/venuepf/(?P<slug>[0-9A-Za-z_-]+)/$', api_views.VenueDetailsPFVenue.as_view()),
    url(r'^api/artistpf/(?P<slug>[0-9A-Za-z_-]+)/$', api_views.ArtistDetailsPFArtist.as_view()),

    #for subscription

    url(r'^api/subscribe', api_views.Subscribe.as_view()),
    url(r'^api/unsubscribe', api_views.Unsubscribe.as_view()),
    #for follow unfollow artists
    url(r'^api/followartist', api_views.FollowArtist.as_view()),
    url(r'^api/unfollowartist', api_views.UnFollowArtist.as_view()),
    url(r'^api/followvenue', api_views.FollowVenue.as_view()),

    #API FOR WEB
    url(r'^api/eventlist/$', api_views.EventListWeb.as_view()),
    #url(r'^api/home/$', api_views.HomeWeb.as_view({"get": "list"}))
    url(r'^api/home/$', api_views.HomeWeb.as_view()),
    url(r'^api/venuelistweb/$', api_views.VenueListWeb.as_view()),
    url(r'^api/artistlistweb/$', api_views.ArtistListWeb.as_view()),
    url(r'^api/eventlistweb/$', api_views.EventsListWeb.as_view()),
    # filter Events

    url(r'^api/eventfilter/$', api_views.EventFilter.as_view()),
    url(r'^homefeatureeventcity/$',collabo_events.homefeatureeventcity),

    url(r'^api/venuelisttype/$', api_views.VenueListType.as_view()),
    url(r'^api/artistlistgenre/$', api_views.ArtistListGenre.as_view()),
    url(r'^api/eventlisttype/$', api_views.EventListType.as_view()),



    #Reseller apis
    url(r'^api/sellerevents/$', api_views.EventListSeller.as_view()),
    #url(r'^api/sellerevent/(?P<slug>[0-9A-Za-z_-]+)/$', api_views.SellerEventDetailsSlug.as_view()),





    #http://13.234.60.82/admin/login/?next=/admin/collabo_events/


    #x/api/cities

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()





