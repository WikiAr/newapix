
## MainPage

The ````MainPage```` class is a core component of the newapi framework that provides a high-level interface for interacting with individual wiki pages across various MediaWiki sites. It encapsulates all operations related to reading, editing, and analyzing specific pages, abstracting away the complexity of direct API calls.

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
# Get basic information
text = page.get_text()
namespace = page.namespace()
timestamp = page.get_timestamp()
word_count = page.get_words()

````

### User Information
To get information about the user who last edited the page:
```` python
# Get username
username = page.get_user()

# Get detailed user information
userinfo = page.get_userinfo()  # Returns dict with "id", "name", "groups"

````

### Templates
Two methods are available for retrieving templates used in a page:
- The get_templates() method returns a more detailed structure that includes template parameters, using the txtlib.extract_templates_and_params() function.

```` python
# Get templates with parameters via text parsing
templates = page.get_templates()
for temp in temps:
    name, namestrip, params, template = temp['name'], temp['namestrip'], temp['params'], temp['item']

# Get templates via API (returns list of template titles)
templates_api = page.get_templates_API()
for temp in templates_api:
    print(temp)
````

### Categories
To retrieve the categories a page belongs to:
```` python
# Get regular categories
categories = page.get_categories()

# Get hidden categories
hidden_categories = page.get_hidden_categories()

# Get all categories including hidden ones
all_categories = page.get_categories(with_hidden=True)
````
### Links
```` python
# Get wiki links (internal links)
wiki_links = page.get_wiki_links_from_text()

# Get language links (interwiki links)
lang_links = page.get_langlinks()

# Get external links
ext_links = page.get_extlinks()

# Get pages linking to this page
links_here = page.get_links_here()

back_links = page.page_backlinks()

links = page.page_links()

````
### HTML Tags
```` python
# Get specific elements from the page
references = page.Get_tags(tag='ref')
for x in references:
    name, contents = x.name, x.contents

````

### Editing Page
This document details how to edit and create wiki pages using the NewAPI framework. It covers the primary methods for page modification, permission checking, and best practices for making edits to MediaWiki pages.

#### Save

```` python

# Edit an existing page
page = MainPage("New Page Title", "en", family="wikipedia")

new_text = "This is the new content of the page."

save_page = page.save(
    newtext=new_text,
    summary="Edit summary",
    nocreate=1,  # Don't create if page doesn't exist
    minor="",    # Not a minor edit
    tags="",     # No special tags
    nodiff=False,# Show diff when ASK is True
    ASK=False    # Don't ask for confirmation
)
````

#### Create

```` python
# Create a new page
page = MainPage("New Page Title", "en", family="wikipedia")

if not page.exists():
    success = page.Create(
        text="This is the content of the new page.",
        summary="Create page",
        nodiff="",   # Show diff when not in nodiff mode
        noask=False  # Ask for confirmation
    )

````

### Additional Page Operations
```` python

# Get page HTML representation
text_html = page.get_text_html()

#
flagged     = page.is_flagged()

#
revisions   = page.get_revisions(rvprops=['content'])

# Purging the Page Cache
purge       = page.purge()

````
