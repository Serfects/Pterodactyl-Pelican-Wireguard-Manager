
## 11. Response Size Management
- **Sectioned Responses:**  
  - When implementing complex changes or large features, break your response into logical sections.
  - After completing each section, ask for my confirmation before proceeding to the next section.
  - Begin each section with a clear heading that indicates the current section number and name.

- **Section Structure:**
  - Start each section with "## Section X: [Name]" followed by a brief description of changes in this section.
  - End each section with:
    ```
    ------ 
    That completes Section X. Would you like me to proceed with Section Y: [Next Section Name], or would you prefer to review these changes first?
    ------
    ```

- **Progress Tracking:**
  - At the beginning of sectioned implementations, provide an outline of all planned sections.
  - When resuming work after confirmation, briefly summarize what has been completed and what remains.
  - For larger implementations with 3+ sections, include a progress indicator (e.g., "Section 2/5: Port Management Implementation").

- **Logical Sectioning:**
  - Group changes by functional area rather than file (e.g., "User Authentication" rather than "auth.py changes").
  - Keep sections to a reasonable size (approximately 50-100 lines of code per section).
  - Prioritize completing core functionality first, then move to enhancements and refinements.
