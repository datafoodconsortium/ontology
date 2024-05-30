# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.13.0] - 2024-05-30
### Added

#### Class
-   Weight, subClassOf: QuantitativeValue.
-   Volume, subClassOf: QuantitativeValue.
-   Length, subClassOf: QuantitativeValue.

#### Property
- holds, domain: SaleSession, inverseOf: belongsTo

### Changed
- Domain : belongsTo, (Order | Agent) -> Order
- Rename: sold -> sells

## [1.12.1] - 2024-02-01
### Added
- file context_1.8.2.json

## [1.12.0] - 2024-02-01
### Added

#### Property
- sold, domain: Agent, inverseOf: soldBy
- soldBy, domain: Order, inverseOf: sold
- hasTransformationType, domain: AsPlannedTransformation, range: skos:Concept and (skos:broader value TransformationType) and (skos:inScheme value DFC_Vocabulary)

## [1.11.1] - 2024-01-29
### Added
- upgrade context.json to add tech ontology object property and owner (required to prototype)
    - dfc-t:represent
    - dfc-t:hasPivot
    - dfc-t:hostedBy
    - dfc:owner

## [1.12.0] - 2024-02-01
### Added

#### Property
- sold, domain: Agent, inverseOf: soldBy
- soldBy, domain: Order, inverseOf: sold
- hasTransformationType, domain: AsPlannedTransformation, range: skos:Concept and (skos:broader value TransformationType) and (skos:inScheme value DFC_Vocabulary)

## [1.11.1] - 2024-01-29
### Added
- upgrade context.json to add tech ontology object property and owner (required to prototype)
    - dfc-t:represent
    - dfc-t:hasPivot
    - dfc-t:hostedBy
    - dfc:owner

## [1.11.0] - 2024-01-11

### Added

#### Property
- region, domain: Address, range: xsd:string

### Changed
- Rename: hasIncome -> hasInput
- Rename: hasOutcome -> hasOutput
- Rename: incomeOf -> inputOf
- Rename: outcomeOf -> outputOf


## [1.10.0] - 2023-12-22

### Added

#### Property
- hasStatus
- hasFulfilmentStatus, domain: Order, range: skos:Concept and (skos:broader value FulfilmentState) and (skos:inScheme value DFC_Vocabulary), subpropertyOf: hasStatus
- hasOrderStatus, domain: Order, range: skos:Concept and (skos:broader value OrderState) and (skos:inScheme value DFC_Vocabulary), subpropertyOf: hasStatus
- hasPaymentStatus, domain: Order, range: skos:Concept and (skos:broader value PaymentState) and (skos:inScheme value DFC_Vocabulary), subpropertyOf: hasStatus

#### Domain
- physicalCharacteristicsOf: PhysicalCharacteristic

#### Range
- stocklimitation: xsd:float
- totalTheoreticalStock: xsd:float

#### Properties characteristics
- inverse property: hasLabellingCharacteristic inverseOf labellingCharacteristicOf

### Changed
- PhysicalProduct: subClassOf (consumedBy only AsRealisedProductionFlow) -> subClassOf (consumedBy only AsRealisedConsumptionFlow)
- Address: subClassOf addressOf only Person and subClassOf addressOf only PhysicalPlace -> subClassOf addressOf only (Person or PhysicalPlace)
- Agent: subClassOf owns only PhysicalProduct -> subClassOf owns only (PhysicalProduct or Brand)
- mainContactOf: subPropertyOf affiliatedBy -> mainContactOf subPropertyOf DFC_BusinessOntology_ObjectProperty
- hasMainContact: subPropertyOf affiliates -> hasMainContact subPropertyOf  DFC_BusinessOntology_ObjectProperty
- Person: mainContactOf only Enterprise -> mainContactOf only (Enterprise or PhysicalPlace)
- Domain: magages, Agent -> Enterprise
- Domain: affiliatedTo, Enterprise -> Agent
- Domain: websitePage, (Agent or VirtualPlace) -> (Agent or VirtualPlace or SocialMedia)
- Rename: affiliatedBy -> affiliatedTo

### Removed

#### Properties characteristics
- symmetry: referencedBy

### Fixed
- upgrade context.json to match ontology
    - replace dfc-b:offeres by dfc-b:offers
    - add dfc-b:offersTo as uri predicate
    - add dfc-b:affiliatedB as uri predicate
    - add dfc-b:orders as uri predicate
    - add dfc-b:orderedBy as uri predicate
    - add dfc-b:hasPart as uri predicate
    - add dfc-b:partOf as uri predicate
    - add dfc-b:belongsTo as uri predicate
    - add dfc-b:selects as uri predicate
    - add dfc-b:concerns as uri predicate
    - add dfc-b:uses as uri predicate
    - add dfc-b:hasOption as uri predicate
    - add dfc-b:hostedAt as uri predicate
    - add dfc-b:lists as uri predicate
    - add dfc-b:listedIn as uri predicate
    - add dfc-b:objectOf as uri predicate
    - add dfc-b:managedBy as uri predicate
    - add dfc-b:coordinatedBy as uri predicate
    - add dfc-b:hasObject as uri predicate
    - add dfc-b:localizedBy as uri predicate
    - add dfc-b:constitutes as uri predicate
    - add dfc-b:identifiedBy as uri predicate
    - add dfc-b:storedIn as uri predicate

## [1.9.0] - 2023-10-05

### Added

#### Class

-   Temperature, subClassOf: QuantitativeValue.

#### ObjectProperty

-   containerInformationOf, domain: skos:Concept and (skos:broader value ContainerInformation) and (skos:inScheme value DFC_ProductGlossary_Facet), subPropertyOf: facetOf, inverseOf: hasContainerInformation.
-   hasContainerInformation, domain: DefinedProduct, subPropertyOf: hasFacet, inverseOf: containterInformationOf.
-   deliveredAt, domain: DeliveryOption.
-   pickedUpAt, domain: PickupOption.
-   hasPaymentMethod, domain: Order, inverseOf: paidWith.
-   paidWith, domain: PaymentMethod, inverseOf: hasPaymentMethod.
-   hasTemperature, domain: SuppliedProduct, inverseOf: hasTemperature.
-   isTemperatureOf, domain: Temperature, inverseOf: hasTemperature.

#### DataProperty

-   minValue, domain: QuantitativeValue, range: float, subPropertyOf: value.
-   maxValue, domain: QuantitativeValue, range: float, subPropertyOf: value.
-   accessibilityInfo, domain: DeliveryOpiton, range: string.
-   deliveryConstraint, domain: DeliveryOption, range: string.
-   frozen, domain: SuppliedProduct, range: boolean.
-   refrigerated, domain: SuppliedProduct, range: boolean.

### Changed

-   Domain hasMainContact: Enterprise -> (Enterprise or PhysicalPlace).
-   Domain hasPhoneNumber: Agent -> (Agent or PhysicalPlace).

### Removed

####

-   Facets classes

#### ObjectProperty

-   refersTo.
-   uses.

## [1.8.0] - 2023-10-03

### Added

-   Add creators: florenceA, baptisteD.
-   Add contributors: maximeL, garetheH.
-   Add .gitignore file.
-   Add the DFC_BusinessOntology.graphml file in the conception folder.

#### Class

-   PhoneNumber subClassOf What Subject.
-   SocialMedia subClassOf What Subject.

#### ObjectProperty

-   hasPhoneNumber: domain Agent, inverse: phoneNumberOf.
-   phoneNumberOf: domain PhoneNumber, inverse: hasPhoneNumber.
-   hasSocialMedia: domain Agent, inverse: socialMediaOf.
-   socialMediaOf: domain SocialMedia, inverse: hasSocialMedia.

#### DataProperty

-   discount: domain (Offer | Order | OrderLine), range: float.
-   websitePage: domain (Agent | VirtualPlace), range: anyURI.
-   countryCode: domain PhoneNumber, range: nonNegativeInteger

### Changed

-   Domain hasQuantity: (DefinedProduct | Ingredient) -> (DefinedProduct | Ingredient | OrderLine).
-   Domain concernedBy: (DefinedProduct | PhysicalProduct) -> (Offer | PhysicalProduct).
-   Domain manages: Enterprise -> Agent.
-   Domain logo: Enterprise -> Agent.
-   ClassName: Repository -> Catalog.
-   Domain phoneNumber: Agent -> PhoneNumber.
-   Range date: date -> dateTime.
-   Replace all links to "static.datafoodconsortium.org" by links to "github.com/datafoodconsortium/.../releases/latest/".
-   Remove link to contributors file.
-   Version number updated to 1.8.0.
-   Last modified date to 2023-02-13.
-   Moved the "context.json" file at the root.

### Removed

-   InstagramPage, LinkedinPage, TwitterPage, facebookPage.
-   Cardiality: stockLimitation.
-   The file `ontologies/catalog-v001.xml` was auto-generated by Protégé.
-   The `businessAPI/` folder has been moved to a [dedicated repository](https://github.com/datafoodconsortium/business-api).
-   The conception PDF files are now released as assets.
-   The `img/` folder contained only the DFC logo wich is hosted [here](https://www.datafoodconsortium.org/wp-content/uploads/2021/04/dfc-logo.png).
-   The `uml/` folder containing the data model has been moved to a [dedicated repository](https://github.com/datafoodconsortium/data-model-uml).
-   The `data/` folder containing taxonomies has been moved to a [dedicated repository](https://github.com/datafoodconsortium/taxonomies).
-   The "static.datafoodconsortium.org" site is replaced by our GitHub home pages so the `CNAME` file and `index.html` are now removed.

## [1.7.3] - 2022-06-03

### Added

#### Class

-   LabellingCharacteristic.

#### ObjectProperty

-   hasLabellingCharacteristic, domain: DefinedProduct.
-   hasLabellingDimension, domain: LabellingCharacteristic.
-   labellingCharacteristicOf, domain: LabellingCharacteristic.
-   labellingDimensionOf, domain: Dimension.

#### DataProperty

-   availabilityDate, domain: Stock.
-   bestBeforeDate, domain: ProductBatch, range: xsd:date.

#### Changed

-   Domain: date, Stock -> (DFC_BusinessOntology_Relation | DFC_BusinessOntology_Subject).

## [1.7.2] - 2022-06-02

### Added

#### Class

-   Ingredient

#### Property

-   composedOf, domain: Ingredient, inverseOf: composes.
-   composes, domain: DefinedProduct, inverseOf: composedOf.
-   hasIngredient, domain: DefinedProduct, inverseOf: isIngredientOf.
-   isIngredientOf, domain: Ingredient, inverseOf: hasIngredient.

### Changed

-   Domain: DefinedProduct hasQuantity -> (DefinedProduct | Ingredient) hasQuantity.

## [1.7.1] - 2022-05-17

### Added

#### Class

-   Price: subpropertyOf QuantitativeValue.

#### ObjectProperty

-   (Offer | PaymentMethod | Transaction ) hasPrice, inverse of isPriceOf.
-   Price isPriceOf, inverse of hasPrice.

#### DataProperty

-   VATrate, domain: Price, range: float.
-   availabilityTime, domain: SuppliedProduct, range: xsd:duration.
-   deliveryCondition, domain: SuppliedProduct, range: xsd:string.
-   extraAvailabilityTime, domain: CatalogItem, range: xsd:duration.
-   extraDeliveryCondition, domain: CatalogItem, range: xsd:string.
-   name, domain: DFC_BusinessOntology_Subject, range: xsd:Name.

#### Changed

-   Domain: VirtualPlace URL -> (DefinedProduct | VirtualPlace) URL.

#### DataProperty

-   price, domain: (Offer | PaymentMethod | Transaction), range: float.

## [1.7.0] - 2022-04-11

-   Introduction of facets vocabulary, remove link to ProductGlossary.

### Added

#### Class

-   Brand: A product can be from an entreprise but an entreprise can manage different brands.

#### Changed

-   http://static.datafoodconsortium.org/ontologies/DFC_ProductGlossary.owl# -> http://static.- datafoodconsortium.org/ontologies/DFC_BusinessOntology.owl#.
-   Domain for subproperty of facetOf: http://static.datafoodconsortium.org/ontologies/- DFC_ProductGlossary.owl#{Facet} -> INSTANCE a skos:Concept AND skos:inScheme http://static.- datafoodconsortium.org/ontologies/DFC_ProductGlossary.owl#{Facet}.
-   dfc_b:referencedBy inverseOf dfc_b:referencedBy -> dfc_b:referencedBy inverseOf references.

#### Removed

-   Brand as a Facet.

[unreleased]: https://github.com/datafoodconsortium/ontology/compare/v1.13.0...master
[1.13.0]: https://github.com/datafoodconsortium/ontology/compare/v1.12.1...1.13.0
[1.12.1]: https://github.com/datafoodconsortium/ontology/compare/v1.12.0...v1.12.1
[1.12.0]: https://github.com/datafoodconsortium/ontology/compare/v1.11.1...v1.12.0
[1.11.1]: https://github.com/datafoodconsortium/ontology/compare/v1.10.1...v1.11.1
[1.9.2]: https://github.com/datafoodconsortium/ontology/compare/v1.9.1...v1.9.2
[1.9.1]: https://github.com/datafoodconsortium/ontology/compare/v1.9.0...v1.9.1
[1.9.0]: https://github.com/datafoodconsortium/ontology/compare/v1.8.0...v1.9.0
[1.8.0]: https://github.com/datafoodconsortium/ontology/compare/v1.7.3...v1.8.0
[1.7.3]: https://github.com/datafoodconsortium/ontology/compare/v1.7.2...v1.7.3
[1.7.2]: https://github.com/datafoodconsortium/ontology/compare/v1.7.1...v1.7.2
[1.7.1]: https://github.com/datafoodconsortium/ontology/compare/v1.7.0...v1.7.1
[1.7.0]: https://github.com/datafoodconsortium/ontology/tree/v1.7.0
