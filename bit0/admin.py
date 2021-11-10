from django.contrib import admin
from .models import crypto_model , connection_model

admin.site.register(crypto_model)
admin.site.register(connection_model)
