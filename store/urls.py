from django.urls import path
from .views import (
    ItemListView, ItemDetailView, ItemCreatView,
    AddToCartView, ShopListView, ShopDetailView, ShopCreateView,
    OrderDetailView, OrderDetailView2, OrderQuantityUpdateView, AddCouponView, 
    CreateCouponView, CouponDetailView, OrderListView, AddressDefaultAPIView,
    OrderDashboardView,
    AddressListView, AddressCreateView, AddressUpdateView, AddressDeleteView, AddressDetailView,
    OrderItemDeleteView, OrderItemListView, OrderUpdateView, PaymentListView, PaymentView
)

urlpatterns = [
    path('api/addresses/', AddressListView.as_view(), name='address-list'),
    path('api/addresses/create/', AddressCreateView.as_view(), name='address-create'),
    path('api/addresses/<pk>/update/', AddressUpdateView.as_view(), name='address-update'),
    path('api/addresses/<pk>/defualt/', AddressDefaultAPIView.as_view()),
    path('api/addresses/<pk>/delete/',AddressDeleteView.as_view(), name='address-delete'),
    path('api/addresses/<pk>/detail/',AddressDetailView.as_view()),

    path('api/shops/', ShopListView.as_view()),
    path('api/shops-create/', ShopCreateView.as_view()),
    path('api/shop-detail/', ShopDetailView.as_view()),
    path('api/products/', ItemListView.as_view()),
    path('api/products-create/', ItemCreatView.as_view()),
    path('api/products/<pk>/', ItemDetailView.as_view()),

    path('api/add-to-cart/<pk>/', AddToCartView.as_view(), name='add-to-cart'),
    path('api/order-summary/', OrderDetailView.as_view(), name='order-summary'),
    path('api/order-detail/<pk>/', OrderDetailView2.as_view()),
    path('api/checkout/', PaymentView.as_view(), name='checkout'),

    path('api/create-coupon/', CreateCouponView.as_view()),
    path('api/detail-coupon/<pk>/', CouponDetailView.as_view()),
    path('api/add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    
    path('api/order-items-list/', OrderItemListView.as_view()),
    path('api/order-items/<pk>/delete/', OrderItemDeleteView.as_view(), name='order-item-delete'),
    path('api/order-item/update-quantity/<pk>/', OrderQuantityUpdateView.as_view()),
    
    path('api/order-list/', OrderListView.as_view()),
    path('api/order-dash/', OrderDashboardView.as_view()),
    path('api/order/<pk>/', OrderUpdateView.as_view()),
    path('api/payments/', PaymentListView.as_view(), name='payment-list'),
]