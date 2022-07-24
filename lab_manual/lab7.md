# **Lab 7 - Checkout Preparation and Security**

## **Objective:**
> 1.  To learn about the preparation of Checkout for the eCommerce website.
> 2. To learn about the various items and things to be known while developing the Checkout system.

## **Introduction:**

1. ### **Payment Gateway**
    <pre>
        A payment gateway is a technology used by merchants to accept debit or credit card purchases from customers. The term includes not only the physical card-reading devices found in brick-and-mortar retail stores but also the payment processing portals found in online stores. It is the front-end technology responsible for sending customer information to the merchant acquiring bank, where the transaction is then processed.
    </pre>

2. ### **UUID**
    <pre>
        UUIDField is a special field to store universally unique identifiers. It uses Python’s UUID class. UUID, Universal Unique Identifier, is a python library that helps in generating random objects of 128 bits as ids. It provides the uniqueness as it generates ids on the basis of time, Computer hardware.
        field_name = models.UUIDField(**options)
    </pre>

3. ### **Meta**
    <pre>
    In Django, Meta is just used to pass information into the process of creating the _meta Options object
    </pre>

4. ### **Payment Token**
    <pre>
    Tokenization is a process of replacing sensitive information with tokens—random strings of characters. Tokens are used to represent cardholder’s information, such as a 16-digit card number or bank account details during the payment process, so the data are passed through a payment gateway without the card details being exposed.
    </pre>

## **Procedure:**

1.  We are going to define our own payment gateway and pay via it.
2. Let’s add a module payment_module
python manage.py startapp payment_manager
3. Go to settings.py and add the module to INSTALLED_APPS list
4. In the payment_module, open “models.py” and add code for payment_gateway.
5. Ensure database table for added model is created properly.
python manage.py makemigrations payment_module
python manage.py migrate payment_module
6. In database tool, verify that the added table is created properly
7.  Run the server and generate token for payment.

## **Conclusion:**
<pre>
    Thus in this lab we got the knowledge of preparing Checkout System, assembling the checkout variables, generating tokens and building a payment gateway for teh consumer and merchant. We also got the knowledge about UUID, render, redirect and @login_required operations to be performed on the Payment Gateway for Checkout system.
</pre>