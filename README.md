# Welcome to the ontology repo of the DFC project

This is a work in progress. We started on Jan 2017 with a group of local food platforms in France to work together on how we could interoperate our platforms. We have first worked on the "semantic" part of the standard: what are the common business concepts that we all manipulate ? What is the meta model for our business? Is there a way to describe it that encompasses all our specificities ?
Then from September 2018 we started working on the technical specifications of the standard, through the development of a first prototype on the use case of sharing of catalogs between platforms and mutualization of logistics.
Versions regularly change as we iterate, both on the semantic and on the technical documentation, so please see if it covers your distribution use cases, and share feedbacks / suggestions if your use case doesn't fit in it.
We don't talk only about food here, as local food hubs usually sell other products like cosmetics, cleaning products, etc.

The detailed specifications of the standard are presented [in a Gitbook](https://datafoodconsortium.gitbook.io/dfc-standard-documentation/), connected to that same repository.

You'll find in this repo the files **concerning the ontology** :

## Human readable files
### The semantic business and product model
It shows how all the concepts we manipulate as distribution platforms organize together operationnaly in our daily business.

### The concepts definitions
We structured concepts 5 categories, what, who, how, where, when. Definitions are explained here. We need to intergate those definitions in Protégé so that they appears in the machine readable file.

### The concepts properties
- Some properties need more than a label to describe them. We have tried to list a first set of properties that we were using as platforms. This is not exhaustive but we are trying to identify the minimum properties we need for the useful info to flow between platforms, so we may add more when neede. If you need more tell us! We tried also to identify the accurate cardinalities (is this info compulsory? Can we have only one, or more than one?)
- Some properties or rules sometimes don’t need to be in the model but will be more “UI” issues.
For instance, a certification always apply to a product. But a platform might want to offer their users the possibility to set up a property to a producer, so that all products from that producer inherit properties. This doesn’t mean that a producer should have the property associated in the business model. Conceptually, a certification is given for a product, the product is certified, not the producer.

### The business rules
Some concepts are inferred from one another through some deduction / calculation logic. For instance quantities sold on a sale session is the sum of quatities in each order. We have started to list some business rules that we will need to program later on. *The business rules are not yet encoded.*


## Machine readable files
These are the owl and pprj files.
We have two sub models, a business model that reflects what concerns the business, independently from the nature of the product, and , and a product glossary, that reflects what concerns the nature of the products. The full model joins the two sub models, so the one you should use is the full model.

Again, consider all that as a work in progress. We are happy to receive feedback and iterate to try to see which cases are not covered by the ontology we came up with so that we can evolve it !
