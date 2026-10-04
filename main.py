import kupiapi.scraper
from flask import Flask, jsonify, request

app = Flask(__name__)
scraper = kupiapi.scraper.KupiScraper()

@app.route('/kupiapi/get-discounts-by-search', methods=['QUERY'])
def search_by_name():
    body = request.get_json()

    res = scraper.get_discounts_by_search("vejce", max_pages=1)
    print(res)
    item_name = res.get('itemName')
    max_pages = res.get('maxPages')

    if not item_name or not max_pages:
        return {"error" : "item and and max pages keys are required: " + body}, 400

    return body

# item = input("cho za zbozi? ")
#print(scraper.get_discounts_by_search("vejce", max_pages=1))
# get_discounts_by_shop(shop, max_pages=0)

if __name__ == '__main__':
    app.run()
