from home.models import Product

# Inserting new record into product model
x = Product(product_name = "Bag", product_price = "300")
x.save()


# To get all the records in a table
all_entries = Product.object.all()


# To filter products by their name
Product.objects.filter(product_name = "Bag")


# To get a single product from the product table
one_entry = Product.object.get(1)
# then input
one_entry


# To change a product price
y = one_entry.product_price("400")
y.save()