from django.db import models
from django.utils.text import slugify
from colorfield.fields import ColorField


class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children',
                                on_delete=models.CASCADE,
                                null=True, blank=True)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True,
                             editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = 'categories'

    def __str__(self):                           
        full_path = [self.title]             
        parent_name = self.parent
        while parent_name is not None:
            full_path.append(parent_name.title)
            parent_name = parent_name.parent
        return ' -> '.join(full_path[::-1])


class Product(models.Model):

    """ This class is for getting the general features of the products. """

    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True,
                             editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='products_cover/')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('slug', 'title',)

    def __str__(self):
        return self.title


class Mobile(models.Model):
    product = models.ForeignKey(Product, related_name='mobiles',
                                 on_delete=models.CASCADE)
    screen_technology = models.CharField(max_length=100, null=True, blank=True)
    size = models.FloatField(null=True, blank=True)
    networks = models.CharField(max_length=100, null=True, blank=True)
    internal_memory = models.CharField(max_length=100, null=True, blank=True)
    ram = models.CharField(max_length=100, null=True, blank=True)
    os_version = models.CharField(max_length=100, null=True, blank=True)
    camera = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.product.title


class Choices(models.Model):
    mobile = models.ForeignKey(Mobile, related_name='mobile_colors',
                                 on_delete=models.CASCADE, default='10')
    color_name = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.color_name
