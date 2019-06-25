from django.contrib import admin

from .models import Rate
from .models import Transaction

# Register model
admin.site.register(Rate)
admin.site.register(Transaction)


