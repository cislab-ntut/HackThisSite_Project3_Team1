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
2.使用hexedit來檢查圖像中的內容<br /><br />
[HXD下載](https://mh-nexus.de/en/downloads.php?product=HxD20)<br /><br />
3.根據提示(2 null bytes)得到我們要找的編碼 <br /><br />
4.根據最低有效位(LSB)我們將16和17轉換為二進制，其中16將為0(偶數)，17將為1(奇數)<br /><br />
5.我們將等於1個字節的每個8位部分劃分為ASCII字符。但是由於二進製字符串的長度為55，因此必須在某處缺少二進製字符串 ” 0 ” 或“ 1”。<br /><br />
6.最後我們得到答案     <br />                                                                
                                                                           0 0 1 1 1 0 0 0 <br />
                                                                           0 1 1 0 0 1 1 0 <br />
                                                                           0 0 1 1 0 1 1 1 <br />
                                                                           0 1 1 0 1 0 0 0 <br />
                                                                           0 1 1 0 0 0 0 1 <br />
                                                                           0 1 1 1 0 0 1 1 <br />
                                                                           0 0 1 1 0 1 1 0 <br />

7.把這組字元串丟進去網站轉換得到 837has6<br />

#1051555 余洪楓
---------------------------------------
#題目: stego mission 3<br />
[題目連結](https://www.hackthissite.org/missions/playit/stego/3)<br />
 ![Image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051555/p1.png)<br />
 
 題目提供了一張灰色的圖片，一個答案輸入框以及確認按鈕。<br />
 判斷資訊隱藏于圖片中後，我決定撰寫一個Python小程式對圖片進行分析。<br />
 ![Image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051555/p2.png)<br />
                    ↓<br />
 ![Image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051555/p3.png)<br />
 使用opencv將圖片以RGB形式讀取，可以看到讀入圖片数据以ndarray形式被儲存起來，共有360*504個pixels<br />
 我查看第一個pixel的RGB值：<br />
 ![Image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051555/p3.png)<br />
 ↓<br />
 ![Image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051555/p4.png)<br />
 發現RGB值均為62，既然圖片藏有資訊，那就可能會有不是62的值，於是用迴圈進行尋找並印出RGB值非全部62的pixel以及找到的pixels總數：<br />
 ![Image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051555/p5.png)<br />
  ↓<br />
 ![Image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051555/p6.png)<br />
 結果顯示有186個非(62,62,62)的pixels。於是我把它們都替換標記為(255,255,255)白色，並重新將ndarray輸出為圖片查看它們所在位置：<br />
 ![Image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051555/p7.png)<br />
  ↓<br />
  ![Image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051555/p8.png)<br />
  一段密文就出現了！<br />
  ![Image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051555/p9.png)<br />
  將密文輸入題目輸入框，按確認按鈕，pass。<br />

#1051335 謝逸德
---------------------------------------
#題目: stego mission 2<br />
[題目連結](https://www.hackthissite.org/missions/playit/stego/2)<br />

1.題目僅有<br /><br />
    did I hear that correctly?<br />
    Thank you tiksi<br /><br />
  和一個詭異的音檔<br />
  ![image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051335/圖片1.png)<br />
2.下載題目的音檔，並使用聲道編輯軟體開啟
  ![image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051335/圖片2.png)<br />
3.選擇新增頻譜圖
  ![image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051335/圖片3.png)<br />
4.發現開出的頻譜圖之中有一字串的模樣
  ![image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051335/圖片4.png)<br />
5.嘗試輸入該字串，即為密碼
  ![image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051335/圖片5.png)<br /> 
  ![image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051335/圖片6.png)<br />
  
  #1051333 李世璽
  -----------------------------------
  #題目: stego mission 4<br />
  
  [題目連結]https://www.hackthissite.org/missions/playit/stego/4<br />

1.題目僅有<br /><br />
   I am being hexed!.<br />
   一個加密過的驗證碼<br />
      ![image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051333/螢幕擷取畫面 (3).png)<br />
2.將驗證碼轉成16進制，並輸入(發現error)<br />
3.另存圖檔，將圖檔在hex編輯器打開<br />
  [HXD下載](https://mh-nexus.de/en/downloads.php?product=HxD20)<br /><br />
4.發現解密過的密碼<br />
      ![image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051333/圖片1.png)<br />
5.將密碼轉成ASCII
      ![image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051333/圖片2.png)<br />
6.輸入密碼(成功)
      ![image](https://github.com/cislab-yzu/Project1-3_Hackthissite/blob/master/1051333/圖片3.png)<br />
