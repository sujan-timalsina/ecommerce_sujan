from django.contrib import admin

# Register your models here.
from .models import PaymentGateway, Invoice, InvoiceDetail


class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = ["token", "balance", "expiry_date", "is_active", ]
    search_fields = ["token", ]

    class Meta:
        model = PaymentGateway


admin.site.register(PaymentGateway, PaymentGatewayAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["user", "token", "payment_date", "total_amount", ]
    search_fields = ["token", ]

    class Meta:
        model = Invoice


admin.site.register(Invoice, InvoiceAdmin)


class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ["invoice", "product", "quantity", "sub_amount", ]
    search_fields = ["invoice", ]

    class Meta:
        model = InvoiceDetail


admin.site.register(InvoiceDetail, InvoiceDetailAdmin)
