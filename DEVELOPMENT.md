# Development Guide

> **For:** Daily development workflow - running the server, adding content, testing changes

## 🖥️ Starting the Development Server

### Quick Start (Virtual Environment Already Activated)

If you see `(.venv)` in your terminal prompt:

```bash
# Local access only
mkdocs serve

# Network access (for containers/remote access)
mkdocs serve --dev-addr 0.0.0.0:8000
```

### Full Start (Starting Fresh)

```bash
# 1. Navigate to project folder
cd itmc-knowledge-base

# 2. Activate virtual environment
.venv\Scripts\Activate.ps1   # Windows PowerShell
source .venv/bin/activate     # Linux/Mac

# 3. Start server
mkdocs serve
```

### Alternative: Without Activating Virtual Environment

```bash
# Windows
.venv\Scripts\python.exe -m mkdocs serve

# Linux/Mac
.venv/bin/python -m mkdocs serve
```

---

## 🌐 Access Your Site

Once the server is running:

- **Local:** http://127.0.0.1:8000/itmc-knowledge-base/
- **Network:** http://YOUR-IP:8000/itmc-knowledge-base/ (if using `0.0.0.0:8000`)

**Server features:**
- ✅ Auto-reload on file changes
- ✅ Browser refreshes automatically
- ✅ Shows build errors in terminal
- ✅ Fast incremental builds

**To stop the server:** Press `Ctrl+C`

---

## ✍️ Adding New Content

### Creating a New Page

**Step 1: Create the Markdown file**

```bash
# Example: Add a new tutorial
echo "# Docker Tutorial" > docs/tutorials/docker.md

# Or create with your editor
# File: docs/tutorials/docker.md
```

**Step 2: Write your content**

```markdown
# Docker Tutorial

## Introduction

Learn how to containerize your application with Docker.

## Prerequisites

- Docker installed
- Basic command line knowledge

## Steps

### 1. Create Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### 2. Build the image

```bash
docker build -t myapp:latest .
```

## Next Steps

Check out our [Kubernetes guide](kubernetes.md) for orchestration.
```

**Step 3: Update navigation**

```bash
# Run the auto-update script
python update_nav.py

# OR without venv
.venv\Scripts\python.exe update_nav.py
```

**Step 4: Check your page**

- The dev server auto-reloads
- Navigate to your new page
- Verify content renders correctly

---

### Creating a New Section

To add a completely new section:

```bash
# 1. Create new folder in docs/
mkdir docs/tutorials

# 2. Create index page (becomes "Overview")
echo "# Tutorials Overview" > docs/tutorials/index.md

# 3. Add pages
echo "# Docker Tutorial" > docs/tutorials/docker.md
echo "# Kubernetes Guide" > docs/tutorials/kubernetes.md

# 4. Update navigation
python update_nav.py
```

**Result in navigation:**
```
- Tutorials
  - Overview
  - Docker Tutorial
  - Kubernetes Guide
```

---

## 🎨 Markdown Features & Syntax

### Basic Formatting

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*
`Inline code`

[Link text](https://example.com)
[Internal link](other-page.md)
```

### Code Blocks

````markdown
```python
def hello():
    print("Hello, World!")
```

```javascript
const greeting = () => {
  console.log('Hello, World!');
};
```
````

### Admonitions (Callouts)

```markdown
!!! note
    This is a note.

!!! warning
    This is a warning!

!!! tip "Custom Title"
    This is a helpful tip with custom title.

!!! danger
    Critical information!
```

### Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| More     | Data     | Here     |
```

### Task Lists

```markdown
- [x] Completed task
- [ ] Pending task
- [ ] Another pending task
```

### Tabs

```markdown
=== "Python"
    ```python
    print("Hello")
    ```

=== "JavaScript"
    ```javascript
    console.log("Hello");
    ```

=== "Java"
    ```java
    System.out.println("Hello");
    ```
```

---

## 🔄 Navigation Auto-Update

### When to Run `update_nav.py`

**Run the script when you:**
- ✅ Add new `.md` files
- ✅ Create new folders in `docs/`
- ✅ Rename or move files
- ✅ Delete files or folders

**Skip the script when you:**
- ❌ Only edit existing file content
- ❌ Change text/code in files
- ❌ Fix typos

### How File Names Become Titles

| Filename | Navigation Title |
|----------|-----------------|
| `getting-started.md` | Getting Started |
| `api-reference.md` | Api Reference |
| `cloud-solutions.md` | Cloud Solutions |
| `index.md` | Overview (in folders) or Home (at root) |

### Manual Navigation (Advanced)

If you need precise control, edit `mkdocs.yml` directly:

```yaml
nav:
  - Home: index.md
  - Guides:
      - Getting Started: guides/getting-started.md
      - Advanced: guides/advanced.md
  - API:
      - Overview: api/index.md
      - Reference: api/reference.md
```

---

## 🧪 Testing Your Changes

### Visual Testing Checklist

Open http://127.0.0.1:8000/itmc-knowledge-base/ and check:

- [ ] All pages load without 404 errors
- [ ] Navigation menu shows correctly
- [ ] Internal links work
- [ ] Code blocks render with syntax highlighting
- [ ] Tables display properly
- [ ] Images load (if any)
- [ ] Admonitions render correctly
- [ ] Mobile view looks good (resize browser)

### Check for Warnings

Watch the terminal for warnings:

```bash
INFO    -  Building documentation...
INFO    -  Doc file 'guide.md' contains a link 'other.md#section', 
           but the doc 'other.md' does not contain an anchor '#section'.
```

**Fix broken links before committing!**

---

## 📂 Working with Assets

### Adding Images

```bash
# 1. Create assets folder if it doesn't exist
mkdir -p docs/assets/images

# 2. Add your image
# Copy image file to docs/assets/images/

# 3. Reference in markdown
```

```markdown
![Alt text](assets/images/diagram.png)

Or with title:
![Architecture Diagram](assets/images/arch.png "System Architecture")
```

### Adding Custom CSS/JavaScript

**Custom CSS:**

1. Create `docs/stylesheets/extra.css`
2. Add to `mkdocs.yml`:
```yaml
extra_css:
  - stylesheets/extra.css
```

---

## 🐛 Common Development Issues

### Server Won't Start

**Error:** `mkdocs: command not found`

**Fix:**
```bash
# Activate virtual environment first
.venv\Scripts\Activate.ps1

# Or use full path
.venv\Scripts\python.exe -m mkdocs serve
```

### Port Already in Use

**Error:** `OSError: Address already in use`

**Fix:**
```bash
# Use different port
mkdocs serve --dev-addr 127.0.0.1:8001
```

### Changes Not Showing

**Solutions:**
1. Hard refresh browser: `Ctrl+F5` (Windows) or `Cmd+Shift+R` (Mac)
2. Check terminal for build errors
3. Restart MkDocs server
4. Clear browser cache

### Broken Links Warning

**Warning:** `Doc file contains a link..., but the doc does not contain an anchor`

**Fix:**
1. Check the target file exists
2. Verify section heading exists (e.g., `## Section Name`)
3. Fix the link or add the missing section

---

## 🔧 Build Commands Reference

```bash
# Start development server
mkdocs serve

# Build static site (for testing)
mkdocs build

# Build with clean (removes old files)
mkdocs build --clean

# Build with strict validation (treats warnings as errors)
mkdocs build --strict

# Get help
mkdocs --help
```

---

## 💡 Development Tips

### 1. Keep the Dev Server Running

Leave `mkdocs serve` running while you work:
- See changes instantly
- Catch errors immediately
- Test as you write

### 2. Use Split Screen

- **Left:** Your code editor
- **Right:** Browser with live preview
- Edit → Save → See changes immediately

### 3. Write Content First, Format Later

- Focus on writing content in Markdown
- Add fancy formatting after content is complete
- Use basic formatting while drafting

### 4. Test Links as You Add Them

- Click every link you add
- Verify internal links work
- Check external links open correctly

### 5. Preview on Mobile

- Resize browser to mobile size
- Or use browser dev tools (F12 → Toggle device toolbar)
- Material theme is responsive but always verify

---

## 📚 What's Next?

Once your changes look good:

→ **Ready to deploy?** See [DEPLOYMENT.md](DEPLOYMENT.md)

→ **Need setup help?** See [SETUP.md](SETUP.md)

→ **General info?** See [PROJECT.md](PROJECT.md)

---

**Happy documenting! 📝**
