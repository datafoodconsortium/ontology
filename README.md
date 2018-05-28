# Welcome to the ontology repo of the DFC project

This is a work in progress. We started on Jan 2016 with a group of local food platforms in France to work together on how we could interoperate our platforms. Our actual work has been mainly on "semantic": on what are the common business concepts that we all manipulate ? What is the meta model for our business? Is there a way to describe it that encompasses all our specificities ?
Here is the v.1 version of our business ontology and product glossary. We will keep on iterating, so please see if it covers your distribution use cases, and share feedbacks / suggestions if your use case doesn't fit in it.
We don't talk only about food here, as local food hubs usually sell other products like cosmetics, cleaning products, etc.
We are working on a prototype to show how that's gonna work in real life.


You'll find in this repo the following files :

## Human readable files
### The semantic business and product model
It shows how all the concepts we manipulate as distribution platforms organize together operationnaly in our daily business.
Let's comment it a bit to help you understand :

**Products:**
- We have identified the different concepts of products we manipulate. As described [in this blogpost from November](http://datafoodconsortium.org/blog/product-ontologies-how-business-invariants-apply-also-to-the-food-system) we distinguished the product “need” (what I want as a customer), from the product “answer” (what I propose as a distributor to satisfy your need), from the product “supply” (what I propose as a producer that enable distributors to meet their promises to customers), all those products being manipulated without any “location” notion. 
- Then a producer identifes a location where their products are supposed to be when they become real product. We call them “localized products”, which is a combination between an ID product (what product it is) and an ID place (where it is). For instance, the potatoes of “Awesome farm” are in theory localized in the farm itself.
- When the potatoes get harvested they become “physical products”, real products that you can hold in your hand. A physical product is also always located somewhere, and belongs to a product batch.
- The product batch carry the information regarding production date and expiry date, as those info are what define a product batch (products that have same production characteristics).
- Theoretical stocks are implicit, through the "quantity" properties on all products as well as on "orders" and "sale sessions". *We will need to discover the business rules behind them to link them all together. Also, we know we are missing some "real stock" concept to be able to capture gaps when some real stock counts are made.*

**Transformation (including transportation):**
- Some products are “composed products”, they are made of other products, processed in some way to make a new product, like a tomato sauce for instance. There is a theoretical transformation that plans a transformation process without any notion of where the products are located, the “recipe” that connects products with one another independently from where they could be. For instance as an artisan cookies maker I can tell that I put 100g flour, 20g chocolate, 2 eggs, etc. in my cookies. In that case I express the recipe in term of “functional products”, I need flour and chocolate. I can be more precise and tell which type exactly of flour and chocolate I use and talk more in term of “technical products”, like wheat flour T110. And I can even tell exactly the flour from which farmer I used in my recipe, so express the recipe in terms of other “supplied products”. The “unit” is always defined at the product level so only quantities need to be specified. This is what we call the “as planned transformation flow”.
- Then this recipe becomes something more like a “production workflow” that adds some notion of location. I have to move the tomato from “Awesome farm” to “TheKitchen”, the onions from “The Other Farm” to “TheKitchen”, etc. When all my components are in "TheKitchen" I can start the production process, cook, mix, bottle, etc. And get some jar of tomato sauce as output, which are located in “TheKitchen”. But this is still only a plan, a production map, I still don’t have the products, I’m just organizing and planning the operations. We realized when iterating that transforming the nature of a localized product was exactly the same flow as transforming the place where this product is supposed to be located. As the localized product is a combination of an ID product and an ID place, one flow was transforming the ID product, the other the ID place. So we are treating transportation as a specific transformation flow. Input will be for instance 100 x potatoes 1kg located in “Awesome Farm” and output will be 100 x potatoes 1kg located in “The Great Town Shop”.
- Then when physical products are concerned this flow becomes a “realized transformation flow”.

**Sale session:**
- A sale session aggregates some “offers” that an enterprise makes and that are specific to customer categories. The product offered can be, depending on the sales and marketing strategy of the distributor, a functional product (ex: tomatoes to stuff), a technical product (ex: beefsteak tomatoes) or a supplied product (ex: beefsteak tomatoes from Awesome Farm).
- The customer makes an order with various order lines in a specific sales session and choose a shipping option - that can be delivery (they are delivered to their home or business address) or pick-up (they need to collect the product in a location defined by the distributor) - and a payment option among those defined by the distributor.
- The sale happens in a place that can be physical (a physical store) or virtual (an online store). Note that this works as well for a physical store: technically each day the store opens and close at a define time, and each day can be considered as a specific sale session. In the case of physical store sales, the shipping option is implicitly “collect on site”.

**Transactions:**
- When an agent has ordered products and products has been delivered through a last transformation flow (transport), the ownership of the product changes hands. The transaction is then officially happening and the previous product owner can invoice the customer.

**Agents**
- For now we have only covered simple relationships between individuals and enterprises: a person can "manage" or "be the main contact" for an enterprise. We know that we might need to go further in the futur with a ternary relation with some "role" concept in between (a person will play a role in an enterprise).

This is not exhaustive but we hope it helps the understanding !

### The concepts definitions
We structured concepts 5 categories, what, who, how, where, when. Definitions are explained here. We need to intergate those definitions in Protégé so that they appears in the machine readable file.

### The concepts properties
Some properties need more than a label to describe them. We have tried to list a first set of properties that we were using as platforms. This is not exhaustive but we are trying to identify the minimum properties we need for the useful info to flow between platforms, so we may add more when neede. If you need more tell us! We tried also to identify the accurate cardinalities (is this info compulsory? Can we have only one, or more than one?)

### The business rules
Some concepts are inferred from one another through some deduction / calculation logic. For instance quantities sold on a sale session is the sum of quatities in each order. We have started to list some business rules that we will need to program later on. *The business rules are not yet encoded.*


## Machine readable files
These are the owl and pprj files.
We have two sub models, and one full model that join the two sub model, so the one you should use is the full model.
We want to review the modularization, this is just a first step.

### Business ontology
It reflects basically what we have said above in a machine readable version.

### Product glossary
- We studies different option for product glossaries/thesaurus. Our challenge is to make sure we can identify uniquely products from one platform to another so that information regarding this product flow without friction. As each platform has its own way of describing products, and its own logic, we choose to adopt a “facet approach” with the following facets: "nature origin" (If the product has a unique “living/mineral” source, what is the source? For instance a steak has as source a living cow from a specific breed.), "part origin" (If the product has a unique “living/mineral” source, what part or product of this source is used? For instance honey comes from a unique living source which is a bee from a specific breed. The part of product of source concerned here is “honey”. If we talk about a carrot, the source will be the carrot variety, and the part concerned will be “the root”.), "processes" (Every product sold will have gone through some sort of processes, at a minimum a tomato has been “harvested” from the living tomato plant.), "geographical origin", "certifications" (labels)
- A product is also identify with a dimension and unit, like potatoes are sold by 1 x kg, a jar of tomato sauce is sold by 1 x item, the item here being a “jar of 500 ml tomato sauce”.
- We also choose to keep a "product type" classification to be able to give more flexibility in the use of the ongology, especially for composed products for which we don't have the decomposition. But this will need to be thought more deeply. This tablel is much more "sales oriented", the idea is to know if we talk about a carrot or a chili con carne.
- Product glossaries are not yet filled in with the content tables, we need to find a way to connect with the relevant table when there is an external relevant one, and define our strategy when it doesn't exist. *This remains to be done.*

### Full model
- For now we have added in the full model some properties concerning products that we don't know if they would need some complex glossary or not (physical characteristics, claims, brand). We might evolve that in the futur and move those properties as "facets" in the product glossary.


Again, consider all that as a work in progress. We are happy to receive feedback and iterate to try to see which cases are not covered by the ontology we came up with so that we can evolve it !
