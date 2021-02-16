# KBC Component

Description

**Table of contents:**

[TOC]


# Functionality notes


# Configuration

## Param 1

## Param 2


## Development

If required, change local data folder (the `CUSTOM_FOLDER` placeholder) path to your custom path in the docker-compose file:

```yaml
    volumes:
      - ./:/code
      - ./CUSTOM_FOLDER:/data
```

Clone this repository, init the workspace and run the component with following command:

```
git clone repo_path my-new-component
cd my-new-component
docker-compose build
docker-compose run --rm dev
```

Run the test suite and lint check using this command:

```
docker-compose run --rm test
```

# Integration

For information about deployment and integration with KBC, please refer to the [deployment section of developers documentation](https://developers.keboola.com/extend/component/deployment/)


## ForeignKey Relations for nested objects

For example Products have multiple attribute

```json
[
  {
    "id": 799,
    "name": "Ship Your Idea",
    "description": "",
    "dimensions": {
      "length": "",
      "width": "",
    },
    "related_ids": [
      31,
      22,
    ],
    "categories": [
      {
        "id": 9,
        "name": "Clothing",
        "slug": "clothing"
      },
      {
        "id": 14,
        "name": "T-shirts",
        "slug": "t-shirts"
      }
    ],
    "images": [
      {
        "id": 795,
        "src": "https://example.com/wp-content/uploads/2017/03/T_4_front-11.jpg",
        "name": ""
      },
      {
        "id": 796,
        "src": "https://example.com/wp-content/uploads/2017/03/T_4_back-10.jpg",
        "name": ""
      },
    ],
    "attributes": [
      {
        "id": 6,
        "name": "Color",
        "options": [
          "Black",
          "Green"
        ]
      },
      {
        "id": 0,
        "name": "Size",
        "options": [
          "S",
          "M"
        ]
      }
    ]
  }
]
```

## Output

There are four tables generated from this schema

- In `products` table columns will be `["id", "name", "description", "dimensions__length", "dimensions__width", "related_ids"]`

- In `products__category` table columns will be `["id", "name", "slug", "product_id"]`

- In `products__images` table columns will be `["id", "src", "name", "product_id"]`

- In `products__attributes` table columns will be `["id", "name", "options", "product_id"]`

Here each table has `id` is primary key for respective table and `product_id` is ForeignKey of `Products` table on `products__category`, `product__images` and `products__attributes` table