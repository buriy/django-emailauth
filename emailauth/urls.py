from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns('emailauth.views',
    url(r'^account/profile/$', 'account', name='ea_account'),
    url(r'^register/$', 'register', name='register'),
    url(r'^register/continue/(?P<email>.+)/$', 'register_continue', name='ea_register_continue'),
    url(r'^verify/(?P<verification_key>\w+)/$', 'verify', name='ea_verify'),
    url(r'^resetpassword/$', 'request_password_reset', name='ea_request_password_reset'),
    url(r'^resetpassword/continue/(?P<email>.+)/$', 'request_password_reset_continue', 
        name='ea_request_password_reset_continue'),
    url(r'^resetpassword/(?P<reset_code>\w+)/$', 'reset_password', name='ea_reset_password'),

    url(r'^account/addemail/$', 'add_email', name='ea_add_email'),
    url(r'^account/addemail/continue/(?P<email>.+)/$', 'add_email_continue', name='ea_add_email_continue'),
    url(r'^account/resendemail/(\d+)/$', 'resend_verification_email', name='ea_resend_verification_email'),

    url(r'^account/changeemail/$', 'change_email', name='ea_change_email'),
    url(r'^account/changeemail/continue/(?P<email>.+)/$', 'change_email_continue', name='ea_change_email_continue'),

    url(r'^account/deleteemail/(\d+)/$', 'delete_email', name='ea_delete_email'),
    url(r'^account/setdefaultemail/(\d+)/$', 'set_default_email', name='ea_set_default_email'),
    url(r'^login/$', 'login', name='login'),
) + patterns('django.contrib.auth.views',
    url(r'^logout/$', 'logout', {'next_page': '/', 'template_name': 'logged_out.html'}, name='logout'),
)
