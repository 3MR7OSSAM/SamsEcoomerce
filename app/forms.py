from flask import request

class ProductForm:
    def __init__(self):
        self.product_name = request.form.get('product_name')
        self.description = request.form.get('description')
        self.image_url = request.form.get('Image')
        self.price = request.form.get('price')
        self.quantity = request.form.get('quantity')
        self.vendor = request.form.get('vendor')

    def __repr__(self):
        return (f"<ProductForm product_name='{self.product_name}', "
                f"description='{self.description[:20]}...', price={self.price}, "
                f"quantity={self.quantity}, vendor='{self.vendor}'>")
