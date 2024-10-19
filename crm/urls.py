from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('profile-page', views.profilepage, name='profilepage'),
    path('profile-edit/<str:pk>', views.profileedit, name='profileedit'),

    # New Company Registration URLS
    path('new-company-registration',
         views.newcompanyregistration, name='newcompregister'),
    path('new-company-edit/<str:pk>', views.newcompanyedit, name='newcompedit'),
    path('company-overview/<str:pk>', views.companyoverview, name='compoverview'),
    path('new-company', views.allnewcompany, name='newcomp'),
    path('new-company-pending-kyc', views.allnewcompanypendingkyc, name='newcomppendingkyc'),
    path('new-company-delete/<str:pk>',
         views.newcompanydelete, name='newcompdelete'),


    # Full KYC Company URLS
    path('company-registration', views.addcompanykyc, name='addcompanykyc'),
    path('company-edit/<str:pk>', views.editcompanykyc, name='editcompanykyc'),
    path('company-profile/<str:pk>',
         views.overviewcompanykyc, name='overviewcompanykyc'),
    path('company-full-kyc', views.allcompanykyc, name='allcompanykyc'),
    path('company-delete-kyc/<str:pk>',
         views.deletecompanykyc, name='deletecompanykyc'),


    # Company Contacts URLS
    path('contact-add', views.addcontact, name='addcontact'),
    path('contact-edit/<str:pk>', views.editcontact, name='editcontact'),
    path('contact-profile/<str:pk>',
         views.overviewcontact, name='overviewcontact'),
    path('contact-table', views.allcontact, name='allcontact'),
    path('contact-delete/<str:pk>',
         views.deletecontact, name='deletecontact'),


    # Company Contacts Open LinksURLS
    path('contact-add-ol', views.addindividualol,
         name='addcontactol'),
    path('contact-edit-ol/<str:pk>', views.editindividual, name='editcontactol'),
    path('contact-table-ol', views.allindividual, name='allcontactol'),
    path('contact-delete-ol/<str:pk>',
         views.deleteindividual, name='deletecontactol'),


    # Arrivals URLS
    path('arrival-add', views.addarrival, name='addarrival'),
    path('arrival-edit/<str:pk>', views.editarrival, name='editarrival'),
    path('arrival-profile/<str:pk>',
         views.overviewarrival, name='overviewarrival'),
    path('arrival-table', views.allarrival, name='allarrival'),
    path('arrival-delete/<str:pk>',
         views.deletearrival, name='deletearrival'),

    # path('profile-setting', views.profilesetting, name='profilesetting'),

    # Feedbacks  URLS
    path('feedback-add', views.addfeedback, name='addfeedback'),
    path('feedback-edit/<str:pk>', views.editfeedback, name='editfeedback'),
    path('feedback-profile/<str:pk>',
         views.overviewfeedback, name='overviewfeedback'),
    path('feedback-table', views.allfeedback, name='allfeedback'),
    path('feedback-delete/<str:pk>',
         views.deletefeedback, name='deletefeedback'),
    path('feedback-status/<str:pk>',
         views.statusfeedback, name='statusfeedback'),




    path('charts-chartjs', views.chartjs, name='chartjs'),
    path('charts-echarts', views.echarts, name='echarts'),
    path('charts-apex-charts', views.apexcharts, name='apexcharts'),
    path('tables-data', views.datatable, name='datatable'),
    path('tables-general', views.generaltable, name='generaltable'),


    path('page-contact', views.contactpage, name='contactpage'),
    path('page-error', views.blankpage, name='blankpage'),
    path('page-error-404', views.error404page, name='error404page'),
    path('page-faq', views.faqpage, name='faqpage'),

    # Charts
    #     path('pie-charts', views.piechart, name='piechart'),
    #     path('apex-chart', views.apexchart, name='apexchart')




    # Travle Agent URLS
    # path('', views.company, name='company'),
    # path('contact', views.contact, name='contact'),
    # # path('arival', views.arivalhome, name='arival'),
    # path('arivalform', views.arivalform, name='arivalform'),

    # path('editcompany/<str:pk>', views.editcompany, name='editcompany'),
    # path('editcontact/<str:pk>', views.editcontact, name='editcontact'),
    # path('edit-arival/<str:pk>', views.editarival, name='editarival'),

    # path('home-contact/<str:pk>', views.deletecontact, name='deletecontact'),
    # path('home-company/<str:pk>', views.deletecompany, name='deletecompany'),
    # path('delete-Arival/<str:pk>', views.deleteArival, name='deleteArival'),


    # # path('login', views.loginPage, name='login-page'),
    # # path('logout/', views.logoutUser, name='logout'),
    # # # path('register/', views.registerPage, name='register'),

    # path('datatable', views.datatableview, name='datatableview'),
    # path('datatable2', views.datatableview2, name='datatable2')



]
