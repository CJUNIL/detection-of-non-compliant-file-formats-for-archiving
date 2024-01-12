# detection-of-non-compliant-file-formats-for-archiving

[![DOI](https://zenodo.org/badge/742504765.svg)](https://zenodo.org/doi/10.5281/zenodo.10498236)

_Python Assignement for modules 2.6 and 2.7 of the Data Steward 2023/2024 Course (University of Vienna)_

This programme is designed to detect, in a given directory, files whose formats are non-compliant with archiving standards. To do this, the extensions of the files in the directory are compared with a list of recommanded formats for archiving: `archiving_formats.txt`

This list is based on _File formats for archiving_ by ETH Zürich / ETH-Bibliothek, Fachstelle Forschungsdatenmanagement und Datenerhalt (FDD), 2023. https://unlimited.ethz.ch/display/DD/File+formats+for+archiving

Once the comparison has been made, the `printed Summary` shows:
* Number of conform files and their volume (GB)
* Number of non-conform files and their volume (GB)
* List of all non-conform files, alphabetically sorted first by extensions and then by file names

Finally, two `plots` are generated:
* Pie chart: % of compliant files vs % of non-compliant files
* Histogram: main extensions/formats of the non-compliants files
