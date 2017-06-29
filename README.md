# Welcome to the ontology repo of the DFC project

This is a work in progress. We started 6 months ago with a group of food platforms in France to work together on how we could interoperate our platforms.
We produced for now a v0 version of a business ontology, which we definitely want to iterate on to go further, see if it cover all the cases of local food (but not only!) distribution. We will need than also to extend the ontology and go more into the production and logistics side as well, but that's for later !

For information we are working on a prototype to show how that's gonna work in real life.

So you'll find in this repo 3 files :

## The business concepts definitions
We have worked together on what are the common business concepts that we all share ? What is the meta model for our business? A way to describe it that encompasses all our specificities ?
It is structured around 5 categories, what, who, how, where, when.

## The semantic model
It shows how all those concepts organize together operationnaly in our daily business.
Let's comment it a bit to help you understand :

- the real product (physical product, tangible product) is the product you can touch with your hand, eat, transport. They correspond to certain batches (for example the day the eggs were picked), and they can be stored, either in bulked, or as products already packaged.

- the product reference (intangible product) is a virtual representation of a real product, the entry that you upload on a product catalog on a computer. We need to describe that product in a way which is intuitive and enable various actors then to exchange information around those products.
The product is made of some "base product" to start with, like black cherry tomatoes. This Base Product can be composed of other based products, like a chili con carne (so it can be raw, or prepared, transformed, frozen, etc.). We will detail later own the properties, we are listing them and working on vocabularies at the moment.
Before you can exchange or trade a product, you need to define what quantity of the product you want to sell, so express the unit of measure and a value (like 500g). The unit of measure can be "item" for certain products, like a bunch of radishes.
Then you will add a packaging. "bulk" is considered as a packaging. So if you sell 1kg of black cherry tomatoes without any packaging, the packaging should be "bulk". This form then the "product as it is sold by the producer" or "as sold product". The "as sold product" can be an aggregation of products, like a basket of season vegetables.
So you can describe that way for example 1 jar of 250g of acacia honey, or a pack of 2 jars of acacia honey.
To finish, on the "distributor side" you will propose on your shop a product which represent the need you want to satisfy. For exampe, you may propose a product called "tomatoes to stuff", or just "old varieties of tomatoes". Then you can match this "product on sale" with one or various "as sold products" that answer your need.

- the sales session is a complex concept that is a specific combination of products from the distributor catalog, proposed to specific customers (like some specific clients, businesses or individuals) at a certain price that depends on the customers categories. The session has an open date and can or not have an end date, like a physical shop has no end date, but an order cycle for a food hub does have a limit date until which you can order. And delivery windows (timeslots) and methods (pickup in a pickup point, deliver at home, etc.) All those parameters are defined in the specific context of a given sales session.

- the nature of the transactions depend of the nature of the distributor. If the distributor is a reseller, the transactions are between the producer and the distributor, and then between the distributor and the customer. If the distributor is a sales facilitator, the transaction is directly between the producer and the customer, and there is another transaction between the producer and the distributor for the sales support service.

This is not exhaustive but we hope it helps the understanding !

## The machine readable business ontology
This is the owl file.

Again, consider all that as a work in progress. We are happy to receive feedback and iterate to try to see which cases are not covered by the ontology we came up with so that we can evolve it !
