from django.db import models

# Create your models here.



class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TableCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Table(models.Model):
    id = models.BigAutoField(primary_key=True)

    category = models.ForeignKey(
        TableCategory,
        on_delete=models.PROTECT,
        related_name='tables'
    )

    table_number = models.CharField(
        max_length=50,
        unique=True
    )

    capacity = models.PositiveIntegerField()

    location = models.CharField(max_length=150)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['table_number']

    def __str__(self):
        return f"Table {self.table_number}"


class ReservationStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Reservation(models.Model):
    id = models.BigAutoField(primary_key=True)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='reservations'
    )

    table = models.ForeignKey(
        Table,
        on_delete=models.PROTECT,
        related_name='reservations'
    )

    reservation_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    guests = models.PositiveIntegerField()

    status = models.ForeignKey(
        ReservationStatus,
        on_delete=models.PROTECT,
        related_name='reservations'
    )

    notes = models.TextField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-reservation_date', 'start_time']

    def __str__(self):
        return (
            f"{self.customer} - "
            f"Table {self.table.table_number} - "
            f"{self.reservation_date}"
        )


class Payment(models.Model):

    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('FAILED', 'Failed'),
        ('REFUNDED', 'Refunded'),
    ]

    id = models.BigAutoField(primary_key=True)

    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = models.CharField(max_length=50)

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='PENDING'
    )

    paid_at = models.DateTimeField(
        null=True,
        blank=True
    )

    transaction_ref = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Payment #{self.id} - {self.amount}"


class AuditLog(models.Model):
    id = models.BigAutoField(primary_key=True)

    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name='audit_logs'
    )

    action = models.CharField(max_length=100)

    performed_by = models.CharField(
        max_length=100
    )

    action_time = models.DateTimeField(
        auto_now_add=True
    )

    details = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-action_time']

    def __str__(self):
        return f"{self.action} - Reservation #{self.reservation.id}"