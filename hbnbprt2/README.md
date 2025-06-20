# HBnB - AirBnB Clone (Part 2)

A comprehensive AirBnB clone implementation focusing on Business Logic and API endpoints using Python, Flask, and Flask-RESTX.

## Project Overview

HBnB is a full-stack web application that replicates AirBnB's core functionality. This project implements the Business Logic and API layers using a modular architecture with three distinct layers:

- **Presentation Layer**: RESTful API endpoints using Flask-RESTX
- **Business Logic Layer**: Core models and business rules
- **Persistence Layer**: In-memory storage (to be replaced with SQLAlchemy in Part 3)

## Architecture

The project follows a **3-layer architecture** with the **Facade pattern** for communication between layers:

```
┌─────────────────┐
│  Presentation   │  ← Flask-RESTX API endpoints
│     Layer       │
├─────────────────┤
│  Business Logic │  ← Core models (User, Place, Review, Amenity)
│     Layer       │
├─────────────────┤
│   Persistence   │  ← In-memory repository (Facade pattern)
│     Layer       │
└─────────────────┘
```

## Project Structure

```
HBnBPrt2/
├── api/
│   └── v1/
│       ├── __init__.py
│       ├── app.py
│       ├── users.py
│       ├── places.py
│       ├── reviews.py
│       └── amenities.py
├── business/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   └── services/
│       ├── __init__.py
│       └── facade.py
├── persistence/
│   ├── __init__.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── in_memory_repository.py
│   └── storage/
│       ├── __init__.py
│       └── storage.py
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   └── test_api.py
├── app.py
├── config.py
└── requirements.txt
```

## Features

### Core Entities
- **User**: Authentication and user management
- **Place**: Property listings with location and pricing
- **Review**: User reviews for places
- **Amenity**: Available amenities for places

### API Endpoints

#### Users
- `POST /api/v1/users/` - Create user
- `GET /api/v1/users/` - List all users
- `GET /api/v1/users/<id>` - Get specific user
- `PUT /api/v1/users/<id>` - Update user

#### Places
- `POST /api/v1/places/` - Create place
- `GET /api/v1/places/` - List all places
- `GET /api/v1/places/<id>` - Get specific place
- `PUT /api/v1/places/<id>` - Update place

#### Reviews
- `POST /api/v1/places/<place_id>/reviews/` - Create review
- `GET /api/v1/places/<place_id>/reviews/` - List place reviews
- `GET /api/v1/reviews/<id>` - Get specific review
- `PUT /api/v1/reviews/<id>` - Update review
- `DELETE /api/v1/reviews/<id>` - Delete review

#### Amenities
- `POST /api/v1/amenities/` - Create amenity
- `GET /api/v1/amenities/` - List all amenities
- `GET /api/v1/amenities/<id>` - Get specific amenity
- `PUT /api/v1/amenities/<id>` - Update amenity

## Setup and Installation

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd hbnbprt2
```

2. **Create virtual environment**
```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Documentation

The API includes automatic Swagger documentation available at:
- **Swagger UI**: `http://localhost:5000/`
- **API Documentation**: `http://localhost:5000/api/v1/`

## Testing

### Manual Testing with cURL

```bash
# Create a user
curl -X POST http://localhost:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123", "first_name": "John", "last_name": "Doe"}'

# Get all users
curl http://localhost:5000/api/v1/users/

# Create a place
curl -X POST http://localhost:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Cozy Apartment", "description": "Beautiful apartment", "price": 100, "owner_id": "user-id"}'
```

### Automated Testing

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_models.py
```

## Design Patterns

### Facade Pattern
The project implements the Facade pattern to simplify communication between the Presentation and Business Logic layers:

```python
class HBnBFacade:
    def __init__(self):
        self.user_repository = InMemoryRepository()
        self.place_repository = InMemoryRepository()
        # ... other repositories
    
    def create_user(self, user_data):
        # Simplified interface for user creation
        return self.user_repository.create(user_data)
```

### Repository Pattern
In-memory repositories handle data storage and validation:

```python
class InMemoryRepository:
    def __init__(self):
        self.storage = {}
    
    def create(self, data):
        # Create and store entity
        pass
    
    def get_by_id(self, id):
        # Retrieve entity by ID
        pass
```

## Data Models

### Base Model
All entities inherit from a base model with common attributes:
- `id`: Unique identifier (UUID)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Entity Relationships
- **User** ↔ **Place**: One-to-many (User owns multiple Places)
- **Place** ↔ **Review**: One-to-many (Place has multiple Reviews)
- **Place** ↔ **Amenity**: Many-to-many (Places have multiple Amenities)
- **User** ↔ **Review**: One-to-many (User writes multiple Reviews)

## Validation Rules

### User Validation
- Email must be unique and valid format
- Password must be at least 6 characters
- First and last names are required

### Place Validation
- Name and description are required
- Price must be positive number
- Latitude must be between -90 and 90
- Longitude must be between -180 and 180

### Review Validation
- Text content is required
- Rating must be between 1 and 5
- Must be associated with valid user and place

## Error Handling

The API returns appropriate HTTP status codes:
- `200`: Success
- `201`: Created
- `400`: Bad Request
- `404`: Not Found
- `422`: Unprocessable Entity
- `500`: Internal Server Error

## Future Enhancements (Part 3)

- SQLAlchemy database integration
- JWT authentication
- Role-based access control
- File upload for place images
- Search and filtering capabilities
- Pagination for large datasets

## Technologies Used

- **Python 3.8+**: Core programming language
- **Flask**: Web framework
- **Flask-RESTX**: RESTful API framework with automatic documentation
- **UUID**: Unique identifier generation
- **datetime**: Timestamp handling
- **unittest/pytest**: Testing framework

## Learning Outcomes

This project demonstrates:
- **Modular Architecture**: Clean separation of concerns
- **RESTful API Design**: Proper HTTP methods and status codes
- **Design Patterns**: Facade and Repository patterns
- **Data Validation**: Input validation and error handling
- **Testing**: Both manual and automated testing approaches
- **Documentation**: API documentation with Swagger

## Project Experience

This project provided excellent hands-on experience with:
- Building scalable web applications
- Implementing RESTful APIs
- Applying design patterns in real-world scenarios
- Managing complex data relationships
- Writing comprehensive tests
- Following Python best practices

The modular architecture and clear separation of concerns make the codebase maintainable and extensible, providing a solid foundation for future enhancements.

## Contributing

This is a learning project for Holberton School. For questions or issues, please refer to the project requirements and documentation.

## License

This project is part of the Holberton School curriculum. 