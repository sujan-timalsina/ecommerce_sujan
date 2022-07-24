# **Lab 3 - Preparing Cart**

## **Objective:**
> 1. To learn about the preparation of Cart for the eCommerce website.
> 2. To learn about the various items and things to be known while developing the Cart.

## **Introduction:**

1. ### **Django Authorization**
    <pre>
        Django comes with a user authentication system. It handles user accounts, groups, permissions and cookie-based user sessions. This section of the documentation explains how the default implementation works out of the box, as well as how to extend and customize it to suit your project’s needs.
    </pre>

2. ### **Login required**
    <pre>
        If the user isn’t logged in, redirect to login_url, passing the current absolute path in the query string. (Example: /accounts/login/?next=/current/path/).
        If the user is logged in, execute the view normally. The view code is free to assume the user is logged in.

    </pre>

3. ### **admin.site.register**
    <pre>
    The inbuilt admin interface is one of the most powerful & popular features of Django.
    Once we create the models, we need to register them with the admin interface, so that it
    can read metadata and populate the interface for it.
    </pre>

## **Procedure:**

1. In the module, open “models.py” and add code for the “cart_item” model. Note:
We use the “user” model from default Django authorization.
2.  Run migrations and ensure database table for the added model is created properly
3. In the database tool, verify that the added table is created properly.
4. Goto “admin.py” and add the following code
from .models import Brand, Category, Product, CartItem
admin.site.register(CartItem)
5.  In “views.py” add the view for “cart”
6.  Run the project and navigate to admin to check the result


## **Conclusion:**
<pre>
    Thus in this lab we got the knowledge of preparing Cart, assembling the cart items, delete/remove operations, add option and manipulation of the cart items. We also got the knowledge about render, redirect and login_required operations to be performed on the Cart.
</pre>