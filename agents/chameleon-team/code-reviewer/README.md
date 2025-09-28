# Code Reviewer Agent

A professional code review agent that provides comprehensive analysis of your code quality, security, and best practices.

## Features

- **Quality Analysis**: Identifies code quality issues and improvement opportunities
- **Security Audit**: Detects potential security vulnerabilities
- **Performance Review**: Suggests optimization opportunities
- **Best Practices**: Ensures adherence to industry standards
- **Multi-language Support**: Works with various programming languages

## Usage

### With Claude Code CLI
```bash
# Install the agent
agents install chameleon-team/code-reviewer

# Use for code review
claude-code review --agent code-reviewer path/to/your/code.js
```

### With VS Code Extension
1. Open the Chameleon extension
2. Navigate to Agent Marketplace
3. Search for "Code Reviewer"
4. Click "Download to Claude Code"
5. Use in your Claude Code conversations

## Example Review

Input:
```javascript
function calculateTotal(items) {
    var total = 0;
    for (var i = 0; i < items.length; i++) {
        total += items[i].price * items[i].quantity;
    }
    return total;
}
```

Output:
```
### Summary
The function calculates order totals but has several areas for improvement.

### Improvements
- Use `const`/`let` instead of `var` for better scoping
- Add input validation for null/undefined items
- Consider using array methods like `reduce()` for cleaner code
- Add JSDoc comments for better documentation

### Suggested Refactor
```javascript
/**
 * Calculates the total cost of items
 * @param {Array<{price: number, quantity: number}>} items - Array of items
 * @returns {number} Total cost
 */
function calculateTotal(items) {
    if (!Array.isArray(items)) {
        throw new Error('Items must be an array');
    }
    
    return items.reduce((total, item) => {
        if (typeof item.price !== 'number' || typeof item.quantity !== 'number') {
            throw new Error('Invalid item format');
        }
        return total + (item.price * item.quantity);
    }, 0);
}
```

## License

MIT License
