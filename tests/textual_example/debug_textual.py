#!/usr/bin/env python3
"""
Utility script to help debug Textual-related issues.
"""
import sys
import importlib

def check_textual_installation():
    """Check if Textual is installed and print version information."""
    try:
        import textual
        print(f"Textual is installed. Version: {textual.__version__}")
        
        # Check key modules
        modules = [
            "textual.app", "textual.binding", "textual.containers",
            "textual.css", "textual.screen", "textual.widgets"
        ]
        
        for module_name in modules:
            try:
                module = importlib.import_module(module_name)
                print(f"✓ Module {module_name} is available")
            except ImportError as e:
                print(f"✗ Module {module_name} failed to import: {e}")
    
    except ImportError:
        print("❌ Textual is not installed.")
        return False
    
    return True

def check_widgets():
    """Check if essential widgets are available."""
    try:
        from textual.widgets import (
            Static, Button, Label, Checkbox, Input, TextArea,
            LoadingIndicator, ProgressBar, DataTable
        )
        
        print("\nChecking essential widgets:")
        widgets = [Static, Button, Label, Checkbox, Input, TextArea,
                  LoadingIndicator, ProgressBar, DataTable]
        
        for widget in widgets:
            print(f"✓ {widget.__name__} is available")
            
        # Check ProgressBar API
        print("\nChecking ProgressBar API:")
        try:
            progress = ProgressBar()
            print("- ProgressBar instantiation: OK")
            
            # Try accessing .progress property
            try:
                progress.progress = 50
                print("- Setting .progress property: OK")
            except AttributeError:
                print("- Setting .progress property: FAILED")
                
            # Try accessing .update() method  
            if hasattr(progress, "update"):
                print("- Has .update() method: YES")
            else:
                print("- Has .update() method: NO")
                
        except Exception as e:
            print(f"- ProgressBar instantiation failed: {e}")
    
    except ImportError as e:
        print(f"Failed to import widgets: {e}")

def check_css():
    """Check CSS capabilities."""
    try:
        from textual.css.stylesheet import Stylesheet
        print("\nCSS capabilities:")
        print(f"✓ Stylesheet class is available")
        
        # Check if most common properties are supported in your Textual version
        try:
            from textual.css.styles import Styles
            style_obj = Styles()
            print("Available style properties:")
            for prop in dir(style_obj):
                if not prop.startswith('_'):
                    print(f"- {prop}")
        except ImportError:
            print("Could not list available style properties")
    
    except ImportError as e:
        print(f"Failed to import CSS modules: {e}")

if __name__ == "__main__":
    print("==== Textual Debug Information ====\n")
    
    if check_textual_installation():
        check_widgets()
        check_css()
        
        print("\nPython version:", sys.version)
        print("\nTo run the example, use:")
        print("python3 textual_example.py")
    else:
        print("\nPlease install Textual first with:")
        print("pip install textual")
