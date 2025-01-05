
# **Blog Platform Application**

This project is a multi-service application for managing users, blogs, and comments. It consists of three services:
1. **User Service**: Handles user registration, authentication, and profile management.
2. **Blog Service**: Manages blog creation, editing, and deletion.
3. **Comment Service**: Manages comments on blog posts.

---

## **Public URLs**
- **User Service**: [https://blog-platform-bdn4.vercel.app/](https://blog-platform-bdn4.vercel.app/)
- **Blog Service**: [https://blog-platform-bupu.vercel.app/](https://blog-platform-bupu.vercel.app/)
- **Comment Service**: [https://commetervice.vercel.app/](https://commetervice.vercel.app/p)
- **PostgreSQL Databases**: Hosted on [Railway](https://railway.app) (secured and private).

---

## **Features**
- User registration, authentication, and profile management.
- Blog creation, editing, and deletion by authenticated users.
- Adding and listing comments on blogs.
- RESTful API design with JWT-based authentication.
- Scalable deployment using Vercel and Railway.

---

## **Local Deployment**

### **Prerequisites**
1. Install **Docker** and **Docker Compose**.
2. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

### **Step 1: Environment Setup**
Create `.env` files in each service folder (`user_service`, `blog_service`, `comment_service`) with the following variables:

#### Example `.env` for User Service:
```plaintext
DATABASE_URL=postgres://postgres:password@user_db:5432/user_service_db
SECRET_KEY=your_secret_key
```

### **Step 2: Build and Run**
Run the following command in the project root directory:
```bash
docker-compose up --build
```

This will:
- Start PostgreSQL databases for all services.
- Build and run the **User**, **Blog**, and **Comment** services.

### **Step 3: Access the Services**
- **User Service**: [http://localhost:8001](http://localhost:8001)
- **Blog Service**: [http://localhost:8002](http://localhost:8002)
- **Comment Service**: [http://localhost:8003](http://localhost:8003)

### **Step 4: Stop the Services**
Stop all running services using:
```bash
docker-compose down
```

---

## **Vercel Deployment**

### **Prerequisites**
1. Create a **Vercel** account at [https://vercel.com](https://vercel.com).
2. Connect your GitHub repository to Vercel.

### **Step 1: Prepare for Deployment**
Ensure each service folder (`user_service`, `blog_service`, `comment_service`) contains a `vercel.json` file:

#### Example `vercel.json`:
```json
{
  "version": 2,
  "builds": [
    { "src": "manage.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "manage.py" }
  ]
}
```

### **Step 2: Update Environment Variables**
In the Vercel dashboard, configure environment variables for each service:

#### Example for User Service:
```plaintext
DATABASE_URL=postgres://<username>:<password>@<railway-host>:5432/user_service_db
SECRET_KEY=your_secret_key
```

### **Step 3: Deploy Each Service**
1. Deploy each service separately through the Vercel dashboard.
2. Vercel will provide public URLs for each service after deployment.

---

## **Inter-Service Communication**
Each service uses environment variables to communicate:

- **Blog Service**:
  ```plaintext
  USER_SERVICE_URL=https://blog-platform-bdn4.vercel.app/
  ```
- **Comment Service**:
  ```plaintext
  USER_SERVICE_URL=https://blog-platform-bdn4.vercel.app/
  BLOG_SERVICE_URL=https://blog-platform-bupu.vercel.app/
  ```

---

## **Technology Stack**
- **Backend**: Django (Python)
- **Database**: PostgreSQL (Railway)
- **Deployment**: Vercel
- **Containerization**: Docker

---

## **API Documentation**
Refer to the [API Documentation](API_DOCUMENTATION.md) for detailed information on available endpoints and usage.

---

## **Contact**
For any issues, please contact [your-email@example.com](mailto:your-email@example.com).
