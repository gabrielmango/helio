# Contributing to the Project

## Prefixes

Before starting to contribute to the Project, it is essential to understand the prefixes used in commits and branch naming. Prefixes help categorize and understand the purpose of changes made to the code and branches. Here are the prefixes with their meanings:

| Prefix    | Meaning                                |
|-----------|----------------------------------------|
| `feat`    | New feature or enhancement             |
| `fix`     | Bug or issue fix                       |
| `chore`   | Maintenance tasks and updates          |
| `docs`    | Documentation updates                  |
| `style`   | Formatting and style changes           |
| `test`    | Additions or modifications to tests    |
| `refactor`| Code refactoring                       |
| `perf`    | Performance improvements               |
| `config`  | Project configuration                  |

Make sure to use these prefixes consistently when making commits and naming branches. This will make the project history more organized and easier to understand.

## Commits

When making commits to the Project, follow the commit naming system to ensure that your changes are well-documented and understandable. Here's how you should create commits:

1. Choose the appropriate prefix for your commit based on the type of change you are making (e.g., `feat`, `fix`, `chore`, etc.).

2. Describe the change clearly and concisely after the prefix. Use a sentence that explains what the commit does.

3. Use the pattern `prefix: Description` to create your commit. For example:
   - `feat: Add a new user profile page`
   - `fix: Fix validation error in the login form`

By following this naming system, you make it easier to identify the purpose of each commit and help other collaborators understand your contributions.

## Branches

Branches are essential for isolating and managing work in progress. When creating new branches, follow the branch naming system to maintain consistency and understanding throughout the development process. Follow these steps:

1. Make sure you are on the main branch (`main`).

2. Update the main branch to the latest version:
   ```shell
   git checkout main
   git pull
   ```

3. Create a new branch for your task, following the pattern `type/task-name`, where `type` is the same prefix used in commits (e.g., `feat`, `fix`, `chore`, etc.), and `task-name` is a descriptive name of your task.

4. Make your code changes on your new branch.

5. After completing the changes, make commits following the naming system mentioned above.

6. When you finish the task, push your branch to the remote repository.

7. Create a Pull Request on GitHub, describing your changes and linking it to the appropriate task, if applicable.

8. Collaborators will review your changes and merge your branch when approved.

The branch naming system helps keep branches organized and related to specific tasks. Make sure to keep your branches up to date with changes from the main branch regularly.

Thank you for contributing to the Project! Your contributions are highly appreciated.