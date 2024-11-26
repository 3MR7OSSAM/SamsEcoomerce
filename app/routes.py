from flask import Blueprint, render_template, request, redirect, url_for, jsonify, current_app,flash

from app import db
import pandas as pd
from app.models import Product
from app.forms import ProductForm  # Adjusted to use the simple form class
from app.data_loader import load_data  # Import the load_data function


main = Blueprint('main', __name__)
@main.route('/', methods=['GET', 'POST'])
def home():
    form = ProductForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_product = Product(
            product_name=form.product_name.data,
            description=form.description.data,
            Image = form.image_url.data,
            price=form.price.data,
            quantity=form.quantity.data
        )
        print(new_product)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('home.html', form=form)


@main.route('/add_product', methods=['POST'])
def add_product():
    # Get form data
    product_name = request.form.get('product_name')
    description = request.form.get('description')
    imageUrl = request.form.get('image_url')  # Correctly capture the image URL
    price = request.form.get('price', type=float)
    quantity = request.form.get('quantity', type=int)
    vendor = request.form.get('vendor')

    # Create a new product object
    new_product = Product(
        product_name=product_name,
        description=description,
        image=imageUrl,  # Assign imageUrl to the Image attribute
        price=price,
        quantity=quantity,
        vendor=vendor
    )

    # Save to database
    db.session.add(new_product)
    db.session.commit()

    return redirect(url_for('main.home'))

@main.route('/api/product-data', methods=['GET'])
def get_product_data():
    product_data = load_data()  # Your data-loading function
    print(product_data) # Your
    return jsonify(product_data.to_dict(orient='records'))


# @main.route('/load_data')
# def load_data_route():
#     customers_df, orders_df, order_items_df, products_df, suppliers_df = load_data()
#     # Here, you can do something with the DataFrames, like pass them to a template or process them further.
#     return "Data loaded successfully!"  # or render a template

@main.route('/dataframes')
def display_dataframes():
    # Query all products from the database
    products = Product.query.all()

    if not products:
        return render_template('dataframes.html', product_table="<p>No products available.</p>")

    # Convert the list of products to a pandas DataFrame
    product_data = {
        'Product ID': [product.product_id for product in products],
        'Product Name': [product.product_name for product in products],
        'Description': [product.description for product in products],
        'Price': [product.price for product in products],
        'Quantity': [product.quantity for product in products],
        'Vendor': [product.vendor for product in products],
        'Created At': [product.created_at for product in products],
        'Updated At': [product.updated_at for product in products],
    }
    product_df = pd.DataFrame(product_data)

    # Convert the DataFrame to an HTML table
    product_html = product_df.to_html(classes='table table-striped', index=False)

    # Render the template and pass the table HTML to it
    return render_template('dataframes.html', product_table=product_html)



@main.route('/delete_product/<int:product_id>', methods=['GET', 'POST'])
def delete_product(product_id):
    product = Product.query.get(product_id)  # Check if the product exists
    if not product:
        # Flash an error message if the product doesn't exist
        flash(f'Product with ID {product_id} does not exist.', 'error')
        return redirect(url_for('main.display_dataframes'))
    
    # If the product exists, proceed to delete it
    db.session.delete(product)
    db.session.commit()
    flash(f'Product with ID {product_id} has been successfully deleted.', 'success')
    return redirect(url_for('main.display_dataframes'))




@main.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)  # Pre-populate form with product data

    if request.method == 'POST' and form.validate_on_submit():
        product.product_name = form.product_name.data
        product.description = form.description.data
        product.image = form.image_url.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        product.vendor = form.vendor.data

        db.session.commit()
        return redirect(url_for('main.display_dataframes'))

    return render_template('editproduct.html', form=form, product_id=product_id)
