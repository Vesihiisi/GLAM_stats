# GLAM_stats
Python script to grab [glamorous](https://tools.wmflabs.org/glamtools/glamorous.php) stats for selected categories in Wikimedia Commons.

Saves result as json, wikitable and markdown files (like this one):

| institution | files | used | % used |
|---|---|---|---|
| [Riksantikvarieämbetet](https://commons.wikimedia.org/wiki/Category:Images_from_the_Swedish_National_Heritage_Board) | 185636 | 2247 | 1.21 |
| [Livrustkammaren, Skoklosters slott och Hallwylska museet](https://commons.wikimedia.org/wiki/Category:Images_from_Livrustkammaren_och_Skoklosters_slott_med_Stiftelsen_Hallwylska_museet) | 46332 | 1760 | 3.8 |
| [Nationalmuseum](https://commons.wikimedia.org/wiki/Category:Images_from_the_Nationalmuseum_Stockholm) | 5401 | 4609 | 85.34 |
| [Musikverket](https://commons.wikimedia.org/wiki/Category:Images_from_the_Swedish_Performing_Arts_Agency) | 4554 | 68 | 1.49 |
| [Nordiska museet](https://commons.wikimedia.org/wiki/Category:Images_from_Nordiska_museet) | 2900 | 531 | 18.31 |
| [Kungliga Biblioteket](https://commons.wikimedia.org/wiki/Category:Images_from_the_National_Library_of_Sweden) | 2525 | 27 | 1.07 |
| [Statens museer för världskultur](https://commons.wikimedia.org/wiki/Category:Media_from_the_National_Museums_of_World_Culture) | 1908 | 98 | 5.14 |
| [Statens maritima museer](https://commons.wikimedia.org/wiki/Category:Images_from_Statens_maritima_museer) | 1003 | 225 | 22.43 |
| [Tekniska museet](https://commons.wikimedia.org/wiki/Category:Images_from_Tekniska_museet) | 987 | 160 | 16.21 |
| [Riksarkivet](https://commons.wikimedia.org/wiki/Category:Images_from_the_National_Archives_of_Sweden) | 677 | 84 | 12.41 |
| [Work With Sounds (Arbetets museum)](https://commons.wikimedia.org/wiki/Category:Media_from_Work_With_Sounds) | 652 | 43 | 6.6 |
| [Spårvägsmuseet](https://commons.wikimedia.org/wiki/Category:Images_from_Spårvägsmuseet) | 247 | 59 | 23.89 |
| [Regionarkivet](https://commons.wikimedia.org/wiki/Category:Images_from_Regionarkivet) | 74 | 24 | 32.43 |
| [Brunnsmuseet](https://commons.wikimedia.org/wiki/Category:Media_provided_by_Brunnsmuseet) | 50 | 7 | 14.0 |
| [Internetmuseum](https://commons.wikimedia.org/wiki/Category:Images_from_Internetmuseum) | 40 | 9 | 22.5 |
| [Riksutställningar](https://commons.wikimedia.org/wiki/Category:Images_from_Riksutställningar) | 37 | 0 | 0.0 |
| [Stockholms stadsarkiv](https://commons.wikimedia.org/wiki/Category:Images_by_Stockholms_stadsarkiv) | 7 | 4 | 57.14 |
| [Stockholms stadsmuseum](https://commons.wikimedia.org/wiki/Category:Images_from_Stockholms_stadsmuseum) | 2 | 1 | 50.0 |

## Installation

Requirements: datetime, lxml, argparse, json, requests

## Usage

You need a json file with the categories you want to analyze. See `se_config.json` for what it needs to look like. Then you pass it to the script:

```bash
$ python3 glam_stats.py --config se_config.json
```

## Acknowledgments
* Based on [Swedish-GLAMwiki-stats](https://github.com/Ambrosiani/Swedish-GLAMwiki-stats) by [Aron Ambrosiani](https://github.com/Ambrosiani)
* Spiritual support by [this cat's upper teethsies](https://commons.wikimedia.org/wiki/File:Cat_teeth.jpg). Have you ever *really* looked at a cat's upper teethsies?