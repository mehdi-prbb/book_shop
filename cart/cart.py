from products.models import Product


class Cart:
    def __init__(self, request):

        """
        Initialize the cart
        """
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity=1, replace_current_quantity=False):
        """
        Add the specified product to the cart if it exists
        """
        product_slug = str(product.slug)

        if product_slug not in self.cart:
            self.cart[product_slug] = {'quantity' : 0}

        if replace_current_quantity:
            self.cart[product_slug]['quantity'] = quantity
        else:
            self.cart[product_slug]['quantity'] += quantity

        self.save()

    def remove(self, product):
        """
        Remove product from the cart
        """
        product_slug = str(product.slug)

        if product_slug in self.cart:
            del self.cart[product_slug]

            self.save()

    def save(self):
        """
        Mark session as modified to save changes
        """
        self.session.modified = True

    def __iter__(self):

        product_slugs = self.cart.keys()
        products = Product.objects.filter(slug__in=product_slugs)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.slug)]['product_obj'] = product

        for item in cart.values():
            yield item

    def __len__(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']

        self.save()

    def get_total_price(self):
        product_slugs = self.cart.keys()
        products = Product.objects.filter(id__in=product_slugs)

        return sum(product.price for product in products)