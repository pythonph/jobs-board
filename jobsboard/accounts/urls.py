from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^profile/update/$', views.ProfileUpdate.as_view(), name='profile_update'),

    url(
        r'^login/$',
        auth_views.login,
        kwargs={
            'template_name': 'accounts/login.html',
        },
        name='login'
    ),
    url(
        r'^logout/$',
        auth_views.logout_then_login,
        name='logout'
    ),
    url(
        r'^password/change/$',
        auth_views.password_change,
        kwargs={
            'template_name': 'accounts/password_change.html',
            'post_change_redirect': 'accounts:password_change_done',
        },
        name='password_change'
    ),
    url(
        r'^password/change/done/$',
        auth_views.password_change_done,
        kwargs={
            'template_name': 'accounts/password_change_done.html',
        },
        name='password_change_done'
    ),
    url(
        r'^password/reset/$',
        auth_views.password_reset,
        kwargs={
            'template_name': 'accounts/password_reset.html',
            'email_template_name': 'accounts/password_reset_email.html',
            'subject_template_name': 'accounts/password_reset_subject.txt',
            'post_reset_redirect': 'accounts:password_reset_done',
        },
        name='password_reset'
    ),
    url(
        r'^password/reset/done/$',
        auth_views.password_reset_done,
        kwargs={
            'template_name': 'accounts/password_reset_done.html',
        },
        name='password_reset_done'
    ),
    url(
        (r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
         '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$'),
        auth_views.password_reset_confirm,
        kwargs={
            'template_name': 'accounts/password_reset_confirm.html',
            'post_reset_redirect': 'accounts:password_reset_complete',
        },
        name='password_reset_confirm'
    ),
    url(
        r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        kwargs={
            'template_name': 'accounts/password_reset_complete.html',
        },
        name='password_reset_complete'
    ),
]
