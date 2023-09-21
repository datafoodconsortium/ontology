# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.8.0] - 2023-02-13

### Added

- Add creators: florenceA, baptisteD
- Add contributors: maximeL, garetheH

**Class**

- PhoneNumber subClassOf What Subject
- SocialMedia subClassOf What Subject

**ObjectProperty**

- hasPhoneNumber: domain Agent, inverse: phoneNumberOf
- phoneNumberOf: domain PhoneNumber, inverse hasPhoneNumber
- hasSocialMedia: domain Agent, inverse: socialMediaOf
- socialMediaOf: domain SocialMedia, inverse: hasSocialMedia

**DataProperty**

- discount: domain (Offer | Order | OrderLine), range: float
- websitePage: domain (Agent | VirtualPlace), range: anyURI
- countryCode: domain PhoneNumber, range: nonNegativeInteger

### Changed

- Domain hasQuantity: (DefinedProduct | Ingredient) -> (DefinedProduct | Ingredient | OrderLine)
- Domain concernedBy: (DefinedProduct | PhysicalProduct) -> (Offer | PhysicalProduct)
- Domain manages: Enterprise -> Agent
- Domain logo: Enterprise -> Agent
- ClassName: Repository -> Catalog
- Domain phoneNumber: Agent -> PhoneNumber
- Range date: date -> dateTime
- Update namespace static.datafoodconsortium.org -> github.com
- Remove link to contributors file

### Removed

- InstagramPage, LinkedinPage, TwitterPage, facebookPage
- Cardiality: stockLimitation


## [1.7.3] - 2022-06-03

### Added

**Class**

- LabellingCharacteristic

**ObjectProperty**

- hasLabellingCharacteristic, domain: DefinedProduct
- hasLabellingDimension, domain: LabellingCharacteristic
- labellingCharacteristicOf, domain: LabellingCharacteristic
- labellingDimensionOf, domain: Dimension

**DataProperty**

- availabilityDate, domain: Stock
- bestBeforeDate, domain: ProductBatch, range: xsd:date


**Changed**

- Domain: date, Stock -> (DFC_BusinessOntology_Relation | DFC_BusinessOntology_Subject)


## [1.7.2] - 2022-06-02

### Added

**Class**

- Ingredient

**Property**

- composedOf, domain: Ingredient, inverseOf: composes
- composes, domain: DefinedProduct, inverseOf: composedOf
- hasIngredient, domain: DefinedProduct, inverseOf: isIngredientOf
- isIngredientOf, domain: Ingredient, inverseOf: hasIngredient

**Changed**

- Domain: DefinedProduct hasQuantity -> (DefinedProduct | Ingredient) hasQuantity 

## [1.7.1] - 2022-05-17

### Added

**Class**

- Price: subpropertyOf QuantitativeValue

**ObjectProperty**

- (Offer | PaymentMethod | Transaction ) hasPrice, inverse of isPriceOf
- Price isPriceOf, inverse of hasPrice

**DataProperty**

- VATrate, domain: Price, range: float
- availabilityTime, domain: SuppliedProduct, range: xsd:duration
- deliveryCondition, domain: SuppliedProduct, range: xsd:string
- extraAvailabilityTime, domain: CatalogItem, range: xsd:duration
- extraDeliveryCondition, domain: CatalogItem, range: xsd:string
- name, domain: DFC_BusinessOntology_Subject, range: xsd:Name

**Changed**

- Domain: VirtualPlace URL -> (DefinedProduct | VirtualPlace) URL

**DataProperty**

- price, domain: (Offer | PaymentMethod | Transaction), range: float

## [1.7.0] - 2022-04-11

- Introduction of facets vocabulary, remove link to ProductGlossary

### Added

**Class**

- Brand: A product can be from an entreprise but an entreprise can manage different brands

**Changed**

- http://static.datafoodconsortium.org/ontologies/DFC_ProductGlossary.owl# -> http://static.- datafoodconsortium.org/ontologies/DFC_BusinessOntology.owl#
- Domain for subproperty of facetOf: http://static.datafoodconsortium.org/ontologies/- DFC_ProductGlossary.owl#{Facet} -> INSTANCE a skos:Concept AND skos:inScheme  http://static.- datafoodconsortium.org/ontologies/DFC_ProductGlossary.owl#{Facet}
- dfc_b:referencedBy inverseOf dfc_b:referencedBy -> dfc_b:referencedBy inverseOf references

**Removed**

- Brand as a Facet

[unreleased]: https://github.com/datafoodconsortium/ontology/compare/v1.8.0...master
[1.8.0]: https://github.com/datafoodconsortium/ontology/compare/v1.7.3...v1.8.0
[1.7.3]: https://github.com/datafoodconsortium/ontology/compare/v1.7.2...v1.7.3
[1.7.2]: https://github.com/datafoodconsortium/ontology/compare/v1.7.1...v1.7.2
[1.7.1]: https://github.com/datafoodconsortium/ontology/compare/v1.7.0...v1.7.1
[1.7.0]: https://github.com/datafoodconsortium/ontology/tree/v1.7.0