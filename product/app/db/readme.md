**Stub and Fake Data**

Also known as mock data, stubs are canned results that are returned without calling
the normal “live” modules. They’re a quick way to test your routes and responses.
A fake is a stand-in for a real data source that performs at least some of the same
functions. An example is an in-memory class that mimics a database. You’ll be mak‐
ing some fake data in this chapter and the next few, as you fill in the code that defines
the layers and their communication, you’ll define an actual live data
store (a database) to replace these fakes.

**Create Common Functions Through the Stack**
Similar to the data examples, the approach to building this site is exploratory. Often it
isn’t clear what will eventually be needed, so let’s start with some pieces that would be
common to similar sites. Providing a frontend for data usually requires ways to do
the following:

• Get one, some, all
• Create
• Replace completely
• Modify partially
• Delete


Essentially, these are the CRUD basics from databases, although I’ve split the U into
partial (modify) and complete (replace) functions. Maybe this distinction will prove
unnecessary! It depends on where the data leads.

**Create Fake Data**
Working top-down, you’ll duplicate some functions in all three levels.