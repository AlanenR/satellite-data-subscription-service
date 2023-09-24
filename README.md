# Satellite Data Subscription Service

The Satellite Data Subscription Service allows users to access and subscribe to satellite data for different solutions e.g wildfire monitoring or flood monitoring.

The features of the application include:
* **User Authentication:** Users can log in and out, create new accounts, and manage subscriptions.
* **Data Filtering:** Users can filter satellite data based on region, time, and data type.
* **Favorites List:** Users can add and remove satellite data records to their favorites list.
* **Admin Panel:** Admin users can add and delete satellite data records. They can also manage which data records are available for each subscription.

**Update 22.9.2023:**
This repository contains the basic project structure and setup. You can test the project setup and run the provided commands, but please note that this is a minimal project template without specific functionality implemented yet.

## Set up

You need to install [PostgreSQL](https://www.postgresql.org/download/) on your machine in advance.

**Step 1: Clone the repo**

```
$ git clone https://github.com/AlanenR/satellite-data-subscription-service

$ cd ./satellite-data-subscription-service

```

**Step 2: Set up the virtual environment and install the requirements in terminal:**
  
    - $ python3 -m venv venv
    - $ source venv/bin/activate
    - $ pip install -r requirements.txt
   
**Step 3: Create the database in PostgreSQL using the following command:**

    - $ psql -d [YOUR_DATABASE_NAME] < schema.sql
  
**Step 4: Start the application by running the following command in your terminal:**
    
    - $ flask run

## Environment Variables

`.env`
|  Parameter  | Description | Default |
| ---  | --- | --- |
| `DATABASE_URL` | The PostgreSQL database address.  |  |

## Planned Database Structure

This section provides an overview of the planned database structure for the Satellite Data Subscription Service application. The database consists of several tables to manage users, subscriptions, data categories, regions, satellites, satellite data, and more.

### Users Table

The `Users` table stores user information, including their `user_id`, `email`, `password`, and `role_id`. The `role_id` is a foreign key linked to the `user_roles` table.

### User Roles Table

The `user_roles` table defines user roles and their corresponding `role_id`. Each role has a unique `role_name`.

### Subscription Options Table

The `subscription_options` table lists available subscription options, each identified by a unique `subscription_id`. Details include the `name`, `description`, and `price` of each subscription.

### User Subscriptions Table

The `user_subscriptions` table links users to their chosen subscriptions. It includes `user_subscription_id`, `user_id`, and `subscription_id`.

### Data Categories Table

The `data_categories` table manages data categories with a unique `category_id`, along with `name` and `description` fields.

### Regions Table

The `regions` table stores geographic regions with a unique `region_id` and `name`.

### Satellites Table

The `satellites` table holds information about satellites, including their `satellite_id` and `name`.

### Satellite Data Table

The `satellite_data` table records satellite data entries. It includes fields such as `data_id`, `timestamp`, `region_id`, `image_url`, `description`, `latitude`, `longitude`, `altitude`, and `satellite_id`.

### Satellite Data Category Mapping Table

The `satellite_data_category_mapping` table maps satellite data to data categories. It has `satellite_data_category_mapping_id`, `data_id`, and `category_id` fields.

### Subscription Category Mapping Table

The `subscription_category_mapping` table connects subscriptions to data categories. It includes `subscription_category_mapping_id`, `subscription_id`, and `category_id`.

### Favorites Table

The `favorites_table` allows users to store their favorite satellite data records. It has `favorites_id`, `user_id`, and `data_id` fields.

These tables work together to manage user roles, subscriptions, satellite data, and more within the application. For more details about the database schema, please refer to the SQL statements used to create each table.