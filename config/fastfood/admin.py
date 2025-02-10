from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Theme)
admin.site.register(Comment)
admin.site.register(Reply_to_Comment)
