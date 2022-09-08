To download data form WooCommerce we need to configure

- `store_url` Website Domain name where WooCommerce is hosted. e.g. https://myshop.com
- `consumer_key` Rest API Consumer Key from WooCommerce Admin panel
- `consumer_secret` Rest API Consumer Secret from WooCommerce Admin panel
- `fetching_mode` If set to Basic Incremental Fetching, data will be fetched using the before and after parameters of the WooCommerce Api. Full Download downloads all data. Custom Incremental Fetching allows the use of custom incremental fetching parameters
- `custom_incremental_field` Custom parameter in WooCommerce for incremental fetching
- `custom_incremental_value` Inclusive Date in YYYY-MM-DD format or a string i.e. 5 days ago, 1 month ago, yesterday, etc. which will be used for fetching with the custom fetching field
- `date_from` Inclusive Date in YYYY-MM-DD format or a string i.e. 5 days ago, 1 month ago, yesterday, etc.
- `date_to` Exclusive Date in YYYY-MM-DD format or a string i.e. 5 days ago, 1 month ago, yesterday, etc.
- `load_type` If set to Incremental update, the result tables will be updated based on primary key. Full load overwrites the destination table each time. NOTE: If you wish to remove deleted records, this needs to be set to Full load and the Period from attribute empty.
- `endpoint` To fetch data from selected endpoints i.e. Customers, Orders and Products. Default selection is all
i.e.
- Orders endpoint list all orders for give date range
- Products endpoint list all Products for given date range
- Customers endpoint list all customers

__NOTE:__ *The date selection does not affect Customers endpoint*

**Getting the token:**

To create or manage keys for a specific WordPress user, go to `WooCommerce > Settings > API > Keys/Apps`.
Click the `Add Key` button. In the next screen, add a description and select the WordPress user you would like to generate the key for
Choose the level of access for this REST API key, which can be Read access. Then click the `Generate API Key` button and WooCommerce will generate REST API keys
These two keys are your Consumer Key and Consumer Secret.


**Custom Fetching:**

You can use [this plugin](https://wordpress.org/plugins/products-and-orders-last-modified-for-wc-rest-api/) or implement the custom incremental field by yourself.