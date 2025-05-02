Python module for Wikimedia API:

----
# Newapi.page Module:

## MainPage

The ````MainPage```` class is a core component of the newapi framework that provides a high-level interface for interacting with individual wiki pages across various MediaWiki sites. It encapsulates all operations related to reading, editing, and analyzing specific pages, abstracting away the complexity of direct API calls.

For general API operations that don't target specific pages, see NEW_API Class. For category-specific operations, see CatDepth.

See [Doc/MainPage.md](Doc/MainPage.md)

```` python
# ---
from newapi.page import MainPage
page      = MainPage('Article title', 'ar', family='wikipedia')
# ---
# Check if the page exists
if not page.exists():
    print("Page doesn't exist")
    return
# ---
if not page.can_edit(script='fixref|cat|stub|tempcat|portal'):
    return
# ---
if page.isRedirect() :
    target = page.get_redirect_target()
    print("Page isRedirect")
    return
# ---
if page.isDisambiguation():
    return
# ---
new_text = text.replace("", "")

# Edit an existing page
save_result = page.save(
    newtext=new_text,
    summary="Edit summary",
    nocreate=1,  # Don't create if page doesn't exist
    minor="",    # Not a minor edit
    tags="",     # No special tags
    nodiff=False,# Show diff when ASK is True
    ASK=False    # Don't ask for confirmation
)

````

## CatDepth

[Doc/CatDepth.md](Doc/CatDepth.md)


## NEW_API
The NEW_API class provides a robust, high-level interface to the MediaWiki API, abstracting away the complexities of direct API interaction. By providing methods for common operations like searching, retrieving pages, working with templates, and handling user contributions, it enables developers to create sophisticated tools and bots for MediaWiki platforms with minimal code.

See [Doc/NEW_API.md](Doc/NEW_API.md)

----
# Newapi.pformat Module:
For complex edits involving templates, the framework includes utilities to format template syntax in a standard way:

```` python
from newapi import pformat

# Format templates in text
new_text = pformat.make_new_text(text)
````
