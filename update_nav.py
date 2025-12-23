#!/usr/bin/env python3
"""
Auto-update MkDocs navigation structure based on docs/ folder contents.
Run this script whenever you add/remove files or folders in docs/.
"""

import os
import yaml
from pathlib import Path


def scan_docs_folder(docs_path='docs'):
    """
    Recursively scan docs folder and build navigation structure.
    Returns a nested dictionary representing the folder structure.
    """
    nav_structure = []
    docs_dir = Path(docs_path)
    
    # Handle root-level files first
    root_files = sorted([f for f in docs_dir.glob('*.md') if f.is_file()])
    
    # Add Home (index.md) first if it exists
    if (docs_dir / 'index.md').exists():
        nav_structure.append({'Home': 'index.md'})
    
    # Add other root-level files (excluding index.md)
    for file in root_files:
        if file.name != 'index.md':
            title = format_title(file.stem)
            nav_structure.append({title: file.name})
    
    # Process subdirectories
    subdirs = sorted([d for d in docs_dir.iterdir() if d.is_dir()])
    
    for subdir in subdirs:
        section = process_directory(subdir, docs_path)
        if section:
            nav_structure.append(section)
    
    return nav_structure


def process_directory(directory, base_path='docs'):
    """
    Process a directory and return its navigation structure.
    """
    dir_path = Path(directory)
    relative_path = dir_path.relative_to(base_path)
    section_name = format_title(dir_path.name)
    
    # Get all markdown files in this directory
    md_files = sorted([f for f in dir_path.glob('*.md') if f.is_file()])
    
    # Get all subdirectories
    subdirs = sorted([d for d in dir_path.iterdir() if d.is_dir()])
    
    # If directory is empty, skip it
    if not md_files and not subdirs:
        return None
    
    section_content = []
    
    # Add index.md as "Overview" if it exists
    if (dir_path / 'index.md').exists():
        section_content.append({
            'Overview': str(relative_path / 'index.md').replace('\\', '/')
        })
    
    # Add other files in this directory
    for file in md_files:
        if file.name != 'index.md':
            title = format_title(file.stem)
            file_path = str(relative_path / file.name).replace('\\', '/')
            section_content.append({title: file_path})
    
    # Process subdirectories recursively
    for subdir in subdirs:
        subsection = process_directory(subdir, base_path)
        if subsection:
            section_content.append(subsection)
    
    return {section_name: section_content}


def format_title(filename):
    """
    Convert filename to readable title.
    Examples:
        'getting-started' -> 'Getting Started'
        'cloud-solutions' -> 'Cloud Solutions'
        'boarding' -> 'Boarding'
    """
    # Replace hyphens and underscores with spaces
    title = filename.replace('-', ' ').replace('_', ' ')
    # Capitalize each word
    title = ' '.join(word.capitalize() for word in title.split())
    return title


def update_mkdocs_yaml(nav_structure, yaml_path='mkdocs.yml'):
    """
    Update the mkdocs.yml file with the new navigation structure.
    Preserves all other configuration while updating only the 'nav' section.
    """
    # Read existing mkdocs.yml as text
    with open(yaml_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find the FIRST nav section and the LAST occurrence
    nav_start = None
    nav_end = None
    found_nav = False
    
    for i, line in enumerate(lines):
        if line.strip() == 'nav:':
            if nav_start is None:
                # First occurrence - this is where we start
                nav_start = i
                found_nav = True
            # Continue searching to find where ALL nav content ends
        elif found_nav and line and not line[0].isspace() and line.strip() and not line.strip().startswith('-'):
            # Found a non-indented, non-empty line that's not a list item - this is the end
            nav_end = i
            break
    
    # If no end found, nav goes to end of file
    if nav_start is not None and nav_end is None:
        nav_end = len(lines)
    
    if nav_start is None:
        print("⚠️  Warning: 'nav:' section not found in mkdocs.yml")
        return
    
    # Generate new nav section as YAML text
    nav_yaml = yaml.dump({'nav': nav_structure}, default_flow_style=False, sort_keys=False, allow_unicode=True)
    nav_lines = nav_yaml.splitlines(keepends=True)
    
    # Ensure proper spacing: add blank line if next section doesn't start with one
    if nav_end < len(lines) and lines[nav_end].strip():
        nav_lines.append('\n')
    
    # Replace old nav section with new one
    new_lines = lines[:nav_start] + nav_lines + lines[nav_end:]
    
    # Write back to file
    with open(yaml_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"✅ Updated {yaml_path} with new navigation structure!")
    print(f"📄 Found {count_pages(nav_structure)} pages")


def count_pages(nav_structure):
    """Count total number of pages in navigation."""
    count = 0
    for item in nav_structure:
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str):
                    count += 1
                elif isinstance(value, list):
                    count += count_pages(value)
    return count


def print_nav_preview(nav_structure, indent=0):
    """Print a preview of the navigation structure."""
    for item in nav_structure:
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str):
                    print('  ' * indent + f'- {key}: {value}')
                elif isinstance(value, list):
                    print('  ' * indent + f'- {key}:')
                    print_nav_preview(value, indent + 1)


if __name__ == '__main__':
    print("🔍 Scanning docs/ folder...")
    
    # Scan docs folder
    nav_structure = scan_docs_folder()
    
    # Preview the structure
    print("\n📋 Navigation structure:")
    print_nav_preview(nav_structure)
    
    # Update mkdocs.yml
    print("\n🔄 Updating mkdocs.yml...")
    update_mkdocs_yaml(nav_structure)
    
    print("\n✨ Done! MkDocs will auto-reload if server is running.")
