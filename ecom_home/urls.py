from django.contrib import admin
from django.urls import path,include
from ecom_home import views
from .views import*
from ecom_home.api import urls
# from ecom_home.api import ulrs 
 
app_name = 'ecom_home'

urlpatterns = [
    # rest frame_work


    # path('api/item/' ,include(ecom_home_api.ulrs, 'item_api')),
    path('api/v1/',include('ecom_home.api.urls',namespace='item_api')),
    # path('',views.indexView.as_view(),name='home'),
    path('adminn/',views.adminn,name='adminn'),
    # path('Home',indexView.as_view(),name='home'),
    path('signup',views.signup,name='signup'),
    # path('product/<slug>/',productsDetailView.as_view(),name='product'),
    path('sell_with_us',views.sell_with_us,name='sell_with_us'),
    path('calculater',views.calculater,name='calculater'),
    path('be_seller_approve/', views.be_seller_approve, name='be_seller_approve'),
    path('login',views.login,name='login'),
    path('product_listing',views.product_listing,name='product_listing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('draft/', views.draft, name='draft'),
    path('update_profile/', views.update_profile, name='update_profile'),
    # 
    path('cart/', cart.as_view(), name='cart'),
    path('testadd/', testadd, name='testadd'),
    path('checkout1/', checkout, name='checkout'),
    path('checknavbarout1/', navbar, name='navbar'),
    # 
    path('pending/', views.pending, name='pending'),
    path('approved/', views.approved, name='approved'),
    path('Inventory/', views.Inventory, name='Inventory'),
    path('Inventory_search/', views.Inventory_search, name='Inventory_search'),
    path('Orders/', views.Orders, name='Orders'),
    path('Orders_details/', views.Orders_details, name='Orders_details'),
    path('New_Orders/', views.New_Orders, name='New_Orders'),
    path('New_Orders_details/', views.New_Orders_details, name='New_Orders_details'),
    path('Shipped/', views.Shipped, name='Shipped'),
    path('Shipped_details/', views.Shipped_details, name='Shipped_details'),
    path('Pending_Orders/', views.Pending_Orders, name='Pending_Orders'),
    path('Pending_Orders_details/', views.Pending_Orders_details, name='Pending_Orders_details'),
    path('Cancelled/', views.Cancelled, name='Cancelled'),
    path('Cancelled_details/', views.Cancelled_details, name='Cancelled_details'),
    path('Return/', views.Return, name='Return'),
    path('Return_details/', views.Return_details, name='Return_details'),
    path('draft_detail/<slug_by_seller>/', views.draft_detail, name='draft_detail'),
    # path('draft_detail/<slug_by_seller>/', draft_detail.as_view, name='draft_detail'),
    # path('dashboard/', SellerDashboard.as_view(), name='dashboard'),

    path('profile/',views.profile,name='profile'),
    path('seller_account/',views.be_seller,name='Seller_account'),
    # path('review_seller_product1/<slug_by_seller>/',views.review_seller_product1,name='review_seller_product1'),
    path('review_seller_product/<slug_by_seller>/', review_seller_product , name='review_seller_product'),
    path('list_of_pro/',views.list_of_pro,name='list_of_pro'),
    path('Category',views.Category,name='Category'),
    path('Sub_Category/<Category>/',views.Sub_Category,name='Sub_Category'),
    path('Type/<Sub_Category>/',views.Type,name='Type'),
    path('seller_product_post/<Type>/',views.seller_product_post,name='seller_product_post'),
    path('', indexView.as_view(), name='home'),
    path('Home', indexView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    # path('review_seller_product1/<slug_by_seller>/', review_seller_product1, name='review_seller_product1'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    # path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
        name='remove-single-item-from-cart'),
    # path('payment/', PaymentView.as_view(), name='payment'),
    # path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
