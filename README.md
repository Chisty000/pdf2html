# PDF to HTML Converter
## Introduction
As a writer myself I wanted to build something that will convert pdf to html. Now even though there are content management softwares such as wordpress they are for heavy websites with a lot of infrastructure. In order to build a plain simple website I can use simple web hosting like 300 mb hostings are enough for me. Now I can fit wordpress into it however, it comes with a requirement of additional database service purchase. Which is often time not required for simple writers. Now we can use Word’s direct html converter but the styling is pretty basic. We can get a template thats a lot of repeated work. Additionally we can use google sheets thats again problematic repeated manual work. Hence I decided to do it programmatically. 

As a programmer myself I went and searched for libraries. I found out pdftohtmllex but it is available for linux only. I am a windows user. Hence I decided to code my own system. 
So I build a python program that does it. Here is how,
## Steps
3 easy steps


**Now open the Pdf processor** 
**Giving your pdf**
In the 44th line you will see something like 
`pdf_processor = PdfProcessor("Afghan Refugee Crisis.pdf")`
Here replace the Afghan Refugee Crisis.pdf with your_pdf_name.pdf
And run the program it will generate a output txt file. This file contains all of your materials in Text format and you will see a images in your folder if there are any images inside your pdf. 
**Now open the html_generator  and run it. It will generate the HTML file.** 

## Further Improvements
If you need to provide images there just use the following piece of code
Outside the p tag and inside the article tag

```<div class="image-container"><img src=”yourImage.jpg/png/whatever image extension" alt="Wrapped Image"></div>```

Development work Pending for version two (Do it if you are interested):
The link_detector file contains a monstrous regex. You have to run it to get all the links in an array. You have to scan the generated html file and replace the links with a tags to make it clickable. 
Scan html then replace(the strings with the link string)
Wrap it like below
`<a href=”{link}”>{link}</a>`


