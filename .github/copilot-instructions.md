# GitHub Copilot Instructions for Logan's Project

---

## 1. General Information & Communication
- **User Identity:** My name is **Logan**. Always address me as Logan.
- **Chat-Only Requests:** If I say “show in chat” or “show before applying,” propose modifications only in chat with no direct code changes.

---

## 2. Project Scope & Language
- **Primary Language:**  
  - The project is written in **Python** (with occasional Bash scripts).
  - Follow common Python best practices (PEP 8, clean code principles, etc.).
- **No Type Hints:**  
  - Under no circumstances should type hints be added or suggested, unless I explicitly request them.
- **User Input & Error Output:**  
  - Use `prompt_user` (or similar functionality) for new or modified user prompts.
  - Reuse the project’s existing error-message functionality for any new or modified error displays.
- **Color & Formatting:**  
  - Adhere to the color/formatting standards found in the existing codebase.
- **Reusability & Logging:**  
  - Reuse existing functions and classes whenever possible.
  - Add logging only where it makes sense or is beneficial. Avoid logging every line unnecessarily.

---

## 3. Code Organization & Structure
- **Logical Grouping:**  
  - Group similar or related functionality together.  
  - Place new code in the most appropriate existing sections.
- **Code Movement & Refactoring:**  
  - If you move code, remove it from the old location.  
  - Update or remove import statements automatically.  
  - Ensure no unused or unreferenced code remains.

---

## 4. Error Handling & Logging
- **Error Handling:**  
  - Use proper error handling to avoid unexpected crashes.  
  - Display errors to the user and log them internally.  
  - Consider using custom exceptions (e.g., `AppError`) for application-specific issues.
- **Logging Strategy:**  
  - Log at appropriate levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).  
  - Provide sufficient context for debugging.  
  - Log the start and completion of major operations if helpful.  
  - Timestamps or unique operation IDs can be used to trace the flow of requests.

---

## 5. Documentation
- **Docstrings & Comments:**  
  - Provide a docstring for every function, class, and significant code block.  
  - Keep docstrings clear, concise, and up to date with the code’s behavior.  
  - Use inline `# comments` to label and describe code sections (e.g., `# ---- Database Functions ----`).  
  - Remove or revise comments that no longer match the code.

---

## 6. Change Management & Reporting
- **Detailed Change Summaries:**  
  - Explain every change in simple, clear language.
- **Multi-File Changes:**  
  - List all affected files and clarify how changes interconnect.
- **Dependency Tracking:**  
  - If you add an external package or dependency, update (or create) a `dependency.md` file with:
    - The package/dependency name  
    - Version requirements (if applicable)  
    - Short usage or installation notes
- **Unrequested Improvements:**  
  - If you make any extra best-practice improvements, notify me with a brief rationale.

---

## 7. Copilot’s Decision-Making & Best Practices
- **Infer Intent:**  
  - Use your judgment to interpret my goals and apply minor improvements that follow Pythonic guidelines.
- **Import Management:**  
  - Keep imports tidy and relevant, adjusting automatically when code is moved or removed.
- **Native/Built-in First:**  
  - Prefer default Linux packages and built-in Python modules before reaching for external dependencies.
  - If Linux and Python both offer similar functionality, use whichever is most reliable and efficient.
  - When an external dependency is clearly superior or simplifies the requested feature significantly, feel free to use it—but remember to update `dependency.md`.
- **Testing & Performance:**  
  - Write functions with single responsibilities and clear inputs/outputs for testability.  
  - Avoid global state.  
  - Use context managers for resource handling.  
  - Optimize where needed, but avoid premature optimization.  

---

## 8. Module Dependency & Organization
- **Dependency Hierarchy:**  
  - Keep utility modules at the bottom (e.g., `base_utils`, `display_utils`, `input_utils`).  
  - Middle-layer modules should only depend on utility modules.  
  - Top-layer modules (like `main_menu` or other features) can depend on both utility and middle-layer modules.
- **Preventing Circular Imports:**  
  - Use dependency injection or, if absolutely necessary, late imports (inside functions).  
  - If a cycle emerges, refactor shared logic into a lower-level module.

---

## 9. User Interface Consistency
- **Color & Formatting:**  
  - Maintain a consistent color scheme for errors, success, warnings, menus, context, details, user input, etc.
- **User Feedback:**  
  - Provide clear success messages and differentiate them from error or warning messages.  
  - Ensure spacing and alignment are consistent in text-based interfaces.

---
