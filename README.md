#1051540 游登翔
---------------------------------------
#題目: stego mission 1
This is an encoded message, the only tip you get is '2 null bytes'
Thank (or blame :P) tiksi for making this challenge
NOTE: There is no encoding error, stop submitting bug reports about it.
[link text](https://www.hackthissite.org/missions/playit/stego/1)

#解法:
1下載我們題目的圖片
2.使用hexedit來檢查圖像中的內容
3.根據提示(2 null bytes)得到我們要找的編碼 
4.根據最低有效位(LSB)我們將16和17轉換為二進制，其中16將為0(偶數)，17將為1(奇數)
5.我們將等於1個字節的每個8位部分劃分為ASCII字符。但是由於二進製字符串的長度為55，因此必須在某處缺少二進製字符串 ” 0 ” 或“ 1”。
6.最後我們得到答案                                                                     
                                                                           0 0 1 1 1 0 0 0 
                                                                           0 1 1 0 0 1 1 0 
                                                                           0 0 1 1 0 1 1 1  
                                                                           0 1 1 0 1 0 0 0  
                                                                           0 1 1 0 0 0 0 1 
                                                                           0 1 1 1 0 0 1 1  
                                                                           0 0 1 1 0 1 1 0

7.把這組字元串丟進去網站轉換得到 837has6



