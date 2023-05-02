# Composite Geographic Location Scoring Model

## Basic strategy on site selection

**Learn the experience of site selection from your competitors.**

> Hong Kong is a developed city with small area(just a small island and peninsula), almost every ecological niche is taken, so you can't find a new niche without competitors. Thus we have to accept this truth and confront with our competitors. 

We are going to utilize the data of current site of Yoshinoya and other famous fast food brands and also the demographic and social data.

We collected the locations and corresponding demographic and social data of all the restaurants of the following brands:

* Cafe de Coral
- Fairwood

- McDonald's

- KFC

- Yoshinoya

for modelling.

## Modelling

Our model consists of 4 sub-models, each of them evaluates different measurement one should care for location selection.

| Sub model                    | Description                                                                                                                                                                                                                    | Goal                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| Modified Similiarity Score   | Measure the similarity between features of candidates and features of exsited Yoshinoya resturant                                                                                                                              | To evaluate how the candidate match the historical pattern of site selection of yoshinoya.    |
| Potential Return Value Score | Measure the potential return by the potential purchase power of customers and average rent of shop in the candidate location                                                                                                   | To evaluate how much return if we invest and open a new restruant at this candidate location. |
| GeoRecommond Model           | Use the customers rating of Yoshinoya and other fast food brands to build a recommond system, in this scenario, we treat each location or geoblock as a user.                                                                  | To evaluate how customers will rating if we open a new restruant at this candiate location    |
| Logistics Regression         | With the exsited distribution data of  Yoshinoya and other fast food brands and demographic data of each location or geoblock, use Logistics Model to regress the likelihood whether there should be a new fast food resturant | To evaluate the likelihood whether one location should have a new fast food restraunt.        |

We linear combine the output score of each sub-model with weight:

$$
Score=\sum_k\omega_k M_k
$$

where $\omega_k$ is the weight of output of the $k^{th}$ model and $M_k$ is the functor of the $k^{th}$ sub-model.

### GeoRecommand Model

We treat each geoblock as a user in the recommand model named as GeoUser.

Then we can construct a Table from the recommand model like this:

|           | Brand_1 | Brand_2 | Brand_3 | Brand_4 | Brand_5 |
| --------- | ------- | ------- | ------- | ------- | ------- |
| GeoUser 1 | 2/5     |         |         | 3/5     | 4/5     |
| GeoUser 2 | 1/5     | 1/5     | 2/5     |         |         |
| GeoUser 3 |         |         |         | 5/5     | 3/5     |

There are many different recommand algorithm on rating prediction, for simplification, we just the most naive one, since you don't pay us for this work.

### Rating Predictions

Let the $r_{ij}$ be the rating of the $i^{th}$ GeoUser on $j^{th}$ brand.

Then we can predict $r_{ij}$ with the formula:

$$
r_{ij} = \frac{\sum_ks_{ki}r_{kj}}{\sum_ks_{ki}}
$$

where $s_{ki}$ is the similarity between $k^{th}$ GeoUser and $j^{th}$ GeoUser.

For simplification, we can use the cosine similarity 

$$
s_{ij} = \cos(r_{i:},r_{j:})
$$
