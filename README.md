# Energy Anomaly Detection

Question : Est-il possible de détecter des anomalies dans une série temporelle de consommation électrique automatiquement à partir de modèles de marchine learning ?

## Dataset

Les données sur lesquelles je travaille sont des données préparées par Georges Hebrail et Alice Berard datées entre 2006 et 2010 (DOI : [10.24432/C58K54](https://doi.org/10.24432/C58K54)). 
La base de donnée est composées d'un peu plus de 2 millions de données minutaires et se présente sous la forme suivante :

| Date       | Time     | Global active power (kW) | Global reactive power (kW) | Voltage (V) | Global intensity (A) | Sub metering 1 (W.h) | Sub metering 2 (W.h) | Sub metering 3 (W.h) |
|------------|----------|:------------------------:|:--------------------------:|:-----------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|
| 16/12/2006 | 17:24:00 | 4.216                    | 0.418                      | 234.840     | 18.400               | 0.000                | 1.000                | 17.0                 |
| 16/12/2006 | 17:25:00 | 5.360                    | 0.436                      | 233.630     | 23.000               | 0.000                | 1.000                | 16.0                 |
| 16/12/2006 | 17:26:00 | 5.374                    | 0.498                      | 233.290     | 23.000               | 0.000                | 2.000                | 17.0                 |

### Remarques :
1) La base de donnée contient des valeurs manquantes (environ 1.25%)

2) *global active power * 1000/60 - sub metering 1 - sub metering 2  - sub metering 3* donne la consommation énergétique en Watt heure des appareils électriques non mesurés par les 3 sous-dispositifs. 

## Explorer les données

La première étape consiste à nettoyer les données. Afin de préparer la base de données au traitement qui va suivre, deux étapes nettoyages s'imposent d'eux-même. La première, qui relève plutôt de la bonne pratique que de la nécessité, consiste à fusionner les colonnes `Date` et `Time` et d'indexer la base de données dessus afin de répondre aux standards en matière de *time serie* -- et se simplifier la vie par la suite. La seconde étape est plus critique car elle concerne les données manquantes. Dans cette situation, deux possibilités s'offrent en général : 

1) Supprimer les lignes incomplètes, ce qui revient à introduire un biais dans les données, en particulier au moment d'observer les tendances.

2) Combler les lignes manquantes par interpolation, ce qui revient également à introduire un biais qui dépend du degré de l'interpolation et qui peut manquer une anomalie ou au contraire en prolonger une.

Pour des raisons techniques, je retiens la seconde option.
