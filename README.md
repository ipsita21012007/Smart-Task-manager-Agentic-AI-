# Smart-Task-manager-Agentic-AI-
📋 Smart Task Manager Agent
A modern, AI-powered task management application built with Streamlit that understands natural language commands and helps you organize your tasks efficiently.

🚀 Features
💬 Natural Language Processing - Understands commands like "Schedule meeting at 2pm" or "Remind me to buy groceries"

🎯 Smart Task Categorization - Automatically detects meeting, reminder, and general task types

📱 Interactive Chat Interface - Real-time conversation with the task manager

⏰ Time Recognition - Extracts time information from natural language input

📊 Visual Task Display - Clean, organized view of all your tasks

🔄 Session Persistence - Tasks persist during your session

🎨 Responsive Design - Works perfectly on desktop and mobile devices

🛠️ Installation
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Step-by-Step Setup
Clone or download the project

bash
cd "Smart Task Manager Agent"
Create a virtual environment (recommended)

bash
# Windows
python -m venv task_env
task_env\Scripts\activate

# Mac/Linux
python3 -m venv task_env
source task_env/bin/activate
Install dependencies

bash
pip install streamlit
Run the application

bash
streamlit run app.py
Open your browser

The app will automatically open at http://localhost:8501

If not, manually navigate to the URL shown in the terminal

💡 How to Use
Basic Commands
Schedule meetings: "Schedule team meeting at 3pm tomorrow"

Set reminders: "Remind me to call John at 4:30pm"

Create tasks: "Need to finish the quarterly report"

General tasks: "Buy groceries after work"

Interface Overview
Left Panel: Chat interface where you interact with the AI

Right Panel: Live task list showing all your scheduled items

Clear Button: Remove all tasks when needed

🏗️ Project Structure
text
Smart Task Manager Agent/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
└── README.md             # This file
🧠 How It Works
Command Parsing: Uses regex patterns to identify task types and extract time information

Task Classification: Categorizes inputs as meetings, reminders, or general tasks

Data Storage: Uses Streamlit's session state for temporary data persistence

Real-time Updates: Instant UI updates when new tasks are added

🔧 Technical Details
Built With
Streamlit - Web application framework

Python 3 - Backend logic

Regex - Natural language processing

Datetime - Time handling and formatting

Key Components
SimpleTaskManager class - Core task management logic

Natural language command parser

Session state management

Responsive UI components

🚀 Future Enhancements
Database integration for permanent storage

Email/SMS notifications

Google Calendar synchronization

Task prioritization and categories

Recurring tasks

File attachments

Team collaboration features

🤝 Contributing
Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🆘 Support
If you encounter any issues:

Check that all dependencies are installed correctly

Ensure you're using Python 3.8 or higher

Verify your virtual environment is activated

Check the terminal for any error messages

📞 Contact
For questions or support, please open an issue in the project repository.

Happy Task Managing! 🎉
