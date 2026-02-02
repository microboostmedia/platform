#!/bin/bash

# AI Builder - Bootstrap & Launch Script
# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 AI Builder Pro Automation Suite${NC}"
echo -e "${BLUE}=================================${NC}\n"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is not installed${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Python 3 found${NC}"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}📦 Creating virtual environment...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo -e "${YELLOW}🔌 Activating virtual environment...${NC}"
source venv/bin/activate

# Install requirements
echo -e "${YELLOW}📥 Installing dependencies...${NC}"
pip install -q -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"

# Check for .env file
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}⚙️ Creating .env file template...${NC}"
    cat > .env << EOF
# Google AI API Configuration
GOOGLE_API_KEY=your-api-key-here

# Cloudflare Configuration
CLOUDFLARE_ACCOUNT_ID=your-account-id
CLOUDFLARE_API_TOKEN=your-api-token

# App Configuration
APPS_DIR=apps
TEMPLATES_DIR=apps/templates
EOF
    echo -e "${YELLOW}⚠️ Please update .env with your API keys${NC}"
    echo -e "${YELLOW}📝 Edit .env and add your Google AI API key${NC}"
fi

# Run setup
echo -e "${YELLOW}🏗️ Running core setup...${NC}"
python setup_core.py
echo -e "${GREEN}✓ Core setup complete${NC}"

# Launch Streamlit
echo -e "${BLUE}=================================${NC}"
echo -e "${BLUE}🎛️ Launching Admin Dashboard...${NC}"
echo -e "${BLUE}=================================${NC}\n"

streamlit run admin_dashboard.py --logger.level=error