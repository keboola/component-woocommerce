# KBC Component

WooCommerce Extractor for Keboola Connection. Download all data under Orders, Products, and Customer hierarchies.

**Table of contents:**

[TOC]

## Background

WooCommerce is a customizable, open-source eCommerce platform built on WordPress that allows anyone to set up an online store and sell their products.

## Requirements

To enable this application you need to:

- API Version: v3
- [Rest API Keys](https://woocommerce.github.io/woocommerce-rest-api-docs/#authentication)
- [Rest API Secret](https://woocommerce.github.io/woocommerce-rest-api-docs/#authentication)

## Generating API keys

To create or manage keys for a specific WordPress user, go to WooCommerce admin interface > Settings > API > Keys/Apps.
Click the "Add Key" button. In the next screen, add a description and select the WordPress user you would like to generate the key for
Choose the level of access for this REST API key, which can be Read access. Then click the "Generate API Key" button and WooCommerce will generate REST API keys
These two keys are your Consumer Key and Consumer Secret.

## Configuration

To download data form WooCommerce we need to configure

### `Store_url`

Website Domain name where WooCommerce is hosted. e.g. https://myshop.com

### `consumer_key`

Rest API Consumer Key from WooCommerce Admin panel

### `consumer_secret`

Rest API Consumer Secret from WooCommerce Admin panel

### `date_from`

Inclusive Date in YYYY-MM-DD format or a string i.e. 5 days ago, 1 month ago, yesterday, etc.

### `date_to`

Exclusive Date in YYYY-MM-DD format or a string i.e. 5 days ago, 1 month ago, yesterday, etc.

### `load_type`

If set to Incremental update, the result tables will be updated based on primary key. Full load overwrites the destination table each time. NOTE: If you wish to remove deleted records, this needs to be set to Full load and the Period from attribute empty.

### `endpoint`

To fetch data from selected endpoints i.e. Customers, Orders and Products. Default selection is all
i.e.

- Orders endpoint list all orders for give date range
- Products endpoint list all Products for given date range
- Customers endpoint list all customers

__NOTE:__ **The date selection does not affect Customers endpoint**

## Foreign Key Relations for nested objects

For example in the `product` hierarchy, each child table contains a `product_id` column as a foreign key reference to 
the parent `product` table:

- In `products` table columns will be `["id", "name", "description", "dimensions__length", "dimensions__width", "related_ids"]`

- In `products__category` table columns will be `["id", "name", "slug", "product_id"]`

- In `products__images` table columns will be `["id", "src", "name", "product_id"]`

- In `products__attributes` table columns will be `["id", "name", "options", "product_id"]`

i.e. the `product` may be joined to its attributes by `product.id` = `products__attributes.id`. 

### Hierarchy of output tables

```bash
tables
├── customer
│   └── customer__metadata
├── order
│   ├── order__coupon_lines
│   │   └── order__coupon_lines__meta_data
│   ├── order__fee_lines
│   │   ├── order__fee_lines__meta_data
│   │   └── order__fee_lines__taxes
│   ├── order__line_items
│   │   ├── order__line_items__meta_data
│   │   └── order__line_items__taxes
│   ├── order__metadata
│   ├── order__refunds
│   ├── order__shipping_lines
│   │   ├── order__shipping_lines__meta_data
│   │   └── order__shipping_lines__taxes
│   └── order__tax_lines
│       └── order__tax_lines__meta_data
└── product
    ├── product__attributes
    ├── product__categories
    ├── product__default_attributes
    ├── product__images
    ├── product__metadata
    └── product__tags
```

## Development

If required, change local data folder (the `CUSTOM_FOLDER` placeholder) path to your custom path in the docker-compose file:

```yaml
    volumes:
      - ./:/code
      - ./CUSTOM_FOLDER:/data
```

Clone this repository, init the workspace and run the component with following command:

```bash
git clone repo_path my-new-component
cd my-new-component
docker-compose build
docker-compose run --rm dev
```

Run the test suite and lint check using this command:

```bash
docker-compose run --rm test
```

## Integration

For information about deployment and integration with KBC, please refer to the [deployment section of developers documentation](https://developers.keboola.com/extend/component/deployment/)


## Setup WooCommerce Test Server

1. create `docker-compose.yml` file on server

```bash

version: '3.3'

services:
  db:
    image: mysql:latest
    volumes:
      - data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: wordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress

  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    ports:
      - "8000:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
volumes:
    data: {}
```
