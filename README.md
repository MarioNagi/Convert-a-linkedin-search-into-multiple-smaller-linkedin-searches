# Convert-a-linkedin-search-into-multiple-smaller-linkedin-searches

This library is created to take a linkedin search query with multiple jobs and converts it into n search query per the number of jobs listed in the original query.

You need to input the excel file name with the links, and the program will output a csv files with all of the output links

converting something like this: 

https://www.linkedin.com/sales/search/people?query=(spellCorrectionEnabled%3Atrue%2CrecentSearchParam%3A(id%3A1545634433%2CdoLogHistory%3Atrue)%2Cfilters%3AList((type%3ACURRENT_TITLE%2Cvalues%3AList((text%3ABiomarkers%2CselectionType%3AINCLUDED%2CcontainsChildren%3Afalse%2CselectedChildren%3AList())%2C(text%3AClinical%2520Biomarkers%2CselectionType%3AINCLUDED%2CcontainsChildren%3Afalse%2CselectedChildren%3AList())%2C(text%3ATranslational%2520Research%2520Medicine%2CselectionType%3AINCLUDED%2CcontainsChildren%3Afalse%2CselectedChildren%3AList())))%2C(type%3AREGION%2Cvalues%3AList((id%3A102095887%2Ctext%3ACalifornia%252C%2520United%2520States%2CselectionType%3AINCLUDED)))%2C(type%3ASENIORITY_LEVEL%2Cvalues%3AList((id%3A6%2Ctext%3ADirector%2CselectionType%3AINCLUDED)%2C(id%3A7%2Ctext%3AVP%2CselectionType%3AINCLUDED)%2C(id%3A8%2Ctext%3ACXO%2CselectionType%3AINCLUDED)%2C(id%3A10%2Ctext%3AOwner%2CselectionType%3AINCLUDED))))%2Ckeywords%3Aimmuno-oncology)&sessionId=nb48EnWYTIGfwV1BOYbI3g%3D%3D&viewAllFilters=true


into the following output:


 
![image](https://user-images.githubusercontent.com/22025520/175935792-62aac9b7-6a65-40de-8ef1-af4061d47af2.png)

