import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Configure page
st.set_page_config(
    page_title="DevCatalyst - Member Portal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beige theme and styling
st.markdown("""
<style>
    .main {
        background-color: #F5F5DC;
        padding: 0;
    }
    
    .stApp {
        background-color: #F5F5DC;
    }
    
    .header-container {
        background: linear-gradient(135deg, #D2B48C 0%, #DEB887 100%);
        padding: 2rem;
        border-radius: 0 0 20px 20px;
        margin: -1rem -1rem 2rem -1rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .club-title {
        font-size: 3rem;
        font-weight: bold;
        color: #8B4513;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .club-subtitle {
        font-size: 1.2rem;
        color: #A0522D;
        margin-bottom: 0;
    }
    
    .welcome-message {
        background-color: #F8F6F0;
        padding: 1.5rem;
        border-radius: 15px;
        border: 2px solid #E6DCC6;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .task-card {
        background-color: #F8F6F0;
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid #E6DCC6;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease;
    }
    
    .task-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    .priority-high {
        border-left: 6px solid #FF6B6B;
    }
    
    .priority-medium {
        border-left: 6px solid #FFD93D;
    }
    
    .priority-low {
        border-left: 6px solid #6BCF7F;
    }
    
    .status-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        text-align: center;
        margin-right: 0.5rem;
    }
    
    .status-pending {
        background-color: #FFE4E4;
        color: #D63384;
    }
    
    .status-progress {
        background-color: #FFF3CD;
        color: #B45309;
    }
    
    .status-completed {
        background-color: #D4F6DD;
        color: #0F5132;
    }
    
    .quick-stats {
        background-color: #F8F6F0;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #E6DCC6;
        text-align: center;
    }
    
    .metric-number {
        font-size: 2rem;
        font-weight: bold;
        color: #8B4513;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #A0522D;
    }
    
    .section-header {
        color: #8B4513;
        font-size: 1.8rem;
        font-weight: bold;
        margin: 2rem 0 1rem 0;
        border-bottom: 3px solid #DEB887;
        padding-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Sample member data
@st.cache_data
def load_member_tasks():
    tasks_data = {
        'Task ID': ['DC-001', 'DC-002', 'DC-003', 'DC-004', 'DC-005', 'DC-006'],
        'Task Title': ['Setup Development Environment', 'Complete React Tutorial', 'Design Database Schema', 
                      'Write API Documentation', 'Code Review - Payment Module', 'Prepare Tech Talk'],
        'Description': [
            'Install and configure VS Code, Node.js, and Git for the upcoming project',
            'Complete the official React tutorial and submit your todo app project',
            'Design the database schema for the new e-commerce platform',
            'Document the REST API endpoints for the user management system',
            'Review the payment integration code and provide feedback',
            'Prepare a 15-minute presentation on modern JavaScript frameworks'
        ],
        'Priority': ['High', 'Medium', 'High', 'Low', 'Medium', 'Low'],
        'Status': ['Pending', 'In Progress', 'Pending', 'Completed', 'In Progress', 'Pending'],
        'Due Date': ['2024-08-20', '2024-08-25', '2024-08-22', '2024-08-18', '2024-08-28', '2024-08-30'],
        'Assigned Date': ['2024-08-16', '2024-08-14', '2024-08-16', '2024-08-10', '2024-08-15', '2024-08-16'],
        'Points': [10, 15, 20, 8, 12, 6]
    }
    return pd.DataFrame(tasks_data)

def get_status_badge(status):
    status_classes = {
        'Pending': 'status-pending',
        'In Progress': 'status-progress', 
        'Completed': 'status-completed'
    }
    return f'<span class="status-badge {status_classes[status]}">{status}</span>'

def get_priority_emoji(priority):
    priority_emojis = {
        'High': '🔴',
        'Medium': '🟡',
        'Low': '🟢'
    }
    return priority_emojis.get(priority, '⚪')

def main():
    # Header
    st.markdown("""
    <div class="header-container">
        <div class="club-title">⚡ DevCatalyst</div>
        <div class="club-subtitle">Accelerating Developer Growth</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Welcome message
    st.markdown("""
    <div class="welcome-message">
        <h2>👋 Welcome back, Alex Johnson!</h2>
        <p>Ready to tackle your development tasks? Let's make today productive! 🚀</p>
        <p><strong>Member ID:</strong> DC2024-157 | <strong>Level:</strong> Intermediate Developer | <strong>Points:</strong> 245</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load member tasks
    df = load_member_tasks()
    
    # Quick stats
    st.markdown('<div class="section-header">📊 Your Progress Overview</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    total_tasks = len(df)
    completed_tasks = len(df[df['Status'] == 'Completed'])
    pending_tasks = len(df[df['Status'] == 'Pending'])
    total_points = df['Points'].sum()
    
    with col1:
        st.markdown(f"""
        <div class="quick-stats">
            <div class="metric-number">{total_tasks}</div>
            <div class="metric-label">Total Tasks</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="quick-stats">
            <div class="metric-number">{completed_tasks}</div>
            <div class="metric-label">Completed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="quick-stats">
            <div class="metric-number">{pending_tasks}</div>
            <div class="metric-label">Pending</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="quick-stats">
            <div class="metric-number">{total_points}</div>
            <div class="metric-label">Total Points</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Progress visualization
    st.markdown('<div class="section-header">📈 Your Achievement Progress</div>', unsafe_allow_html=True)
    
    completion_rate = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Progress bar
        progress_html = f"""
        <div style="background-color: #E6DCC6; border-radius: 10px; padding: 10px; margin: 10px 0;">
            <div style="background-color: #6BCF7F; height: 20px; border-radius: 10px; width: {completion_rate}%;"></div>
            <p style="text-align: center; margin-top: 10px; color: #8B4513;"><strong>{completion_rate:.1f}% Complete</strong></p>
        </div>
        """
        st.markdown(progress_html, unsafe_allow_html=True)
    
    with col2:
        # Status breakdown with visual indicators
        status_counts = df['Status'].value_counts()
        st.markdown("**📊 Task Status:**")
        
        for status, count in status_counts.items():
            percentage = (count / len(df)) * 100
            if status == 'Completed':
                color = "#6BCF7F"
                emoji = "✅"
            elif status == 'In Progress':
                color = "#FFD93D" 
                emoji = "🔄"
            else:
                color = "#FF6B6B"
                emoji = "⏳"
            
            st.markdown(f"""
            <div style="margin: 5px 0; padding: 8px; background-color: {color}20; border-radius: 5px; border-left: 4px solid {color};">
                {emoji} <strong>{status}:</strong> {count} ({percentage:.0f}%)
            </div>
            """, unsafe_allow_html=True)
    
    # Task filters
    st.markdown('<div class="section-header">📋 Your Assigned Tasks</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        status_filter = st.selectbox("🔍 Filter by Status:", ["All Tasks"] + list(df['Status'].unique()))
    
    with col2:
        sort_option = st.selectbox("📊 Sort by:", ["Due Date", "Priority", "Points", "Status"])
    
    # Apply filters and sorting
    filtered_df = df.copy()
    if status_filter != "All Tasks":
        filtered_df = filtered_df[filtered_df['Status'] == status_filter]
    
    # Sort data
    if sort_option == "Due Date":
        filtered_df = filtered_df.sort_values('Due Date')
    elif sort_option == "Priority":
        priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
        filtered_df['priority_num'] = filtered_df['Priority'].map(priority_order)
        filtered_df = filtered_df.sort_values('priority_num')
        filtered_df = filtered_df.drop('priority_num', axis=1)
    elif sort_option == "Points":
        filtered_df = filtered_df.sort_values('Points', ascending=False)
    else:
        filtered_df = filtered_df.sort_values('Status')
    
    # Display tasks
    if len(filtered_df) == 0:
        st.info("🎉 No tasks found with the selected filter. Great job if you've completed everything!")
    else:
        for _, task in filtered_df.iterrows():
            priority_class = f"priority-{task['Priority'].lower()}"
            
            # Calculate days until due
            due_date = pd.to_datetime(task['Due Date'])
            days_left = (due_date - pd.Timestamp.now()).days
            
            if days_left < 0:
                due_text = f"⚠️ Overdue by {abs(days_left)} days"
                due_color = "color: red;"
            elif days_left == 0:
                due_text = "🔥 Due Today!"
                due_color = "color: orange;"
            elif days_left <= 2:
                due_text = f"⏰ Due in {days_left} days"
                due_color = "color: orange;"
            else:
                due_text = f"📅 Due in {days_left} days"
                due_color = "color: green;"
            
            st.markdown(f"""
            <div class="task-card {priority_class}">
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 10px;">
                    <h3 style="margin: 0; color: #8B4513;">{get_priority_emoji(task['Priority'])} {task['Task Title']}</h3>
                    <div style="text-align: right;">
                        {get_status_badge(task['Status'])}
                        <div style="font-size: 0.9rem; margin-top: 5px; {due_color}"><strong>{due_text}</strong></div>
                    </div>
                </div>
                
                <p style="color: #666; margin: 10px 0;">{task['Description']}</p>
                
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px; padding-top: 10px; border-top: 1px solid #E6DCC6;">
                    <div>
                        <span style="color: #8B4513;"><strong>Task ID:</strong> {task['Task ID']}</span> | 
                        <span style="color: #8B4513;"><strong>Priority:</strong> {task['Priority']}</span> | 
                        <span style="color: #8B4513;"><strong>Points:</strong> {task['Points']}</span>
                    </div>
                    <div style="color: #A0522D; font-size: 0.9rem;">
                        <strong>Assigned:</strong> {task['Assigned Date']}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Quick actions
    st.markdown('<div class="section-header">⚡ Quick Actions</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📝 Submit Work", use_container_width=True):
            st.info("This would open a submission form for completed tasks")
    
    with col2:
        if st.button("❓ Ask for Help", use_container_width=True):
            st.info("This would open a help request form or connect to mentors")
    
    with col3:
        if st.button("📊 View Full Profile", use_container_width=True):
            st.info("This would show detailed member profile and achievement history")
    
    # Footer message
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #A0522D; padding: 20px;">
        <p><strong>💡 DevCatalyst Tip:</strong> Complete tasks on time to earn bonus points and unlock new challenges!</p>
        <p>Need help? Contact your mentor or check our <a href="#" style="color: #8B4513;">community resources</a> 📚</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
