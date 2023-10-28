from django.contrib import admin
from .models import Team,Member,BillMember
# Register your models here.
admin.site.register(Team)
admin.site.register(Member)
admin.site.register(BillMember)
