import streamlit as st
import json
from datetime import datetime
import re

class SimpleTaskManager:
    def __init__(self):
        if 'tasks' not in st.session_state:
            st.session_state.tasks = []
    
    def parse_command(self, user_input):
        """Simple command parsing"""
        input_lower = user_input.lower()
        
        if any(word in input_lower for word in ['schedule', 'meeting', 'appointment']):
            time_match = re.search(r'(\d{1,2}(?::\d{2})?\s*(?:am|pm)?)', input_lower)
            time_str = time_match.group(1) if time_match else "unknown time"
            return {
                "action": "schedule",
                "title": "Meeting",
                "time": time_str,
                "description": user_input
            }
        elif any(word in input_lower for word in ['remind', 'reminder']):
            time_match = re.search(r'(\d{1,2}(?::\d{2})?\s*(?:am|pm)?)', input_lower)
            time_str = time_match.group(1) if time_match else "unknown time"
            return {
                "action": "reminder", 
                "title": "Reminder",
                "time": time_str,
                "description": user_input
            }
        else:
            return {
                "action": "task",
                "title": "Task",
                "time": "",
                "description": user_input
            }
    
    def add_task(self, task_data):
        task_id = len(st.session_state.tasks) + 1
        task = {
            "id": task_id,
            "title": task_data["title"],
            "description": task_data["description"],
            "time": task_data["time"],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "status": "pending"
        }
        st.session_state.tasks.append(task)
        return task

def main():
    st.set_page_config(page_title="Smart Task Manager", page_icon="✅", layout="wide")
    
    # Initialize task manager
    task_manager = SimpleTaskManager()
    
    # Header
    st.title("📋 Smart Task Manager")
    st.markdown("Try: **'Schedule meeting at 2pm'** or **'Remind me to buy groceries'**")
    
    # Chat and input section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("💬 Chat Interface")
        
        # Display chat messages
        if 'messages' not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hello! I'm your Smart Task Manager. How can I help you schedule tasks today?"}
            ]
        
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Type your task here..."):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Process the message
            parsed = task_manager.parse_command(prompt)
            task = task_manager.add_task(parsed)
            
            # Generate bot response
            response = f"✅ Added: **{task['title']}**"
            if task['time']:
                response += f" at **{task['time']}**"
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)
    
    with col2:
        st.subheader("📝 Your Tasks")
        
        if not st.session_state.tasks:
            st.info("No tasks yet. Start by typing a task in the chat!")
        else:
            for task in st.session_state.tasks:
                with st.container():
                    st.markdown(f"""
                    <div style="border-left: 4px solid #4CAF50; padding: 10px; margin: 10px 0; background: #f8f9fa; border-radius: 5px;">
                        <strong>{task['title']}</strong>
                        {f"<br>⏰ <strong>Time:</strong> {task['time']}" if task['time'] else ""}
                        <br>📝 <strong>Description:</strong> {task['description']}
                        <br><small>📅 Created: {task['created_at']}</small>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Clear tasks button
        if st.session_state.tasks:
            if st.button("🗑️ Clear All Tasks", use_container_width=True):
                st.session_state.tasks = []
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": "All tasks have been cleared!"
                })
                st.rerun()

if __name__ == '__main__':
    main()