Python module for Wikimedia API:

----
# Newapi.page Module:

## MainPage
The ````MainPage```` class is a core component of the newapi framework that provides a high-level interface for interacting with individual wiki pages across various MediaWiki sites. It encapsulates all operations related to reading, editing, and analyzing specific pages, abstracting away the complexity of direct API calls.

For general API operations that don't target specific pages, see NEW_API Class. For category-specific operations, see CatDepth.

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
user = page.get_user()
userinfo    = page.get_userinfo() # "id", "name", "groups"
word_count = page.get_words()

# templates
templates = page.get_templates()
for temp in temps:
    name, namestrip, params, template = temp['name'], temp['namestrip'], temp['params'], temp['item']

# Get links and categories
categories = page.get_categories(with_hidden=False)
hidden_categories = page.get_hidden_categories()

templates_api = page.get_templates_API()
langlinks = page.get_langlinks()
extlinks = page.get_extlinks()
wiki_links = page.get_wiki_links_from_text()
back_links = page.page_backlinks()
links       = page.page_links()

# Get page HTML representation
text_html = page.get_text_html()

# Get specific elements from the page
references = page.Get_tags(tag='ref')
# for x in ref: name, contents = x.name, x.contents

# ---
flagged     = page.is_flagged()
revisions   = page.get_revisions(rvprops=['content'])
# ---
purge       = page.purge()

# Edit an existing page
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

# Create a new page
success = page.Create(
    text="This is the content of the new page.",
    summary="Create page",
    nodiff="",   # Show diff when not in nodiff mode
    noask=False  # Ask for confirmation
)

````
## CatDepth

```` python
from newapi.page import CatDepth

cat_members = CatDepth("Category title", sitecode='en', family="wikipedia", depth=0, ns="all", nslist=[], tempyes=[])

````
## NEW_API
The NEW_API class provides a robust, high-level interface to the MediaWiki API, abstracting away the complexities of direct API interaction. By providing methods for common operations like searching, retrieving pages, working with templates, and handling user contributions, it enables developers to create sophisticated tools and bots for MediaWiki platforms with minimal code.

### list of pages

```` python
from newapi.page import NEW_API

# Initialize API with language and family
api = NEW_API('en', family='wikipedia')

# Login to the wiki
api.Login_to_wiki()

# get list of pages:
# pages_info = api.Get_All_pages_generator(start="A", namespace="0", limit="max")
# pages    = api.Get_All_pages(start='', namespace="0", limit="max", apfilterredir='', limit_all=0)

# Get up to 5000 contributions from User:Example in all namespaces
contribs = api.UserContribs("User:Example", limit=5000, namespace="*", ucshow="")

# Find pages with titles starting with "Python"
results = api.PrefixSearch("Python", ns="0", pslimit="max")

newpages = api.Get_Newpages(limit="max", namespace="0", rcstart="", user='', three_houers=False)

# Process each page
for title in newpages:
    page = MainPage(title, 'en', family='wikipedia')

    # Skip redirects and non-existent pages
    if not page.exists() or page.isRedirect():
        continue

    # Get page content
    text = page.get_text()

    # Process the page as needed
    # ...

````
### Search

```` python
results = api.Search(value="solar system", ns="0", srlimit="10", RETURN_dict=False, addparams={})

# Results will be a list of page titles matching the search query
for title in results:
    print(title)

````

### Find_pages_exists_or_not
```` python
# Check if multiple pages exist
pages_to_check = ["Earth", "Mars", "NonExistentPage123"]
existence_info = api.Find_pages_exists_or_not(pages_to_check)

# existence_info will be a dictionary mapping titles to boolean values
for title, exists in existence_info.items():
    status = "exists" if exists else "does not exist"
    print(f"Page '{title}' {status}")
````

### move

```` python
# Move a page (requires appropriate permissions)
result = api.move(
    old_title="Draft:MyArticle",
    to="MyArticle",
    reason="Article ready for mainspace",
    noredirect=False
)

if result is True:
    print("Move successful")
else:
    print(f"Move failed: {result}")

````
### Other funcations:

```` python
# Get information about users
info = api.users_infos(ususers=["User1", "User2"])

# Get all pages using Template:Infobox
pages = api.Get_template_pages("Template:Infobox", namespace="*", Max=10000)

# Get German equivalents for English pages
lang_links = api.Get_langlinks_for_list(["Page1", "Page2"], targtsitecode="de")

# Get wanted categories
wanted = api.querypage_list(qppage="Wantedcategories", qplimit="max")

# Get pages with unlinked Wikibase IDs
pages = api.pageswithprop(pwppropname="unlinkedwikibase_id", Max=10000)

l_links  = api.Get_langlinks_for_list(titles, targtsitecode="", numbes=50)
text_w   = api.expandtemplates(text)
subst    = api.Parse_Text('{{subst:page_name}}', title)
extlinks = api.get_extlinks(title)
revisions= api.get_revisions(title)
json1    = api.post_params(params, addtoken=False)

````

### Files
```` python

# Get detailed information about an image
info = api.Get_imageinfo("Example.jpg")

# Get URL for an image file
url = api.Get_image_url("Example.jpg")

# Uploading a File
result = api_new.upload_by_file(
    'Example.jpg',
    '{{Information|description=Example image}}',
    '/path/to/local/file.jpg',
    comment='Uploading example image'
)

````

### Adding Text to a Page without using MainPage
```` python
# added    = api_new.Add_To_Bottom(text, summary, title, poss="Head|Bottom")

result = api_new.Add_To_Bottom(
    '== New section ==\nSome new content.',
    'Adding new section',
    'Page Title'
)

````
