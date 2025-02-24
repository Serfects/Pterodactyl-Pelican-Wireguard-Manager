# GitHub Copilot Instructions for Logan's Project

---

## 1. General Information & Communication

- **User Identity:** My name is **Logan**. Please always address me as Logan.
- **Detailed Explanations:**  
  - Provide clear, detailed, and easy-to-understand explanations for every change.
  - When making multiple changes, break your explanations into bullet points or separate sections.
- **Chat-Only Requests:**  
  - If I request you to "show in chat" or "show before applying," **do not make any code changes**.
  - Only respond with the proposed modifications or suggestions in chat.

---

## 2. Project Scope & Language

- **Primary Language:**  
  - The project is written entirely in **Python**, with some occasional Bash scripts.
  - All generated code and suggestions should follow common Python best practices (PEP 8, clean code principles, etc.).
- **No Type Hints:**  
  - Under no circumstances should type hints be added or suggested. This project explicitly avoids type hinting.

---

## 3. Code Organization & Structure

- **Logical Grouping:**  
  - Organize code by grouping similar or related functionality together.
  - Place new code in the correct sections of the existing codebase.
- **Code Movement & Refactoring:**  
  - When moving code between modules or sections, **remove the old code** from its original location.
  - Automatically update, add, or remove import statements in both the source and destination files.
  - Ensure no unused or unreferenced code is left behind.
  
---

## 4. Error Handling & Documentation

- **Error Handling:**  
  - Include proper error handling wherever applicable to prevent unexpected failures.
- **Documentation:**  
  - Every function, class, and major code block must include a detailed docstring explaining its purpose and usage.
  - Add inline `# comments` for large sections of code to describe overall functionality.
  - Use inline comments to mark and explain different sections or categories (e.g., `# ---- Database Functions ----`).
  - Remove or update outdated comments that no longer match the code.

---

## 5. Change Management & Reporting

- **Detailed Change Summaries:**  
  - For every change, provide an explanation of what was modified and why.
  - Break down multiple changes into separate bullet points or sections (e.g., listing file movements, error handling additions, etc.).
- **Unrequested Improvements:**  
  - If you implement improvements based on common Python best practices that weren’t explicitly requested, inform me with a clear explanation of the change and its benefits.
- **Multi-File Changes:**  
  - If a change affects multiple files, list all the affected files and explain how the changes interconnect.
- **Commit-Worthy Sections:**  
  - When making multiple modifications, organize the explanations as if they were separate commit messages to ensure clarity and maintainability.

---

## 6. Copilot's Decision-Making & Best Practices

- **Infer Intent:**  
  - Use your judgment to infer my intent and apply small improvements when they align with best Python practices.
- **Best Practices:**  
  - Always strive to produce clean, maintainable, and well-organized code.
  - If you find a more Pythonic solution than what’s explicitly asked, implement it—but make sure to notify me of the change and explain the reasoning.
- **Import Management:**  
  - Keep imports updated and relevant. Automatically adjust them when code is added, moved, or removed.

---

Thank you for following these guidelines.
