# ITMD523_FinalProject
The repo for our Freelancer Job Role App. Users can post freelance job listings, search for available roles, and apply to jobs.


# Freelancer Job Role App

### Project Overview
This web-based app allows users to post freelance job listings, search available roles, and apply for positions. It’s built using Python (Flask), MySQL, and includes a simple front-end interface.

### Team Members
- **Hinaba** - Database Design
- **Kat** - Backend Development
- **Paige** - Frontend Development

### Features
- User Registration and Login
- Job Listing Management
- Application Tracking

### Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/freelancer-job-role-app.git
   cd freelancer-job-role-app
   ```

2. **Install Requirements** (for the backend):
   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Database Setup**:
   - Use the SQL scripts in `database/` to create the necessary tables.

### Project Structure
- `backend/`: Contains Flask app code and backend logic.
- `frontend/`: Contains HTML, CSS, and JavaScript files for the user interface.
- `database/`: SQL scripts and database schema.

### Usage
Run the Flask app from the `backend` folder:
```bash
python backend/app.py
