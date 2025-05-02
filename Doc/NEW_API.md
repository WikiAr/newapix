
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

