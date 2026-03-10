from django.contrib import admin
from .models import Seating, Table, Reservation

# Register your models here.
class SeatingAdmin(admin.ModelAdmin):
    model = Seating
    list_display = ('seating', 'id', 'capacity', 'bar')

class TableAdmin(admin.ModelAdmin):
    model = Table
    list_display = ('id', 'table_type','table_type__bar')

    def table_type__bar(self, obj):
        return obj.table_type.bar


class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ('id', 'hopper', 'date', 'start_time', 'end_time')


admin.site.register(Seating, SeatingAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Reservation, ReservationAdmin)
