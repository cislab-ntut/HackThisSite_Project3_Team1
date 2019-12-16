 Hackthissite   Stago Mission 3  1051555 余洪楓<br />
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
  將密文輸入題目輸入框，按確認按鈕，pass。
 
 
 
 

 
