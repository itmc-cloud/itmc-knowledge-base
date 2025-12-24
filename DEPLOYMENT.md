# Deployment Guide

> **For:** Committing changes and deploying to GitHub Pages

## 🚨 Important

**Deployment Branch:** All changes must be pushed to the **`dev`** branch to trigger automatic deployment.

**Deployment URL:** https://itmc-cloud.github.io/itmc-knowledge-base

---

## ✅ Pre-Deployment Checklist

Complete **ALL 5 steps** before pushing to `dev`:

---

### ✓ Step 1: Update Navigation

**Run if you added/removed/moved files:**

```bash
# With venv activated
python update_nav.py

# Without venv activated (Windows)
.venv\Scripts\python.exe update_nav.py

# Linux/Mac
.venv/bin/python update_nav.py
```

**Skip if:** You only edited existing file content.

---

### ✓ Step 2: Test Locally

```bash
# Start development server
mkdocs serve

# Or without venv
.venv\Scripts\python.exe -m mkdocs serve
```

**Open:** http://127.0.0.1:8000/itmc-knowledge-base/

**Check:**
- [ ] All pages load without errors
- [ ] Navigation menu is correct
- [ ] New content appears properly
- [ ] Internal links work
- [ ] Code blocks render correctly
- [ ] No 404 errors

**Stop server:** `Ctrl+C`

---

### ✓ Step 3: Build and Validate

**This step is REQUIRED and must pass:**

```bash
# Build with strict validation
mkdocs build --clean --strict

# Or without venv
.venv\Scripts\python.exe -m mkdocs build --clean --strict
```

**Expected output:**
```
INFO    -  Cleaning site directory
INFO    -  Building documentation to directory: ./site
INFO    -  Documentation built in 2.12 seconds
```

**If you see errors:**
- ❌ **DO NOT PUSH** until all errors are fixed
- ⚠️ Common issues:
  - Broken internal links
  - Missing anchor references
  - Invalid YAML syntax in `mkdocs.yml`
  - Missing files referenced in navigation

**Fix errors and re-run until it passes!**

---

### ✓ Step 4: Review Changes

```bash
# See what files changed
git status

# Review specific changes
git diff docs/
git diff mkdocs.yml
git diff PROJECT.md
```

**Files to commit:**
- ✅ `docs/**/*.md` - Your documentation content
- ✅ `mkdocs.yml` - If navigation was updated
- ✅ `requirements.txt` - If you added dependencies
- ✅ `*.md` files in root (SETUP.md, DEVELOPMENT.md, etc.)

**Files to NEVER commit:**
- ❌ `site/` folder (auto-generated)
- ❌ `.venv/` folder (virtual environment)
- ❌ `__pycache__/` folders
- ❌ `.DS_Store`, `Thumbs.db` (OS files)

---

### ✓ Step 5: Commit and Push

```bash
# Add files
git add docs/
git add mkdocs.yml
git add SETUP.md DEVELOPMENT.md DEPLOYMENT.md  # If updated

# Commit with descriptive message
git commit -m "Add Docker tutorial to guides section"

# Push to dev branch (triggers deployment!)
git push origin dev
```

**Good commit messages:**
- ✅ "Add Kubernetes deployment guide"
- ✅ "Update API reference with new endpoints"
- ✅ "Fix broken links in services section"
- ✅ "Reorganize guides folder structure"

**Bad commit messages:**
- ❌ "Update"
- ❌ "Changes"
- ❌ "Fix stuff"

---

## 🚀 Automatic Deployment Process

### What Happens After You Push

```
1. Push to dev branch
   ↓
2. GitHub Actions triggers
   ↓
3. Checkout code
   ↓
4. Setup Python 3.11
   ↓
5. Install dependencies
   ↓
6. Run: mkdocs build --strict
   ↓
7. Deploy to GitHub Pages
   ↓
8. Site live in ~2-3 minutes!
```

### Monitoring Deployment

**1. Go to Actions tab:**
```
https://github.com/itmc-cloud/itmc-knowledge-base/actions
```

**2. Find your workflow run:**
- Look for "Deploy MkDocs to GitHub Pages"
- Shows your commit message
- Status: 🟡 In progress / ✅ Success / ❌ Failed

**3. Click to see details:**
- View each step's progress
- See build logs
- Check for errors

**4. Wait for completion:**
- Build: ~30-45 seconds
- Deploy: ~30-45 seconds
- **Total: ~2-3 minutes**

**5. Verify on live site:**
```
https://itmc-cloud.github.io/itmc-knowledge-base
```

Hard refresh browser: `Ctrl+F5` (Windows) or `Cmd+Shift+R` (Mac)

---

## 🛑 If Deployment Fails

### Step 1: Check the Error

1. Go to **Actions** tab
2. Click the **failed workflow**
3. Click on the **failed job**
4. Read the **error message**

### Step 2: Common Failures & Fixes

| Error Message | Cause | Solution |
|--------------|-------|----------|
| `mkdocs build --strict` failed | Build errors (broken links, missing files) | Run `mkdocs build --strict` locally and fix errors |
| `could not determine a constructor for the tag` | Invalid YAML in `mkdocs.yml` | Check YAML syntax, especially special characters |
| `No such file or directory` | Referenced file doesn't exist | Verify file path is correct and file is committed |
| `Failed to create deployment (status: 404)` | GitHub Pages not enabled | Enable GitHub Pages in repository settings |
| Module not found | Missing dependency | Add to `requirements.txt` and push again |

### Step 3: Fix and Retry

```bash
# 1. Fix the issue locally
# Edit the problematic files

# 2. Test the fix
mkdocs build --clean --strict

# 3. Commit and push fix
git add .
git commit -m "Fix: [describe what you fixed]"
git push origin dev
```

---

## 🔧 GitHub Pages Configuration

### Required Settings

**Go to:** https://github.com/itmc-cloud/itmc-knowledge-base/settings/pages

**Configuration:**
- **Source:** GitHub Actions (NOT "Deploy from a branch")
- **Custom domain:** (leave empty unless you have one)

**If you see 404 errors on deployment:**
1. Verify Source is set to "GitHub Actions"
2. Re-run the workflow after changing settings
3. Wait 2-3 minutes for propagation

---

## 📋 Quick Deployment Commands

**Copy and paste these commands for each deployment:**

```bash
# ============================================
# QUICK DEPLOYMENT CHECKLIST
# ============================================

# 1. Update navigation (if you added/removed files)
python update_nav.py

# 2. Test locally
mkdocs serve
# → Check http://127.0.0.1:8000/itmc-knowledge-base/
# → Press Ctrl+C when done

# 3. Build and validate (MUST PASS!)
mkdocs build --clean --strict

# 4. Review and commit
git status
git add docs/ mkdocs.yml
git commit -m "Your descriptive message"

# 5. Push to dev branch
git push origin dev

# 6. Monitor deployment
# → https://github.com/itmc-cloud/itmc-knowledge-base/actions
# → Wait ~2-3 minutes
# → Check https://itmc-cloud.github.io/itmc-knowledge-base
```

---

## 🔄 Deployment Workflow Details

### GitHub Actions Configuration

**File:** `.github/workflows/deploy.yml`

**Triggers on:**
- Push to `dev` branch
- Pull request to `dev` branch (build only, no deploy)
- Manual trigger (workflow_dispatch)

**Jobs:**

1. **Build Job:**
   - Checkout code
   - Setup Python 3.11
   - Cache pip dependencies
   - Install from `requirements.txt`
   - Run `mkdocs build --strict`
   - Upload artifact to GitHub

2. **Deploy Job** (only on push to dev):
   - Download artifact from build
   - Deploy to GitHub Pages
   - Update live site

### Build Timing Breakdown

| Step | Time | Cumulative |
|------|------|------------|
| Checkout repository | 5-10s | 10s |
| Setup Python + cache | 15-20s | 30s |
| Install dependencies | 20-30s | 60s |
| Build documentation | 3-5s | 65s |
| Upload artifact | 10-15s | 80s |
| Deploy to Pages | 30-45s | 125s |

**Total:** ~2-3 minutes from push to live

---

## 🧪 Manual Deployment (Alternative)

If automatic deployment isn't working, you can deploy manually:

```bash
# 1. Build the site
mkdocs build --clean

# 2. Deploy using gh-deploy command
mkdocs gh-deploy --force

# This will:
# - Build the site
# - Push to gh-pages branch
# - Update GitHub Pages
```

**Note:** Automatic deployment via GitHub Actions is preferred. Use manual deployment only for emergencies.

---

## 💡 Deployment Tips

### 1. Always Test Before Pushing

**Never push untested code:**
- Test locally with `mkdocs serve`
- Build with `mkdocs build --strict`
- Fix ALL errors before pushing

### 2. Push Small, Focused Changes

**Good practice:**
- One feature or fix per commit
- Clear commit messages
- Easy to review and rollback

**Bad practice:**
- Multiple unrelated changes
- Large commits with many files
- Vague commit messages

### 3. Check Deployment Status

**Don't assume it worked:**
- Always check GitHub Actions
- Verify on live site
- Test key pages after deployment

### 4. Fix Failures Quickly

**If deployment fails:**
- Fix immediately
- Don't push more changes on top
- Test fix thoroughly before pushing

### 5. Keep Documentation Current

**When you deploy:**
- Update CHANGELOG if you have one
- Update version numbers if applicable
- Document breaking changes

---

## 🆘 Getting Help

**If you're stuck:**

1. **Check this guide again** - Most issues are covered here
2. **Read the error message** - It usually tells you what's wrong
3. **Check GitHub Actions logs** - Detailed error information
4. **Test locally** - Reproduce the issue on your machine
5. **Ask the team** - Someone may have seen this before

**Useful resources:**
- [MkDocs Documentation](https://www.mkdocs.org/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [GitHub Pages Docs](https://docs.github.com/en/pages)

---

## 📚 Related Documentation

- **[SETUP.md](SETUP.md)** - Initial environment setup
- **[DEVELOPMENT.md](DEVELOPMENT.md)** - Daily development workflow
- **[PROJECT.md](PROJECT.md)** - Complete project documentation

---

**Ready to deploy? Follow the checklist above! 🚀**
