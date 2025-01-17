import streamlit as st

def main():
    st.title('Bank Marketing Dataset Information')

    markdown_content = """
    ## Citation Request

    This dataset is publicly available for research. The details are described in Moro et al., 2011. Please include this citation if you plan to use this database:

    ```
    [Moro et al., 2011] S. Moro, R. Laureano and P. Cortez. Using Data Mining for Bank Direct Marketing: An Application of the CRISP-DM Methodology.
    In P. Novais et al. (Eds.), Proceedings of the European Simulation and Modelling Conference - ESM'2011, pp. 117-121, Guimarães, Portugal, October, 2011. EUROSIS.
    ```

    **Available at:**
    - [PDF](http://hdl.handle.net/1822/14838)
    - [BIB](http://www3.dsi.uminho.pt/pcortez/bib/2011-esm-1.txt)

    ### Sources
    Created by Paulo Cortez (Univ. Minho) and Sérgio Moro (ISCTE-IUL) in 2012

    ### Past Usage
    The full dataset was described and analyzed in:
    ```
    S. Moro, R. Laureano and P. Cortez. Using Data Mining for Bank Direct Marketing: An Application of the CRISP-DM Methodology.
    In P. Novais et al. (Eds.), Proceedings of the European Simulation and Modelling Conference - ESM'2011, pp. 117-121, Guimarães,
    Portugal, October, 2011. EUROSIS.
    ```

    ### Relevant Information
    The data is related to direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls, often requiring more than one contact to the same client to assess if the product (bank term deposit) would be subscribed.

    #### Datasets
    1. **bank-full.csv** - Contains all examples, ordered by date (from May 2008 to November 2010).
    2. **bank.csv** - Contains 10% of the examples (4521), randomly selected from bank-full.csv. This smaller dataset is provided to test more computationally demanding machine learning algorithms (e.g., SVM).

    #### Classification Goal
    To predict if the client will subscribe to a term deposit (variable `y`).

    ### Number of Instances
    - **bank-full.csv**: 45211
    - **bank.csv**: 4521

    ### Number of Attributes
    16 input attributes + output attribute.

    ### Attribute Information
    For more detailed information, read [Moro et al., 2011].

    #### Input Variables
    - **Bank Client Data:**
      1. `age` - numeric
      2. `job` - type of job (categorical: "admin.", "unknown", "unemployed", etc.)
      3. `marital` - marital status (categorical: "married", "divorced", "single")
      4. `education` - level of education (categorical: "unknown", "secondary", etc.)
      5. `default` - has credit in default? (binary: "yes", "no")
      6. `balance` - average yearly balance, in euros (numeric)
      7. `housing` - has housing loan? (binary: "yes", "no")
      8. `loan` - has personal loan? (binary: "yes", "no")

    - **Related with the Last Contact of the Current Campaign:**
      9. `contact` - contact communication type (categorical: "unknown", "telephone", "cellular")
      10. `day` - last contact day of the month (numeric)
      11. `month` - last contact month of year (categorical: from "jan" to "dec")
      12. `duration` - last contact duration, in seconds (numeric)

    - **Other Attributes:**
      13. `campaign` - number of contacts performed during this campaign for this client (numeric)
      14. `pdays` - number of days that passed after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)
      15. `previous` - number of contacts performed before this campaign for this client (numeric)
      16. `poutcome` - outcome of the previous marketing campaign (categorical: "

        #### Output Variable (Desired Target)
        17. `y` - has the client subscribed a term deposit? (binary: "yes", "no")

        ### Missing Attribute Values
        None
    """

    st.markdown(markdown_content, unsafe_allow_html=True)

if __name__ == "__main__":
    main()