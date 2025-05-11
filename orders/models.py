from django.db import models

class Stall(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    stall = models.ForeignKey(Stall, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)  # 👈 New field
    delivery_type = models.CharField(max_length=50, choices=[('pickup', 'Pickup'), ('delivery', 'Delivery')])
    is_paid = models.BooleanField(default=False)
    is_ready = models.BooleanField(default=False)
    order_time = models.DateTimeField(auto_now_add=True)
    

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PREPARING', 'Preparing'),
        ('READY', 'Ready'),
        ('COMPLETED', 'Completed'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    def __str__(self):
        return f"{self.customer_name} - {self.menu_item.name} x{self.quantity}"
