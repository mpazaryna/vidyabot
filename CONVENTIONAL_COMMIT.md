# Conventional Commits Cheat Sheet

## Commit Message Structure

## Primary Types

| Type     | Description                                                   | Version Bump |
|----------|---------------------------------------------------------------|--------------|
| feat     | A new feature                                                 | minor        |
| fix      | A bug fix                                                     | patch        |
| docs     | Documentation only changes                                    | -            |
| style    | Changes that do not affect the meaning of the code            | -            |
| refactor | A code change that neither fixes a bug nor adds a feature     | -            |
| perf     | A code change that improves performance                       | patch        |
| test     | Adding missing tests or correcting existing tests             | -            |
| build    | Changes that affect the build system or external dependencies | -            |
| ci       | Changes to our CI configuration files and scripts             | -            |
| chore    | Other changes that don't modify src or test files             | -            |
| revert   | Reverts a previous commit                                     | patch        |

## Examples

feat: add user authentication feature
fix: resolve issue with data persistence
docs: update README with new build instructions
style: format code according to style guide
refactor: restructure data processing module
perf: optimize database queries for faster retrieval
test: add unit tests for user registration process
build: update dependencies to latest versions
ci: configure GitHub Actions for automated testing
chore: clean up deprecated files
revert: revert commit "add user authentication feature"

## Special Cases

### Breaking Changes

For commits that introduce breaking changes, add `BREAKING CHANGE:` in the commit body or footer:

feat: change API response format
BREAKING CHANGE: The response format has changed from XML to JSON. Clients will need to be updated.

### Multiple Types

If a commit fits multiple types, prioritize in this order: 
1. fix 
2. feat 
3. other types

### Scope

You can add a scope for additional context:

feat(auth): implement two-factor authentication

## Best Practices

1. Keep the subject line concise (50 chars or less)
2. Use the imperative mood in the subject line
3. Do not end the subject line with a period
4. Separate subject from body with a blank line
5. Use the body to explain what and why vs. how
6. Can use multiple paragraphs in the body
7. Use footers for related issue references and breaking change notes


## Example message for doc change

```sh
docs: add conventional commits cheat sheet

- Create CONVENTIONAL_COMMITS.md with quick reference guide
- Include commit types, structure, and best practices
```
