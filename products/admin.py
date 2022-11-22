from django.contrib import admin

from .models import Category, Product, Choices, Mobile, Laptop


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'created_at', 'active']


class MobileChoicesInline(admin.TabularInline):
    model = Mobile.choices.through
    extra = 1


@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'get_price', 'get_create_time',
                     'get_modified_time', 'get_status' ]
    def get_queryset(self, request):
        return super(MobileAdmin,self).get_queryset(request).select_related('product')

    @admin.display(description='Title')
    def get_name(self, obj):
        return obj.product.title

    @admin.display(description='price')
    def get_price(self, obj):
        return obj.product.price

    @admin.display(description='active')
    def get_status(self, obj):
        return obj.product.active

    @admin.display(description='created_at')
    def get_create_time(self, obj):
        return obj.product.created_at

    @admin.display(description='modified_at')
    def get_modified_time(self, obj):
        return obj.product.modified_at

    inlines = [MobileChoicesInline, ]
    exclude = ['choices']

admin.site.register(Choices)


class LaptopChoicesInline(admin.TabularInline):
    model = Laptop.choices.through
    extra = 1

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'get_price', 'get_create_time',
                     'get_modified_time', 'get_status' ]
                     
    def get_queryset(self, request):
        return super(LaptopAdmin,self).get_queryset(request).select_related('product')

    @admin.display(description='Title')
    def get_name(self, obj):
        return obj.product.title

    @admin.display(description='price')
    def get_price(self, obj):
        return obj.product.price

    @admin.display(description='active')
    def get_status(self, obj):
        return obj.product.active

    @admin.display(description='created_at')
    def get_create_time(self, obj):
        return obj.product.created_at

    @admin.display(description='modified_at')
    def get_modified_time(self, obj):
        return obj.product.modified_at

    inlines = [LaptopChoicesInline, ]
    exclude = ['choices']