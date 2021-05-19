from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    """
        A model to link a user to bookmarked product
    """
    user = models.OneToOneField(
        UserProfile, null=False, blank=False, related_name='wishlist',
        on_delete=models.CASCADE)

    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    """
        A many to many model to bookmark products
    """
    wishlist = models.ForeignKey(
        Wishlist, null=False, blank=False, related_name='wishlist_items',
        on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=False, blank=False, related_name='wishlist_products',
        on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
