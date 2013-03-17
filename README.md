# Chinese Movie Reviews Datasets #

Here Contains Chinese Movie Reviews Datasets for All.

## Chinese Yahoo! Movie Reviews ##

- Files: **127K_YMovies_reviews.obj**
- SIZE: **29.6 MB**
- Movie Numbers: **1700**
- Genres: **18**


## Statistic ##
<pre>
Opinion Number in Genre and Ranked
Genres	Rank-1	Rank-2	Rank-3	Rank-4	Rank-5
A       1870    700     979     1433    4137
B       2151    857     1403    2323    9657
C       1116    326     535     934     2769
D       8659    2799    4334    7577    33492
E       315     134     250     481     2798
F       7741    2822    4535    7550    27690
G       148     62      95      217     1654
H       3628    1078    1599    2833    13455
I       4023    1301    1893    2818    8414
J       623     203     316     458     1710
K       3261    712     1019    1454    2734
L       888     306     468     826     4189
M       415     172     291     583     4094
N       647     17      43      51      878
O       160     60      112     182     436
P       405     193     367     779     4534
Q       2097    855     1323    2463    8250
R       6343    1881    2825    4456    11056
</pre>

## Genres ##
A= 奇幻 Fantasy  
B= 科幻 Science Fiction  
C= 犯罪 Crime  
D= 懸疑/驚悚 Mystery/Thriller  
E= 劇情 Drama  
F= 溫馨/家庭 Romance/Family  
G= 動作  Action  
H= 勵志  Inspiring  
I= 愛情  Love Story  
J= 冒險  Adventure  
K= 歷史/傳記 History/Biography  
L= 恐怖  Terror  
M= 戰爭  War  
N= 音樂/歌舞  Music/Dance  
O= 紀錄片  Documentary  
P= 武俠  Martial Arts  
Q= 動畫  Animation  
R= 喜劇  Comedy

## Usage ##

1. use tools/zpickle.py to read files
2. after you zloads(_file_name_), you will get a list contains elements as following: 

``(auth, rank, gens, name_ch, name_en, opnTxt, opnFeats) = opin_list_element``