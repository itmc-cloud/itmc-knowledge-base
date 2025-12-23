# Project Documentation

## 📋 Overview

This is the ITMC Knowledge Base, a documentation site built with **MkDocs** and **Material for MkDocs** theme. The site automatically builds and deploys to GitHub Pages whenever changes are pushed to the `dev` branch.

**Live Site:** https://itmc-cloud.github.io/itmc-knowledge-base

---

## 📚 Documentation Guides

Choose the guide that fits your needs:

### 🚀 [SETUP.md](SETUP.md) - Environment Setup
**For new team members setting up for the first time**

- Prerequisites and installation
- Clone repository
- Create virtual environment
- Install dependencies
- Verify installation
- Troubleshooting setup issues

**Start here if:** You're new to the project or setting up on a new machine.

---

### 💻 [DEVELOPMENT.md](DEVELOPMENT.md) - Development Workflow
**For daily development - running server, adding content**

- Starting the development server
- Adding new pages and sections
- Markdown features and syntax
- Navigation auto-update
- Testing your changes
- Working with assets
- Common development issues

**Use this for:** Day-to-day content creation and updates.

---

### 🚀 [DEPLOYMENT.md](DEPLOYMENT.md) - Deployment & Commit
**For deploying changes to production**

- Pre-deployment checklist (5 steps)
- Commit and push workflow
- Monitoring deployment
- Troubleshooting failed builds
- GitHub Pages configuration
- Quick deployment commands

**Use this when:** You're ready to publish your changes live.

---

---

## 🏗️ Project Structure

```
itmc-knowledge-base/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions deployment
├── docs/                        # Documentation content (Markdown files)
│   ├── index.md                # Homepage
│   ├── about.md                # About page
│   ├── guides/                 # User guides
│   ├── services/               # Service documentation
│   └── snippets/               # Code snippets
├── site/                        # Generated static site (don't commit)
├── .venv/                       # Virtual environment (don't commit)
├── mkdocs.yml                   # MkDocs configuration
├── requirements.txt             # Python dependencies
├── update_nav.py                # Navigation auto-update script
├── SETUP.md                     # Environment setup guide
├── DEVELOPMENT.md               # Development workflow guide
├── DEPLOYMENT.md                # Deployment guide
├── PROJECT.md                   # This file - documentation hub
└── README.md                    # Repository README
```

---

## ⚡ Quick Start

### First Time Setup

```bash
# 1. Clone and navigate
git clone https://github.com/itmc-cloud/itmc-knowledge-base.git
cd itmc-knowledge-base

# 2. Setup virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate   # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt
```

**Full details:** See [SETUP.md](SETUP.md)

### Daily Development

```bash
# 1. Start dev server
mkdocs serve

# 2. Edit files in docs/

# 3. If you added files, update navigation
python update_nav.py
```

**Full details:** See [DEVELOPMENT.md](DEVELOPMENT.md)

### Deploy Changes

```bash
# 1. Update navigation (if needed)
python update_nav.py

# 2. Test locally
mkdocs serve

# 3. Validate build
mkdocs build --clean --strict

# 4. Commit and push to dev
git add docs/ mkdocs.yml
git commit -m "Your message"
git push origin dev
```

**Full details:** See [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 🎯 Common Tasks

### I want to add a new page

1. Create `.md` file in `docs/` folder
2. Write content in Markdown
3. Run `python update_nav.py`
4. Check with `mkdocs serve`

**Guide:** [DEVELOPMENT.md - Adding New Content](DEVELOPMENT.md#adding-new-content)

### I want to deploy my changes

1. Follow the 5-step checklist
2. Push to `dev` branch
3. Monitor GitHub Actions
4. Verify on live site

**Guide:** [DEPLOYMENT.md - Pre-Deployment Checklist](DEPLOYMENT.md#pre-deployment-checklist)

### I'm getting build errors

1. Run `mkdocs build --strict` locally
2. Fix reported errors (broken links, missing files)
3. Test again until it passes

**Guide:** [DEPLOYMENT.md - If Deployment Fails](DEPLOYMENT.md#if-deployment-fails)

### I need to set up on a new machine

1. Follow SETUP.md step-by-step
2. Verify with `mkdocs --version`
3. Test with `mkdocs serve`

**Guide:** [SETUP.md - Initial Setup](SETUP.md#initial-setup)

---

## 📖 Key Concepts

### MkDocs
Static site generator that converts Markdown files into a documentation website.

### Material Theme
Modern, responsive design theme for MkDocs with advanced features.

### Auto-Deployment
GitHub Actions automatically builds and deploys when you push to `dev` branch.

### Navigation Script
`update_nav.py` scans your `docs/` folder and updates the navigation menu in `mkdocs.yml`.

### Virtual Environment
Isolated Python environment (`.venv` folder) that keeps project dependencies separate.

---

---

## 🔗 Useful Links

- **Live Site:** https://itmc-cloud.github.io/itmc-knowledge-base
- **Repository:** https://github.com/itmc-cloud/itmc-knowledge-base
- **GitHub Actions:** https://github.com/itmc-cloud/itmc-knowledge-base/actions
- **GitHub Pages Settings:** https://github.com/itmc-cloud/itmc-knowledge-base/settings/pages

---

## 📞 Support & Resources

**Documentation:**
- [MkDocs Official Docs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)

**Need Help?**
- Check the relevant guide above
- Contact the ITMC Cloud team
- Open an issue on GitHub
- Review GitHub Actions logs for deployment issues

---

**Last Updated:** December 23, 2025

### Quick Start (if virtual environment is already activated)

```bash
# If you see (.venv) in your terminal prompt, simply run:
mkdocs serve

# For network access:
mkdocs serve --dev-addr 0.0.0.0:8000
```

### Full Start (if starting fresh)

```bash
# 1. Activate virtual environment first
.venv\Scripts\Activate.ps1   # Windows PowerShell
# OR
source .venv/bin/activate     # Linux/Mac

# 2. Then run MkDocs
mkdocs serve

# For network access:
mkdocs serve --dev-addr 0.0.0.0:8000
```

### Using Python Module Method (works without activating venv)

```bash
# Windows
.venv\Scripts\python.exe -m mkdocs serve

# Network access
.venv\Scripts\python.exe -m mkdocs serve --dev-addr 0.0.0.0:8000

# Linux/Mac
.venv/bin/python -m mkdocs serve
```

### Access URLs

- **Local only:** `http://127.0.0.1:8000/itmc-knowledge-base/`
- **Network:** `http://YOUR-IP:8000/itmc-knowledge-base/` (replace YOUR-IP with your machine's IP)

### Features of Development Server

- ✅ **Auto-reload**: Changes to `.md` files or `mkdocs.yml` trigger automatic rebuild
- ✅ **Live browser refresh**: Browser updates automatically
- ✅ **Error reporting**: Build errors shown in terminal
- ✅ **Fast rebuilds**: Only changed files are processed

## ✍️ Adding New Content

### Creating a New Page

1. **Create a Markdown file in `docs/` folder**
   ```bash
   # Example: Create a new tutorial
   touch docs/tutorials/kubernetes.md
   ```

2. **Write your content** (use Markdown format)
   ```markdown
   # Kubernetes Tutorial
   
   ## Introduction
   Your content here...
   
   ## Code Example
   ```yaml
   apiVersion: v1
   kind: Pod
   ```
   ```

3. **Update navigation automatically**
   ```bash
   python update_nav.py
   ```

4. **View your changes**
   - If `mkdocs serve` is running, the site will auto-reload
   - Your new page will appear in the navigation menu

### Creating a New Section

```bash
# Create a new folder with an index page
mkdir docs/tutorials
echo "# Tutorials Overview" > docs/tutorials/index.md

# Add some pages
echo "# Docker Tutorial" > docs/tutorials/docker.md
echo "# Kubernetes Tutorial" > docs/tutorials/kubernetes.md

# Update navigation
python update_nav.py
```

The script will automatically create a "Tutorials" section with:
- Overview (from `index.md`)
- Docker Tutorial
- Kubernetes Tutorial

## 🔄 Navigation Auto-Update Script

### Usage

```bash
python update_nav.py
```

### What It Does

1. **Scans** all files and folders in `docs/`
2. **Generates** hierarchical navigation structure
3. **Updates** the `nav:` section in `mkdocs.yml`
4. **Preserves** all other MkDocs configuration
5. **Triggers** auto-reload if dev server is running

### Naming Conventions

The script automatically formats filenames into readable titles:

| Filename | Navigation Title |
|----------|-----------------|
| `getting-started.md` | Getting Started |
| `cloud-solutions.md` | Cloud Solutions |
| `api-reference.md` | Api Reference |
| `index.md` | Overview (in sections) or Home (at root) |

### Manual Navigation (if needed)

If you prefer manual control, edit the `nav:` section in `mkdocs.yml`:

```yaml
nav:
  - Home: index.md
  - Guides:
      - Getting Started: guides/getting-started.md
      - Deployment: guides/deployment.md
```

## 🏗️ Building for Production

### Build Static Site

```bash
mkdocs build
```

This generates the static site in the `site/` directory.

### Build with Clean

```bash
mkdocs build --clean
```

Removes old files before building (recommended before deployment).

### Validate Build

```bash
mkdocs build --strict
```

Treats warnings as errors - useful for CI/CD validation.

## 📤 Committing and Submitting Changes

### ✅ Pre-Deployment Checklist

Complete **ALL** steps before pushing to `dev` branch:

#### Step 1: Update Navigation (if you added/removed files)

```bash
# Run navigation update script
python update_nav.py

# OR without venv activated (Windows)
.venv\Scripts\python.exe update_nav.py
```

**When to run:**
- ✅ After adding new `.md` files
- ✅ After creating new folders in `docs/`
- ✅ After renaming or moving files
- ❌ Skip if you only edited existing content

---

#### Step 2: Test Locally

```bash
# Start development server
mkdocs serve

# OR without venv activated (Windows)
.venv\Scripts\python.exe -m mkdocs serve
```

**What to check:**
- ✅ All pages load without errors
- ✅ Navigation menu is correct
- ✅ Internal links work
- ✅ Code blocks render properly
- ✅ Images display correctly
- ✅ No 404 errors

**Access:** `http://127.0.0.1:8000/itmc-knowledge-base/`

---

#### Step 3: Build and Validate

```bash
# Clean build with strict validation
mkdocs build --clean --strict

# OR without venv activated (Windows)
.venv\Scripts\python.exe -m mkdocs build --clean --strict
```

**What this does:**
- 🧹 Removes old `site/` folder
- 🏗️ Builds fresh static site
- ⚠️ Treats warnings as errors
- 🔍 Catches broken links and missing anchors

**Expected output:**
```
INFO    -  Cleaning site directory
INFO    -  Building documentation to directory: ./site
INFO    -  Documentation built in 2.12 seconds
```

**If you see errors:**
- ❌ Fix all errors before continuing
- ❌ Do NOT push with build errors
- ✅ Common issues: broken links, missing anchors, invalid YAML

---

#### Step 4: Review Changes

```bash
# Check what changed
git status

# Review specific file changes
git diff docs/
git diff mkdocs.yml
```

**Files to include:**
- ✅ `docs/**/*.md` - Your content changes
- ✅ `mkdocs.yml` - If navigation updated
- ✅ `requirements.txt` - If added dependencies
- ✅ `PROJECT.md` or `README.md` - If updated docs

**Files to NEVER commit:**
- ❌ `site/` folder (auto-generated)
- ❌ `.venv/` folder (virtual environment)
- ❌ `__pycache__/` folders
- ❌ `.DS_Store` or OS-specific files

---

#### Step 5: Commit and Push

```bash
# Add your changes
git add docs/          # Documentation changes
git add mkdocs.yml     # Navigation updates
git add PROJECT.md     # If you updated docs

# Commit with descriptive message
git commit -m "Add Kubernetes tutorial to guides section"

# Push to dev branch (triggers deployment!)
git push origin dev
```

**Commit message tips:**
- ✅ Be descriptive: "Add Docker deployment guide"
- ✅ Use present tense: "Update API documentation"
- ✅ Be specific: "Fix broken links in services section"
- ❌ Avoid vague: "Update files" or "Changes"

---

### 🚀 After Pushing (Automatic Deployment)

Once you push to `dev`:

1. **GitHub Actions triggers** automatically
2. **Monitor progress:**
   - Go to: `https://github.com/itmc-cloud/itmc-knowledge-base/actions`
   - Click on latest workflow run
   - Watch build progress (~2-3 minutes)

3. **Deployment steps:**
   ```
   ✓ Checkout repository        (~10s)
   ✓ Setup Python 3.11          (~20s)
   ✓ Install dependencies       (~30s)
   ✓ Build with mkdocs         (~5s)
   ✓ Deploy to GitHub Pages    (~30s)
   ```

4. **Verify deployment:**
   - Wait 2-3 minutes for completion
   - Visit: `https://itmc-cloud.github.io/itmc-knowledge-base`
   - Hard refresh browser (Ctrl+F5)
   - Check your changes are live

---

### 🛑 If Build Fails on GitHub

**Check the error:**
1. Go to Actions tab
2. Click failed workflow
3. Read error message

**Common failures:**

| Error | Cause | Fix |
|-------|-------|-----|
| `mkdocs build --strict` fails | Broken links or anchors | Run `mkdocs build --strict` locally and fix errors |
| YAML parsing error | Invalid `mkdocs.yml` syntax | Check YAML formatting |
| Missing file | Referenced file doesn't exist | Verify all linked files are committed |
| Module not found | Missing dependency | Update `requirements.txt` |

**To fix:**
```bash
# 1. Fix the issue locally
# 2. Test again
mkdocs build --clean --strict

# 3. Commit fix
git add .
git commit -m "Fix: [describe the fix]"
git push origin dev
```

---

### 📋 Complete Pre-Push Command Sequence

**Copy and run these commands before every push to dev:**

```bash
# 1. Update navigation (if you added/removed files)
python update_nav.py

# 2. Test locally - CHECK THE SITE!
mkdocs serve
# → Open http://127.0.0.1:8000/itmc-knowledge-base/
# → Verify everything works
# → Press Ctrl+C to stop

# 3. Build and validate - MUST PASS!
mkdocs build --clean --strict

# 4. If build passes, commit and push
git status
git add docs/ mkdocs.yml
git commit -m "Your descriptive message"
git push origin dev

# 5. Monitor deployment
# → https://github.com/itmc-cloud/itmc-knowledge-base/actions
```

### GitHub Pages Deployment

**IMPORTANT:** The site automatically deploys when you push to the **`dev`** branch.

#### How Automatic Deployment Works

```
Push to dev branch
      ↓
GitHub Actions triggers
      ↓
Installs Python 3.11 & dependencies
      ↓
Runs: mkdocs build --strict
      ↓
Deploys to GitHub Pages
      ↓
Site live in ~2-3 minutes
```

#### Deployment Configuration

The deployment is configured in [.github/workflows/deploy.yml](.github/workflows/deploy.yml):

- **Trigger:** Push to `dev` branch
- **Build:** `mkdocs build --strict` (treats warnings as errors)
- **Deploy:** Automatic to GitHub Pages
- **Live URL:** `https://itmc-cloud.github.io/itmc-knowledge-base`

#### Before Pushing to Dev

**Always complete this checklist:**

```bash
# 1. Update navigation (if you added/removed files)
python update_nav.py

# 2. Test locally
mkdocs serve
# → Check http://127.0.0.1:8000/itmc-knowledge-base/

# 3. Build and validate
mkdocs build --strict
# → Must complete without errors

# 4. If build passes, commit and push
git add .
git commit -m "Your descriptive message"
git push origin dev
```

#### Monitor Deployment

After pushing to `dev`:

1. Go to your GitHub repository
2. Click **Actions** tab
3. Watch the "Deploy MkDocs to GitHub Pages" workflow
4. Deployment takes ~2-3 minutes
5. Check the live site at: `https://itmc-cloud.github.io/itmc-knowledge-base`

#### Deployment Workflow Details

| Step | Action | Duration |
|------|--------|----------|
| 1. Checkout | Clone repository | ~10s |
| 2. Setup Python | Install Python 3.11 | ~20s |
| 3. Install deps | `pip install -r requirements.txt` | ~30s |
| 4. Build | `mkdocs build --strict` | ~5s |
| 5. Deploy | Upload to GitHub Pages | ~30s |

**Total time:** ~2-3 minutes from push to live

#### Troubleshooting Deployment

**Build fails with `--strict` errors:**
- Check warnings during local `mkdocs build`
- Fix broken links and missing anchors
- Run `mkdocs build --strict` locally first

**Deployment doesn't trigger:**
- Verify you pushed to `dev` branch (not `main`)
- Check GitHub Actions is enabled in repository settings
- Review `.github/workflows/deploy.yml` configuration

**Site doesn't update:**
- Wait 3-5 minutes for full deployment
- Hard refresh browser (Ctrl+F5)
- Check GitHub Pages settings (Settings → Pages)

#### Manual Deployment (Alternative)

If you need to deploy manually:

```bash
# Build the site
mkdocs build --clean

# Deploy using MkDocs deploy command
mkdocs gh-deploy --force
```

**Note:** This is rarely needed as automatic deployment is preferred.

## 🎨 Markdown Features

### Supported Extensions

#### Code Blocks with Syntax Highlighting

````markdown
```python
def hello_world():
    print("Hello, World!")
```
````

#### Admonitions (Callouts)

```markdown
!!! note "Note Title"
    This is a note admonition.

!!! warning
    This is a warning.

!!! tip
    This is a helpful tip!
```

#### Tabs

```markdown
=== "Tab 1"
    Content for tab 1

=== "Tab 2"
    Content for tab 2
```

#### Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
```

#### Task Lists

```markdown
- [x] Completed task
- [ ] Pending task
- [ ] Another pending task
```

### Internal Links

Link to other pages in your documentation:

```markdown
[Getting Started](guides/getting-started.md)
[Cloud Solutions](services/cloud-solutions.md)
```

## 🐛 Troubleshooting

### Common Issues

#### MkDocs command not found

**Problem**: `mkdocs: The term 'mkdocs' is not recognized...`

**Solution**: 
```bash
# Activate virtual environment first
.venv\Scripts\Activate.ps1

# Or use full path
.venv\Scripts\python.exe -m mkdocs serve
```

#### Broken anchor warnings

**Problem**: `Doc file contains a link 'page.md#section', but the doc does not contain an anchor '#section'`

**Solution**: Either:
1. Add the missing section heading in the target page
2. Remove or fix the broken link

#### Port already in use

**Problem**: `OSError: [Errno 98] Address already in use`

**Solution**:
```bash
# Use a different port
mkdocs serve --dev-addr 0.0.0.0:8001
```

#### Navigation not updating

**Problem**: New files don't appear in navigation

**Solution**:
```bash
# Run the auto-update script
python update_nav.py

# Or manually add to mkdocs.yml nav section
```

## 📚 Additional Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)

## 🤝 Contributing Guidelines

### Content Guidelines

1. **Write clear, concise documentation**
2. **Use proper Markdown formatting**
3. **Include code examples where relevant**
4. **Test all code snippets before adding**
5. **Use consistent terminology**

### File Naming

- Use lowercase with hyphens: `getting-started.md`
- Be descriptive: `docker-deployment-guide.md` not `docker.md`
- Use `.md` extension for Markdown files

### Folder Organization

```
docs/
├── guides/          # Step-by-step tutorials
├── services/        # Service descriptions
├── snippets/        # Reusable code examples
└── [new-section]/   # Organize by topic
```

## 📋 Checklist for Contributors

Before submitting your changes:

- [ ] Created/edited Markdown files in `docs/` folder
- [ ] Ran `python update_nav.py` to update navigation
- [ ] Tested locally with `mkdocs serve`
- [ ] Checked for broken links and errors
- [ ] Built with `mkdocs build --strict` (no errors)
- [ ] Committed changes with descriptive message
- [ ] Did NOT commit `site/` or `.venv/` folders

## 🎯 Quick Reference Commands

```bash
# ============================================
# INITIAL SETUP (ONE TIME ONLY)
# ============================================

# Clone repository
git clone https://github.com/itmc-cloud/itmc-knowledge-base.git
cd itmc-knowledge-base

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\Activate.ps1              # Windows PowerShell
.venv\Scripts\activate.bat              # Windows CMD
source .venv/bin/activate               # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# ============================================
# DAILY DEVELOPMENT
# ============================================

# Start development server (after activating venv)
mkdocs serve                            # Local only
mkdocs serve --dev-addr 0.0.0.0:8000    # Network accessible

# OR without activating venv (Windows)
.venv\Scripts\python.exe -m mkdocs serve
.venv\Scripts\python.exe -m mkdocs serve --dev-addr 0.0.0.0:8000

# Add new content
python update_nav.py                    # Update navigation after adding files

# ============================================
# BEFORE COMMITTING
# ============================================

# Build and validate
mkdocs build --clean                    # Clean build
mkdocs build --strict                   # Validate (must pass!)

# OR without activating venv (Windows)
.venv\Scripts\python.exe -m mkdocs build --clean
.venv\Scripts\python.exe -m mkdocs build --strict

# ============================================
# GIT WORKFLOW
# ============================================

# Check status and commit
git status
git add .
git commit -m "Your descriptive message"
git push origin dev                     # Triggers auto-deployment!
```

## 📞 Support

For issues or questions:
- Check this documentation first
- Review [MkDocs documentation](https://www.mkdocs.org/)
- Contact ITMC Cloud team
- Open an issue on GitHub

---

**Last Updated**: December 23, 2025
