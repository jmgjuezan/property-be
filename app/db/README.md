# About
This backend API is built initially connected to MongoDB Atlas, a no SQL type of cloud based storage.

## Structure

### 1. Database

- MongoDB Connection: property-management
- MongoDB Cluster: prop-mgmt-prod
- MongoDB Database: prop-mgmt
- MongoDB Collections: dues, exclusions, payments, properties, tenants

### 2. Collections

- Dues - expected receivable from tenant
- Exclusions - payment exception or deduction
- Payments - paid by tenants
- Properties - rentable real estate

| Column        | Type |                          Constraints |
|:--------------|:----:|-------------------------------------:|
| _id           | str  |     Required, Auto-generated, Unique |
| name          | str  |    Required, Length (min=5, max=100) |
| address       | str  |   Optional, Length (min=25, max=250) |
| currentTenant | int  | Optional, greater than or equal to 0 |
| maxTenant     | int  |             Optional, greater than 0 |
| acquiredDate  | date |          Optional, yyyy-MM-dd format |
| standBy       | bool |                             Optional |

- Tenants - a occupant of property

| Column      | Type |                            Constraints |
|:------------|:----:|---------------------------------------:|
| _id         | str  |       Required, Auto-generated, Unique |
| firstName   | str  |      Required, Length (min=2, max=100) |
| middleName  | str  |      Optional, Length (min=2, max=100) |
| lastName    | str  |      Required, Length (min=2, max=100) |
| property    | str  | Required, Referenced to properties _id |
| moveInDate  | date |            Required, yyyy-MM-dd format |
| paymentDate | date |            Optional, yyyy-MM-dd format |
| rentAmount  | int  |               Required, greater than 0 |

## Definitions

- A MongoDB "Connection" uses a string to link your app to a Cluster (a group of servers hosting your data)

- A "Cluster" is the underlying infrastructure that hosts your data, typically configured as a replica set (for high availability) or a sharded cluster (for horizontal scaling).

- Inside the cluster, you organize data into "Databases" that are containers for collections.

- "Collections" is the equivalent of relational tables, storing JSON-like documents.

## Reference

[MongoDB](https://cloud.mongodb.com/)
