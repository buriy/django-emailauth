from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns('emailauth.views',
    url(r'^account/profile/$', 'account', name='emailauth_account'),
    url(r'^register/$', 'register', name='register'),
    url(r'^register/continue/(?P<email>.+)/$', 'register_continue', name='emailauth_register_continue'),
    url(r'^verify/(?P<verification_key>\w+)/$', 'verify', name='emailauth_verify'),
    url(r'^resetpassword/$', 'request_password_reset', name='emailauth_request_password_reset'),
    url(r'^resetpassword/continue/(?P<email>.+)/$', 'request_password_reset_continue', 
        name='emailauth_request_password_reset_continue'),
    url(r'^resetpassword/(?P<reset_code>\w+)/$', 'reset_password', name='emailauth_reset_password'),

    url(r'^account/addemail/$', 'add_email', name='emailauth_add_email'),
    url(r'^account/addemail/continue/(?P<email>.+)/$', 'add_email_continue', name='emailauth_add_email_continue'),
    url(r'^account/resendemail/(\d+)/$', 'resend_verification_email', name='emailauth_resend_verification_email'),

    url(r'^account/changeemail/$', 'change_email', name='emailauth_change_email'),
    url(r'^account/changeemail/continue/(?P<email>.+)/$', 'change_email_continue', name='emailauth_change_email_continue'),

    url(r'^account/deleteemail/(\d+)/$', 'delete_email', name='emailauth_delete_email'),
    url(r'^account/setdefaultemail/(\d+)/$', 'set_default_email', name='emailauth_set_default_email'),
    url(r'^login/$', 'login', name='login'),
) + patterns('django.contrib.auth.views',
    url(r'^logout/$', 'logout', {'next_page': '/', 'template_name': 'logged_out.html'}, name='logout'),
)
