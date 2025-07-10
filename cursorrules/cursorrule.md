# Cursor Rules

This document outlines the cursor rules for the Streamlit and Dash insights project.

## Overview

Cursor rules define how cursor interactions should behave across the application.

## Global Cursor Rules

### 1. Default Cursor Behavior
- **Pointer cursor**: Used for clickable elements
- **Text cursor**: Used for text input fields
- **Default cursor**: Used for non-interactive elements

### 2. Interactive Elements
- Buttons and links should show pointer cursor on hover
- Form inputs should show text cursor when focused
- Disabled elements should show not-allowed cursor

### 3. Custom Cursor Rules
- Data visualization areas: crosshair cursor for selection
- Draggable elements: grab/grabbing cursors
- Loading states: wait cursor

## Implementation Guidelines

### CSS Classes
```css
.clickable { cursor: pointer; }
.text-input { cursor: text; }
.disabled { cursor: not-allowed; }
.selectable { cursor: crosshair; }
.draggable { cursor: grab; }
.dragging { cursor: grabbing; }
.loading { cursor: wait; }
```

### JavaScript/React
```javascript
// Example cursor rule implementation
const setCursor = (element, cursorType) => {
  element.style.cursor = cursorType;
};
```

## Best Practices

1. **Consistency**: Maintain consistent cursor behavior across similar elements
2. **Accessibility**: Ensure cursor changes provide clear visual feedback
3. **Performance**: Avoid excessive cursor changes that might impact performance
4. **User Experience**: Use cursors that match user expectations

## Notes

- Update this document as new cursor rules are added
- Test cursor behavior across different browsers and devices
- Consider accessibility guidelines when implementing cursor rules 