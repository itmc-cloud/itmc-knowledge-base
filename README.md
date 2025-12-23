# ITMC Knowledge Base

![Build Status](https://github.com/itmc-cloud/itmc-knowledge-base/workflows/Deploy%20MkDocs%20to%20GitHub%20Pages/badge.svg)
![License](https://img.shields.io/github/license/itmc-cloud/itmc-knowledge-base)

> Comprehensive knowledge base for ITMC Cloud - Services, Guides & Code Snippets

## 📚 About

This is the official knowledge base for ITMC Cloud, containing documentation, code snippets, and guides for cloud solutions and software development services.

**Live Documentation**: [https://itmc-cloud.github.io/itmc-knowledge-base](https://itmc-cloud.github.io/itmc-knowledge-base)

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/itmc-cloud/itmc-knowledge-base.git
   cd itmc-knowledge-base
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server**
   ```bash
   mkdocs serve
   ```

4. **Open your browser**
   Navigate to [http://localhost:8000](http://localhost:8000)

The site will automatically reload when you make changes to the documentation.

## 📖 Documentation Structure

```
docs/
├── index.md                    # Homepage
├── about.md                    # About ITMC Cloud
├── services/
│   ├── index.md               # Services overview
│   ├── cloud-solutions.md     # Cloud services
│   └── development.md         # Development services
├── guides/
│   └── getting-started.md     # Getting started guide
└── snippets/
    ├── index.md               # Snippets overview
    ├── python.md              # Python code examples
    ├── javascript.md          # JavaScript/TypeScript examples
    └── devops.md              # DevOps configurations
```

## 🛠️ Building the Site

To build the static site:

```bash
mkdocs build
```

The built site will be in the `site/` directory.

## 🚢 Deployment

This site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch. The deployment is handled by GitHub Actions.

### Manual Deployment

```bash
mkdocs gh-deploy
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test locally**
   ```bash
   mkdocs serve
   ```
5. **Commit your changes**
   ```bash
   git commit -m "Add: your feature description"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request**

### Contribution Guidelines

- Use clear, concise language
- Include code examples where appropriate
- Follow the existing documentation structure
- Test all code snippets before submitting
- Add relevant tags and categories

## 📝 Adding Content

### Creating a New Page

1. Create a new `.md` file in the appropriate directory under `docs/`
2. Add front matter if needed
3. Write your content using Markdown
4. Update `mkdocs.yml` to include your page in the navigation

### Adding Code Snippets

Code snippets should include:
- Clear description
- Language-specific syntax highlighting
- Comments explaining key parts
- Usage examples

Example:
````markdown
### Example Snippet

```python
def example_function():
    """This is an example function"""
    return "Hello, World!"
```
````

## 🎨 Features

- **Material Theme**: Modern, responsive design
- **Dark Mode**: Automatic theme switching
- **Search**: Full-text search across all documentation
- **Code Highlighting**: Syntax highlighting for multiple languages
- **Mermaid Diagrams**: Support for flowcharts and diagrams
- **Responsive**: Works on desktop, tablet, and mobile

## 📋 Requirements

See [requirements.txt](requirements.txt) for Python dependencies.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Documentation**: [https://itmc-cloud.github.io/itmc-knowledge-base](https://itmc-cloud.github.io/itmc-knowledge-base)
- **GitHub**: [https://github.com/itmc-cloud/itmc-knowledge-base](https://github.com/itmc-cloud/itmc-knowledge-base)
- **Issues**: [https://github.com/itmc-cloud/itmc-knowledge-base/issues](https://github.com/itmc-cloud/itmc-knowledge-base/issues)
- **MkDocs**: [https://www.mkdocs.org](https://www.mkdocs.org)
- **Material for MkDocs**: [https://squidfunk.github.io/mkdocs-material](https://squidfunk.github.io/mkdocs-material)

## 📞 Contact

For questions or support, please:
- Open an issue on GitHub
- Contact us at contact@itmc-cloud.com

---

**Made with ❤️ by ITMC Cloud Team**
