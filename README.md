These find and replace expressions are ones that I used in Nepali text cleaning in VS code.  
To use these expressions enable the regular expressions icon (.*) in the find widget. 


![{CD6A94A5-FFB8-4DDF-9EB8-00EC68F03B21}](https://github.com/user-attachments/assets/2756930a-7167-425d-9b93-3685613ba29f)

The regular expressions are as follows
> 1. Nepali numbers

    [०-९]+  
> 2. Find lines with two '।' 

    .*।.*।.*  

You can replace '।' with the character that you want to see lines with that character repeating twice.  
> 3. Find entire lines with a  

    ^.*a.*$
You can replace 'a' with the character that you want to find lines with.  
> 4. Find lines without characters abc  

    ^(?!.*[abc]).*$
You can replace the [abc] with the characters that you don't want the lines to contain.  
> 5. Find empty lines  

    ^\s*$\n  

> 6. Find lines with two words  

    ^\s*\S+\s+\S+\s*$  

> 7. Find non nepali characters along with ? ! , ( ) - ' " : /

    [^\u0900-\u097F !\?,":()-/'"]  

I will be adding more expressions that I use here in this readme file.  
Thank you for visiting. 😊
