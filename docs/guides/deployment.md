# Deployment Guide

Complete guide for deploying the ITMC Knowledge Base to GitHub Pages.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Deployment Methods](#deployment-methods)
- [Automatic Deployment (Recommended)](#automatic-deployment-recommended)
- [Manual Deployment](#manual-deployment)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)
- [Useful Commands](#useful-commands)

## 🔧 Prerequisites

Before deploying, ensure you have:

- [x] Repository pushed to GitHub
- [x] GitHub Pages enabled in repository settings
- [x] All changes committed and pushed
- [x] MkDocs and dependencies installed locally
- [x] Appropriate permissions (write access to repository)

### Check Your Setup

```bash
# Verify you're on the correct branch
git branch --show-current

# Check if there are uncommitted changes
git status

# Verify MkDocs installation
mkdocs --version

# Test build locally
mkdocs build --strict
```

## 🚀 Deployment Methods

There are two ways to deploy the knowledge base:

1. **Automatic Deployment** (via GitHub Actions) - ✅ Recommended
2. **Manual Deployment** (via `mkdocs gh-deploy` command)

---

## 🤖 Automatic Deployment (Recommended)

The site automatically deploys when you push to the `dev` branch using GitHub Actions.

### Step 1: Configure GitHub Pages

First-time setup only:

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (left sidebar)
3. Under **Build and deployment**:
   - **Source**: Select **GitHub Actions**
   - Click **Save** if needed

![GitHub Pages Settings](https://docs.github.com/assets/cb-49177/images/help/pages/github-actions-source.png)

### Step 2: Push Your Changes

```bash
# Make sure you're on the dev branch
git checkout dev

# Add all changes
git add .

# Commit with a descriptive message
git commit -m "docs: update documentation content"

# Push to GitHub
git push origin dev
```

### Step 3: Monitor Deployment

#### View GitHub Actions Workflow

1. Go to your repository on GitHub
2. Click the **Actions** tab
3. You'll see the workflow run: "Deploy MkDocs to GitHub Pages"
4. Click on the workflow run to see details

![GitHub Actions](https://docs.github.com/assets/cb-125349/images/help/repository/actions-tab.png)

#### Workflow Stages

The deployment has two stages:

```
┌─────────────────────────┐
│  1. Build               │
│  - Checkout code        │
│  - Setup Python         │
│  - Install dependencies │
│  - Build MkDocs site    │
│  - Upload artifact      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  2. Deploy              │
│  - Deploy to Pages      │
│  - Update site URL      │
└─────────────────────────┘
```

#### Check Deployment Status

**Via GitHub UI:**
- Green checkmark (✓) = Successful deployment
- Red X (✗) = Failed deployment
- Yellow circle = In progress

**Via Command Line:**
```bash
# Using GitHub CLI (if installed)
gh run list --workflow=deploy.yml --limit 5

# Check specific run
gh run view [RUN_ID]

# Watch logs in real-time
gh run watch
```

### Step 4: Access Your Site

After successful deployment (usually 2-5 minutes):

🌐 **Live Site**: [https://itmc-cloud.github.io/itmc-knowledge-base](https://itmc-cloud.github.io/itmc-knowledge-base)

**Note**: First deployment might take up to 10 minutes to propagate.

---

## 🔨 Manual Deployment

For immediate deployment or troubleshooting.

### Prerequisites for Manual Deployment

```bash
# Ensure virtual environment is activated
.venv\Scripts\Activate.ps1  # Windows
# source .venv/bin/activate  # Linux/Mac

# Verify MkDocs installation
pip list | grep mkdocs
```

### Method 1: Using `mkdocs gh-deploy`

```bash
# Build and deploy in one command
mkdocs gh-deploy

# With custom commit message
mkdocs gh-deploy -m "Deploy: updated documentation [skip ci]"

# Force push (use with caution)
mkdocs gh-deploy --force
```

**What happens:**
1. Builds the site to `site/` directory
2. Creates/updates `gh-pages` branch
3. Pushes built site to `gh-pages` branch
4. GitHub Pages serves from `gh-pages` branch

### Method 2: Manual Build and Push

```bash
# Step 1: Build the site
mkdocs build --clean --strict

# Step 2: Verify build output
ls site/

# Step 3: Deploy using ghp-import (if installed)
pip install ghp-import
ghp-import -n -p -f site

# Or manually push to gh-pages branch
git checkout gh-pages
cp -r site/* .
git add .
git commit -m "Update documentation"
git push origin gh-pages
git checkout dev
```

### When to Use Manual Deployment

- ✅ Quick hotfix deployment
- ✅ Testing deployment process
- ✅ GitHub Actions quota exceeded
- ✅ Troubleshooting build issues
- ❌ Regular updates (use automatic instead)

---

## ✅ Verification

### 1. Check Build Success

```bash
# Test build locally first
mkdocs build --strict --verbose

# Check for errors in output
# Should end with: "Documentation built in X.XX seconds"
```

### 2. Verify GitHub Actions

**Check workflow file:**
```bash
# View the workflow configuration
cat .github/workflows/deploy.yml

# Validate workflow syntax (requires act CLI)
act -l
```

**View recent deployments:**
```bash
# Using GitHub CLI
gh run list --workflow=deploy.yml --limit 10

# Check status of latest run
gh run view --web
```

### 3. Test Deployed Site

```bash
# Open site in browser (Windows)
start https://itmc-cloud.github.io/itmc-knowledge-base

# Linux/Mac
open https://itmc-cloud.github.io/itmc-knowledge-base
# or
xdg-open https://itmc-cloud.github.io/itmc-knowledge-base
```

**Manual verification checklist:**
- [ ] Homepage loads correctly
- [ ] Navigation menu works
- [ ] Search functionality works
- [ ] All pages are accessible
- [ ] Images and assets load
- [ ] Code syntax highlighting works
- [ ] Dark/light mode toggle works
- [ ] Mobile responsive design works

### 4. Check for Broken Links

```bash
# Install linkchecker (optional)
pip install linkchecker

# Check for broken links
linkchecker https://itmc-cloud.github.io/itmc-knowledge-base
```

---

## 🐛 Troubleshooting

### Issue: Workflow Doesn't Trigger

**Symptoms:**
- Push to dev branch but no workflow runs

**Solutions:**

```bash
# 1. Check workflow file exists
ls .github/workflows/deploy.yml

# 2. Verify branch name in workflow
grep -A 3 "on:" .github/workflows/deploy.yml

# 3. Manually trigger workflow
gh workflow run deploy.yml

# 4. Check GitHub Actions is enabled
# Go to Settings → Actions → General → Allow all actions
```

### Issue: Build Fails

**Symptoms:**
- Red X in GitHub Actions
- Build error messages

**Solutions:**

```bash
# 1. Build locally to see errors
mkdocs build --strict --verbose

# 2. Check Python version
python --version  # Should be 3.11+

# 3. Verify all dependencies
pip install -r requirements.txt

# 4. Check for syntax errors in mkdocs.yml
python -c "import yaml; yaml.safe_load(open('mkdocs.yml'))"

# 5. Look for missing files referenced in nav
grep -E "^\s+-.*\.md" mkdocs.yml
```

### Issue: Site Shows 404

**Symptoms:**
- Site URL returns 404 Not Found

**Solutions:**

```bash
# 1. Verify GitHub Pages is enabled
# Settings → Pages → Check source is set to GitHub Actions

# 2. Check if gh-pages branch exists
git ls-remote --heads origin gh-pages

# 3. Wait 5-10 minutes for DNS propagation

# 4. Check repository visibility (must be public or have GitHub Pro)

# 5. Verify base URL in mkdocs.yml
grep "site_url" mkdocs.yml
```

### Issue: Old Content Still Showing

**Symptoms:**
- Changes don't appear on live site

**Solutions:**

```bash
# 1. Hard refresh browser (Ctrl+F5 or Cmd+Shift+R)

# 2. Clear browser cache

# 3. Check deployment timestamp
gh run list --workflow=deploy.yml --limit 1

# 4. Force rebuild
git commit --allow-empty -m "Force rebuild"
git push origin dev

# 5. Check CDN cache (if using custom domain)
# Wait 5-10 minutes for cache invalidation
```

### Issue: Permissions Error

**Symptoms:**
- "Permission denied" or "403 Forbidden"

**Solutions:**

```bash
# 1. Check GitHub token permissions
# Settings → Actions → General → Workflow permissions
# Should be: "Read and write permissions"

# 2. Verify you have write access
gh api repos/itmc-cloud/itmc-knowledge-base | grep '"permissions"' -A 10

# 3. Re-authenticate GitHub CLI
gh auth refresh

# 4. Check branch protection rules
# Settings → Branches → Check if dev is protected
```

### Issue: Missing Dependencies

**Symptoms:**
- "ModuleNotFoundError" or "ImportError"

**Solutions:**

```bash
# 1. Reinstall all dependencies
pip install --force-reinstall -r requirements.txt

# 2. Verify requirements.txt is committed
git ls-files requirements.txt

# 3. Check Python version matches workflow
grep "python-version" .github/workflows/deploy.yml

# 4. Update pip
python -m pip install --upgrade pip
```

---

## 📝 Useful Commands

### Build & Test Commands

```bash
# Build site (clean build)
mkdocs build --clean

# Build with strict mode (fail on warnings)
mkdocs build --strict

# Build with verbose output
mkdocs build --verbose

# Serve locally
mkdocs serve

# Serve on different port
mkdocs serve -a localhost:8001

# Serve and auto-reload on changes
mkdocs serve --dirtyreload
```

### Git Commands

```bash
# Check current status
git status

# View commit history
git log --oneline -10

# View remote URLs
git remote -v

# See what will be pushed
git log origin/dev..dev

# Check which branch you're on
git branch --show-current

# View all branches
git branch -a

# Compare with remote
git fetch
git diff origin/dev
```

### GitHub CLI Commands

```bash
# View workflow runs
gh run list --workflow=deploy.yml

# Watch live workflow
gh run watch

# View specific run
gh run view [RUN_ID]

# Download workflow logs
gh run download [RUN_ID]

# View repository info
gh repo view

# Open repository in browser
gh repo view --web

# Open Actions page
gh browse /actions
```

### Debugging Commands

```bash
# Validate YAML files
python -c "import yaml; yaml.safe_load(open('mkdocs.yml'))"

# Check for syntax errors in markdown
find docs -name "*.md" -exec python -m markdown {} \; > /dev/null

# List all files that will be deployed
mkdocs build && find site -type f

# Check site size
mkdocs build && du -sh site/

# Generate site map
mkdocs build && cat site/sitemap.xml

# Test specific page build
mkdocs build && cat site/guides/deployment/index.html
```

### Maintenance Commands

```bash
# Update dependencies
pip install --upgrade mkdocs mkdocs-material pymdown-extensions

# Check for outdated packages
pip list --outdated

# Show dependency tree
pip install pipdeptree
pipdeptree

# Clean build artifacts
rm -rf site/

# Remove virtual environment
rm -rf .venv/

# Fresh install
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 🔄 Deployment Workflow Summary

### Automatic Deployment (Every Push to dev)

```mermaid
graph LR
    A[Make Changes] --> B[git add .]
    B --> C[git commit]
    C --> D[git push origin dev]
    D --> E[GitHub Actions Triggered]
    E --> F[Build Site]
    F --> G[Deploy to Pages]
    G --> H[Site Live]
```

### Manual Deployment (On Demand)

```mermaid
graph LR
    A[Make Changes] --> B[mkdocs build]
    B --> C[mkdocs gh-deploy]
    C --> D[Push to gh-pages]
    D --> E[Site Live]
```

---

## 📊 Deployment Checklist

Before deploying to production:

- [ ] All content reviewed and approved
- [ ] Local build successful (`mkdocs build --strict`)
- [ ] Local preview tested (`mkdocs serve`)
- [ ] All links verified
- [ ] Images optimized and loading
- [ ] Search functionality working
- [ ] Mobile responsive design checked
- [ ] Dark/light mode tested
- [ ] No console errors in browser
- [ ] Git status clean (`git status`)
- [ ] All changes committed
- [ ] Pushed to correct branch (`dev`)
- [ ] Deployment workflow successful
- [ ] Live site verified
- [ ] All pages accessible
- [ ] No 404 errors

---

## 🎯 Quick Reference

### First Time Setup

```bash
# 1. Enable GitHub Pages
# Go to Settings → Pages → Source: GitHub Actions

# 2. Push to dev branch
git push origin dev

# 3. Wait for deployment (2-5 minutes)

# 4. Visit your site
# https://itmc-cloud.github.io/itmc-knowledge-base
```

### Regular Updates

```bash
# Daily workflow
git add .
git commit -m "docs: update content"
git push origin dev

# Verify deployment
gh run list --workflow=deploy.yml --limit 1
```

### Emergency Hotfix

```bash
# Quick manual deployment
mkdocs gh-deploy -m "Hotfix: [description]"
```

---

## 📞 Need Help?

If you encounter issues:

1. **Check the logs**: GitHub Actions → View workflow run
2. **Test locally**: `mkdocs build --strict --verbose`
3. **Search issues**: [GitHub Issues](https://github.com/itmc-cloud/itmc-knowledge-base/issues)
4. **Documentation**: 
   - [MkDocs Documentation](https://www.mkdocs.org)
   - [Material Theme Docs](https://squidfunk.github.io/mkdocs-material)
   - [GitHub Pages Docs](https://docs.github.com/en/pages)

---

**Last Updated**: December 2025 | **Version**: 1.0
