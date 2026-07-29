[
  {
    "Windows PowerShell
Copyright (C) Microsoft Corporation. Todos os direitos reservados.

PS C:\Users\12502898> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"pequeno príncipe","autor":"ione","ano":2024}'
Invoke-RestMethod :
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xed in position 21: invalid continuation
byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebExc
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS C:\Users\12502898> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"pequeno principe","autor":"ione","ano":2024}'


ano          : 2024
autor        : ione
data_criacao : 2026-07-29 09:11:54.018946
id           : 4
titulo       : pequeno principe



PS C:\Users\12502898> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Harry Potter e a Pedra Filosofal","autor":"J.K. Rowling","ano":1997}'


ano          : 1997
autor        : J.K. Rowling
data_criacao : 2026-07-29 09:13:10.328439
id           : 5
titulo       : Harry Potter e a Pedra Filosofal



PS C:\Users\12502898> ^C
PS C:\Users\12502898> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Clean Code","autor":"Robert C. Martin","ano":2008}'


ano          : 2008
autor        : Robert C. Martin
data_criacao : 2026-07-29 09:14:29.898489
id           : 6
titulo       : Clean Code



PS C:\Users\12502898> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"O Guia do Mochileiro das Galáxias","autor":"Douglas Adams","ano":1979}'
Invoke-RestMethod :
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xe1 in position 39: invalid continuation
byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebExc
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS C:\Users\12502898> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"O Guia do Mochileiro das Galaxias","autor":"Douglas Adams","ano":1979}'


ano          : 1979
autor        : Douglas Adams
data_criacao : 2026-07-29 09:15:25.548992
id           : 7
titulo       : O Guia do Mochileiro das Galaxias



PS C:\Users\12502898> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Fundacao","autor":"Isaac Asimov","ano":1951}'


ano          : 1951
autor        : Isaac Asimov
data_criacao : 2026-07-29 09:15:58.940029
id           : 8
titulo       : Fundacao



PS C:\Users\12502898> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Fahrenheit 451","autor":"Ray Bradbury","ano":1953}'


ano          : 1953
autor        : Ray Bradbury
data_criacao : 2026-07-29 09:16:34.691038
id           : 9
titulo       : Fahrenheit 451



PS C:\Users\12502898> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body  '{"titulo":"O Iluminado","autor":"Stephen King","ano":1977}'


ano          : 1977
autor        : Stephen King
data_criacao : 2026-07-29 09:17:11.401298
id           : 10
titulo       : O Iluminado



PS C:\Users\12502898> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body   '{"titulo":"O Código Da Vinci","autor":"Dan Brown","ano":2003}'
Invoke-RestMethod :
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xf3 in position 14: invalid continuation
byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebExc
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS C:\Users\12502898> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body   '{"titulo":"O Codigo Da Vinci","autor":"Dan Brown","ano":2003}'


ano          : 2003
autor        : Dan Brown
data_criacao : 2026-07-29 09:17:39.135631
id           : 11
titulo       : O Codigo Da Vinci



PS C:\Users\12502898> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body    '{"titulo":"O Senhor dos Anais","autor":"J.R.R. Tolkien","ano":1954}'


ano          : 1954
autor        : J.R.R. Tolkien
data_criacao : 2026-07-29 09:18:03.936789
id           : 12
titulo       : O Senhor dos Anais



PS C:\Users\12502898>

