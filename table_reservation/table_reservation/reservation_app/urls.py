from django.urls import path

from . import views


app_name = 'reservation_app'


urlpatterns = [

    # =====================================================
    # CUSTOMER
    # =====================================================

    path(
        'customers/',
        views.customer_list,
        name='customer-list'
    ),

    path(
        'customers/add/',
        views.customer_create,
        name='customer-create'
    ),

    path(
        'customers/<int:pk>/',
        views.customer_detail,
        name='customer-detail'
    ),

    path(
        'customers/<int:pk>/edit/',
        views.customer_update,
        name='customer-update'
    ),

    path(
        'customers/<int:pk>/delete/',
        views.customer_delete,
        name='customer-delete'
    ),


    # =====================================================
    # TABLE CATEGORY
    # =====================================================

    path(
        'table-categories/',
        views.table_category_list,
        name='table-category-list'
    ),

    path(
        'table-categories/add/',
        views.table_category_create,
        name='table-category-create'
    ),

    path(
        'table-categories/<int:pk>/',
        views.table_category_detail,
        name='table-category-detail'
    ),

    path(
        'table-categories/<int:pk>/edit/',
        views.table_category_update,
        name='table-category-update'
    ),

    path(
        'table-categories/<int:pk>/delete/',
        views.table_category_delete,
        name='table-category-delete'
    ),


    # =====================================================
    # TABLE
    # =====================================================

    path(
        'tables/',
        views.table_list,
        name='table-list'
    ),

    path(
        'tables/add/',
        views.table_create,
        name='table-create'
    ),

    path(
        'tables/<int:pk>/',
        views.table_detail,
        name='table-detail'
    ),

    path(
        'tables/<int:pk>/edit/',
        views.table_update,
        name='table-update'
    ),

    path(
        'tables/<int:pk>/delete/',
        views.table_delete,
        name='table-delete'
    ),


    # =====================================================
    # RESERVATION STATUS
    # =====================================================

    path(
        'reservation-statuses/',
        views.reservation_status_list,
        name='reservation-status-list'
    ),

    path(
        'reservation-statuses/add/',
        views.reservation_status_create,
        name='reservation-status-create'
    ),

    path(
        'reservation-statuses/<int:pk>/edit/',
        views.reservation_status_update,
        name='reservation-status-update'
    ),

    path(
        'reservation-statuses/<int:pk>/delete/',
        views.reservation_status_delete,
        name='reservation-status-delete'
    ),


    # =====================================================
    # RESERVATION
    # =====================================================

    path(
        'reservations/',
        views.reservation_list,
        name='reservation-list'
    ),

    path(
        'reservations/add/',
        views.reservation_create,
        name='reservation-create'
    ),

    path(
        'reservations/<int:pk>/',
        views.reservation_detail,
        name='reservation-detail'
    ),

    path(
        'reservations/<int:pk>/edit/',
        views.reservation_update,
        name='reservation-update'
    ),

    path(
        'reservations/<int:pk>/cancel/',
        views.reservation_cancel,
        name='reservation-cancel'
    ),


    # =====================================================
    # PAYMENT
    # =====================================================

    path(
        'payments/',
        views.payment_list,
        name='payment-list'
    ),

    path(
        'payments/add/',
        views.payment_create,
        name='payment-create'
    ),

    path(
        'payments/<int:pk>/',
        views.payment_detail,
        name='payment-detail'
    ),

    path(
        'payments/<int:pk>/edit/',
        views.payment_update,
        name='payment-update'
    ),


    # =====================================================
    # AUDIT LOG
    # =====================================================

    path(
        'audit-logs/',
        views.audit_log_list,
        name='audit-log-list'
    ),

    path(
        'audit-logs/<int:pk>/',
        views.audit_log_detail,
        name='audit-log-detail'
    ),
]