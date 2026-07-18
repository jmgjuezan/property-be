# About
This backend API is built initially connected to MongoDB Atlas, a no SQL type of cloud based storage.

## Structure

### 1. Database

- MongoDB Connection: property-management
- MongoDB Cluster: prop-mgmt-prod
- MongoDB Database: prop-mgmt
- MongoDB Collections: dues, exclusions, payments, properties, tenants

### 2. Collections

- Dues
| Column  |
| --- | --- | --- |
| dueDate |

- Exclusions
- Payments
- Properties
- Tenants

## Definitions

- A MongoDB connection uses a string to link your app to a Cluster (a group of servers hosting your data)

- A cluster is the underlying infrastructure that hosts your data, typically configured as a replica set (for high availability) or a sharded cluster (for horizontal scaling).

- Inside the cluster, you organize data into Databases (containers for collections).

- Collections (the equivalent of relational tables, storing JSON-like documents).

- Dues -
- Exclusions -
- Payments -
- Properties -
- Tenants -

## Reference

[MongoDB](https://cloud.mongodb.com/)
