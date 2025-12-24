# ITMC Knowledge Base

![Build Status](https://github.com/itmc-cloud/itmc-knowledge-base/workflows/Deploy%20MkDocs%20to%20GitHub%20Pages/badge.svg)
![License](https://img.shields.io/github/license/itmc-cloud/itmc-knowledge-base)

> Comprehensive knowledge base for ITMC Cloud - Services, Guides & Code Snippets

## 📚 About

This is the official knowledge base for ITMC Cloud, containing documentation, code snippets, and guides for cloud solutions and software development services. Built with **MkDocs** and **Material for MkDocs**, it automatically deploys to GitHub Pages when changes are pushed to the `dev` branch.

**🌐 Live Site:** [https://itmc-cloud.github.io/itmc-knowledge-base](https://itmc-cloud.github.io/itmc-knowledge-base)

---

## 📖 Documentation

This repository contains comprehensive documentation organized into specialized guides:

### 🚀 [SETUP.md](SETUP.md) - First Time Setup
**Start here if you're new or setting up on a new machine**
- Prerequisites and installation
- Clone repository and create virtual environment
- Install dependencies
- Troubleshooting setup issues

### 💻 [DEVELOPMENT.md](DEVELOPMENT.md) - Daily Development
**Use this for adding content and daily work**
- Running the development server
- Adding new pages and sections
- Markdown syntax and features
- Testing your changes
- Development tips and tricks

### 🚀 [DEPLOYMENT.md](DEPLOYMENT.md) - Deploy Changes
**Follow this before pushing to production**
- Pre-deployment checklist (5 steps)
- Commit and push workflow
- Monitoring GitHub Actions
- Troubleshooting deployment failures
- Quick command reference

### 📋 [PROJECT.md](PROJECT.md) - Complete Documentation Hub
**Main documentation index with all details**
- Project overview and structure
- Quick start guides
- Common tasks
- Links to all documentation

---

## ⚡ Quick Start

### For New Contributors

```bash
# 1. Clone the repository
git clone https://github.com/itmc-cloud/itmc-knowledge-base.git
cd itmc-knowledge-base

# 2. Setup virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
source .venv/bin/activate   # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start development server
mkdocs serve
```

**📚 Full details:** See [SETUP.md](SETUP.md)

### For Active Contributors

```bash
# Start server
mkdocs serve

# Add content, then update navigation
python update_nav.py

# Before deploying
mkdocs build --clean --strict
git add docs/ mkdocs.yml
git commit -m "Your message"
git push origin dev
```

**📚 Full details:** See [DEVELOPMENT.md](DEVELOPMENT.md) and [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 🎨 Features

- ✅ **Auto-reload**: Changes trigger automatic rebuild
- ✅ **Material Theme**: Modern, responsive design with dark mode
- ✅ **Auto-navigation**: Script automatically updates navigation menu
- ✅ **Auto-deployment**: Push to `dev` branch deploys to GitHub Pages
- ✅ **Search**: Full-text search across all documentation
- ✅ **Code Highlighting**: Syntax highlighting for multiple languages
- ✅ **Copy to Clipboard**: Easy code snippet copying
- ✅ **Responsive**: Works on desktop, tablet, and mobile

---

## 🏗️ Project Structure

```
itmc-knowledge-base/
├── docs/                    # Documentation content (Markdown files)
│   ├── index.md            # Homepage
│   ├── about.md            # About page
│   ├── guides/             # User guides
│   ├── services/           # Service documentation
│   └── snippets/           # Code snippets
├── .github/workflows/      # GitHub Actions
│   └── deploy.yml          # Auto-deployment configuration
├── site/                   # Generated static site (don't commit)
├── .venv/                  # Virtual environment (don't commit)
├── mkdocs.yml              # MkDocs configuration
├── requirements.txt        # Python dependencies
├── update_nav.py           # Navigation auto-update script
├── SETUP.md                # Setup guide
├── DEVELOPMENT.md          # Development guide
├── DEPLOYMENT.md           # Deployment guide
├── PROJECT.md              # Main documentation hub
└── README.md               # This file
```

---

## 🤝 Contributing

We welcome contributions! Here's the workflow:

1. **Read the documentation**: Start with [SETUP.md](SETUP.md)
2. **Make your changes**: Follow [DEVELOPMENT.md](DEVELOPMENT.md)
3. **Deploy safely**: Follow [DEPLOYMENT.md](DEPLOYMENT.md) checklist
4. **Submit Pull Request**: Target the `dev` branch

### Contribution Guidelines

- ✅ Use clear, concise language
- ✅ Include code examples where appropriate
- ✅ Test all code snippets before submitting
- ✅ Run `python update_nav.py` after adding files
- ✅ Run `mkdocs build --strict` before pushing
- ✅ Follow existing documentation structure
- ✅ Add descriptive commit messages

### Pull Request Process

```bash
# 1. Fork and clone
git clone https://github.com/YOUR-USERNAME/itmc-knowledge-base.git
cd itmc-knowledge-base

# 2. Create feature branch
git checkout -b feature/your-feature-name

# 3. Make changes and test
mkdocs serve

# 4. Update navigation if needed
python update_nav.py

# 5. Validate build
mkdocs build --clean --strict

# 6. Commit and push
git add .
git commit -m "feat: your feature description"
git push origin feature/your-feature-name

# 7. Open Pull Request to 'dev' branch
```

---

## 🚀 Deployment

**Automatic Deployment:**
- Push to `dev` branch → GitHub Actions → Live in ~2-3 minutes
- **URL:** https://itmc-cloud.github.io/itmc-knowledge-base

**Before Pushing:**
1. ✅ Run `python update_nav.py` (if you added files)
2. ✅ Test with `mkdocs serve`
3. ✅ Validate with `mkdocs build --clean --strict`
4. ✅ Commit and push to `dev` branch

**Full deployment guide:** [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 🛠️ Tools & Technologies

- **[MkDocs](https://www.mkdocs.org/)** - Static site generator
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** - Material Design theme
- **[PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)** - Markdown extensions
- **[GitHub Actions](https://github.com/features/actions)** - CI/CD automation
- **[GitHub Pages](https://pages.github.com/)** - Hosting

---

## 🆘 Need Help?

### Common Issues

| Issue | Solution |
|-------|----------|
| `mkdocs: command not found` | Activate virtual environment first |
| Build errors | Run `mkdocs build --strict` and fix reported errors |
| Port already in use | Use `mkdocs serve --dev-addr 127.0.0.1:8001` |
| Changes not showing | Hard refresh browser (Ctrl+F5) |
| Deployment failed | Check [DEPLOYMENT.md](DEPLOYMENT.md) troubleshooting section |

### Get Support

- 📖 **Read the docs**: [SETUP.md](SETUP.md), [DEVELOPMENT.md](DEVELOPMENT.md), [DEPLOYMENT.md](DEPLOYMENT.md)
- 🐛 **Open an issue**: [GitHub Issues](https://github.com/itmc-cloud/itmc-knowledge-base/issues)
- 💬 **Contact us**: contact@itmc-cloud.com
- 📋 **Check Actions**: [GitHub Actions](https://github.com/itmc-cloud/itmc-knowledge-base/actions)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Useful Links

- **Live Documentation**: https://itmc-cloud.github.io/itmc-knowledge-base
- **Repository**: https://github.com/itmc-cloud/itmc-knowledge-base
- **Issues**: https://github.com/itmc-cloud/itmc-knowledge-base/issues
- **GitHub Actions**: https://github.com/itmc-cloud/itmc-knowledge-base/actions
- **GitHub Pages Settings**: https://github.com/itmc-cloud/itmc-knowledge-base/settings/pages

---

**Made with ❤️ by ITMC Cloud Team**
