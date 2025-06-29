**LG Display VH 교육, Copyright@2023, LG Display** 1

### **Nội dung chi tiết**
##### **Chương 1 Phân tích dung sai**

       - 2.1. **Sơlượcvềphân tích dung sai** **4**

       - 2.2. **Phân tíchdung sai vềmặtthốngkê** **7**

       - 2.3. **Phân tíchdung sai dạng phi tuyếntính** **22**

       - 2.4. **Táithiết kếvà kiểm duyệt** **30**

**LG Display VH 교육, Copyright@2023, LG Display** 2

## **1. Phân tích dung sai**

Mục tiêu

       Nắm bắt được khái niệm về thiết kế giá trị cho phép (Permitted Deviation).

       Có khả năng thiết kế và phân tích giá trị cho phép (Permitted Deviation.

Nội dung

1. Khái quát

2. Phân tích dung sai về mặt thống kê

3. Phân tích dung sai dạng phi tuyến tính

4. Tái thiết kế và kiểm chứng

**LG Display VH 교육, Copyright@2023, LG Display** 3

**Quy cách và dung sai**

**Quy cách** : Là chỉsốđược quy định vềcác hạng mục kĩ thuật liên quan trực tiếp hoặc gián tiếp tới vật thể, cấu


thành bởi Giá trị tiêu chuẩn (Giá trị danh nghĩa) dung sai

**Giá trị danh nghĩa** : Là trọng tâm của quy cách hay chỉsốđược lấy làm chuẩn vềđặc trưng chất lượng yêu cầu

**Giá trị cho phép** : Là giới hạn cho phép quy định bởi giá trị tiêu chuẩn, phạm vi từ giá trị tiêu chuẩn đến giá trị

giới hạn quy định

**dung sai (Tolerance)** : Có tính chất chất lượng là sự chênh lệch giữa giá trị tối đa và giá trị tối thiểu được xác
~~định~~ ~~bởi~~ ~~tổng~~ ~~độphân~~ ~~tán~~ ~~cho~~ ~~phép~~

※ Tham khảo: Quy cách và dung sai đều là Tolerance.







**LG Display VH 교육, Copyright@2023, LG Display** 4

**Hiểu được mối liên hệvềmặt chức năng giữa các sản phẩm/System cần phát triển và linh kiện/**
**Component cấu tạo nên chúng, qua đó định nghĩa đặc trưng tính chất của sản phẩm và linh kiện**
**theo tiêu chuẩn 6σ**

 Phân tích dung sai (Tolerance Analysis): Chuỗi phương pháp thiết lập giới hạn cho phép về giá trị tiêu chuẩn
(X’s) của linh kiện và các Component để Output của System (Y) có thể đáp ứng nhu cầu của khách hàng

 Phân tích dung sai về mặt thống kê: Phương pháp thống kê thiết lập dung sai của hệ thống căn cứ vào
chỉ số và năng lực công đoạn của nhiều linh kiện cấu thành hệ thống









**LG Display VH 교육, Copyright@2023, LG Display** 5

**Phân tích dung sai về mặt thống kế**

**Thiết kế dung sai phù hợp nhờ vận dụng quy trình và phương pháp phân tích dung sai đúng chuẩn**

**thông qua xem xét mối liên hệ giữa linh kiện cấu thành và hệ thống.**











**LG Display VH 교육, Copyright@2023, LG Display** 6



am:
Loop Diagr Hình vẽ thể hiện bằng biểu đồmối liên hệtuyến tính giữa linh kiện cấu thành hệ

thống và điều kiện bắt buộc vềmặt kỹthuật có thể tìm ở phần phát sinh Gap hoặc nhiễu loạn
(Interference) nào đó.

Hình thức cơ bản


Loop



~~Tiêu~~ ~~chuẩn~~

Envelope (bên phải)

Gap


Envelope (bên trái)

##### Gap W = A – B1 – B2 – B3 – B4


**LG Display VH 교육, Copyright@2023, LG Display** 7

Sơ lược vềVector Loop

  Step1 Vẽcấu tạo khái quát giữa các linh kiện và hệthống.

  Step2 Xác định Gap.

  Step3 Chọn điểm tiêu chuẩn.

  Step4 Thiết lập hướng Vector.

~~▪~~ ~~Step5~~ ~~Phân~~ ~~chia~~ ~~và~~ ~~đánh~~ ~~dấu~~ ~~＋~~ ~~/~~ ~~－~~ .


Biểu thịdấu hiệu cho Vector


Trường hợp biểu thịVector ( ＋ )

 - Chỉsốcàng tăng thì Gap càng tăng

 - Chỉsốcàng tăng thì lượng nhiễu loạn (Interference)
càng giảm

－
Trường hợp biểu thịVector ( )
- Chỉsốcàng tăng thì Gap càng giảm
- Chỉsốcàng tăng thì lượng nhiễu loạn (Interference)
càng tăng





**LG Display VH 교육, Copyright@2023, LG Display** 8

 Step6 Hoàn thiện Loop Diagram và tính Gap.

Loop


~~Tiêu~~ ~~chuẩn~~

Envelope (bên phải)

Gap




Envelope (bên trái)

##### Gap W = A – B1 – B2 – B3 – B4


**LG Display VH 교육, Copyright@2023, LG Display** 9

##### **Phân tích dung sai tuyến tính**

   - Phương pháp phân tích dung sai trong trường hợp công thức hàm sốhiệu năng được xác định

bằng tổng và hiệu của chỉsốgiữa các linh kiện/Component cấu thành

   - Xác định công thức mối liên hệtuyến tính thông qua Loop Diagram

   - Đưa ra độlệch chuẩn nhờ vân dụng Root Sum of square (RSS)

※ Phân loại mối liên hệgiữa các chỉ số của linh kiện/Component thành hai trường hợp là độc

lập tương hỗ(Mutually Independent) và trường hợp còn lại

**LG Display VH 교육, Copyright@2023, LG Display** 10

 Trường hợp các chỉsốcó mối liên hệđộc lập tương hỗ

: là trường hợp các chỉsốcủa các linh kiện/Component riêng lẻkhông ảnh hưởng đến các chỉsốcủa linh kiện khác
Ví dụ: Lắp ráp ngẫu nhiên hai linh kiện được cung cấp bởi hai nhà phân phối đối tác khác nhau

Gap
(Hiệu năng của hệthống - System Performance)


|μ μ μ<br>P1 P2 P3<br>σ σ σ<br>P1 P2 P3|Col2|Col3|Col4|
|---|---|---|---|
|P1|P2|P3|P3|


E

μ E

σ E






**LG Display VH 교육, Copyright@2023, LG Display** 11

[Ví dụ]





- Nếu Gap nhỏhơn 0.0 sẽphát sinh can thiệp (interference) giữa linh kiện 1,2

với linh kiện 3.

Trung bình Gap : μ Gap = μ 3 – μ 1+2 = 80.0 – 79.0 = 1.0mm



Độlệch chuẩn của Gap :


σ Gap = √ σ 3


2 + σ 1


2 + σ 2


2



σ Gap = √ 0.3048 [2] + 0.2032 [2] + 0.1270 [2]

σ Gap = 0.3877

Z gap = (1.0-0) / 0.3877 = 2.58


Khả năng xảy ra nhiễu loạn từ bảng phân phối chuẩn là 0,49%.
(Tỷ lệ nhỏ hơn "0" so với phân phối chuẩn là 0,49%)

**LG Display VH 교육, Copyright@2023, LG Display** 12

 Trường hợp các chỉsốkhông có mối liên hệ độc lập tương hỗ

: là trường hợp các chỉsốcủa các linh kiện/Component riêng lẻgây ảnh hưởng đến các chỉsốcủa linh kiện khác
Ví dụ: Chiều dài và chiều rộng của các linh kiện xuất ra từ cùng một thiết bị đồng nhất

                              - Nếu gọi D là Gap – hiệu năng của hệthống (System
Performance) mà ta cần tìm, thì:

D = A - B - C





Do “A” và “B” là hai chỉ số của cùng một linh kiện nên chúng
có quan hệ tương quan với nhau về lượng. Do đó, chỉsố“A”,
và “B” không được coi là độc lập.
###### ※ Note: σ A − B − C  σ A + σ B + σ C


**LG Display VH 교육, Copyright@2023, LG Display** 13

 Trường hợp các chỉ số không có mối liên hệ độc lập tương hỗ

: là trường hợp các chỉ số của các linh kiện/Component riêng lẻ gây ảnh hưởng đến các chỉ số của linh kiện khác
Ví dụ: Chiều dài và chiều rộng của các linh kiện xuất ra từ cùng một thiết bị đồng nhất

Trong trường hợp không độc lập tương hỗ, có thểtồn tại





hiệp phương sai khác “0” giữa các chỉsốđược xem xét

   x và y trong Cov(x,y) là hiệp phương sai thểhiện

mức độtương hỗ

   -  trong `Cov` `(x,y)` =   σ `X` ,    là hệsốtương hỗ σ `Y`


~~Phương~~ ~~sai~~ ~~và~~ ~~trung~~ ~~bình~~ ~~của~~ ~~tổng~~ ~~tuyến~~ ~~tính~~ ~~giữa~~ ~~các~~ ~~chỉsố~~

**LG Display VH 교육, Copyright@2023, LG Display** 14



[Ví dụ]

~~▪~~ μ 1+2 = μ 1 ~~+~~ μ 2 = ~~1~~ . ~~01~~ ~~+~~ ~~2~~ . ~~10~~ = ~~3~~ . ~~11~~


2 + σ 2


2 + 2σ 12



- σ 1+2


2
= σ 1


μ 1 μ 2

ρ 12 = 0.71


= 0.005 [2] + 0.008 [2] + 2(0.0000284) = 0.0001458

Tại đây,

σ 12 = COV(X 1, X 2 ) = ρ 12 × σ 1 × σ 2

= 0.71 × 0.005 × 0.008

= 0.0000284

∴ σ 1+2 = 0.0121


**LG Display VH 교육, Copyright@2023, LG Display** 15

Các bước phân tích dung sai tuyến tính

Trường hợp mối quan hệ giữa linh kiện và hệthống là dạng tuyến tính, phải hiểu được các bước phân tích dung sai đúng.
※ Trường hợp mối quan hệgiữa các linh kiện có tính phụthuộc vềmặt thống kê, vận dụng RSS đểxem xét hiệp phương sai.

   Step1 Thiết lập và kiểm thảo tiêu chuẩn thiết kế

   Step2 Xác định năng lực công đoạn và thu thập Data liên quan

   - Step3 Soạn Loop Diagram

   Step4 Tính Gap danh nghĩa

   Step5 Vận dụng RSS đểtính độlệch chuẩn của công đoạn ngắn hạn cho Gap đã tính được

   Step6 Vận dụng độlệch chuẩn của Gap đã tính được rồi Tính Z-Value

   Step7 Áp dụng đa dạng các kếhoạch cải tiến, lặp lại các Bước 1- 6 cho tới khi đạt được
tiêu chuẩn 6Sigma

**LG Display VH 교육, Copyright@2023, LG Display** 16

  Step1 Thiết lập và kiểm thảo tiêu chuẩn thiết kế

: Xác định rõ các điều kiện bắt buộc vềkĩ thuật cần phải xửlý và các yêu cầu của khách hàng,
sau đó thiết lập các tiêu chuẩn thiết kếcơ bản.






Target = 0.3 ㎜
USL = 0.55 ㎜

LSL = 0.05 ㎜


|Block1 20㎜ Block4 36㎜ Block3 40㎜ Block2 30㎜|Col2|Col3|Col4|
|---|---|---|---|
|20 30 40 36<br>(±0.1) (±0.07) (＋0.15 (＋0.05<br>－0.1 ) －0.1 )|20 30 40 36<br>(±0.1) (±0.07) (＋0.15 (＋0.05<br>－0.1 ) －0.1 )|20 30 40 36<br>(±0.1) (±0.07) (＋0.15 (＋0.05<br>－0.1 ) －0.1 )|20 30 40 36<br>(±0.1) (±0.07) (＋0.15 (＋0.05<br>－0.1 ) －0.1 )|
|||||


Envelope = 126.4 ㎜ ( ± 0.1)




        - Yêu cầu của khách hàng:
Block (1, 2, 3, 4) trong Envelope không được thay đổi, không có phát sinh các nhiễu loạn với Envelope

        - Yêu cầu vềkỹthuật

㎜
: Thông số kỹ thuật của Gap là (LSL, Target, USL) = (0.05, 0.3, 0.55)

※ Tham khảo bản vẽ các linh kiện tương tự cho giá trị danh nghĩa và dung sai của các linh kiện liên quan được thiết kếmới

**LG Display VH 교육, Copyright@2023, LG Display** 17

  Step2 Xác định năng lực công đoạn và thu thập dữliệu liên quan

: Sử dụng Data của các linh kiện tương tự hoặc đồng nhất đểtính σ có độđóng góp lớn nhất
: Sử dụng dữ liệu lịch sử(historical data) trong trường hợp độđóng góp thấp

※ Không tính σ bằng dung sai hiện tại!!

Điều kiện yêu cầu vềGap; USL = 0.55 ㎜
LSL = 0.05 ㎜

~~Target~~ ~~=~~ ~~0~~ . ~~3~~ ~~㎜~~


Đặc tính của linh kiện;

Block 1

Block 2

Block 3

Block 4

Envelope


Average/Trung bình (μ) Tolerance/dung saiStandard deviation/Độ lệch chuẩn (σ)


20 ㎜

30 ㎜

39.6 ㎜

36 ㎜

126 ㎜

Nhập dữliệu.


± 0.1 ㎜

± 0.07 ㎜

＋ 0.15 / － 0.1 ㎜

＋ 0.05 / － 0.1 ㎜

± 0.1 ㎜


0.0317

0.0259

0.0347

0.0227

0.0513


**LG Display VH 교육, Copyright@2023, LG Display** 18

  Step3 Soạn Loop Diagram




|(-)|(-)|(-)|(-)|Col5|
|---|---|---|---|---|
|1|2|3|4|4|

Step4 Tính Gap danh nghĩa



Gap

Envelope
Bên trái Block 1 Block 2 Block 3 Block 4


Envelope
Bên phải

Gap


㎜
: Gap danh nghĩa = 126 -20 -30 -39.6 -36 = 0.4
##### ∴ μ Gap = 0.4 ㎜

**LG Display VH 교육, Copyright@2023, LG Display** 19

   Step5 Vận dụng RSS đểtính độlệch chuẩn của công đoạn ngắn hạn
cho Gap đã tính được
#### ˆ 2 2 2 2 2 = σ (.00317) + (.00259) + (.00347) + (.00227) + (.00513)

_Gap_

~~=~~ ~~0~~ . ~~0776~~

**LG Display VH 교육, Copyright@2023, LG Display** 20

  Step6 Vận dụng độlệch chuẩn của Gap đã tính được rồi tính Z-Value


- `Z` `USL` = `USL` −  `Gap` = `0.55` − `0.40` = `1.93` và, P USL = 0.0268


`USL` −  `Gap` `0.55` − `0.40`

= = =
σ `0.0776`

```
          Gap
```

=
```
USL

```
```
   .
```

= `1.93`
```
0.0776

```

−
```
      LSL
```

 `Gap`

`Z` =
```
 LSL

```
```
   .
```

= `4.51`
```
0.0776

```

 `Gap` − `LSL` `0.40` − `0.05`

= = =
σ `0.0776`


− −

 `Gap` `.` `.`

= = `4.51` và, P USL = 0.00000329



              - ~~P~~ TOT = ~~(P~~ USL + ~~P~~ LSL ~~)~~ = ~~(0~~ . ~~0268~~ + ~~0~~ . ~~00000329)~~ = ~~0~~ . ~~02680329~~

          - Vận dụng bảng phân phối chuẩn tắc, tính Z-Value cho tổng NG P TOT

: Z-Value = 1.93 → 1.93 Mức Sigma

   Step7 Áp dụng đa dạng các kếhoạch cải tiến, lặp lại các Bước 1-6
cho tới khi đạt được tiêu chuẩn 6Sigma

**LG Display VH 교육, Copyright@2023, LG Display** 21

**Trường hợp mối quan hệ giữa các linh kiện/Component của hệthống không phải dạng**
**tuyến tính, không thểáp dụng giá trị trung bình và độlệch chuẩn được tính theo RSS**

   **Ví dụvềdung sai phi tuyến tính**

    - Dung tích icemaker của máy làm đá= Rate of Fill X Time of Fill

    - Noise [dB(A)] được xác định bằng Log Scale

    - Thiết bịtruyền động Door của VCR bao hàm góc (sin,cos)

→

    - Máy giặt cũ hoạt động bịlệch tâm Hướng di chuyển lệch tâm như sau:

~~Góc~~ ~~thẳng~~ ~~đứng~~ ~~(α0)~~, ~~góc~~ ~~ngang~~ ~~(β0)~~

  **Kết luật mô hình đểphân tích dung sai**

: Kết quả phân tích dung sai là mô hình Gap cho một chỉ số cụ thể.
Vector Loop diagram hữu ích cho các vấn đề dạng tuyến tính, nhưng không áp dụng được cho các vấn đề phi tuyến tính.
.Các cách sau sẽgiúp quyết định mô hình:

     - Vẽ biểu đồ các chức năng liên quan.

     - Phân loại mỗi linh kiện/hệ thống thành các đơn vịnhỏhơn, quyết định dung sai của các đơn vịnhỏtrước
→ Q uyết định dung sai thông qua tổ hợp này

     - Xửlý các trường hợp đặc biệt hoặc trường hợp đơn giản trước, sau đó khái quát hóa chúng.
-Tham khảo các ví dụliên quan/ hoặc tìm kiếm sựhỗtrợtừcác chuyên gia.

**LG Display VH 교육, Copyright@2023, LG Display** 22

**Monte Carlo Simulation**

: MCS là phương pháp xửlý kích thước của các linh kiện/Component được xem xét trong
mô hình Engineering phi tuyến tính không thểgiải quyết được bằng các phương pháp như RSS
thông qua việc tạo ra sốngẫu nhiên bằng máy tính
(※ Sốlượt Simulation phải trên 10,000 lần)

   Sốlần thí nghiệm mô phỏng và độlệch chuẩn được ước tính

Tuy được phân tích rằng không có sựchênh lệch đáng kể(Significant Difference) về phương sai khi sốlần thí nghiệm mô
phỏng thay đổi, tuy nhiên sốlần thí nghiệm mô phỏng càng ít thì càng có khảnăng dẫn đến thiết kếdung sai quá mức.

**LG Display VH 교육, Copyright@2023, LG Display** 23

**Quy trình phân tích dung sai phi tuyến tính**

   **Step1** **Xác định điều kiện cần của Y**

   - **Step2** **Định nghĩa toán học của hàm sốY = f(X’s)**

   **Step3** **Xác định điều kiện của các biến input X**

   - ~~**St**~~ **ep** ~~**4**~~ ~~**Xá**~~ **c** ~~**đị**~~ **n** ~~**h**~~ ~~**th**~~ **am s** ~~**ố**~~ **v** ~~**à**~~ **p** ~~**hâ**~~ **n p** ~~**hối**~~ **c** ~~**ủ**~~ **a c** ~~**á**~~ **c** ~~**X**~~ **r** ~~**iê**~~ **ng** ~~**biệt**~~

   - **Step5** **Tạo ra sốngẫu nhiên (Random Data) của các X riêng biệt**

   - **Step6** **Tính giá trịcủa Y có sửdụng công thức hàm sốở Step 2**

   - **Step7** **Kiểm tra và kiểm thảo kết quảlấy Z-Value làm trọng tâm**

   - **Step8** **Áp dụng đa dạng các kếhoạch cải tiến, lặp lại bước 3-7 cho tới khi đạt tiêu chuẩn 6Sigma**

**LG Display VH 교육, Copyright@2023, LG Display** 24

[Ví dụ]



Standard deviation
Điều kiện của X’s Input Average Distribution

(short-term)

V in -2V 0.316V Chuẩn

R1 20 ㏀ 0.447 ㏀ Chuẩn

R2 100 ㏀ 1 ㏀ Chuẩn

**LG Display VH 교육, Copyright@2023, LG Display** 25

   - **Step5** **Tạo ra sốngẫu nhiên (Random Data) của các X riêng biệt**

**Calc > Random Data > Normal Distribution**

Tên biến X và phân phối giảđịnh
Chỉđịnh giá trịcủa tham số

R2 và Vin cũng tạo ra các sốngẫu nhiên xác suất chuẩn bằng phương pháp tương tự.

**LG Display VH 교육, Copyright@2023, LG Display** 26

   - **Step6** **Tính giá trịcủa Y có sửdụng công thức hàm sốở step 2**

**Calc > Caculator**

**LG Display VH 교육, Copyright@2023, LG Display** 27

   - **Step7** **Xác nhận và kiểm thảo kết quảtập lấy Z-value làm trọng tâm**

             - Z-Value = 0.80

   - **Step8** **Áp dụng đa dạng các kếhoạch cải tiến, lặp lại bước 3-7 cho tới khi đạt tiêu chuẩn 6**
**Sigma**

**LG Display VH 교육, Copyright@2023, LG Display** 28

Ví dụ) Trường hợp đặt linh kiện A và linh kiện B vào trong linh kiện C

Gap




Linh kiện B USL = 10 ㎜ **chuẩn**


Target = 5 ㎜
USL = 10 ㎜

LSL = 0 ㎜



|Linh kiện A Linh kiện B|Col2|
|---|---|
|||


Linh kiện C = 1000 ㎜ ( ± 2)

1) Vận dụng phân tích dung sai tuyến tính

Gap = Linh kiện C – Linh kiện A – Linh kiện B

μ Gap = μ C – μ A – μ B

= 1000 – 395 – 600 = 5
σ Gap = root (3 [2] + 4 [2] + 5 [2] )

= 7.07

Zusl = (10 – 5 ) ÷ 7.07 = 0.707

→ Tỷ lệNG = 23.9%
Zlsl = (5 – 0 ) ÷ 7.07 = 0.707

→ TỷlệNG = 23.9%
Tổng tỷlệNG = 47.8%


|Col1|Trung bình|Độlệch<br>chuẩn|Phân phối|
|---|---|---|---|
|Linh kiện A|395|3|Phân phối<br>chuẩn|
|Linh kiện B|600|4|Phân phối<br>chuẩn|
|Linh kiện C|1000|5|Phân phối<br>chuẩn|


2) Phân tích dung sai phi tuyến tính (số lượng
Data = 10,000) - Tổng tỷ lệ NG = 48.2%


3) Phân tích dung sai phi tuyến tính (số lượng
Data = 10,000) - Tổng tỷ lệ NG = 47.8%


**LG Display VH 교육, Copyright@2023, LG Display** 29

**Tìm kiếm Phương hướng cải tiến năng lực công đoạn của Y bằng phân tích dung sai sau đó tái thiết kế**
**dung sai của linh kiện/ Component của hệ thống**
※ Sau khi tái thiết kế, nhất định phải kiểm duyệt xem liệu năng lực công doạn có thích hợp không, có phản tác dụng không.

 **Phương pháp tái thiết kế**

 **Sửa đổi Nominal của mỗi linh kiện đểgiá trịmục tiêu của Y và trung bình kết quảSimulation được đồng nhất**

   - Khi cải tiến giai đoạn đâu, thửđiều chỉnh giá trịmục tiêu của Y (theo hướng thích hợp)

 **Cải tiến năng lực công đoạn bằng cách điều chỉnh giảm độlệch chuẩn của linh kiện hoặc Assy**

   - Sửa đổi mục tiêu của Process và nghiên cứu tìm kiếm biện pháp đối ứng. (Cải tiến độ chính xác của khuôn, thay đổi phương pháp thực hiện/

dụng cụđo, nâng cao độchính xác của Gage)

 - **Tái thiết kếcấu tạo sản phẩm/hệ** **thống hoặc thực hiện thiết kếbổsung cho các phần cần thiết**

   - Áp dụng và thiết kế Process mới giúp duy trì hiệu suất mong muốn. (Ví dụ) Thay đổi Process lắp ráp/ Thay đổi Bắt vít → Hàn ; Hàn → Quy
trình phát triển tích hợp

 **Xem xét điều chỉnh USL và/hoặc LSL của giới hạn cho phép**


※ Cần nhận thức được rằng việc mởrộng giới hạn cho phép sẽdẫn đến tăng khảnăng phát sinh NG, nên cần phải có quy trình xác nhận chắc
chắn sẽkhông ảnh hưởng đến chất lượng (NG) sản phẩm do mởrộng giới hạn quy cách.

**협력사의** **변경을** **추진**



**Tiến hành thay đổi công ty đối tác.**

 - 동일 작업/부품에 대한 공정 관리가 우수한 협력사로 납품처를 변경



- Thay đổi địa điểm phân phối sang các đối tác có hoạt động quản lý Process sản xuất các linh kiện đồng nhất vượt trội.



   **Kiểm tra kết quả**

     **Trường hợp Z-Value của tính năng đạt kết quảcao, có thểthay đổi giá trị danh nghĩa của linh kiện, trong**

**trường hợp cần thiết có thểcho phép phân tán thêm một chút** .

     **Trường hợp Z-Value của tính năng không đạt được tới giá trịmục tiêu, phải tiến hành tái thiết kế** .

※ Khi tái thiết kế, phải kiểm tra xác định trước những tác động có thểxảy ra với các biến Input khác do các hạng mục bịthay đổi.

**LG Display VH 교육, Copyright@2023, LG Display** 30

Q1. Trong thiết kế, coi Max/Min là +3σ/-3σ và phân tích dung sai. Có nhất thiết phải đo và phản

ánh độ lệch chuẩn của linh kiện đểphân tích được dung sai hay không?

±

    - Thông thường, nếu cho Min/Max sử dụng bằng 3σ, sẽ có khả năng phát sinh chênh lệch lớn trong

trường hợp đo lường Data thực. Vì vậy để có thể phân tích dung sai chính xác hơn, cần phải trực tiếp đo

chỉ số của linh kiện, tức biến sốX.

Q2. Phải phân tích dung sai như thếnào trong trường hợp phân tích dung sai hỗn tạp vừa tuyến

tính vừa phi tuyến tính?

×

  - Ví dụ, nếu Y=1+X1+X2 X3 thì tiến hành X2 và X3 dưới dạng phi tuyến tính, sau đó tiến hành phân tích

×
dung sai giá trịX1 và X2 X3 dưới dạngtuyến tính. Nói cách khác, phép +/- thì thực hiện dưới dạng tuyến

tính, còn các trường hợp còn lại tiến hành phi tuyến tính.

**LG Display VH 교육, Copyright@2023, LG Display** 31

