from django.contrib import admin
from .models import crypto_model , connection_model , mobile_number_model , price_model

admin.site.register(crypto_model)
admin.site.register(connection_model)
admin.site.register(mobile_number_model)
admin.site.register(price_model)