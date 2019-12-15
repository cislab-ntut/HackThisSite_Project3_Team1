#1051540 游登翔
---------------------------------------
#題目: stego mission 1<br />
This is an encoded message, the only tip you get is '2 null bytes'<br />
Thank (or blame :P) tiksi for making this challenge<br />
NOTE: There is no encoding error, stop submitting bug reports about it.<br />
[題目連結](https://www.hackthissite.org/missions/playit/stego/1)<br />

#解法:
1下載我們題目的圖片<br />
![image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051540/1.bmp)<br />
2.使用hexedit來檢查圖像中的內容<br />
[HXD下載](https://mh-nexus.de/en/downloads.php?product=HxD20)<br />
3.根據提示(2 null bytes)得到我們要找的編碼 <br />
4.根據最低有效位(LSB)我們將16和17轉換為二進制，其中16將為0(偶數)，17將為1(奇數)<br />
5.我們將等於1個字節的每個8位部分劃分為ASCII字符。但是由於二進製字符串的長度為55，因此必須在某處缺少二進製字符串 ” 0 ” 或“ 1”。<br />
6.最後我們得到答案     <br />                                                                
                                                                           0 0 1 1 1 0 0 0 <br />
                                                                           0 1 1 0 0 1 1 0 <br />
                                                                           0 0 1 1 0 1 1 1 <br />
                                                                           0 1 1 0 1 0 0 0 <br />
                                                                           0 1 1 0 0 0 0 1 <br />
                                                                           0 1 1 1 0 0 1 1 <br />
                                                                           0 0 1 1 0 1 1 0 <br />

7.把這組字元串丟進去網站轉換得到 837has6



