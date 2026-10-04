import kupiapi.scraper
from flask import Flask, jsonify, request

app = Flask(__name__)
scraper = kupiapi.scraper.KupiScraper()

@app.route('/kupiapi/get-discounts-by-search', methods=['GET', 'POST'])
def search_by_name():
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        search_query = data.get('search')
        max_pages = data.get('max_pages', 0)
    else:
        search_query = request.args.get('search')
        max_pages = request.args.get('max_pages', 0)

    if not search_query:
        return jsonify({"error": "The 'search' parameter is required."}), 400

    try:
        res = scraper.get_discounts_by_search(search_query, max_pages=int(max_pages))
        return jsonify(res)
    except ValueError:
        return jsonify({"error": "'max_pages' must be an integer."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/kupiapi/get-discounts-by-shop', methods=['GET', 'POST'])
def search_by_shop():
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        shop_query = data.get('shop')
        max_pages = data.get('max_pages', 0)
    else:
        shop_query = request.args.get('shop')
        max_pages = request.args.get('max_pages', 0)

    if not shop_query:
        return jsonify({"error": "The 'shop' parameter is required."}), 400

    try:
        res = scraper.get_discounts_by_shop(shop_query, max_pages=int(max_pages))
        return jsonify(res)
    except ValueError:
        return jsonify({"error": "'max_pages' must be an integer."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
