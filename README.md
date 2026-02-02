# 🚀 AI Builder Pro - Automation Suite

A comprehensive, scalable multi-tenant tool empire with a visual Admin Dashboard. Build, deploy, and monetize calculators and productivity tools in minutes using AI-powered automation.

## 🎯 Features

### ✨ Core Features
- **🤖 AI-Powered Tool Generation**: Uses Google Gemini AI to generate tool logic automatically
- **🎨 Visual Admin Dashboard**: Streamlit-based control center for managing everything
- **📝 pSEO Blog Engine**: Auto-generates SEO-optimized blog posts with schema markup
- **🚀 One-Click Deployment**: Deploy to Cloudflare, GitHub Pages, or manual hosting
- **🔄 Multi-Tenant Architecture**: Manage unlimited tools from a single platform

### 🛠️ System Components

1. **setup_core.py** - Initializes directory structure and templates
2. **utils.py** - Core utility functions for tool management
3. **builder.py** - Intelligent tool code generator (JavaScript + HTML)
4. **content_engine.py** - AI-powered blog content generation
5. **admin_dashboard.py** - Visual control center (Streamlit)
6. **run.sh** - Bootstrap and launcher script

---

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google AI API Key (free at [Google AI Studio](https://aistudio.google.com))
- Cloudflare account (optional, for deployment)

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/microboostmedia/platform.git
cd platform
git checkout develop
```

### 2. Get Your Google AI API Key

1. Go to [Google AI Studio](https://aistudio.google.com)
2. Click "Get API Key"
3. Create a new key in Google Cloud Console
4. Copy the API key

### 3. Set Up Environment Variables

Create a `.env` file in the project root:
```bash
# Google AI API Configuration
GOOGLE_API_KEY=your-api-key-here

# Cloudflare Configuration (optional)
CLOUDFLARE_ACCOUNT_ID=your-account-id
CLOUDFLARE_API_TOKEN=your-api-token

# App Configuration
APPS_DIR=apps
TEMPLATES_DIR=apps/templates
```

### 4. Launch the Platform

```bash
bash run.sh
```

This will:
- ✓ Create a virtual environment
- ✓ Install all dependencies
- ✓ Initialize the core system
- ✓ Launch the Streamlit admin dashboard

The dashboard will open at `http://localhost:8501`

---

## 📖 How to Use

### Creating a New Tool

1. **Click "+ Create New Tool"** in the sidebar
2. **Enter Tool Details**:
   - Tool Name: `loan_calculator`
   - Display Title: `Loan Calculator`
   - Description: What does it do?
   - Formula/Logic: How does it work?

### Configuring Tool Inputs

1. **Go to Configuration Tab**
2. **Add Input Fields**:
   - Label: "Loan Amount"
   - ID: "principal"
   - Type: "number"
   - Placeholder: "Enter amount"

3. **Save Configuration**

### Generating Tool Code

1. **Go to Build & Preview Tab**
2. **Click "Generate Code"**
3. The AI will:
   - Generate JavaScript logic using Gemini
   - Create HTML interface
   - Preview both before saving

### Publishing Blog Articles

1. **Go to Content Studio Tab**
2. **Enter Target Keyword** (e.g., "how to calculate loan payments")
3. **Click "Write Article"**
4. The AI will:
   - Generate 1500+ word SEO-optimized content
   - Add schema markup
   - Auto-link to your tool
   - Save as HTML

### Deploying Your Tools

1. **Go to Deployment Tab**
2. **Choose Deployment Method**:
   - **Cloudflare Pages**: One-click deploy via Wrangler
   - **GitHub Pages**: Static site hosting
   - **Manual**: Download and upload

---

## 📁 Project Structure

```
platform/
├── apps/                          # All tools stored here
│   ├── templates/
│   │   ├── base_tool.html        # Tool UI template
│   │   └── base_blog.html        # Blog post template
│   └── [tool_name]/
│       ├── config.json           # Tool configuration
│       ├── public/               # Generated files
│       │   ├── index.html
│       │   ├── script.js
│       │   └── blog/
│       ├── src/                  # Source code
│       └── content/              # Content files
├── setup_core.py                 # Core initialization
├── utils.py                      # Utility functions
├── builder.py                    # Tool code generator
├── content_engine.py             # Content generator
├── admin_dashboard.py            # Admin interface
├── requirements.txt              # Python dependencies
├── run.sh                        # Launch script
└── README.md                     # This file
```

---

## 🔧 Configuration

### Tool Configuration (config.json)

```json
{
  "title": "Loan Calculator",
  "description": "Calculate monthly loan payments",
  "formula_description": "Uses amortization formula...",
  "inputs": [
    {
      "id": "principal",
      "label": "Loan Amount ($)",
      "type": "number",
      "placeholder": "Enter loan amount"
    },
    {
      "id": "rate",
      "label": "Annual Interest Rate (%)",
      "type": "number",
      "placeholder": "e.g., 5.5"
    },
    {
      "id": "years",
      "label": "Loan Term (Years)",
      "type": "number",
      "placeholder": "e.g., 30"
    }
  ]
}
```

---

## 🌐 Generated Tool Structure

Each tool generates:

```
loan_calculator/
├── public/
│   ├── index.html               # Generated UI
│   ├── script.js                # Generated Logic
│   └── blog/
│       ├── how-to-calculate-loan-payments.html
│       └── [more articles...]
├── src/                         # Source code (if any)
└── config.json                  # Configuration
```

---

## 🚀 Deployment Guide

### Cloudflare Pages (Recommended)

```bash
# Install Wrangler CLI
npm install -g wrangler

# Authenticate
wrangler login

# Deploy
wrangler pages deploy apps/loan_calculator/public
```

### GitHub Pages

1. Push `apps/[tool_name]/public` to your GitHub repo
2. Go to Settings → Pages
3. Set source to the `/docs` folder or deploy from branch

### Manual Deployment

1. Download the `public` folder
2. Upload to your hosting provider
3. Set the domain

---

## 💡 Example Tools to Build

- 💰 **Loan Calculator** - Calculate monthly payments
- 📊 **ROI Calculator** - Measure return on investment
- 🏠 **Mortgage Calculator** - Home financing
- ⏱️ **Time Converter** - Convert between timezones
- 📐 **Geometry Calculator** - Area, perimeter, volume
- 📈 **Investment Calculator** - Compound interest
- 💪 **BMI Calculator** - Health metrics
- 🎓 **GPA Calculator** - Academic performance

---

## 🔐 Security Best Practices

1. **Never commit your `.env` file** - Add to `.gitignore`
2. **Keep API keys secret** - Use environment variables
3. **Validate user input** - Tool generates validation code
4. **Use HTTPS** - Always deploy on secure servers
5. **Update dependencies** - Run `pip install --upgrade -r requirements.txt`

---

## 📊 Performance Tips

- **Cache Generated Content** - Blog posts are static HTML
- **Optimize Images** - Use responsive images in templates
- **Lazy Load Scripts** - Load JavaScript only when needed
- **Use CDN** - Serve CSS/JS from Tailwind CDN (already included)

---

## 🐛 Troubleshooting

### "GOOGLE_API_KEY not found"
```bash
# Make sure .env file exists and has the key
cat .env
```

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### "Wrangler command not found"
```bash
# Install Cloudflare Wrangler CLI
npm install -g wrangler
```

### Dashboard won't load
```bash
# Clear Streamlit cache and restart
streamlit cache clear
bash run.sh
```

---

## 📚 Advanced Usage

### Custom JavaScript Logic

Edit generated `script.js` files to add custom logic:
```javascript
function calculateResult() {
    const input1 = parseFloat(document.getElementById('input1').value);
    const input2 = parseFloat(document.getElementById('input2').value);
    
    // Your custom logic here
    const result = input1 * input2;
    
    document.getElementById('resultValue').textContent = result.toFixed(2);
    document.getElementById('result').classList.remove('hidden');
}
```

### Custom Styling

Modify templates in `apps/templates/` to customize appearance:
- Update Tailwind CSS classes
- Add custom fonts
- Modify color schemes
- Add animations

### Custom Blog Templates

Edit `base_blog.html` to customize blog layout:
- Change header design
- Modify CTA button
- Update author box
- Adjust responsive layout

---

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Support

- 📖 **Documentation**: [Wiki](https://github.com/microboostmedia/platform/wiki)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/microboostmedia/platform/discussions)
- 🐛 **Issues**: [Report a Bug](https://github.com/microboostmedia/platform/issues)
- 📧 **Email**: support@microboostmedia.com

---

## 🎉 Built With

- [Streamlit](https://streamlit.io) - Admin Dashboard
- [Google Generative AI](https://ai.google.dev) - AI Logic Generation
- [Jinja2](https://jinja.palletsprojects.com) - Template Engine
- [Tailwind CSS](https://tailwindcss.com) - Styling
- [Cloudflare Pages](https://pages.cloudflare.com) - Deployment

---

## 🚀 Roadmap

- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Custom domain management
- [ ] Team collaboration features
- [ ] API endpoint generation
- [ ] Mobile app builder
- [ ] Monetization integration
- [ ] White-label solutions

---

**Made with ❤️ by MicroBoost Media**
