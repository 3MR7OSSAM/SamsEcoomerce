# Flask API Documentation

## Overview
This Flask application serves as a product management system that allows users to perform CRUD operations on products, view data in table format, and access API endpoints. It integrates a SQL database with Flask and utilizes Pandas for data processing and HTML rendering.

---

## Endpoints

### 1. `GET /`
**Description:** Displays the homepage with a form to add new products.

**Methods:**
- GET: Renders the `home.html` template with a product form.
- POST: Processes form data to create a new product.

**Input (POST):**
- `product_name`: Name of the product (string).
- `description`: Product description (string).
- `image_url`: URL to the product image (string).
- `price`: Price of the product (float).
- `quantity`: Available quantity (integer).

**Response:** Redirects to the homepage after adding the product.

---

### 2. `POST /add_product`
**Description:** Adds a product using form data submitted directly.

**Methods:**
- POST: Processes raw form data to add a new product to the database.

**Input:**
- `product_name` (string).
- `description` (string).
- `image_url` (string).
- `price` (float).
- `quantity` (integer).
- `vendor` (string).

**Response:** Redirects to the homepage.

---

### 3. `GET /api/product-data`
**Description:** Provides product data as JSON for API consumers.

**Methods:**
- GET: Calls the `load_data` function and returns a JSON response.

**Response:**
- JSON array of product data:
  ```json
  [
    {
      "Product Name": "Example",
      "Description": "Description here",
      "Price": 10.99,
      "Quantity": 5,
      "Vendor": "Vendor Name"
    }
  ]
  ```

---

### 4. `GET /dataframes`
**Description:** Displays all product data in a table format.

**Methods:**
- GET: Queries the database for all products, converts the data to a Pandas DataFrame, and renders an HTML table in `dataframes.html`.

**Response:**
- HTML table containing product details.

---

### 5. `GET, POST /delete_product/<int:product_id>`
**Description:** Deletes a product by its ID.

**Methods:**
- GET/POST: Deletes the specified product from the database if it exists.

**Path Parameter:**
- `product_id`: ID of the product to delete.

**Response:**
- Redirects to the `/dataframes` endpoint with a success or error flash message.

---

### 6. `GET, POST /edit_product/<int:product_id>`
**Description:** Allows editing of an existing product.

**Methods:**
- GET: Pre-populates a form with the product's current data.
- POST: Updates the product in the database with the new data.

**Path Parameter:**
- `product_id`: ID of the product to edit.

**Input (POST):**
- `product_name`: Updated name of the product (string).
- `description`: Updated product description (string).
- `image_url`: Updated URL to the product image (string).
- `price`: Updated price of the product (float).
- `quantity`: Updated available quantity (integer).
- `vendor`: Updated vendor name (string).

**Response:** Redirects to the `/dataframes` endpoint.

---

## Additional Features

### Data Loading Utility
**Function:** `load_data`

**Description:**
- A utility function to load data into Pandas DataFrames.

**Usage:**
- Utilized in the `/api/product-data` endpoint to provide a JSON representation of data.

---

## Templates

1. **`home.html`:**
   - Displays a form for adding products.

2. **`dataframes.html`:**
   - Displays product data as an HTML table.

3. **`editproduct.html`:**
   - Displays a form to edit product details.

---

## Database Model

### Product
Fields:
- `product_id`: Integer (Primary Key).
- `product_name`: String.
- `description`: String.
- `image`: String (URL to product image).
- `price`: Float.
- `quantity`: Integer.
- `vendor`: String.
- `created_at`: DateTime (automatically set).
- `updated_at`: DateTime (automatically set).

---

## Flash Messages

- Success and error messages are used in the delete and edit endpoints to provide user feedback.

---

## Dependencies

- Flask
- SQLAlchemy
- Pandas
- Flask-WTF

---

## Running the Application

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   flask run
   ```

---

## Repository Images

### Image Previews

#### 1. Screenshot of Feature 1:
<div align="center">
  <img src="https://github.com/user-attachments/assets/d51763c8-fcc8-438f-9c01-70e0b3f81611" width="500px">
</div>

#### 2. Screenshot of Feature 2:
<div align="center">
  <img src="https://github.com/user-attachments/assets/5b20407b-0133-44f5-8df4-cf508241b773" width="500px">
</div>

#### 3. Screenshot of Feature 3:
<div align="center">
  <img src="https://github.com/user-attachments/assets/8d6fc61b-4194-4f3d-afb1-7cf0bb6f3561" width="500px">
</div>

