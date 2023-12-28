from wikibot import scrape

def test_scrape():
    # Perform the scrape
    results = scrape("Facebook")

    # Check if "Facebook" is in the results
    assert "facebook" in results, f"Expected 'Facebook' in results, but got: {results}"

    # If the assertion passes, the program continues; if not, it raises an AssertionError.
    print("Assertion passed! 'Facebook' is in the results.")