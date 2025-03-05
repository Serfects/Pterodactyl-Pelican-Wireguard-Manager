# GitHub Copilot Instructions for Logan's Project

---

## 1. General Information & Communication
- **User Identity:** My name is **Logan**. Always address me as Logan.
- **Chat-Only Requests:** If I say “show in chat” or “show before applying,” propose modifications only in chat with no direct code changes.
- **Project References:**
  - **“The Script” / “The Project”:** Refers to the codebase in `/workspaces/Pterodactyl-Pelican-Wireguard-Manager/src/ppwm-dev-pt` unless otherwise stated.
- **Notifications:** Notify me if any requests counter or contradict the existing instructions/project structure/guidelines.

---

## 2. Project Scope & Language
- **Python Version & Modernization:**
  - The project targets **Python 3.11+** or the newest available version.
  - Prefer modern Python features from the newest stable release; backward compatibility with older versions is not a priority.
- **Primary Language & Frameworks:**
  - Written in **Python**, with occasional Bash scripts.
  - **prompt_toolkit v3.0.38+** or the newest available version is the primary UI framework.
  - If built-in Python or prompt_toolkit functionalities can replace existing code, feel free to migrate or rewrite that code for clarity and maintainability.
- **Coding Standards:**
  - Follow common Python best practices (PEP 8, clean code principles, etc.).
  - **No Type Hints:** Do not add or suggest type hints unless I explicitly request them.
- **Error Output:**
  - Reuse the project’s existing error-message functionality for all new or modified error displays.
- **Color & Formatting:**
  - Adhere to established color/formatting standards.
  - Define or adjust styles in `pt_comps.py`. Introduce additional libraries if needed for modern features or compatibility.
- **Reusability & Logging:**
  - Reuse existing functions/classes whenever possible.
  - Add logging only where it’s truly beneficial. Avoid logging every line unnecessarily.

---

## 3. Code Organization & Structure
- **Logical Grouping:**
  - Group similar or related functionality together.
  - Place new code in the most appropriate existing sections.
- **Module Segregation & Prompt Toolkit:**
  - `pt_comps.py` should contain key prompt_toolkit-based components.
  - Related features (e.g., navigation, display) can remain in or move to their respective modules if it’s logical to do so.
  - If prompt_toolkit provides a better implementation for an existing feature, feel free to rewrite or relocate that feature accordingly.
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
  - Explain changes in simple, clear language.
- **One Module at a Time:**
  - Only modify one file/module at a time if changes are large or complex.
  - Provide an outline or plan for each module’s refactoring before making the changes.
  - We can revisit previously touched modules if needed, but keep the overall approach incremental and well-documented.
- **Dependency Tracking:**
  - If you add an external package or dependency, update (or create) a `dependency.md` file with:
    - The package/dependency name
    - Version requirements (if applicable)
    - Short usage or installation notes
  - Always list required dependencies in `dependency.md`. We aim to use the newest stable versions available.
- **Unrequested Improvements:**
  - If you make extra best-practice improvements, notify me with a brief rationale.

---

## 7. Copilot’s Decision-Making & Best Practices
- **Infer Intent:**
  - Use your judgment to interpret my goals and apply minor improvements that follow Pythonic guidelines.
- **Import Management:**
  - Keep imports tidy and relevant, adjusting automatically when code is moved or removed.
- **Native/Built-in First:**
  - Prefer default Linux packages and built-in Python modules before reaching for external dependencies.
  - If Linux and Python both offer similar functionality, use whichever is more reliable and efficient.
  - If an external dependency simplifies the task significantly or provides a modern advantage, include it—but remember to update `dependency.md` and inform me.
- **Testing & Performance:**
  - Write functions with single responsibilities and clear inputs/outputs for testability.
  - Avoid global state.
  - Use context managers for resource handling.
  - Optimize only where needed; avoid prematurely or overly optimizing.

---

## 8. Module Dependency & Organization
- **Dependency Hierarchy:**
  - Keep utility modules at the bottom (e.g., `base_utils`, `display_utils`, `input_utils`).
  - Middle-layer modules should only depend on utility modules.
  - Top-layer modules (like `main_menu` or other features) can depend on both utility and middle-layer modules.
- **Preventing Circular Imports:**
  - Use dependency injection or late imports (inside functions) only if absolutely necessary.
  - If a cycle emerges, refactor shared logic into a lower-level module.

---

## 9. UI & Interface Guidelines
### 9.1 Framework & Requirements
- **prompt_toolkit v3.0.38+:** or the newest available version is the primary UI framework (no colorama needed).
- **pygments:** Use for syntax highlighting if needed (e.g., text editors).
- **`pt_comps.py`:** 
  - Base module for prompt_toolkit functionality (`show_message()`, `prompt_input()`, `show_progress_bar()`, etc.).
  - Extend the `PPWM_STYLE` dict or existing references if new colors or symbols are needed.
- **No Direct Terminal Manipulation:** Avoid manual screen clearing, cursor movement, or similar. Rely primarily on prompt_toolkit.

### 9.2 Interface Design Principles
- **Keyboard-First Navigation:**
  - All UI elements must be fully accessible via keyboard.
  - Logical tab order, optional mouse support, on-screen shortcut hints.
- **Terminal Compatibility & Fallbacks:**
  - Target modern terminal emulators with 256+ colors. 
  - Provide minimal fallbacks if it’s simple and beneficial, but legacy support isn’t a priority.
  - Handle terminal resizing gracefully.
  - Minimum recommended size: 80x24.
- **Styling & Consistency:**
  - Use the `PPWM_STYLE` dictionary for uniform styling (colors, symbols, etc.).
  - Maintain the color palette:
    - **Blue (#3498db):** highlights, buttons, focus
    - **Green (#2ecc71):** successes, positive feedback
    - **Red (#e74c3c):** errors, destructive actions
    - **Yellow (#f39c12):** warnings, cautions
  - Use consistent status symbols (✓, ⚠, etc.).
  - Add new colors and or symbols and or formatting to features that don’t have them that you feel would benefit from them.
  - Attempt to follow the existing color and formatting standards when adding new colors or symbols to features.
  - HTML-like tags (`<tag>text</tag>`) may be used if supported by prompt_toolkit.
  - Remove `colorama` unless absolutely necessary for compatibility.

### 9.3 Implementation Guidelines
- **Dialog Components:**
  - Use prompt_toolkit’s dialog features for modals, input dialogs, etc.
  - Clear titles, optional bottom toolbar for shortcuts, proper focus management.
- **Form Input & Validation:**
  - Provide validation with clear error messages.
  - Offer sensible defaults where possible.
  - Use auto-completion if it improves user experience.
  - Support cancellation (Esc) and confirmation (Enter).
- **Progress Indicators:**
  - Deterministic progress bars for known-duration tasks, indeterminate spinners otherwise.
  - Show status updates during lengthy operations.
- **Menu Systems:**
  - Keyboard shortcuts for navigation (numbers, arrow keys).
  - Keep menu structures consistent and logical.
  - Allow both number-based and arrow-key selections.

### 9.4 Accessibility Considerations
- **Screen Reader Compatibility:**
  - Use descriptive labels for interactive elements.
  - Ensure critical alerts (errors) are screen reader-friendly.
- **Environment Checks:**
  - Check terminal size and color support at startup.
  - Warn if below recommended size or lacking features.
- **Feedback & Status:**
  - Provide clear success/error messages after each operation.
  - Use a bottom toolbar for contextual help, updates, or status.
  - If an unrecoverable error occurs, show an explanatory message before exiting.

---

## 10. Response Size Management
- **Sectioned Responses:**
  - For complex or large features, break your response into logical sections.
  - After each section, ask for confirmation before moving on.
- **Section Structure:**
  - Start each section with “## Section X: [Name]” and a brief description.
  - End each section with:
    ```
    ------
    That completes Section X. Would you like me to proceed with Section Y: [Next Section Name], or would you prefer to review these changes first?
    ------
    ```
- **Progress Tracking:**
  - At the start of a multi-section implementation, outline all planned sections.
  - Summarize completed tasks and remaining work when resuming.
  - For 3+ sections, include a progress indicator (e.g., “Section 2/5: Port Management Implementation”).
- **Logical Sectioning:**
  - Group changes by functional area (e.g., “User Authentication” vs. “auth.py changes”).

---
