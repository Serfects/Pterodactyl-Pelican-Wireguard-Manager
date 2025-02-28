
# Recommended Guidelines for Copilot Instructions

## Module Dependency and Import Management

- **Dependency Hierarchy:**
  - Maintain a clear dependency hierarchy where utility modules (like base_utils, display_utils, input_utils) are at the bottom layer.
  - Middle-layer modules (like navigation, configuration handlers) should depend only on utility modules.
  - Top-layer modules (like main_menu, application-specific features) can depend on both utility and middle-layer modules.

- **Import Structure:**
  - Group imports logically: standard library first, third-party packages second, local modules last.
  - Within each group, maintain alphabetical order when possible.
  - Use explicit imports (e.g., `from module import specific_function`) for clarity.

- **Preventing Circular Imports:**
  - When creating new modules or refactoring existing ones, draw a dependency diagram to visualize relationships.
  - Use dependency injection where appropriate (passing dependencies as parameters).
  - Consider using late imports (importing inside functions) only when necessary to break circular dependencies.
  - When faced with potential circular imports, extract shared functionality to a lower-level module.

## Code Organization Standards

- **Module Organization:**
  - Organize related functionality into cohesive modules.
  - Each module should have a clear, single responsibility.
  - Keep modules focused on specific domains (e.g., UI, network, configuration).

- **Function and Class Placement:**
  - Place functions in modules where they have the strongest conceptual connection.
  - Move frequently reused utility functions to appropriate utility modules.
  - When a function serves a very specific purpose for a single feature, keep it in the feature module.

- **Reusability:**
  - Design functions and classes with reusability in mind.
  - Avoid hardcoding values that might need to change across different uses.
  - Use parameter defaults for optional configuration.

## Error Handling and Logging

- **Error Management Hierarchy:**
  - Use custom AppError exceptions for application-specific errors.
  - Implement contextual error messages that guide the user toward resolution.
  - Separate user-facing error messages from technical logs.

- **Logging Strategy:**
  - Log at appropriate levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
  - Include sufficient context in log messages for troubleshooting.
  - Log start and completion of significant operations.
  - Add timestamps and operation IDs for tracing request flows.

## Testing and Documentation

- **Testable Code Structure:**
  - Design functions with testing in mind (single responsibility, clear inputs/outputs).
  - Avoid global state that complicates testing.
  - Use dependency injection to make components testable in isolation.

- **Documentation Standards:**
  - Maintain consistent docstring format across all code.
  - Document parameters, return values, and exceptions raised.
  - Include usage examples for complex functions.
  - Add module-level docstrings explaining the overall purpose and organization.

## Performance Considerations

- **Resource Management:**
  - Close resources (files, connections) using context managers when possible.
  - Be mindful of memory usage with large data structures.

- **Optimization Guidelines:**
  - Focus on algorithm efficiency before micro-optimizations.
  - Use appropriate data structures (dictionaries for lookups, sets for membership tests).
  - Avoid premature optimization but be aware of operations that scale poorly.

## User Interface Consistency

- **Color and Formatting:**
  - Maintain consistent color schemes for different message types (errors, success, warnings, menus, context, details, user input, etc.).
  - Follow established patterns for menu layouts and user prompts.
  - Ensure consistent spacing and alignment in text-based interfaces.

- **User Feedback:**
  - Confirm successful operations with clear messages.
