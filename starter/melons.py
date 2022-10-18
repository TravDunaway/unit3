import csv

class Melon:

    def __init__ (self, melon_id, common_name, price, image_url, color, seedless):
        
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless
    def __repr__(self):
        return (f"<Melon: {self.melon_id}, {self.common_name}>")
        """Convenience method to show information about melon in console."""

    def price_str(self):
        return f"${self.price:.2f}"
        """Return price formatted as string $x.xx"""

with open("melons.csv") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        print(row)

melon_dict = {}

with open("melons.csv") as csvfile:
   rows = csv.DictReader(csvfile)

   for row in rows:
      melon_id = row['melon_id']
      melon = Melon(melon_id, row['common_name'], float(row['price']),row['image_url'],row['color'],eval(row['seedless']))
      melon_dict[melon_id] = melon

def get_by_id(melon_id):
    return melon_dict[melon_id]
    """Return a melon, given its ID."""
def get_all():
   return list(melon_dict.values())
   """Return list of melons."""

@app.route("/add_to_cart/<melon_id>")
def add_to_cart(melon_id):

   if 'username' not in session:
      return redirect("/login")

   if 'cart' not in session:
      session['cart'] = {}
   cart = session['cart']

   cart[melon_id] = cart.get(melon_id, 0) + 1
   session.modified = True
   flash(f"Melon {melon_id} successfully added to cart.")
   print(cart)

   return redirect("/cart"
