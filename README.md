# OT2 - Data Mining Project

Data mining project on keystroke dynamics as part of the Machine Learning course (OT2) at INSA Lyon.

Keystroke dynamics can be used as a soft biometric authentication procedure. The project is about setting up from 
scratch such an authentication procedure and studying if/how it works,what are the main parameters,
what makes a profile, a signature, etc.

The goal is to study different research aspects of keystroke dynamics using a data science approach through data mining
and knowledge discovery.

## Chosen Approach

We had to make several choices regarding the data acquisition, processing, exploration and evaluation. 

We'll sum up our different choices here :
- **Research questions we want to address**
    - To what extent can we identify users only using their keystrokes signature?
    - Has the keyboard layout an influence on the users keystroke profile?
    - What are the most important (i.e discriminant) features extractable from the data?
- **Data acquisition**
    - Keylogger to acquire our own data on a fixed text (pangrams) for the references, and [random texts](https://www.typelit.io/) for the traces to re-identify
- **Methods**
    - Scaled manhattan distance
    - Keyboard image mapping
    - Decision Tree
- **Data evaluation**
    - Accuracy
    - f1-Score
    - log-loss Crossentropy

## Project Structure

Here's the global file structure of our project :
- **/data_visualisation_images**
    - Contains a few images reprensenting our metrics
- **/notebooks**
    - Contains old notebooks we merged in the final report
- **/data**
    - **/training**
        - **/input_data**
            - Contains raw data extracted with our keylogger with ``<name>_<trace_number>.csv`` format
        - **/input_data_merged**
            - Contains raw data merged per user with ``name.csv`` format
        - **/preprocessed_data**
            - Contains merged data per user preprocessed (cleaned, ...) with ``name.csv`` format
        - **/reference**
            - Contains one file per user with statistics for each key with ``name.csv`` format
    - **/test**
        - **/input_data_unknown**
            - Contains raw data extracted with our keylogger with ``<name>_<trace_number>.csv`` format
        - **/preprocessed_data_unknown**
            - Contains data per user preprocessed (cleaned, ...) with ``name.csv`` format
        - **/reference_unknown**
            - Contains one file per user with statistics for each key with ``name.csv`` format


## Bibliography

- [Keystroke Dynamics for User Authentication](https://projet.liris.cnrs.fr/imagine/pub/proceedings/CVPR2012/data/papers/workshops/W13_18.pdf)
- [Utilizing overt and latent linguistic structure to improve keystroke-based authentication](https://www.sciencedirect.com/science/article/abs/pii/S0262885616301019)

## Authors

- [Hugo Degeorges](https://github.com/Belzerion)
- [Benjamin Kermani](https://github.com/b3nker)
- [Andrieu Girard](https://github.com/AndrieuGirard)
- [Johannes Hygrell](https://github.com/Johannes-Hygrell)
