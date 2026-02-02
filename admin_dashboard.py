import streamlit as st
import json
import subprocess
import os
from pathlib import Path
from utils import ToolManager
from builder import ToolBuilder
from content_engine import ContentEngine

# Page config
st.set_page_config(
    page_title="AI Builder Admin Dashboard",
    page_icon="🎛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 16px;
        font-weight: 600;
    }
    .metric-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize managers
tool_manager = ToolManager()
builder = ToolBuilder()
content_engine = ContentEngine()

# Sidebar Navigation
st.sidebar.title("🎛️ AI Builder Admin")
st.sidebar.markdown("---")

# Tool Selection
available_tools = tool_manager.list_tools()

col1, col2 = st.sidebar.columns([3, 1])
with col1:
    selected_tool = st.selectbox(
        "Active Tool",
        available_tools + ["+ Create New Tool"],
        key="tool_selector"
    )
with col2:
    st.write("")  # Spacing

# Main Dashboard
if selected_tool == "+ Create New Tool":
    st.title("🚀 Create New Tool")
    
    with st.form("new_tool_form"):
        tool_name = st.text_input("Tool Name (lowercase, no spaces)", placeholder="loan_calculator")
        title = st.text_input("Display Title", placeholder="Loan Calculator")
        description = st.text_area("Description", placeholder="Calculate monthly loan payments with ease")
        formula_description = st.text_area("Formula/Logic Description", placeholder="Uses amortization formula...")
        
        submitted = st.form_submit_button("✨ Create Tool", use_container_width=True)
    
    if submitted and tool_name:
        if tool_manager.tool_exists(tool_name):
            st.error(f"⚠️ Tool '{tool_name}' already exists!")
        else:
            # Initialize tool structure
            tool_manager.ensure_directories(tool_name)
            
            # Create default config
            default_config = {
                "title": title,
                "description": description,
                "formula_description": formula_description,
                "inputs": [
                    {
                        "id": "input1",
                        "label": "Input 1",
                        "type": "number",
                        "placeholder": "Enter value"
                    }
                ]
            }
            
            tool_manager.save_config(tool_name, default_config)
            st.success(f"✅ Tool '{tool_name}' created! Refresh to see it in the list.")
            st.rerun()

else:
    # Load active tool
    config = tool_manager.load_config(selected_tool)
    
    if "error" not in config:
        st.title(f"🛠️ {config['title']}")
        st.markdown(f"**Description:** {config.get('description', 'N/A')}")
        st.markdown("---")
        
        # Tabs for different features
        tab1, tab2, tab3, tab4 = st.tabs(["⚙️ Configuration", "🔨 Build & Preview", "📝 Content Studio", "🚀 Deployment"])
        
        # Tab 1: Configuration
        with tab1:
            st.subheader("Configuration Editor")
            
            col1, col2 = st.columns(2)
            
            with col1:
                new_title = st.text_input("Title", value=config['title'], key="config_title")
                new_description = st.text_area("Description", value=config.get('description', ''), key="config_desc")
            
            with col2:
                new_formula = st.text_area("Formula Description", value=config.get('formula_description', ''), key="config_formula")
            
            # Color picker (optional)
            st.subheader("Theme Color")
            color = st.color_picker("Choose theme color", "#667eea")
            
            st.subheader("Input Fields Editor")
            
            inputs = config.get('inputs', [])
            
            # Display existing inputs
            for i, inp in enumerate(inputs):
                with st.expander(f"Input {i+1}: {inp['label']}"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        inputs[i]['label'] = st.text_input("Label", value=inp['label'], key=f"label_{i}")
                    with col2:
                        inputs[i]['id'] = st.text_input("ID", value=inp['id'], key=f"id_{i}")
                    with col3:
                        inputs[i]['type'] = st.selectbox("Type", ["text", "number", "email", "date"], key=f"type_{i}", index=1)
                    
                    inputs[i]['placeholder'] = st.text_input("Placeholder", value=inp.get('placeholder', ''), key=f"placeholder_{i}")
            
            # Add new input
            if st.button("➕ Add Input Field", use_container_width=True):
                inputs.append({
                    "id": f"input{len(inputs)+1}",
                    "label": "New Input",
                    "type": "number",
                    "placeholder": "Enter value"
                })
                st.rerun()
            
            # Save configuration
            if st.button("💾 Save Configuration", use_container_width=True, type="primary"):
                updated_config = {
                    "title": new_title,
                    "description": new_description,
                    "formula_description": new_formula,
                    "inputs": inputs,
                    "color": color
                }
                
                if tool_manager.save_config(selected_tool, updated_config):
                    st.success("✅ Configuration saved!")
                    st.rerun()
                else:
                    st.error("❌ Failed to save configuration")
        
        # Tab 2: Build & Preview
        with tab2:
            st.subheader("Generate Tool Code")
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write("Click the button below to generate the complete tool interface and JavaScript logic.")
            with col2:
                generate_btn = st.button("⚡ Generate Code", use_container_width=True, type="primary")
            
            if generate_btn:
                with st.spinner("🤖 Building your tool..."):
                    if builder.build_tool_code(selected_tool, config):
                        st.success("✅ Tool built successfully!")
                        
                        # Show file structure
                        st.subheader("Generated Files")
                        tool_path = Path("apps") / selected_tool / "public"
                        
                        if (tool_path / "index.html").exists():
                            st.success("✓ index.html")
                        if (tool_path / "script.js").exists():
                            st.success("✓ script.js")
                        
                        # Preview HTML
                        st.subheader("HTML Preview")
                        html_preview = builder.preview_html(selected_tool)
                        with st.expander("📄 View HTML Code"):
                            st.code(html_preview, language="html")
                    else:
                        st.error("❌ Failed to build tool")
        
        # Tab 3: Content Studio
        with tab3:
            st.subheader("Content Studio - Blog Generator")
            
            col1, col2 = st.columns([3, 1])
            with col1:
                target_keyword = st.text_input("Target Keyword", placeholder="e.g., 'how to calculate loan payments'")
            with col2:
                st.write("")  # Spacing
            
            if st.button("✍️ Write Article", use_container_width=True, type="primary"):
                if target_keyword:
                    with st.spinner("🤖 Generating article with Gemini AI..."):
                        article_content = content_engine.generate_article(selected_tool, target_keyword)
                        
                        if content_engine.publish_article(selected_tool, target_keyword, article_content):
                            st.success("✅ Article published!")
                            st.balloons()
                        else:
                            st.error("❌ Failed to publish article")
                else:
                    st.error("Please enter a target keyword")
            
            # Display existing articles
            st.subheader("Published Articles")
            articles = tool_manager.get_blog_articles(selected_tool)
            
            if articles:
                article_df = st.dataframe(
                    [
                        {
                            "Title": art['title'],
                            "Keyword": art['keyword'],
                            "Status": art['status'],
                            "Published": art['published_date'][:10]
                        }
                        for art in articles
                    ],
                    use_container_width=True
                )
            else:
                st.info("No articles published yet. Create one to get started!")
        
        # Tab 4: Deployment
        with tab4:
            st.subheader("Deployment Options")
            
            deployment_option = st.radio("Choose deployment method", ["Cloudflare Pages", "GitHub Pages", "Manual"])
            
            if deployment_option == "Cloudflare Pages":
                st.write("### Deploy to Cloudflare")
                st.write("""
                1. Install Wrangler CLI: `npm install -g wrangler`
                2. Authenticate: `wrangler login`
                3. Deploy: `wrangler pages deploy apps/{tool_name}/public`
                """)
                
                if st.button("🚀 Deploy to Cloudflare", use_container_width=True, type="primary"):
                    try:
                        tool_public_path = f"apps/{selected_tool}/public"
                        result = subprocess.run(
                            ["wrangler", "pages", "deploy", tool_public_path],
                            capture_output=True,
                            text=True
                        )
                        
                        st.code(result.stdout, language="bash")
                        
                        if result.returncode == 0:
                            st.success("✅ Deployment successful!")
                        else:
                            st.error(f"Deployment failed: {result.stderr}")
                    except Exception as e:
                        st.error(f"Error: {e}")
            
            elif deployment_option == "GitHub Pages":
                st.write("### Deploy to GitHub Pages")
                st.write(f""
                1. Push the `apps/{selected_tool}/public` directory to your GitHub repo
                2. Enable GitHub Pages in repository settings
                3. Set source to the deployed files
                """)
            
            else:
                st.write("### Manual Deployment")
                tool_public_path = Path("apps") / selected_tool / "public"
                st.write(f"Copy the contents of `{tool_public_path}` to your web server.")
            
            st.markdown("---")
            st.info("✨ Pro Tip: Use environment variables for sensitive configuration")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Tools Created", len(available_tools))
with col2:
    total_articles = sum(len(tool_manager.get_blog_articles(tool)) for tool in available_tools)
    st.metric("Articles Published", total_articles)
with col3:
    st.metric("API Status", "✅ Connected")
