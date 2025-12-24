# Deployment Guide

> **For:** Committing changes and deploying to GitHub Pages

## 🚨 Important

**Deployment Branch:** All changes must be pushed to the **`dev`** branch to trigger automatic deployment.

**Deployment URL:** https://itmc-cloud.github.io/itmc-knowledge-base

---

## 📖 Table of Contents

1. [Pre-Deployment Checklist](#-pre-deployment-checklist)
2. [Step-by-Step Deployment Process](#-step-by-step-deployment-process)
3. [Branch Workflow & Pull Requests](#-branch-workflow--pull-requests)
4. [Automatic Deployment Process](#-automatic-deployment-process)
5. [Monitoring Deployment](#monitoring-deployment)
6. [Troubleshooting Cache Issues](#-troubleshooting-cache-issues)
7. [If Deployment Fails](#-if-deployment-fails)

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

## � Step-by-Step Deployment Process

### Direct Push to Dev (Simple Changes)

**Use this workflow for quick, simple changes:**

```bash
# Step 1: Make sure you're on dev branch
git checkout dev
git pull origin dev

# Step 2: Make your changes
# Edit files in docs/ folder

# Step 3: Test locally
mkdocs serve

# Step 4: Validate build
mkdocs build --clean --strict

# Step 5: Commit and push
git add docs/
git commit -m "docs: update getting started guide"
git push origin dev

# Step 6: Monitor deployment
# Go to: https://github.com/itmc-cloud/itmc-knowledge-base/actions
# Wait for build AND deploy jobs to complete (2-3 minutes)

# Step 7: Verify changes
# Open: https://itmc-cloud.github.io/itmc-knowledge-base/
# Clear cache: Ctrl+Shift+Delete
# Hard refresh: Ctrl+F5
```

**Timeline:**
- 0:00 - Push to dev
- 0:10 - GitHub Actions starts
- 0:45 - Build job completes
- 1:30 - Deploy job completes
- 2:00 - Site is live with changes
- 2:00+ - Clear cache and verify

---

## 🔀 Branch Workflow & Pull Requests

### When to Use Feature Branches

**Use feature branches for:**
- Complex changes that need review
- Working on issues
- Experimenting with new features
- Multiple people working on different features
- Changes that might break things

**Don't use feature branches for:**
- Typo fixes
- Minor documentation updates
- Single-line changes

### Feature Branch Workflow (Step-by-Step)

#### Step 1: Create Feature Branch

```bash
# Make sure dev is up to date
git checkout dev
git pull origin dev

# Create and switch to feature branch
git checkout -b feature/add-docker-guide

# Or if working on an issue:
git checkout -b fix/issue-123-broken-links
```

#### Step 2: Make Your Changes

```bash
# Edit files
# Add new pages to docs/

# Test locally
mkdocs serve

# Validate build
mkdocs build --clean --strict
```

#### Step 3: Commit to Feature Branch

```bash
# Stage your changes
git add docs/guides/docker-guide.md
git add mkdocs.yml  # If navigation changed

# Commit with clear message
git commit -m "feat: add comprehensive Docker deployment guide"

# Push feature branch to GitHub
git push origin feature/add-docker-guide
```

**⚠️ IMPORTANT:** Pushing to a feature branch does **NOT** trigger deployment!
- Only pushes to `dev` branch trigger deployment
- Feature branches are for development only

#### Step 4: Create Pull Request

**On GitHub:**

1. Go to: https://github.com/itmc-cloud/itmc-knowledge-base
2. You'll see "Compare & pull request" button
3. Click it
4. Fill in PR details:
   - **Base branch:** `dev` (must target dev!)
   - **Compare branch:** `feature/add-docker-guide`
   - **Title:** Clear description
   - **Description:** Explain what changed and why

**Pull Request Template:**
```markdown
## Changes
- Added Docker deployment guide
- Updated navigation
- Added code examples

## Testing
- [x] Tested locally with mkdocs serve
- [x] Build passes with mkdocs build --strict
- [x] All links work
- [x] Code examples tested

## Screenshots (if UI changes)
[Add screenshots if needed]
```

#### Step 5: Review Process

**What happens during PR:**
- ✅ GitHub Actions runs **build job only** (no deployment)
- ✅ Other team members can review
- ✅ You can make additional commits if requested
- ❌ Changes are **NOT deployed yet**

**To add more changes to PR:**
```bash
# Still on feature branch
git add docs/guides/docker-guide.md
git commit -m "fix: address review comments"
git push origin feature/add-docker-guide

# Changes automatically appear in PR
```

#### Step 6: Merge Pull Request

**When PR is approved:**

1. Click "Merge pull request" on GitHub
2. Choose merge method:
   - **"Squash and merge"** (recommended) - Combines all commits into one
   - **"Merge commit"** - Keeps all commits
   - **"Rebase and merge"** - Rebases commits
3. Click "Confirm merge"
4. Delete feature branch (optional but recommended)

**⚠️ DEPLOYMENT TRIGGERS NOW!**
- Merging to `dev` triggers automatic deployment
- GitHub Actions runs build + deploy jobs
- Site updates in 2-3 minutes

#### Step 7: Monitor Merge Deployment

```bash
# Pull latest dev branch locally
git checkout dev
git pull origin dev

# Monitor deployment
# Go to: https://github.com/itmc-cloud/itmc-knowledge-base/actions
# Look for workflow run with your merge commit message

# Verify both jobs complete:
# - ✅ build
# - ✅ deploy

# Check live site (clear cache first!)
```

#### Step 8: Clean Up Local Branches

```bash
# After successful merge, delete feature branch
git branch -d feature/add-docker-guide

# If you want to delete remote branch too
git push origin --delete feature/add-docker-guide
```

### Branch Workflow Summary

**Timeline Example:**

```
Day 1, 10:00 AM - Create feature branch
Day 1, 10:30 AM - Make changes
Day 1, 11:00 AM - Push to feature branch (NO deployment)
Day 1, 11:05 AM - Create Pull Request
Day 1, 02:00 PM - Team reviews
Day 1, 03:00 PM - Address review comments
Day 1, 04:00 PM - Merge to dev (DEPLOYMENT TRIGGERS!)
Day 1, 04:03 PM - Site is live with changes
```

### Common Branch Scenarios

#### Scenario 1: Simple Documentation Update
```bash
# Direct push to dev (no PR needed)
git checkout dev
git add docs/about.md
git commit -m "docs: update company description"
git push origin dev
# ✅ Deploys immediately
```

#### Scenario 2: New Feature with Review
```bash
# Use feature branch + PR
git checkout -b feature/new-section
# Make changes
git push origin feature/new-section
# Create PR → Review → Merge to dev
# ✅ Deploys after merge
```

#### Scenario 3: Fixing an Issue
```bash
# Use issue branch
git checkout -b fix/issue-45-broken-link
# Fix the issue
git push origin fix/issue-45-broken-link
# Create PR with "Fixes #45" in description
# Review → Merge to dev
# ✅ Deploys after merge + closes issue #45
```

### Key Points About Branches

**✅ Deployment ONLY happens when:**
- Code is pushed directly to `dev` branch
- A PR is merged into `dev` branch
- Manual workflow dispatch is triggered on `dev` branch

**❌ Deployment DOES NOT happen when:**
- You push to a feature branch
- You create a Pull Request (builds only, no deploy)
- You push to any branch other than `dev`

**🔄 Workflow file checks:**
```yaml
# From .github/workflows/deploy.yml
deploy:
  needs: build
  if: github.event_name == 'push' && github.ref == 'refs/heads/dev'
  # ☝️ This means deploy ONLY runs on push to dev
```

---

## �🚀 Automatic Deployment Process

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

**⚠️ CRITICAL: Verify BOTH jobs complete!**
- Click on your workflow run
- Check that **TWO jobs** are listed:
  - ✅ **build** - Builds the MkDocs site
  - ✅ **deploy** - Deploys to GitHub Pages
- **Both must show success** for changes to be live
- If only "build" shows, the site won't update!

**3. Click to see details:**
- View each step's progress
- See build logs
- Check for errors

**4. Wait for completion:**
- Build: ~30-45 seconds
- Deploy: ~30-45 seconds
- **Total: ~2-3 minutes**
- **⚠️ Wait for deploy job to complete before viewing site!**

**5. Verify on live site:**
```
https://itmc-cloud.github.io/itmc-knowledge-base
```

**🔑 IMPORTANT - Clear Browser Cache FIRST:**

**Method 1: Clear Cache (Recommended):**
1. Press `Ctrl + Shift + Delete` (Windows) or `Cmd + Shift + Delete` (Mac)
2. Select "Cached images and files"
3. Click "Clear data"
4. Refresh page with `Ctrl + F5`

**Method 2: Use Incognito/Private Window:**
- Chrome/Edge: `Ctrl + Shift + N`
- Firefox: `Ctrl + Shift + P`
- This bypasses all cache

**Method 3: Hard Refresh:**
- Windows: `Ctrl + F5` or `Ctrl + Shift + R`
- Mac: `Cmd + Shift + R`

**⚠️ If changes don't appear after clearing cache:**
See "Troubleshooting Cache Issues" section below.

---

## � Troubleshooting Cache Issues

### Problem: Site Still Shows Old Content

Even after successful deployment, you might see old content due to aggressive caching.

**Symptoms:**
- GitHub Actions shows ✅ success for both build and deploy
- Local build is correct (`mkdocs build`)
- Live site shows outdated content

**Solution 1: Force Fresh Deployment**

```bash
# This triggers a completely new deployment cycle
git commit --allow-empty -m "trigger: force fresh deployment"
git push origin dev

# Then wait 2-3 minutes and clear browser cache
```

**Solution 2: Clear All Cache Levels**

```bash
# 1. Clear browser cache (see steps above)
# 2. Try multiple browsers
# 3. Use incognito mode
# 4. Wait 5-10 minutes for CDN propagation
```

**Solution 3: Verify GitHub Pages Settings**

Go to: https://github.com/itmc-cloud/itmc-knowledge-base/settings/pages

Confirm:
- **Source:** Must be set to "GitHub Actions" (NOT "Deploy from a branch")
- If it's set to branch deployment, change it to "GitHub Actions"

### Best Practices to Avoid Cache Issues

**✅ DO:**
1. Always wait for BOTH build AND deploy jobs to complete
2. Clear browser cache before viewing changes
3. Use incognito mode for immediate verification
4. Allow 2-3 minutes for full propagation
5. Check GitHub Actions deploy job status

**❌ DON'T:**
1. View site immediately after pushing (wait for deploy!)
2. Assume build success = deployment success (check deploy job!)
3. Skip cache clearing steps
4. Panic if changes don't appear instantly

---

## �🛑 If Deployment Fails

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
