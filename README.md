These find and replace expressions are ones that I used in Nepali text cleaning in VS code.  
TO use those expressions enable the regular expressions icon (.*) in the find widget. 


![{CD6A94A5-FFB8-4DDF-9EB8-00EC68F03B21}](https://github.com/user-attachments/assets/2756930a-7167-425d-9b93-3685613ba29f)

The regular expressions are as follows
> Nepali numbers

    [०-९]+
> find lines with two '।' 

    .*।.*।.*

> Find entire lines with a  

    ^.*a.*$

> Find lines without characters abc  

    ^(?!.*[abc]).*$

> Find empty lines  

    ^\s*$\n

> Find lines with two words  

    ^\s*\S+\s+\S+\s*$

>Find non nepali characters along with ? ! , ( ) - ' " : /

    [^\u0900-\u097F !\?,":()-/'"]
