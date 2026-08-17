from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

# Create your views here.

from .models import (
    Customer,
    TableCategory,
    Table,
    ReservationStatus,
    Reservation,
    Payment,
    AuditLog,
)

from .forms import (
    CustomerForm,
    TableCategoryForm,
    TableForm,
    ReservationStatusForm,
    ReservationForm,
    PaymentForm,
)


# ============================================================
# CUSTOMER
# ============================================================

def customer_list(request):
    customers = Customer.objects.all()

    data = [
        {
            'id': customer.id,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'email': customer.email,
            'phone': customer.phone,
        }
        for customer in customers
    ]

    return JsonResponse(data, safe=False)


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    return JsonResponse({
        'id': customer.id,
        'first_name': customer.first_name,
        'last_name': customer.last_name,
        'email': customer.email,
        'phone': customer.phone,
    })


@require_http_methods(["POST"])
def customer_create(request):
    form = CustomerForm(request.POST)

    if form.is_valid():
        customer = form.save()

        return JsonResponse({
            'message': 'Customer created successfully.',
            'id': customer.id,
        }, status=201)

    return JsonResponse({
        'errors': form.errors
    }, status=400)


@require_http_methods(["POST"])
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    form = CustomerForm(
        request.POST,
        instance=customer
    )

    if form.is_valid():
        customer = form.save()

        return JsonResponse({
            'message': 'Customer updated successfully.',
            'id': customer.id,
        })

    return JsonResponse({
        'errors': form.errors
    }, status=400)


@require_http_methods(["POST", "DELETE"])
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    customer.delete()

    return JsonResponse({
        'message': 'Customer deleted successfully.'
    })


# ============================================================
# TABLE CATEGORY
# ============================================================

def table_category_list(request):
    categories = TableCategory.objects.all()

    data = [
        {
            'id': category.id,
            'name': category.name,
            'description': category.description,
            'is_active': True,
        }
        for category in categories
    ]

    return JsonResponse(data, safe=False)


def table_category_detail(request, pk):
    category = get_object_or_404(
        TableCategory,
        pk=pk
    )

    return JsonResponse({
        'id': category.id,
        'name': category.name,
        'description': category.description,
    })


@require_http_methods(["POST"])
def table_category_create(request):
    form = TableCategoryForm(request.POST)

    if form.is_valid():
        category = form.save()

        return JsonResponse({
            'message': 'Table category created successfully.',
            'id': category.id,
        }, status=201)

    return JsonResponse({
        'errors': form.errors
    }, status=400)


@require_http_methods(["POST"])
def table_category_update(request, pk):
    category = get_object_or_404(
        TableCategory,
        pk=pk
    )

    form = TableCategoryForm(
        request.POST,
        instance=category
    )

    if form.is_valid():
        category = form.save()

        return JsonResponse({
            'message': 'Table category updated successfully.',
            'id': category.id,
        })

    return JsonResponse({
        'errors': form.errors
    }, status=400)


@require_http_methods(["POST", "DELETE"])
def table_category_delete(request, pk):
    category = get_object_or_404(
        TableCategory,
        pk=pk
    )

    category.delete()

    return JsonResponse({
        'message': 'Table category deleted successfully.'
    })


# ============================================================
# TABLE
# ============================================================

def table_list(request):
    tables = Table.objects.select_related('category').all()

    data = [
        {
            'id': table.id,
            'category_id': table.category.id,
            'category': table.category.name,
            'table_number': table.table_number,
            'capacity': table.capacity,
            'location': table.location,
            'is_active': table.is_active,
        }
        for table in tables
    ]

    return JsonResponse(data, safe=False)


def table_detail(request, pk):
    table = get_object_or_404(
        Table.objects.select_related('category'),
        pk=pk
    )

    return JsonResponse({
        'id': table.id,
        'category_id': table.category.id,
        'category': table.category.name,
        'table_number': table.table_number,
        'capacity': table.capacity,
        'location': table.location,
        'is_active': table.is_active,
    })


@require_http_methods(["POST"])
def table_create(request):
    form = TableForm(request.POST)

    if form.is_valid():
        table = form.save()

        return JsonResponse({
            'message': 'Table created successfully.',
            'id': table.id,
        }, status=201)

    return JsonResponse({
        'errors': form.errors
    }, status=400)


@require_http_methods(["POST"])
def table_update(request, pk):
    table = get_object_or_404(
        Table,
        pk=pk
    )

    form = TableForm(
        request.POST,
        instance=table
    )

    if form.is_valid():
        table = form.save()

        return JsonResponse({
            'message': 'Table updated successfully.',
            'id': table.id,
        })

    return JsonResponse({
        'errors': form.errors
    }, status=400)


@require_http_methods(["POST", "DELETE"])
def table_delete(request, pk):
    table = get_object_or_404(
        Table,
        pk=pk
    )

    table.delete()

    return JsonResponse({
        'message': 'Table deleted successfully.'
    })


# ============================================================
# RESERVATION STATUS
# ============================================================

def reservation_status_list(request):
    statuses = ReservationStatus.objects.all()

    data = [
        {
            'id': status.id,
            'name': status.name,
            'description': status.description,
            'is_active': status.is_active,
        }
        for status in statuses
    ]

    return JsonResponse(data, safe=False)


@require_http_methods(["POST"])
def reservation_status_create(request):
    form = ReservationStatusForm(request.POST)

    if form.is_valid():
        status = form.save()

        return JsonResponse({
            'message': 'Reservation status created successfully.',
            'id': status.id,
        }, status=201)

    return JsonResponse({
        'errors': form.errors
    }, status=400)


@require_http_methods(["POST"])
def reservation_status_update(request, pk):
    status = get_object_or_404(
        ReservationStatus,
        pk=pk
    )

    form = ReservationStatusForm(
        request.POST,
        instance=status
    )

    if form.is_valid():
        status = form.save()

        return JsonResponse({
            'message': 'Reservation status updated successfully.',
            'id': status.id,
        })

    return JsonResponse({
        'errors': form.errors
    }, status=400)


@require_http_methods(["POST", "DELETE"])
def reservation_status_delete(request, pk):
    status = get_object_or_404(
        ReservationStatus,
        pk=pk
    )

    status.delete()

    return JsonResponse({
        'message': 'Reservation status deleted successfully.'
    })


# ============================================================
# RESERVATION
# ============================================================

def reservation_list(request):
    reservations = Reservation.objects.select_related(
        'customer',
        'table',
        'status'
    ).all()

    customer_id = request.GET.get('customer')
    reservation_date = request.GET.get('reservation_date')

    if customer_id:
        reservations = reservations.filter(
            customer_id=customer_id
        )

    if reservation_date:
        reservations = reservations.filter(
            reservation_date=reservation_date
        )

    data = [
        {
            'id': reservation.id,
            'customer_id': reservation.customer.id,
            'customer': str(reservation.customer),
            'table_id': reservation.table.id,
            'table': reservation.table.table_number,
            'status_id': reservation.status.id,
            'status': reservation.status.name,
            'reservation_date': reservation.reservation_date,
            'start_time': reservation.start_time,
            'end_time': reservation.end_time,
            'guests': reservation.guests,
            'notes': reservation.notes,
        }
        for reservation in reservations
    ]

    for item in data:
        item['reservation_date'] = str(
            item['reservation_date']
        )
        item['start_time'] = str(
            item['start_time']
        )
        item['end_time'] = str(
            item['end_time']
        )

    return JsonResponse(data, safe=False)


def reservation_detail(request, pk):
    reservation = get_object_or_404(
        Reservation.objects.select_related(
            'customer',
            'table',
            'status'
        ),
        pk=pk
    )

    return JsonResponse({
        'id': reservation.id,
        'customer_id': reservation.customer.id,
        'table_id': reservation.table.id,
        'status_id': reservation.status.id,
        'reservation_date': str(
            reservation.reservation_date
        ),
        'start_time': str(
            reservation.start_time
        ),
        'end_time': str(
            reservation.end_time
        ),
        'guests': reservation.guests,
        'notes': reservation.notes,
    })


@require_http_methods(["POST"])
def reservation_create(request):
    form = ReservationForm(request.POST)

    if form.is_valid():
        reservation = form.save()

        AuditLog.objects.create(
            reservation=reservation,
            action='CREATED',
            performed_by='SYSTEM',
            details='Reservation created.'
        )

        return JsonResponse({
            'message': 'Reservation created successfully.',
            'id': reservation.id,
        }, status=201)

    return JsonResponse({
        'errors': form.errors
    }, status=400)


@require_http_methods(["POST"])
def reservation_update(request, pk):
    reservation = get_object_or_404(
        Reservation,
        pk=pk
    )

    form = ReservationForm(
        request.POST,
        instance=reservation
    )

    if form.is_valid():
        reservation = form.save()

        AuditLog.objects.create(
            reservation=reservation,
            action='UPDATED',
            performed_by='SYSTEM',
            details='Reservation updated.'
        )

        return JsonResponse({
            'message': 'Reservation updated successfully.',
            'id': reservation.id,
        })

    return JsonResponse({
        'errors': form.errors
    }, status=400)


@require_http_methods(["POST"])
def reservation_cancel(request, pk):
    reservation = get_object_or_404(
        Reservation,
        pk=pk
    )

    cancelled_status = get_object_or_404(
        ReservationStatus,
        name__iexact='CANCELLED'
    )

    reservation.status = cancelled_status
    reservation.save()

    AuditLog.objects.create(
        reservation=reservation,
        action='CANCELLED',
        performed_by='SYSTEM',
        details='Reservation cancelled.'
    )

    return JsonResponse({
        'message': 'Reservation cancelled successfully.',
        'id': reservation.id,
    })


# ============================================================
# PAYMENT
# ============================================================

def payment_list(request):
    payments = Payment.objects.select_related(
        'reservation'
    ).all()

    reservation_id = request.GET.get('reservation')

    if reservation_id:
        payments = payments.filter(
            reservation_id=reservation_id
        )

    data = [
        {
            'id': payment.id,
            'reservation_id': payment.reservation.id,
            'amount': str(payment.amount),
            'payment_method': payment.payment_method,
            'payment_status': payment.payment_status,
            'paid_at': payment.paid_at,
            'transaction_ref': payment.transaction_ref,
        }
        for payment in payments
    ]

    return JsonResponse(data, safe=False)


def payment_detail(request, pk):
    payment = get_object_or_404(
        Payment,
        pk=pk
    )

    return JsonResponse({
        'id': payment.id,
        'reservation_id': payment.reservation.id,
        'amount': str(payment.amount),
        'payment_method': payment.payment_method,
        'payment_status': payment.payment_status,
        'paid_at': payment.paid_at,
        'transaction_ref': payment.transaction_ref,
    })


@require_http_methods(["POST"])
def payment_create(request):
    form = PaymentForm(request.POST)

    if form.is_valid():
        payment = form.save()

        return JsonResponse({
            'message': 'Payment created successfully.',
            'id': payment.id,
        }, status=201)

    return JsonResponse({
        'errors': form.errors
    }, status=400)


@require_http_methods(["POST"])
def payment_update(request, pk):
    payment = get_object_or_404(
        Payment,
        pk=pk
    )

    form = PaymentForm(
        request.POST,
        instance=payment
    )

    if form.is_valid():
        payment = form.save()

        return JsonResponse({
            'message': 'Payment updated successfully.',
            'id': payment.id,
        })

    return JsonResponse({
        'errors': form.errors
    }, status=400)


# ============================================================
# AUDIT LOG
# ============================================================

def audit_log_list(request):
    logs = AuditLog.objects.select_related(
        'reservation'
    ).all()

    reservation_id = request.GET.get('reservation')

    if reservation_id:
        logs = logs.filter(
            reservation_id=reservation_id
        )

    data = [
        {
            'id': log.id,
            'reservation_id': log.reservation.id,
            'action': log.action,
            'performed_by': log.performed_by,
            'action_time': log.action_time,
            'details': log.details,
        }
        for log in logs
    ]

    return JsonResponse(data, safe=False)


def audit_log_detail(request, pk):
    log = get_object_or_404(
        AuditLog,
        pk=pk
    )

    return JsonResponse({
        'id': log.id,
        'reservation_id': log.reservation.id,
        'action': log.action,
        'performed_by': log.performed_by,
        'action_time': log.action_time,
        'details': log.details,
    })