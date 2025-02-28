# GitHub Copilot Instructions for Logan's Project

## 1. General Information & Communication

- **User Identity:** My name is **Logan**. Please always address me as Logan.
- **Chat-Only Requests:**  
  - If I request you to "show in chat" or "show before applying," **do not make any code changes** and only respond with the proposed modifications or suggestions in chat.

---

## 2. Project Scope & Language

- **Primary Language:**  
  - The project is written entirely in **Python**, with some occasional Bash scripts.
  - All generated code and changes to code and suggestions should follow common Python best practices (PEP 8, clean code principles, etc.).
- **No Type Hints:**  
  - Under no circumstances should type hints be added or suggested. This project explicitly avoids type hinting.
  - If new user prompts are generated or modified, ensure the generated code is using the `get_input` or similar functionality from wherever there is reusable code for getting user input.
  - If generating or modifying code to display an error to the user, ensure the generated code is using the reusable error message functionality.
  - When generating or changing any code, ensure that color and formatting standards found in already existing working files are followed.
  - Always reuse existing functions and classes when possible.
  - When generating or modifying code, try to make classes and functions reusable by other parts of the codebase.
  - When generating new code or adding new code or changing existing code, ensure that the logging feature is being used within the new or modified code to properly log information. Do not add logging to every single feature, only where it makes sense or is beneficial to add logging.

---

## 3. Code Organization & Structure

- **Logical Grouping:**  
  - Organize code by grouping similar or related functionality together.
  - Place new code in the correct sections of the existing codebase.
- **Code Movement & Refactoring:**  
  - When moving code between modules or sections, **remove the old code** from its original location.
  - Automatically update, add, or remove import statements in both the source and destination files.
  - Ensure no unused or unreferenced code is left behind. Diligently check and remove any unused or unnecessary code.

---

## 4. Error Handling & Documentation

- **Error Handling:**  
  - Include proper error handling wherever applicable to prevent unexpected failures.
  - With error handling, ensure that error messages are displayed to the user and also logged using the logging functionality.
- **Documentation:**  
  - Every function, class, and major code block must include a detailed docstring explaining its purpose and usage.
  - Add comprehensive module-level and function-level docstrings.
  - Add inline `# comments` for large sections of code to describe overall functionality in addition to docstrings.
  - Use inline comments to mark and explain different sections or categories (e.g., `# ---- Database Functions ----`).
  - Remove or update outdated comments that no longer match the code or its explanation.
  - Ensure that all docstrings and comments are written in clear, concise, and easy-to-understand language.

---

## 5. Change Management & Reporting

- **Detailed Change Summaries and Explanations:**  
  - For every change, provide clear, detailed, and easy-to-understand explanations.
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
  - If functions or classes or anything related is changed, look through the modules and ensure that imports and names within the code of all the affected modules are properly updated to reflect the changes.

---

# Additional / Enhanced Guidelines (from the Proposed Set)

Below are expanded sections that incorporate the second set of guidelines. These sections complement the existing instructions above without replacing them.

## 7. Module Dependency & Import Management

1. **Dependency Hierarchy:**
   - Maintain a clear dependency hierarchy where utility modules (like `base_utils`, `display_utils`, `input_utils`) are at the bottom layer.
   - Middle-layer modules (e.g., navigation, configuration handlers) should depend only on utility modules.
   - Top-layer modules (such as `main_menu` or application-specific features) can depend on both utility and middle-layer modules.

2. **Import Structure:**
   - Group imports logically: standard library first, third-party packages second, local modules last.
   - Within each group, maintain alphabetical order when possible.
   - Use explicit imports (e.g., `from module import specific_function`) for clarity.

3. **Preventing Circular Imports:**
   - When creating new modules or refactoring existing ones, sketch a dependency diagram to visualize relationships.
   - Use dependency injection where appropriate (passing dependencies as parameters).
   - Consider using late imports (importing inside functions) **only** when necessary to break circular dependencies.
   - When faced with potential circular imports, extract shared functionality to a lower-level module.

4. **Preference for Native/Built-in Packages:**
   - **Use default Linux packages and built-in Python modules first** before considering external dependencies.
   - If both Linux and Python provide similar functionality, choose the method or resource that is most efficient, stable, and secure.
   - Only reach for external packages, dependencies, or libraries if they significantly improve or simplify the requested functionality beyond what the built-in tools provide.
   - **Whenever you add a new dependency**, you must add an entry to a `dependency.md` file located in the codebase. If that file doesn’t already exist, create it and list the new dependency there along with any relevant usage notes or version requirements.

> _Note:_ These details augment the existing “Import Management” bullet in Section 6. In practice, follow both sets of guidelines to ensure clarity and maintainability.

---

## 8. Additional Code Organization Standards

- **Module Organization:**
  - Organize related functionality into cohesive modules, each with a clear, single responsibility.
  - Keep modules focused on specific domains (e.g., UI, network, configuration).

- **Function and Class Placement:**
  - Place functions in the modules where they have the strongest conceptual connection.
  - Move frequently reused utility functions to appropriate utility modules.
  - When a function serves a very specific purpose for a single feature, keep it in that feature’s module.

- **Reusability:**
  - Design functions and classes with reusability in mind.
  - Avoid hardcoding values that might need to change across different uses.
  - Use parameter defaults for optional configuration.

---

## 9. Extended Error Handling & Logging

- **Error Management Hierarchy:**
  - Use custom `AppError` (or similarly named) exceptions for application-specific errors.
  - Provide contextual error messages that guide the user toward resolution.
  - Separate user-facing error messages from technical logs where it makes sense.

- **Logging Strategy:**
  - Log at appropriate levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
  - Include sufficient context in log messages for troubleshooting.
  - Log start and completion of significant operations.
  - Add timestamps and operation IDs (if applicable) for tracing request flows.

> _Note:_ This section expands upon the logging and error-handling guidelines in Section 4. Use whichever aspects are most beneficial in context.

---

## 10. Testing & Documentation Enhancements

- **Testable Code Structure:**
  - Write functions with clear inputs/outputs and single responsibilities to facilitate easier testing.
  - Avoid global state that complicates testing.
  - Use dependency injection to isolate components during tests.

- **Documentation Standards:**
  - Maintain a consistent docstring format across all code.
  - Document parameters, return values, and exceptions raised.
  - Include usage examples for more complex functions.
  - Provide module-level docstrings explaining the overall purpose and organization.

> _Note:_ These points reinforce Section 4’s docstring and documentation rules by providing extra detail on testing and usage examples.

---

## 11. Performance Considerations

- **Resource Management:**
  - Use context managers (e.g., `with open(...) as f:`) to ensure files and connections are properly closed.
  - Be mindful of memory usage with large data structures.

- **Optimization Guidelines:**
  - Focus on algorithmic efficiency before micro-optimizations.
  - Use appropriate data structures (dictionaries for lookups, sets for membership tests, etc.).
  - Avoid premature optimization, but be aware of operations that scale poorly.

---

## 12. User Interface Consistency

- **Color and Formatting:**
  - Maintain consistent color schemes for different message types (errors, success, warnings, menus, context, details, user input, etc.).
  - Follow established patterns for menu layouts and user prompts.
  - Ensure consistent spacing and alignment in text-based interfaces.

- **User Feedback:**
  - Provide clear messages to confirm successful operations.
  - Make sure error and warning messages are easily distinguishable from normal or success messages.

---
