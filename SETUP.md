# Environment Setup Guide

> **For:** New team members setting up the project for the first time

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.11 or higher** (tested with Python 3.12)
- **pip** (Python package manager - comes with Python)
- **Git** (for version control)
- **Text editor** (VS Code recommended)
- **Terminal** (PowerShell, CMD, or bash)

### Check Your Python Version

```bash
python --version
# Should show: Python 3.11.x or 3.12.x or higher
```

If you don't have Python installed, download it from: https://www.python.org/downloads/

---

## 🚀 Initial Setup

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/itmc-cloud/itmc-knowledge-base.git

# Navigate to project directory
cd itmc-knowledge-base
```

---

### Step 2: Create Virtual Environment

A virtual environment keeps project dependencies isolated from your system Python.

```bash
# Create virtual environment
python -m venv .venv
```

**What this does:**
- Creates a `.venv` folder in your project
- Contains isolated Python installation
- Keeps dependencies separate from system Python

---

### Step 3: Activate Virtual Environment

**Windows PowerShell:**
```bash
.venv\Scripts\Activate.ps1
```

**Windows CMD:**
```bash
.venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

**How to know it's activated:**
- You'll see `(.venv)` at the beginning of your terminal prompt
- Example: `(.venv) PS C:\...\itmc-wiki>`

---

### Step 4: Install Dependencies

```bash
# Make sure virtual environment is activated first!
pip install -r requirements.txt
```

**What gets installed:**
- `mkdocs` - Static site generator
- `mkdocs-material` - Material Design theme
- `pymdown-extensions` - Markdown extensions
- `pyyaml` - For navigation script

**Installation time:** ~30-60 seconds

---

## ✅ Verify Installation

Test that everything is installed correctly:

```bash
# Check MkDocs version
mkdocs --version

# Should show something like:
# mkdocs, version 1.5.3
```

---

## 📁 Project Structure Overview

```
itmc-knowledge-base/
├── .venv/                   # Virtual environment (don't commit)
├── .github/                 # GitHub Actions workflows
│   └── workflows/
│       └── deploy.yml      # Auto-deployment configuration
├── docs/                    # Your documentation content
│   ├── index.md            # Homepage
│   ├── about.md            # About page
│   ├── guides/             # User guides
│   ├── services/           # Service documentation
│   └── snippets/           # Code snippets
├── site/                    # Generated static site (don't commit)
├── mkdocs.yml              # MkDocs configuration
├── requirements.txt        # Python dependencies
├── update_nav.py           # Navigation auto-update script
├── PROJECT.md              # Main documentation hub
├── SETUP.md               # This file
├── DEVELOPMENT.md         # Development guide
├── DEPLOYMENT.md          # Deployment guide
└── README.md              # Repository README
```

---

## 🔍 Understanding Key Files

### `mkdocs.yml`
- **Purpose:** MkDocs configuration
- **Contains:** Site settings, theme config, navigation structure
- **Edit when:** Changing site settings or manually editing navigation

### `requirements.txt`
- **Purpose:** Lists all Python dependencies
- **Edit when:** Adding new Python packages
- **Format:** One package per line with version

### `update_nav.py`
- **Purpose:** Automatically updates navigation in `mkdocs.yml`
- **Run when:** Adding/removing files or folders in `docs/`
- **How:** `python update_nav.py`

### `docs/` folder
- **Purpose:** All your Markdown documentation files
- **Add:** New `.md` files and folders here
- **Don't add:** Images go in `docs/assets/images/` (if needed)

### `site/` folder
- **Purpose:** Auto-generated static HTML files
- **Don't edit:** Rebuilt every time you run `mkdocs build`
- **Don't commit:** Already in `.gitignore`

---

## 🎓 Next Steps

**Setup complete! Now you're ready to:**

1. **Start development** → See [DEVELOPMENT.md](DEVELOPMENT.md)
2. **Add new content** → See [DEVELOPMENT.md](DEVELOPMENT.md#adding-new-content)
3. **Deploy changes** → See [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 🆘 Troubleshooting

### Virtual Environment Won't Activate

**Windows PowerShell - Execution Policy Error:**
```bash
# Run PowerShell as Administrator and execute:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activating again
.venv\Scripts\Activate.ps1
```

### Python Command Not Found

**Windows:**
- Make sure Python is in your PATH
- Try `py` instead of `python`
- Reinstall Python and check "Add Python to PATH"

**Linux/Mac:**
- Try `python3` instead of `python`
- Install Python: `sudo apt install python3` (Ubuntu/Debian)

### pip Install Fails

**Try upgrading pip first:**
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Wrong Python Version

**Check available Python versions:**
```bash
# Windows
py -0

# Linux/Mac
python3 --version
python3.11 --version
python3.12 --version
```

**Use specific version:**
```bash
# Windows
py -3.12 -m venv .venv

# Linux/Mac
python3.12 -m venv .venv
```

---

## 📚 Additional Resources

- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

---

**Need help?** Ask the team or check [PROJECT.md](PROJECT.md) for more documentation links.
