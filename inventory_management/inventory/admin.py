from django.contrib import admin
from .models import Category, Supplier, Product


# Register the Category model with basic settings
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")  # Fields displayed in the list view
    search_fields = ("name",)  # Enables searching by name


# Register the Supplier model with additional fields in the list view
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_info", "address", "payment_terms")
    search_fields = ("name", "contact_info")  # Allows searching by name or contact info


# Register the Product model with comprehensive list display and filters
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "supplier",
        "cost_price",
        "sell_price",
        "stock_quantity",
        "SKU",
    )
    search_fields = ("name", "SKU")  # Allows searching by product name or SKU
    list_filter = (
        "category",
        "supplier",
    )  # Adds filters for category and supplier in the admin sidebar
