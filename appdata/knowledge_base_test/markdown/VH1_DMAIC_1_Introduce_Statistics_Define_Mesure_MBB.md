Biz Innoavtion / Big Six Sigma Team

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**

**Contents**

     **Introduction**

**1.** **Define**

~~**2**~~ **.** ~~**M**~~ **easure**

**3.** **Analyze**

**4.** **Improve**

**5.** **Control**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
~~1~~

**1. Khái niệm cơ bản**

**2. Lý thuyết cơ bản về phân tích dữ liệu**

**3. Kiểm định giả thuyết thống kê**

**4. Phương pháp luận**

**Trước khi bắt đầu**

**Sigma**



**Là 1 chữ thường trong bảng chữ cái Hy Lạp,**

**mô tả độ lệch chuẩn của tổng thể.**

~~•~~
~~**Là**~~ ~~**một**~~ ~~**chỉ**~~ ~~**số**~~ ~~**chất**~~ ~~**lượng**~~ ~~**thống**~~ ~~**kê**~~ ~~**đại**~~ ~~**diện**~~ ~~**cho**~~


**được bao gồm Spec.**


**năng lực quy trình, biểu thị bằng độ lệch chuẩn (σ)**


**Mức Sigma**



**- Mức Sigma (σ level)**,

Các chỉ số chât lượng như năng suất, tỷ lệ lỗi, DPU(defects per unit),

PPM(parts per million), DPMO, xác suất thất bại/ lỗi ...

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
3

**Trước khi bắt đầu**

    Giá trị thống kê thể hiện mức chất lượng hiện tại đáp ứng bao nhiêu yêu cầu của khách hàng.

    Được thể hiện bằng số lượng độ lệch chuẩn phù hợp từ giá trị trung tâm đến yêu cầu của khách
hàng (Spec).
→ Kết hợp với xác suất phân phối chuẩn, từ đó dự đoán xác suất sai lệch so với yêu cầu của khách
hàng.


**Mức Sigma**


Giá trị trung tâm và yêu cầu của

khách hàng cách nhau 3σ, gọi là 3



|Col1|Col2|Col3|Yêu cầu của khách hà<br>Độ lệch chuẩn (σ)<br>= 2<br>σ σ σ|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||


**6** **8** **10** **12** **14** **16** **18**

평균 (μ) = 10

                              - **Lỗi/ Khiếm khuyết** (Defects)

: Sản phẩm/ Dịch vụ/ Quy trình không được khách hàng chấp nhận

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
4

**Trước khi bắt đầu**

**σ** **Level** **DPMO** **[1)]** 1) DPMO : Defects Per Million Opportunities

**<As was>**


**1** **158,665**

**2** **22,750**

**3** **1** **350**

**4** **31.7**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
5


**691,462**

**308,537**

**66,807**

**6,210**

**233**

**3.4**

**Trước khi bắt đầu**


**①** **Sản xuất : cải tiến phân phối CTQ thông qua tối ưu hóa quy trình**









**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
6

#### **1. Khái niệm cơ bản**

**1.1. Chọn mẫu**

**1.2. Loại hình dữ liệu và thang đo**

**1.3. Phân phối xác suất**

**1.4. Phân phối chọn mẫu**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
7

**Thông thường, mẫu được lấy ra từ một phần của tổng thể, từ đó suy luận đặc điểm của tổng thể.**
**Tham số** (parameter) **là giá trị biểu thị đặc tính của tổng thể,**
**Lượng thống kê** (statistic) **là giá trị biểu thị đặc tính của mẫu.**


Tham số: đặc tính của tổng

thể

(Trung bình tổng thểμ, độ

lệch chuẩn tổng thểσ)


**Tổng thể**
**Mẫu**


2. Phân tích dữ liệu

Lượng thống kê : đặc tính của mẫu

(Trung bình mẫu ത𝑋, độ lệch chuẩn mẫu S)



|Phân loại|Trung bình<br>tổng thể|Trung bình mẫu|Kết quả|
|---|---|---|---|
|Chọn mẫu 1st|100|101|Không có sựkhác biệt giữa TB tổng thểvà TB mẫu|
|Chọn mẫu 2nd|100|200|Có sựkhác biệt giữa TB mẫu và TB tổng thể|


→ Khi Chọn mẫu lần thứ 2, tại sao có sự khác biệt khi ước lượng trung bình tổng thể với trung bình mẫu?

※ Thông thường rất khó để xác định và biết được Trung bình mẫu, trong giáo trình, người ta đặt giả thuyết rằng đã biết TB tổng thể để giải thích về sai số .

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
8

**Sai số được chia thành sai số chọn mẫu và sai số phi chọn mẫu, trong sai số chọn mẫu, có thể**
**giảm sai số ngẫu nhiên bằng cách chọn mẫu đúng.**

**1) Sai số chọn mẫu: sai số xuất hiện do suy luận đặc tính của toàn bộ tổng thể thông qua dữ liệu từ mẫu**
**là một phần của tổng thể.**

    **Sai số ngẫu nhiên (random error)**
    - Xảy ra ngẫu nhiên do các yếu tố không thể kiểm soát.
**→ Giảm sai số bằng cách tăng kích thước mẫu ngẫu nhiên (sample size)**

    **Độ lệch (bias)**

      Xảy ra do mẫu không được chọn ngẫu nhiên.

     - Dù số lượng dữ liệu lớn cũng không thể giảm sai số. Mất niềm tin vào kết quả lệch.
**→Việc lựa chọn phương pháp chọn mẫu rất quan trọng.**

**2) Sai số phi chọn mẫu : là sai số còn lại sau khi loại trừ sai số chọn mẫu, sai số đo lường chủ yếu do**
**phương pháp quan sát (đo lường) không chính xác.**



**Bảng câu hỏi**

**Phương pháp đo lường**

**không chính xác**

**Nhập dữ liệu**

**Khác**


: câu hỏi dẫn dắt (dự kiến câu trả lời), thuật ngữ chuyên môn, thuật ngữ thể hiện tần
suất, cấu trúc bảng câu hỏi, thứ tự câu hỏi…
: điều kiện làm tròn, xóa dữ liệu dưới hoặc trên một giá trị nào đó …

: lỗi ghi chép, truyền đạt dữ liệu chưa chính xác, Typing Error…

: Câu trả lời không đúng trọng tâm câu hỏi…


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
9

**Có thể ra quyết định mang tính thống kê với một mẫu nhỏ không? Kích thước mẫu nên là bao nhiêu?**
 - Kích thước mẫu phụ thuộc vào **kích thước tổng thể** và mức độ đại diện cho tổng thể của mẫu được lấy ra.

 - Tăng kích thước mẫu có thể cải thiện độ chính xác nhưng lại làm tăng chi phí. Kích thước mẫu lớn không phải khi nào cũng
là tốt.

 **Trước tiên phải xác định/ dư đoán sự phân tán của tổng thể** → nếu phân tán của tổng thể nhỏ, có thể giảm kích thước mẫu
một cách đáng kể.

→ **Có thể đưa ra quyết định mang tính thống kê với một kích thước mẫu nhỏ nếu phương sai tổng thể (σ** **[2]** **) đủ nhỏ.**

※ Giả sử trong trường hợp không có sự phân tán, quyết điịnh có thể đưa ra dù chỉ với 1 samle.

→ Có thể đưa ra quyết định mang tính thống kê với số lượng mẫu tối thiểu nếu các mẫu mô phỏng (Mock-up) trong gia đoạn phát

~~triển~~ ~~được~~ ~~sản~~ ~~xuất~~ ~~dựa~~ ~~trên~~ ~~nhiều~~ ~~giá~~ ~~trị~~ ~~trung~~ ~~tâm.~~

Ngược lại, nếu kích thước mẫu quá nhỏ so với kích thước phân tán của tổng thể, xác suất đưa ra quyết định đúng là rất thấp.

Giả sử phân phối chuẩn,
công thức tính kích thước mẫu

**2**

_**n**_ **=**

_n_ = kích thước mẫu
_**s**_ **= ước lượng độ lệch chuẩn của tổng thể**
_e_ = sai số cho phép
1.96 = 95% hằng số khoảng tin cậy
1-β = 검정력 (power)


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
10

**Phương pháp chọn mẫu để loại bỏ bias:**
**①** **Chọn mẫu ngẫu nhiên đơn thuần,** **②** **Chọn mẫu hệ thống,**
**③** **Chọn mẫu ngẫu nhiên phân tầng,** **④** **Chọn mẫu theo cụm**

**1. Chọn mẫu ngẫu nhiên đơn thuần (simple random sampling)**

      Việc lựa chọn các mẫu riêng lẻ từ một tổng thể một cách tình cờ để chúng có xác suất được chọn như

nhau.

      Được sử dụng khi tổng thể thống nhất.

**2. Chọn mẫu hệ thống (systematic sampling)**

      Trường hợp tổng thẻ được chọn mẫu quá lớn để thực hiện phương pháp chọn mẫu ngẫu nhiên đơn thuần thông

qua bảng số ngẫu nhiên, một phương pháp chọn mẫu theo các khoảng thời gian đều đặn, giả định rằng thành

phần của tổng thể là ngẫu nhiên.

**3. Chọn mẫu ngẫu nhiên phân tầng (stratified random sampling)**

      Khi một tổng thể bao gồm các phần tửu không đồng nhất, một phương pháp phân chia chúng thành các nhóm

đồng nhất không chồng chéo (tầng) và ở mỗi tầng chọn, mẫu bằng cách thực hiện lấy mẫu ngẫu nhiên đơn

thuần.
**4. Chọn mẫu theo cụm (cluster sampling)**

      Một phương pháp trong đó một tổng thể bao gồm một nhóm đồng nhất kết hợp với nhau, sao cho một nhóm

(cụm, cluster) cụ thể được chọn và kiểm tra tất cả chúng, hoặc một số phần tử nhất định được chọn ngẫu nhiên từ

nhóm được chọn.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
11

|F1|F2|F3|F4|F5|F6|F7|M1|M2|M3|M4|M5|M6|M7|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E8|E9|EA|EB|EC|ED|EE|L8|L9|LA|LB|LC|LD|LE|
|E1|E2|E3|E4|E5|E6|E7|L1|L2|L3|L4|L5|L6|L7|
|D1|D2|D3|D4|D5|D6|D7|K1|K2|K3|K4|K5|K6|K7|
|C8|C9|CA|CB|CC|CD|CE|J8|J9|JA|JB|JC|JD|JE|
|C1|C2|C3|C4|C5|C6|C7|J1|J2|J3|J4|J5|J6|J7|
|B1|B2|B3|B4|B5|B6|B7|H1|H2|H3|H4|H5|H6|H7|
|A8|A9|AA|AB|AC|AD|AE|G8|G9|GA|GB|GC|GD|GE|
|A1|A2|A3|A4|A5|A6|A7|G1|G2|G3|G4|G5|G6|G7|

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|R|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|F1|F2|F3|F4|F5|F6|F7|M1|M2|M3|M4|M5|M6|R<br>M7|
|E8|E9|EA|EB|EC|ED|EE|L8|L9|LA|LB|LC|LD|LER|
|E1|E2|E3|E4|E5|E6|E7|L1|L2|L3|L4|L5|L6|L7<br>R|
|D1|D2|D3|D4|D5|D6|D7|K1|K2|K3|K4|K5|K6|K7|
|C8|C9|CA|CB|CC|CD|CE|J8|J9|JA|JB|JC|JD|JE|
|C1|C2|C3|C4|C5|C6|C7|J1|J2|J3|J4|J5|J6|J7|
|B1|B2|B3|B4|B5|B6|B7|H1|H2|H3|H4|H5|H6|H7|
|A8|A9|AA|AB|AC|AD|AE|G8|G9|GA|GB|GC|GD|GE|
|A1|A2|A3|A4|A5|A6|A7|G1|G2|G3|G4|G5|G6|G7|






|F1|F2|F3|F4|F5|F6|F7|M1|M2|M3|M4|M5|M6|M7|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E8|E9|EA|EB|EC|ED|EE|L8|L9|LA|LB|LC|LD|LE|
|E1|E2|E3|E4|E5|E6|E7|L1|L2|L3|L4|L5|L6|L7|
|D1|D2|D3|D4|D5|D6|D7|K1|K2|K3|K4|K5|K6|K7|
|C8|C9|CA|CB|CC|CD|CE|J8|J9|JA|JB|JC|JD|JE|
|C1|C2|C3|C4|C5|C6|C7|J1|J2|J3|J4|J5|J6|J7|
|B1|B2|B3|B4|B5|B6|B7|H1|H2|H3|H4|H5|H6|H7|
|A8|A9|AA|AB|AC|AD|AE|G8|G9|GA|GB|GC|GD|GE|
|A1|A2|A3|A4|A5|A6|A7|G1|G2|G3|G4|G5|G6|G7|

|Col1|Col2|Col3|F1|Col5|F2|Col7|F3|Col9|F4|Col11|F5|Col13|F6|Col15|F7|Col17|M1|Col19|M2|Col21|M3|Col23|M4|Col25|TMổ5n|Col27|gM t6h|Col29|ểM/ 71|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||F1|F1||||||||||||||||||||||||||||
||F1|F1|F2|F2|F3|F3|F4|F4|F5|F5|F6|F6|F7|F7|M1|M1|M2|M2|M3|M3|M4|M4|M5|M5|M6|M6|M7<br>LD|M7<br>LD|LE|
|F|||E|8|E|9|E|A|E|B|E|C|E|D|E|E|L|8|L|9|L|A|L|B|L|C|L|L|L|
|F|1<br>E|F<br>8|2|F|3|F|4|F|5|F|6|F|7|M|1|M|2|M|3|M|4|M|5|M|6|M|7|||
|F|1<br>E|F<br>8|E<br>E|9<br>1|E<br>E|A<br>2|E<br>E|B<br>3|E<br>E|C<br>4|E<br>E|D<br>5|E<br>E|E<br>6|L<br>E|8<br>7|L<br>L|9<br>1|L<br>L|A<br>2|L<br>L|B<br>3|L<br>L|C<br>4|L<br>L|D<br>5|L<br>L|E<br>6|L7|
|E|8<br>E|E<br>1|9<br>E|E<br>2|A<br>E|E<br>3|B<br>E|E<br>4|C<br>E|E<br>5|D<br>E|E<br>6|E<br>E|L<br>7|8<br>L|L<br>1|9<br>L|L<br>2|A<br>L|L<br>3|B<br>L|L<br>4|C<br>L|L<br>5|D<br>L|L<br>6|E<br>L|7|7|
|E|1|E|D<br>2|1<br>E|D<br>3|2<br>E|D<br>4|3<br>E|D<br>5|4<br>E|D<br>6|5<br>E|D<br>7|6<br>L|D<br>1|7<br>L|K<br>2|1<br>L|K<br>3|2<br>L|K<br>4|3<br>L|K<br>5|4<br>L|K<br>6|5<br>L|K<br>7|6|K7|
|D|D|1|D<br>C|2<br>8|D<br>C|3<br>9|D<br>C|4<br>A|D<br>C|5<br>B|D<br>C|6<br>C|D<br>C|7<br>D|K<br>C|1<br>E|K<br>J|2<br>8|K<br>J|3<br>9|K<br>J|4<br>A|K<br>J|5<br>B|K<br>J|6<br>C|K<br>J|7<br>D|JE|
|D|1<br>C|D<br>8|2|D|3|D|4|D|5|D|6|D|7|K|1|K|2|K|3|K|4|K|5|K|6|K|7|||
|D|1<br>C|D<br>8|C|9|C|A|C|B|C|C|C|D|C|E|J|8|J|9|J|A|J|B|J|C|J|D|J|E<br>6|J7|
|C|||C|1|C|2|C|3|C|4|C|5|C|6|C|7|J|1|J|2|J|3|J|4|J|5|J|J|J|
|C|8<br>C|C<br>1|9|C|A|C|B|C|C|C|D|C|E|J|8|J|9|J|A|J|B|J|C|J|D|J|E|||
|C|8<br>C|C<br>1|C|2|C|3|C|4|C|5|C|6|C|7|J|1|J|2|J|3|J|4|J|5|J|6|J|7<br>6|H7|
|C|||B|1|B|2|B|3|B|4|B|5|B|6|B|7|H|1|H|2|H|3|H|4|H|5|H|H|H|
|C|1<br>B|C<br>1|2|C|3|C|4|C|5|C|6|C|7|J|1|J|2|J|3|J|4|J|5|J|6|J|7|||
|C|1<br>B|C<br>1|B|2|B|3|B|4|B|5|B|6|B|7|H|1|H|2|H|3|H|4|H|5|H|6|H|7<br>D|GE|
|B|||A|8|A|9|A|A|A|B|A|C|A|D|A|E|G|8|G|9|G|A|G|B|G|C|G|G|G|
|B|1<br>A|B<br>8|2|B|3|B|4|B|5|B|6|B|7|H|1|H|2|H|3|H|4|H|5|H|6|H|7|||
|B|1<br>A|B<br>8|A|9|A|A|A|B|A|C|A|D|A|E|G|8|G|9|G|A|G|B|G|C|G|D|G|E<br>6|G7|
|A|||A|1|A|2|A|3|A|4|A|5|A|6|A|7|G|1|G|2|G|3|G|4|G|5|G|G|G|
|A|8<br>A|A<br>1|9|A|A|A|B|A|C|A|D|A|E|G|8|G|9|G|A|G|B|G|C|G|D|G|E|||
|A|8<br>A|A<br>1|A|2|A|3|A|4|A|5|A|6|A|7|G|1|G|2|G|3|G|4|G|5|G|6|G|7|7|
|A1||||||||||||||||||||||||||||||
|A1||A2|A2|A3|A3|A4|A4|A5|A5|A6|A6|A7|A7|G1|G1|G2|G2|G3|G3|G4|G4|G5|G5|G6|G6|G7|G7|G7|G7|

|Chọn mẫu ngẫu nhiên đơn thuần (<br>simple random sampling)|Chọn mẫu ngẫu nhiên phân tầng<br>(stratified random sampling)|
|---|---|
|Chọn mẫu ngẫu nhiên đơn thuần<br>Random<br>F1 F2 F3 F4 F5 F6 F7 M1 M2 M3 M4 M5 M6 M7<br>E8 E9 EA EB EC ED EE L8 L9 LA LB LC LD LE<br>E1 E2 E3 E4 E5 E6 E7 L1 L2 L3 L4 L5 L6 L7 F2 L9 D5 …<br>D1 D2 D3 D4 D5 D6 D7 K1 K2 K3 K4 K5 K6 K7<br>C8 C9 CA CB CC CD CE J8 J9 JA JB JC JD JE<br>C1 C2 C3 C4 C5 C6 C7 J1 J2 J3 J4 J5 J6 J7<br>B1 B2 B3 B4 B5 B6 B7 H1 H2 H3 H4 H5 H6 H7<br>A8 A9 AA AB AC AD AE G8 G9 GA GB GC GD GE<br>A1 A2 A3 A4 A5 A6 A7 G1 G2 G3 G4 G5 G6 G7|Chọn mẫu ngẫu nhiên phân tầng<br>Random<br>F1 F2 F3 F4 F5 F6 F7 M1 M2 M3 M4 M5 M6 M7<br>Group 1 2 3<br>E8 E9 EA EB EC ED EE L8 L9 LA LB LC LD LERandom …<br>F7 M6 E8<br>E1 E2 E3 E4 E5 E6 E7 L1 L2 L3 L4 L5 L6 L7<br>Random<br>D1 D2 D3 D4 D5 D6 D7 K1 K2 K3 K4 K5 K6 K7<br>C8 C9 CA CB CC CD CE J8 J9 JA JB JC JD JE<br>C1 C2 C3 C4 C5 C6 C7 J1 J2 J3 J4 J5 J6 J7<br>B1 B2 B3 B4 B5 B6 B7 H1 H2 H3 H4 H5 H6 H7<br>A8 A9 AA AB AC AD AE G8 G9 GA GB GC GD GE<br>A1 A2 A3 A4 A5 A6 A7 G1 G2 G3 G4 G5 G6 G7|
|Chọn mẫu hệ thống<br>(systematic sampling)|Chọn mẫu theo cụm<br>(cluster sampling)|
|Chọn mẫu hệ thống<br>Cách 5 cái<br>F1 F2 F3 F4 F5 F6 F7 M1 M2 M3 M4 M5 M6 M7<br>E8 E9 EA EB EC ED EE L8 L9 LA LB LC LD LE<br>E1 E2 E3 E4 E5 E6 E7 L1 L2 L3 L4 L5 L6 L7 F3 M1 M6 …<br>D1 D2 D3 D4 D5 D6 D7 K1 K2 K3 K4 K5 K6 K7<br>C8 C9 CA CB CC CD CE J8 J9 JA JB JC JD JE<br>C1 C2 C3 C4 C5 C6 C7 J1 J2 J3 J4 J5 J6 J7<br>B1 B2 B3 B4 B5 B6 B7 H1 H2 H3 H4 H5 H6 H7<br>A8 A9 AA AB AC AD AE G8 G9 GA GB GC GD GE<br>A1 A2 A3 A4 A5 A6 A7 G1 G2 G3 G4 G5 G6 G7|Chọn mẫu theo cụ<br>F1 F2 F3 F4 F5 F6 F7 M1 M2 M3 M4 TMổ5n gM t6h ểM/ 71 phần<br>F1 F2 F3 F4 F5 F6 F7 M1 M2 M3 M4 M5 M6 M7<br>E8 E9 EA EB EC ED EE L8 L9 LA LB LC LD LE<br>F1 F2 F3 F4 F5 F6 F7 M1 M2 M3 M4 M5 M6 M7<br>E8 E9 EA EB EC ED EE L8 L9 LA LB LC LD LE<br>E1 E2 E3 E4 E5 E6 E7 L1 L2 L3 L4 L5 L6 L7<br>E8 E1E 9 E2E A E3E B EE 4 C EE 5 D E6E E E7L 8 L1L 9 L2L A L3L B L4L C L5L D L6L E L7 F1 ~ G7<br>D1 D2 D3 D4 D5 D6 D7 K1 K2 K3 K4 K5 K6 K7<br>E1 E2 E3 E4 E5 E6 E7 L1 L2 L3 L4 L5 L6 L7<br>D1 D2 D3 D4 D5 D6 D7 K1 K2 K3 K4 K5 K6 K7<br>C8 C9 CA CB CC CD CE J8 J9 JA JB JC JD JE<br>D1 D2 D3 D4 D5 D6 D7 K1 K2 K3 K4 K5 K6 K7<br>C8 C9 CA CB CC CD CE J8 J9 JA JB JC JD JE<br>C1 C2 C3 C4 C5 C6 C7 J1 J2 J3 J4 J5 J6 J7<br>C8 C9 CA CB CC CD CE J8 J9 JA JB JC JD JE<br>C1 C2 C3 C4 C5 C6 C7 J1 J2 J3 J4 J5 J6 J7<br>B1 B2 B3 B4 B5 B6 B7 H1 H2 H3 H4 H5 H6 H7<br>C1 C2 C3 C4 C5 C6 C7 J1 J2 J3 J4 J5 J6 J7<br>B1 B2 B3 B4 B5 B6 B7 H1 H2 H3 H4 H5 H6 H7<br>A8 A9 AA AB AC AD AE G8 G9 GA GB GC GD GE<br>B1 B2 B3 B4 B5 B6 B7 H1 H2 H3 H4 H5 H6 H7<br>A8 A9 AA AB AC AD AE G8 G9 GA GB GC GD GE<br>A1 A2 A3 A4 A5 A6 A7 G1 G2 G3 G4 G5 G6 G7<br>A8 A9 AA AB AC AD AE G8 G9 GA GB GC GD GE<br>A1 A2 A3 A4 A5 A6 A7 G1 G2 G3 G4 G5 G6 G7<br>A1 A2 A3 A4 A5 A6 A7 G1 G2 G3 G4 G5 G6 G7|


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
12

**Làm thế nào để đo lường?**




**Dữ liệu rời rạc**

 Gía trị đặc trưng thu được bằng cách
đếm số lượng dữ liệu đo được.

 Không thể phân tách dữ liệu

예 ) Số SP lỗi, số defect, số người đỗ,...

※ Dữ liệu liên tục được chuyển thành
dữ liệu rời rạc bằng cách phân loại.

Dữ liệu rời rạc không thể chuyển

thành dữ liệu liên tục.








**Dữ liệu liên tục**

Dữ liệu định lượng được đo một

cách liên tục.

Có thể phân tách dữ liệu và kích
thước của số đo có ý nghĩa.

예 ) Chiều dài, cân nặng, diện tích,
thể tích, dung lượng,...



Thời gian, dài rộng...
4m gấp 2 lần 2m. 1inch = 2.54cm


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
13

   **Thang đo danh nghĩa (nominal scale)**

**Thang đo để phân loại các đối tượng có cùng đặc điểm nhằm mục đích phân loaị chúng theo các**
**đặc điểm riêng biệt của chúng.**

      - Dữ liệu đơn giản phân loại : Không thể cho biết thứ tự hoặc sự khác

biệt [ (Nam+Nữ) / 2 = ? ]

Ex: Màu sắc, Nam/nữ, Vật liệu1/2/3

~~▪~~ ~~**Thang**~~ ~~**đo**~~ ~~**thứ**~~ ~~**bậc**~~ ~~**(ordinal**~~ ~~**scale)**~~

**Thang đo phân loại theo đặc tính đối tượng đo lường, theo thứ hạng hoặc độ lớn.**

      - Có thể nói về mức độ thứ tự nhưng không thể xác định sự khác biệt.

Ex: Khảo sát mức độ hài lòng 5đ/7đ, mức độ lỗi vết ố

         - △△△△△△△         - △△△△△△△

Vết ố thẳng đứng

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
14

   **Thang đo khoảng(interval scale)**

**Một thang đo trong đó các giá trị số được đưa ra trong các khoảng cách bằng nhau theo mức độ**
**định lượng của thuộc tính đối tượng đó.**

예 ) Nhiệt độ, chỉ số chứng khoán, Z Value,...

   **Thang đo tỷ lệ(ratio scale)**

**Một thang đo giống như thang đo khoảng và có thể tính gốc tọa độ tuyệt đối và tỷ lệ.**

       - Thời gian, chiều dài, khối lượng... tồn tại điểm gốc ‘0’.

Ex: 4m gấp 2 lần 2m. 1inch = 2.54cm

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
15

 **Quan hệ giữa dữ liệu liên tục và dữ liệu rời rạc**

   - Dữ liệu liên tục chứa nhiều thông tin hơn dữ liệu rời rạc.
: Thang đo tỷ lệ→ có thể biến đổi thành thang đo thứ bậc, thang đo danh nghĩa.

   - Để có được thông tin có ý nghĩa bằng cách sử dụng dữ liệu rời rạc, cần có nhiều dữ liệu hơn so với dữ

liệu liên tục.

※ Photo CD Spec : 2.0um ± 0.1um


**Photo CD**
**(Thang đo tỷ lệ)**



**Level lỗi**

**(Thang đo thứ bậc)**


Photo CD : data 100 cái

Tỷ lệ NG : data 1 cái

|Col1|Col2|※ Photo C|
|---|---|---|
|1.70um 1.85um 1.90um 1.95um 2.05um<br>Level 5 Level 4 Level 3 Level 2 Level 1 Level<br>ậc)|1.70um 1.85um 1.90um 1.95um 2.05um<br>Level 5 Level 4 Level 3 Level 2 Level 1 Level<br>ậc)|2.10um 2.15um 2.30um<br>2 Level 3 Level 4 Level 5|


**HàngOK/NG**

**(Thang đo danh nghĩa)**


NG OK NG


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
16

   **Phân phối xác suất (probability distribution)?**

**: Tất cả những sự kiện xảy ra đều có thể được biểu thị dưới dạng xác suất theo quan điểm toán hoc**,
Phân phối xác suất thể hiện **xác suất của những sự kiện có thể xảy ra dưới dạng phân phối.**

    **Biểu thị dưới dạng bảng, đồ thị, hàm số,... về các giá trị mà một biến ngẫu nhiên có thể lấy và**
**xác suất để lấy giá trị đó.**
    - Biến ngẫu nhiên là một số được gán cho từng biến cố cấu thành không gian mẫu.






P(
X)

1/6



1     2     3     4     5     6

       
|Sốxúc xắc<br>(Xác suất biến cố X)|Xác suất<br>(P(X))|Sốxúc xắc<br>(Xác suất biến cốX)|Xác suất<br>(P(X))|
|---|---|---|---|
|1|1/6|4|1/6|
|2|1/6|5|1/6|
|3|1/6|6|1/6|

**Mục đích**

         **Phản ánh cấu trúc tổng thể từ các mẫu**

         **Tính xác suất của sự kiện quan tâm**

**→ Xác suất lỗi/khuyết điểm, xác suất giả thuyết sai.**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
17

**1) Phân phối xác suất rời rạc**

     **Phân phối các biến ngẫu nhiên với các giá trị có thể đếm được.**

Ex: Số mặt ngửa khi tung đồng xu.

       - Phân phối nhị thức : Số SP lỗi khi mẫu (n cái) được chọn ngẫu nhiên từ một tổng thể vô hạn với tỷ lệ lỗi là P.

      - Phân phối Poisson : Được dùng khi muón biết số lần xuất hiện của một biến cố trong đơn vị thời gian hoặc

không gian

**2) Phân ph** ~~**ố**~~ **i xác su** ~~**ấ**~~ **t liên tục**

      Phân phối các biến ngẫu nhiên với các giá trị của thuộc tính mang tính liên tục..

Ex: Thu nhập trung bình hàng năm của mỗi hộ gia đình, cân nặng, chiều cao...

        - Phân phối chuẩn : Là phân phối hình chuông lấy đối xứng qua

đường trung bình.

        - Phân phối chuẩn tắc (Phân phối Z) : Mean =0, độ lệch chuẩn=1.

        - Ngoài ra còn có phân phối t, phân phối F.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
18

*Thử nghiệm Bernoulli : một thử nghiệm chỉ xảy ra 1 trong 2 sự kiên (Pass/Fail)

 **Phân phối nhị thức (binomial distribution) : B(n, p)**

   - Phân phối nhị thức là phân phối xác suất rời rạc, trong đó n phép thử độc lập liên tiếp, mỗi phép thử
có xác suất n.

   - Đặc trưng : số phế phẩm trong một đơn vị mẫu (n) được lấy ra từ một tổng thể (vô hạn) với tỷ lệ phế
phẩm cụ thể (p).

   - Tham số của phân phối : tỷ lệ lỗi (p), kích thước mẫu (n)

   - Trung bình : np, phương sai = np(1-p)


**※ Khi n = 10, p = 0.1, 0.5, 0.9**


**Xác suất**

0.4

0.3

0.2

0.1


**n = 10, p = 0.1**


☞
Khi tăng số phép thử (n), phân phối nhị thức tiến tới đối xứng.
→ np ≥ 5 và n(1-p) ≥5, xấp xỉ phân phối chuẩn.

**n = 10, p = 0.5** **Xác suất** **n = 10, p = 0.9**

0.4

0.3

0.2

0.1

0.0

0 2 4 6 8 10 5 6 7 8 9 10 11
**Số cái** **Số cái**


0.0
0 1 2 3 4 5

**Số cái**


**확률**

0.25

0.20

0.15

0.10

0.05

0.00


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
19

※ Điểm xấp xỉ Poisson của phân phối nhị thức

: trong phân phối nhị thức, khi n lớn và p rất

 - **Phân phối Poisson(poisson distribution),** **Poi(λ)** bé.thì nó giống với phân phối Poisson.
(Tại đó, gỉa sử np = λ)

   - Phân phối xác suất rời rạc thể hiện số lần một sự kiện sẽ xảy ra trong một đơn vị nhất định (thời
gian, diện tích, độ dài).

   - Thuộc tính : Tần suất của một lỗi cụ thể xảy ra trong một đơn vị nhát định.

   - Tham số của phân phối : Số lỗi trung bình trên một đơn vị (λ)

   - Mean : λ, Phương sai = λ


**Xác suất** **λ = 1**

0.4

0.3

0.2

0.1

0.0
0 1 2 3 4 5 6

**Số cái**


**λ = 5**

**Xác suất**

0.20

0.15

0.10

0.05

0.00
0 2 4 6 8 10 12 14

**Số cái**


**λ = 10**

**Xác suất**

0.12

0.08

0.04

0.00
0 5 10 15 20

**Số cái**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
20

**Ví dụ: Tính xác suất dữ liệu rời rạc (Phân phối nhị thức)**



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
21

**Cal > Probability distribution > binomial distribution**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
22


**Cal > Probability distribution > binomial distribution**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
23


**Cal > Probability distribution > binomial distribution**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
24


**Cal > Probability distribution > poisson distribution**





**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
25

   **Có thể được biết được trước khi cải tiến và sau**
**khi cải tiến thông qua so sánh các phân phối.**

         - **Xác suất Zero Defect** **: 0.00001%**

         **Mức độ quản lí (≤5) Xác suất thỏa mãn :**

**0.155%**

         - **Xác suất Zero Defect** **: 1.76%**

         - **Mức độ quản lí (≤5) Xác suất thỏa mãn : 78.7%**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
26


**Trước cải tiến**

**Sau cải tiến**

**Ví dụ: Tính toán xác suất dữ liệu rời rạc (Phân phối Poisson)**



**Cal > Probability distribution > poisson distribution**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
27

**Ví dụ: Tính toán xác suất dữ liệu rời rạc (Phân phối Poisson)**



**Cal > Probability distribution > poisson distribution**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
28


① Trước tiên, tìm xác suất nhỏ hơn

② Xác suất lớn hơn 15

1 - P( X ≤ 14) =

1 - 0.916542 = 0.083458

➔ 8.35%

 **Phân phối xác suất liên tục ?**

  - Là một phân phối có thể liên tục nhận giá trị xác suất tại mọi điểm thuộc một khoảng nào đó.

  - Giá trị xác suất mà biến ngẫu nhiên liên tục X lấy từ a đến b là diện tích từ a đến b như trong hình bên dưới

**- Mối quan tâm chính : Năng lực quá trình**


+∞


𝒃


**Đặc điểm**


**①** **f(x) ≥ 0** **②** 𝒇𝒙𝒅𝒙 **= 1** **③** **P(a ≤ x ≤ b) =**

න −∞ න


**②** 𝒇𝒙𝒅𝒙 **= 1** **③** 𝒇𝒙𝒅𝒙 ( 단, - ∞ ≤ a ≤ b ≤ + ∞)


𝒇𝒙𝒅𝒙 **= 1** **③** **P(a ≤ x ≤ b) =** 𝒇𝒙𝒅𝒙

න න


−∞


𝒂


**f(x)**

**P(a ≤ x ≤ b**

~~**)**~~
**a** **b**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
29


**x**

 **Phân phối chuẩn (normal distribution), N(μ, σ** **[2]** **)**

    - Đặc điểm : Giá trị đo lường liên tục với đồ thị hình chuông đối xứng hai bên.

**- Tham số của phân phối : Trung bình (μ), Phương sai (σ** **[2]** **)**

99.9999998%

99.999943%

~~99.9937%~~

99.73%

95.45%

68.27%

Độ lệch chuẩn

(σ)


μ-6σ μ-5σ μ-4σ μ-3σ μ-2σ μ-1σ **Mean(μ)** μ+1σ μ+2σ μ+3σ μ+4σ μ+5σ μ+6σ


μ-3σ μ-2σ μ-1σ **Mean(μ)** μ+1σ μ+2σ μ+3σ


**Mean(μ)**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
30

 **Phân phối chuẩn và phân phối chuẩn tắc**

    **Phân phối chuẩn tắc là gì? Giá trị (X) của Phân phối chuẩn được chuyển thành giá trị Z, phân phối chuẩn với**
**Mean=0 và phương sai=1.**

    **Lý do sử dụng phân phối chuẩn tắc?**

     - Hữu ích trong việc so sánh tương đối dữ liệu được thu thập từ các phân phối khác nhau về đơn vị đo lường hoặc khác
nhau giữa trung bình và phương sai.


|Col1|N(μ, σ2)|Col3|
|---|---|---|
||||


μ-3σ μ-2σ μ-1σ **Mean(μ)** [μ+1σ] μ+2σ μ+3σ


**x**

**z**


※ ý nghĩa của Z-Value


|Z-Value<br>uẩn cách giá trị<br>bao nhiêu lần?<br>Phân phối chuẩn tắc|Col2|Col3|Col4|
|---|---|---|---|
|Z-Value<br>uẩn cách giá trị<br>bao nhiêu lần?<br>Phân phối chuẩn tắc||||


-3 -2 -1 **0** 1 2 3

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
31

 **Z-Value và Phân phối chuẩn tắc**

Nếu áp dụng bảng phân phối chuẩn tắc, có thể tính toán được Z-Value thông qua xác suất, hoặc
ngược lại.

➢ **Áp dụng bảng phân phối chuẩn tắc:**

      - Được sử dụng làm bảng để tính toán xác suất khi sử dụng **Z-Value** (phần tô màu ở đồ thị bên dưới)

      - Được sử dụng làm bảng để lấy Z-Value bằng các sử dụng xác suất. Trục X là Z-Value, Trục Y là

giá trị xác suất.

Phân phối chuẩn tắc


(Mean 0, Phương sai 1)


N (0, 1 [2] )


Z
-4 -3 -2 -1 0 1 2 3 4

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
32

**Ví dụ: Điểm thi lần thứ 2 cao hơn so với lần thứu nhất.**

**Điểm của bạn có thực sự cải thiện so với bài kiểm tra trước không?**

Anh N.V.A đã làm bài thi thử môn toán 2 lần và nhận được kết quả như sau.

Phân phối điểm của tất cả những người tham gia tuân thủ theo phân phối chuẩn và giá trị trung bình và

độ lệch chuẩn của mỗi bài kiểm tra như sau:

     - Test 1 : 65đ(Trung bình: 50đ, độ lệch chuẩn: 10đ)

     - Test 2 : 75đ(Trung bình: 70đ, độ lệch chuẩn: 20đ)

Anh N.V.A đã làm tốt bài kiểm tra nào?

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
33

**Ví dụ: Điểm thi lần thứ 2 cao hơn so với lần thứ nhất.**

**Điểm của bạn có thực sự cải thiện so với bài kiểm tra trước không?**

    - Test 1 : 65đ (Trung bình: 50đ, độ lệch chuẩn: 10đ)

    - Test 2 : 75đ (Trung bình: 70đ, độ lệch chuẩn: 20đ)

**①** **Nếu chỉ đánh giá bằng điểm, lần thứ 2 đạt kết quả tốt hơn lần 1.**
**②** **Trường hợp áp dụng chuẩn tắc,**


_X_ −  65 − 50

~~=~~ ~~=~~ ~~=~~
 10


_X_ −  65 − 50 _X_ −  75 − 70
~~_Z_~~ ~~=~~ ~~=~~ ~~=~~ ~~1~~ . ~~5~~ ~~**Test**~~ ~~**2**~~ ~~**:**~~ ~~_Z_~~ ~~=~~ ~~**Test**~~ ~~=~~ ~~**1**~~ ~~=~~ ~~0~~ . ~~25~~

 10  20


~~=~~ ~~1~~ . ~~5~~ ~~**Test**~~ ~~**2**~~ ~~**:**~~ ~~_Z_~~ ~~=~~ ~~**Test**~~ ~~=~~ ~~**1**~~

10 


~~**Test**~~ ~~**1**~~ ~~**:**~~ ~~_Z_~~ ~~=~~ ~~=~~ ~~=~~ ~~1~~ . ~~5~~ ~~**Test**~~ ~~**2**~~ ~~**:**~~


_X_ − 
~~_Z_~~ ~~=~~


_X_ −  75 − 70

~~=~~ ~~=~~ ~~=~~

~~**Test**~~ ~~**1**~~

 20


➔ **So với Test 2 thì Test 1 có kết quả tốt hơn**

**Test 1**


~~**N(0**~~ **,** ~~**1)**~~

**Z**

**Test 2** **Test 1**


**Test 2**

50 70




**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
34

**[Ví dụ] Z-Value và Phân phối chuẩn tắc**

Độ dài của linh kiện A tuân theo phân phối chuẩn với trung bình 300, độ lệch chuẩn 10.

Giả sử độ dài thỏa mãn phải nằm trong khoảng (290,310) thì mới gọi là hàng OK. Hãy trả lời những câu hỏi sau:

(1) Xác suất linh kiện bị lỗi do dài hơn so với giới hạn cho phép là bao nhiêu?

(2) Xác suất linh kiện bị lỗi do ngắn hơn so với giới hạn cho phép là bao nhiêu?

(3) Xác suất kinh kiện bị lỗi là bao nhiêu?


**Phân phối chuẩn tắc**

**N(0, 1)**


**Phân phối chuẩn**

**N(300, 10** **[2]** **)**



**15.87%** **15.87%** **15.87%** **15.87%**


290


300 310
**길이** **(** **㎛** **)**


-1 0 +1


**Z**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
35

(1) Xác suất linh kiện bị lỗi do dài hơn so với giới hạn cho phép là bao nhiêu?

|Z|0|0 .0 1|0 .0 2|0 .0 3|0 .0 4|0 .0 5|0 .0 6|0 .0 7|0 .0 8|0 .0 9|
|---|---|---|---|---|---|---|---|---|---|---|
|0 .0|5.00E-01|4.96E-01|4.92E-01|4.88E-01|4.84E-01|4.80E-01|4.76E-01|4.72E-01|4.68E-01|4.64E-01|
|0 .1|4.60E-01|4.56E-01|4.52E-01|4.48E-01|4.44E-01|4.40E-01|4.36E-01|4.33E-01|4.29E-01|4.25E-01|
|0 .2|4.21E-01|4.17E-01|4.13E-01|4.09E-01|4.05E-01|4.01E-01|3.97E-01|3.94E-01|3.90E-01|3.86E-01|
|0 .3|3.82E-01|3.78E-01|3.74E-01|3.71E-01|3.67E-01|3.63E-01|3.59E-01|3.56E-01|3.52E-01|3.48E-01|
|0 .4|3.45E-01|3.41E-01|3.37E-01|3.34E-01|3.30E-01|3.26E-01|3.23E-01|3.19E-01|3.16E-01|3.12E-01|
|0 .5|3.09E-01|3.05E-01|3.02E-01|2.98E-01|2.95E-01|2.91E-01|2.88E-01|2.84E-01|2.81E-01|2.78E-01|
|0 .6|2.74E-01|2.71E-01|2.68E-01|2.64E-01|2.61E-01|2.58E-01|2.55E-01|2.51E-01|2.48E-01|2.45E-01|
|0 .7|2.42E-01|2.39E-01|2.36E-01|2.33E-01|2.30E-01|2.27E-01|2.24E-01|2.21E-01|2.18E-01|2.15E-01|
|0 .8|2.12E-01|2.09E-01|2.06E-01|2.03E-01|2.00E-01|1.98E-01|1.95E-01|1.92E-01|1.89E-01|1.87E-01|
|0 .9|1.84E-01|1.81E-01|1.79E-01|1.76E-01|1.74E-01|1.71E-01|1.69E-01|1.66E-01|1.64E-01|1.61E-01|
|1 .0|1.59E-01|1.56E-01|1.54E-01|1.52E-01|1.49E-01|1.47E-01|1.45E-01|1.42E-01|1.40E-01|1.38E-01|
|1 .1|1.36E-01|1.33E-01|1.31E-01|1.29E-01|1.27E-01|1.25E-01|1.23E-01|1.21E-01|1.19E-01|1.17E-01|
|1 .2|1.15E-01|1.13E-01|1.11E-01|1.09E-01|1.07E-01|1.06E-01|1.04E-01|1.02E-01|1.00E-01|9.85E-02|
|1 .3|9.68E-02|9.51E-02|9.34E-02|9.18E-02|9.01E-02|8.85E-02|8.69E-02|8.53E-02|8.38E-02|8.23E-02|
|1 .4|8.08E-02|7.93E-02|7.78E-02|7.64E-02|7.49E-02|7.35E-02|7.21E-02|7.08E-02|6.94E-02|6.81E-02|
|1 .5|6.68E-02|6.55E-02|6.43E-02|6.30E-02|6.18E-02|6.06E-02|5.94E-02|5.82E-02|5.71E-02|5.59E-02|
|1 .6|5.48E-02|5.37E-02|5.26E-02|5.16E-02|5.05E-02|4.95E-02|4.85E-02|4.75E-02|4.65E-02|4.55E-02|
|1 .7|4.46E-02|4.36E-02|4.27E-02|4.18E-02|4.09E-02|4.01E-02|3.92E-02|3.84E-02|3.75E-02|3.67E-02|
|1 .8|3.59E-02|3.51E-02|3.44E-02|3.36E-02|3.29E-02|3.22E-02|3.14E-02|3.07E-02|3.01E-02|2.94E-02|
|1 .9|2.87E-02|2.81E-02|2.74E-02|2.68E-02|2.62E-02|2.56E-02|2.50E-02|2.44E-02|2.39E-02|2.33E-02|
|2 .0|2.28E-02|2.22E-02|2.17E-02|2.12E-02|2.07E-02|2.02E-02|1.97E-02|1.92E-02|1.88E-02|1.83E-02|
|2 .1|1.79E-02|1.74E-02|1.70E-02|1.66E-02|1.62E-02|1.58E-02|1.54E-02|1.50E-02|1.46E-02|1.43E-02|
|2 .2|1.39E-02|1.36E-02|1.32E-02|1.29E-02|1.25E-02|1.22E-02|1.19E-02|1.16E-02|1.13E-02|1.10E-02|
|2 .3|1.07E-02|1.04E-02|1.02E-02|9.90E-03|9.64E-03|9.39E-03|9.14E-03|8.89E-03|8.66E-03|8.42E-03|
|2 .4|8.20E-03|7.98E-03|7.76E-03|7.55E-03|7.34E-03|7.14E-03|6.95E-03|6.76E-03|6.57E-03|6.39E-03|
|2 .5|6.21E-03|6.04E-03|5.87E-03|5.70E-03|5.54E-03|5.39E-03|5.23E-03|5.08E-03|4.94E-03|4.80E-03|
|2 .6|4.66E-03|4.53E-03|4.40E-03|4.27E-03|4.15E-03|4.02E-03|3.91E-03|3.79E-03|3.68E-03|3.57E-03|
|2 .7|3.47E-03|3.36E-03|3.26E-03|3.17E-03|3.07E-03|2.98E-03|2.89E-03|2.80E-03|2.72E-03|2.64E-03|
|2 .8|2.56E-03|2.48E-03|2.40E-03|2.33E-03|2.26E-03|2.19E-03|2.12E-03|2.05E-03|1.99E-03|1.93E-03|
|2 .9|1.87E-03|1.81E-03|1.75E-03|1.69E-03|1.64E-03|1.59E-03|1.54E-03|1.49E-03|1.44E-03|1.39E-03|
|3 .0|1.35E-03|1.31E-03|1.26E-03|1.22E-03|1.18E-03|1.14E-03|1.11E-03|1.07E-03|1.04E-03|1.00E-03|



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
36

(2) Xác suất linh kiện bị lỗi do ngắn hơn so với giới hạn cho phép là bao nhiêu?

|Z|0|0 .0 1|0 .0 2|0 .0 3|0 .0 4|0 .0 5|0 .0 6|0 .0 7|0 .0 8|0 .0 9|
|---|---|---|---|---|---|---|---|---|---|---|
|0 .0|5.00E-01|4.96E-01|4.92E-01|4.88E-01|4.84E-01|4.80E-01|4.76E-01|4.72E-01|4.68E-01|4.64E-01|
|0 .1|4.60E-01|4.56E-01|4.52E-01|4.48E-01|4.44E-01|4.40E-01|4.36E-01|4.33E-01|4.29E-01|4.25E-01|
|0 .2|4.21E-01|4.17E-01|4.13E-01|4.09E-01|4.05E-01|4.01E-01|3.97E-01|3.94E-01|3.90E-01|3.86E-01|
|0 .3|3.82E-01|3.78E-01|3.74E-01|3.71E-01|3.67E-01|3.63E-01|3.59E-01|3.56E-01|3.52E-01|3.48E-01|
|0 .4|3.45E-01|3.41E-01|3.37E-01|3.34E-01|3.30E-01|3.26E-01|3.23E-01|3.19E-01|3.16E-01|3.12E-01|
|0 .5|3.09E-01|3.05E-01|3.02E-01|2.98E-01|2.95E-01|2.91E-01|2.88E-01|2.84E-01|2.81E-01|2.78E-01|
|0 .6|2.74E-01|2.71E-01|2.68E-01|2.64E-01|2.61E-01|2.58E-01|2.55E-01|2.51E-01|2.48E-01|2.45E-01|
|0 .7|2.42E-01|2.39E-01|2.36E-01|2.33E-01|2.30E-01|2.27E-01|2.24E-01|2.21E-01|2.18E-01|2.15E-01|
|0 .8|2.12E-01|2.09E-01|2.06E-01|2.03E-01|2.00E-01|1.98E-01|1.95E-01|1.92E-01|1.89E-01|1.87E-01|
|0 .9|1.84E-01|1.81E-01|1.79E-01|1.76E-01|1.74E-01|1.71E-01|1.69E-01|1.66E-01|1.64E-01|1.61E-01|
|1 .0|1.59E-01|1.56E-01|1.54E-01|1.52E-01|1.49E-01|1.47E-01|1.45E-01|1.42E-01|1.40E-01|1.38E-01|
|1 .1|1.36E-01|1.33E-01|1.31E-01|1.29E-01|1.27E-01|1.25E-01|1.23E-01|1.21E-01|1.19E-01|1.17E-01|
|1 .2|1.15E-01|1.13E-01|1.11E-01|1.09E-01|1.07E-01|1.06E-01|1.04E-01|1.02E-01|1.00E-01|9.85E-02|
|1 .3|9.68E-02|9.51E-02|9.34E-02|9.18E-02|9.01E-02|8.85E-02|8.69E-02|8.53E-02|8.38E-02|8.23E-02|
|1 .4|8.08E-02|7.93E-02|7.78E-02|7.64E-02|7.49E-02|7.35E-02|7.21E-02|7.08E-02|6.94E-02|6.81E-02|
|1 .5|6.68E-02|6.55E-02|6.43E-02|6.30E-02|6.18E-02|6.06E-02|5.94E-02|5.82E-02|5.71E-02|5.59E-02|
|1 .6|5.48E-02|5.37E-02|5.26E-02|5.16E-02|5.05E-02|4.95E-02|4.85E-02|4.75E-02|4.65E-02|4.55E-02|
|1 .7|4.46E-02|4.36E-02|4.27E-02|4.18E-02|4.09E-02|4.01E-02|3.92E-02|3.84E-02|3.75E-02|3.67E-02|
|1 .8|3.59E-02|3.51E-02|3.44E-02|3.36E-02|3.29E-02|3.22E-02|3.14E-02|3.07E-02|3.01E-02|2.94E-02|
|1 .9|2.87E-02|2.81E-02|2.74E-02|2.68E-02|2.62E-02|2.56E-02|2.50E-02|2.44E-02|2.39E-02|2.33E-02|
|2 .0|2.28E-02|2.22E-02|2.17E-02|2.12E-02|2.07E-02|2.02E-02|1.97E-02|1.92E-02|1.88E-02|1.83E-02|
|2 .1|1.79E-02|1.74E-02|1.70E-02|1.66E-02|1.62E-02|1.58E-02|1.54E-02|1.50E-02|1.46E-02|1.43E-02|
|2 .2|1.39E-02|1.36E-02|1.32E-02|1.29E-02|1.25E-02|1.22E-02|1.19E-02|1.16E-02|1.13E-02|1.10E-02|
|2 .3|1.07E-02|1.04E-02|1.02E-02|9.90E-03|9.64E-03|9.39E-03|9.14E-03|8.89E-03|8.66E-03|8.42E-03|
|2 .4|8.20E-03|7.98E-03|7.76E-03|7.55E-03|7.34E-03|7.14E-03|6.95E-03|6.76E-03|6.57E-03|6.39E-03|
|2 .5|6.21E-03|6.04E-03|5.87E-03|5.70E-03|5.54E-03|5.39E-03|5.23E-03|5.08E-03|4.94E-03|4.80E-03|
|2 .6|4.66E-03|4.53E-03|4.40E-03|4.27E-03|4.15E-03|4.02E-03|3.91E-03|3.79E-03|3.68E-03|3.57E-03|
|2 .7|3.47E-03|3.36E-03|3.26E-03|3.17E-03|3.07E-03|2.98E-03|2.89E-03|2.80E-03|2.72E-03|2.64E-03|
|2 .8|2.56E-03|2.48E-03|2.40E-03|2.33E-03|2.26E-03|2.19E-03|2.12E-03|2.05E-03|1.99E-03|1.93E-03|
|2 .9|1.87E-03|1.81E-03|1.75E-03|1.69E-03|1.64E-03|1.59E-03|1.54E-03|1.49E-03|1.44E-03|1.39E-03|
|3 .0|1.35E-03|1.31E-03|1.26E-03|1.22E-03|1.18E-03|1.14E-03|1.11E-03|1.07E-03|1.04E-03|1.00E-03|



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
37

(3) Xác suất kinh kiện bị lỗi là bao nhiêu?

|Z|0|0 .0 1|0 .0 2|0 .0 3|0 .0 4|0 .0 5|0 .0 6|0 .0 7|0 .0 8|0 .0 9|
|---|---|---|---|---|---|---|---|---|---|---|
|0 .0|5.00E-01|4.96E-01|4.92E-01|4.88E-01|4.84E-01|4.80E-01|4.76E-01|4.72E-01|4.68E-01|4.64E-01|
|0 .1|4.60E-01|4.56E-01|4.52E-01|4.48E-01|4.44E-01|4.40E-01|4.36E-01|4.33E-01|4.29E-01|4.25E-01|
|0 .2|4.21E-01|4.17E-01|4.13E-01|4.09E-01|4.05E-01|4.01E-01|3.97E-01|3.94E-01|3.90E-01|3.86E-01|
|0 .3|3.82E-01|3.78E-01|3.74E-01|3.71E-01|3.67E-01|3.63E-01|3.59E-01|3.56E-01|3.52E-01|3.48E-01|
|0 .4|3.45E-01|3.41E-01|3.37E-01|3.34E-01|3.30E-01|3.26E-01|3.23E-01|3.19E-01|3.16E-01|3.12E-01|
|0 .5|3.09E-01|3.05E-01|3.02E-01|2.98E-01|2.95E-01|2.91E-01|2.88E-01|2.84E-01|2.81E-01|2.78E-01|
|0 .6|2.74E-01|2.71E-01|2.68E-01|2.64E-01|2.61E-01|2.58E-01|2.55E-01|2.51E-01|2.48E-01|2.45E-01|
|0 .7|2.42E-01|2.39E-01|2.36E-01|2.33E-01|2.30E-01|2.27E-01|2.24E-01|2.21E-01|2.18E-01|2.15E-01|
|0 .8|2.12E-01|2.09E-01|2.06E-01|2.03E-01|2.00E-01|1.98E-01|1.95E-01|1.92E-01|1.89E-01|1.87E-01|
|0 .9|1.84E-01|1.81E-01|1.79E-01|1.76E-01|1.74E-01|1.71E-01|1.69E-01|1.66E-01|1.64E-01|1.61E-01|
|1 .0|1.59E-01|1.56E-01|1.54E-01|1.52E-01|1.49E-01|1.47E-01|1.45E-01|1.42E-01|1.40E-01|1.38E-01|
|1 .1|1.36E-01|1.33E-01|1.31E-01|1.29E-01|1.27E-01|1.25E-01|1.23E-01|1.21E-01|1.19E-01|1.17E-01|
|1 .2|1.15E-01|1.13E-01|1.11E-01|1.09E-01|1.07E-01|1.06E-01|1.04E-01|1.02E-01|1.00E-01|9.85E-02|
|1 .3|9.68E-02|9.51E-02|9.34E-02|9.18E-02|9.01E-02|8.85E-02|8.69E-02|8.53E-02|8.38E-02|8.23E-02|
|1 .4|8.08E-02|7.93E-02|7.78E-02|7.64E-02|7.49E-02|7.35E-02|7.21E-02|7.08E-02|6.94E-02|6.81E-02|
|1 .5|6.68E-02|6.55E-02|6.43E-02|6.30E-02|6.18E-02|6.06E-02|5.94E-02|5.82E-02|5.71E-02|5.59E-02|
|1 .6|5.48E-02|5.37E-02|5.26E-02|5.16E-02|5.05E-02|4.95E-02|4.85E-02|4.75E-02|4.65E-02|4.55E-02|
|1 .7|4.46E-02|4.36E-02|4.27E-02|4.18E-02|4.09E-02|4.01E-02|3.92E-02|3.84E-02|3.75E-02|3.67E-02|
|1 .8|3.59E-02|3.51E-02|3.44E-02|3.36E-02|3.29E-02|3.22E-02|3.14E-02|3.07E-02|3.01E-02|2.94E-02|
|1 .9|2.87E-02|2.81E-02|2.74E-02|2.68E-02|2.62E-02|2.56E-02|2.50E-02|2.44E-02|2.39E-02|2.33E-02|
|2 .0|2.28E-02|2.22E-02|2.17E-02|2.12E-02|2.07E-02|2.02E-02|1.97E-02|1.92E-02|1.88E-02|1.83E-02|
|2 .1|1.79E-02|1.74E-02|1.70E-02|1.66E-02|1.62E-02|1.58E-02|1.54E-02|1.50E-02|1.46E-02|1.43E-02|
|2 .2|1.39E-02|1.36E-02|1.32E-02|1.29E-02|1.25E-02|1.22E-02|1.19E-02|1.16E-02|1.13E-02|1.10E-02|
|2 .3|1.07E-02|1.04E-02|1.02E-02|9.90E-03|9.64E-03|9.39E-03|9.14E-03|8.89E-03|8.66E-03|8.42E-03|
|2 .4|8.20E-03|7.98E-03|7.76E-03|7.55E-03|7.34E-03|7.14E-03|6.95E-03|6.76E-03|6.57E-03|6.39E-03|
|2 .5|6.21E-03|6.04E-03|5.87E-03|5.70E-03|5.54E-03|5.39E-03|5.23E-03|5.08E-03|4.94E-03|4.80E-03|
|2 .6|4.66E-03|4.53E-03|4.40E-03|4.27E-03|4.15E-03|4.02E-03|3.91E-03|3.79E-03|3.68E-03|3.57E-03|
|2 .7|3.47E-03|3.36E-03|3.26E-03|3.17E-03|3.07E-03|2.98E-03|2.89E-03|2.80E-03|2.72E-03|2.64E-03|
|2 .8|2.56E-03|2.48E-03|2.40E-03|2.33E-03|2.26E-03|2.19E-03|2.12E-03|2.05E-03|1.99E-03|1.93E-03|
|2 .9|1.87E-03|1.81E-03|1.75E-03|1.69E-03|1.64E-03|1.59E-03|1.54E-03|1.49E-03|1.44E-03|1.39E-03|
|3 .0|1.35E-03|1.31E-03|1.26E-03|1.22E-03|1.18E-03|1.14E-03|1.11E-03|1.07E-03|1.04E-03|1.00E-03|



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
38

 **Tính xác suất tích lũy bằng Minitab**

**(1) Xác suất linh kiện bị lỗi do dài hơn so với giới hạn cho phép là bao nhiêu?**


**Cal > Probability Distributions > Normal Distribution**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
39


**※ Xác suất dài hơn 310**
**: Vì Minitab chỉ cung cấp các giá trị**

**xác suất tích lũy thấp hơn, nên hãy**
**tính toán theo cách sau.**

**①** **Xác suất nhỏ hơn 310,**



 **Tính xác suất tích lũy bằng Minitab**

**(2) Xác suất linh kiện bị lỗi do ngắn hơn so với giới hạn cho phép là bao nhiêu?**

**Cal > Probability Distributions > Normal Distribution**

**※ Tính xác suất ngắn hơn 290**



**③** **Xác suất nhỏ hơn 290,**




**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
40

✓ **Chuẩn hóa**



- Biến cố xác suất : X i **★** − - Biến cố xác suất : Z i


☞
Tham khảo biến ngẫu nhiên ngoài chuẩn hóa Z-Value


**★**


−
`x` `i` 






















































**★** **: Nội dung học bắt buộc**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
41


**Xấp xỉ phân phối (** ≒ **)**

 **Phân phối chọn mẫu (sampling distribution) : Một phân phối với biến cố xác suất**
**là thống kê được tính toán từ mẫu.**

   - Là phân phối trong đó biến cố (X) là một thống kê (trung bình, phương sai) được rút ra từ càng
nhiều nhóm mẫu càng tốt (về lý thuyết là vô hạn).

✓ **Làm thế nào chính ta có thể suy ra số liệu thống kê của tổng thể từ các giá trị được rút ra từ các mẫu?**


**①** **Trung bình cộng của mẫu bằng trung bình tổng thể.**

~~**N**~~ **=** ~~**3**~~ ~~**Mẫu**~~ ~~**n=2**~~





**Tổng**
**thể**








~~**Trung**~~ ~~**bình**~~ ~~**tổng**~~ ~~**thể**~~ ~~**(100)**~~ ~~**=**~~ ~~**Trung**~~ ~~**bình**~~ ~~**của**~~ ~~**trung**~~ ~~**bình**~~ ~~**mẫu(100)**~~

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
42


**②** **Phân tán: độ phân tán (phương sai) của các trung bình**

**mẫu càng nhỏ khi kích thước mẫu (n) càng lớn.**

~~Trung~~ ~~bình~~ ~~tổng~~ ~~thể~~

N(100, 10 [2] /n)

|: N(100, 102)|Col2|
|---|---|
|ối chọn mẫu :<br>102/n)||



~~**Ph**~~ **ư** ~~**ơ**~~ **ng sa** ~~**i**~~ **c** ~~**ủ**~~ **a p** ~~**hâ**~~ **n p** ~~**hối**~~ **c** ~~**h**~~ **ọn m** ~~**ẫ**~~ **u =** ~~**Ph**~~ **ư** ~~**ơ**~~ **ng sa** ~~**i**~~ **c** ~~**ủ**~~ **a** ~~**tổ**~~ **ng** ~~**thể**~~ ~~**÷**~~ ~~**S**~~ **amp** ~~**l**~~ **e** ~~**Si**~~ **ze** ~~**(**~~ **n** ~~**)**~~

**[VD] Phân phối chuẩn (Mean : 100, Độ lệch chuẩn : 5)**

Khi kích thước mẫu tăng lên, độ lệch chuẩn của trung bình mẫu sẽ nhỏ đi.




thì dần dần sẽ tiệm cận với mức trung bình

변수 của tổng thể. Vì vậy, sự phân tán của mẫu
normal10 giảm khi kích thước mẫu sẽ tăng lên.





**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
43

  **Định lý giới hạn trung tâm**



Trung bình nhóm Sample



Nhóm Sample











|σ<br>n|Kích thước m|
|---|---|
|μ<br>𝑋<br>Phân phối<br>chuẩn|μ<br>𝑋<br>Phân phối<br>chuẩn|


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
44

-3 -2 -1 **0** 1 2 3



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
45

- −
**Khi có một tổng thể nhưng chưa biết phương sai của nó** _X_ 

_t_ =

**→ Uớc tính trung bình tổng thể thay thế cho độ lệch chuẩn mẫu** _s_ / _n_
**(s) bằng cách sử dụng phân phối t.**


−

_X_
_t_ =



※ Sử dụng để kiểm tra giá trị trung bình



**Tham số của phân phối: Bậc tự do (degree of freedom : n-1)**


*Hình dạng phân phối được quyết định dựa trên bậc tự do



   **Phân phối t giống với phân phối chuẩn tắc là đều đối xứng tại 0, nhưng có đuôi dài hơn phân**

**phối chuẩn.**

~~▪~~ ~~**Khi**~~ ~~**bậc**~~ ~~**tự**~~ ~~**do**~~ ~~**càng**~~ ~~**lớn**~~ **,** ~~**vì**~~ ~~**phân**~~ ~~**phối**~~ ~~**t**~~ ~~**càng**~~ ~~**giống**~~ ~~**với**~~ ~~**phân**~~ ~~**phối**~~ ~~**Z**~~ **,** ~~**nên**~~ ~~**trong**~~ ~~**trường**~~ ~~**hợp**~~ ~~**n**~~ ~~≥~~

**30, có thể sử dùng phân phối Z thay thế phân phối t.**

n = 10

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**

|Col1|Col2|Col3|
|---|---|---|
|||n = 30<br>n = 20<br>n =|
||||

46

※Dùng khi kiểm định tính độc

lập, tính đồng nhất.

 **Được sử dụng để ước tính phương sai tổng thể, kiểm tra tính độc lập/đồng nhất của dữ liệu**

**.**
**dạng phân loại (Categorical data), mức độ phù hợp của phân phối**

 **Tham số của phân phối : Bậc tự do(degree of freedom : n-1)**



- Đặc điểm : Hình dạng thay đổi theo bậc tự do.
Nếu tổng thể là phân phối chuẩn, phải biết phương sai của tổng thể (σ [2] ).


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
47

※ Dùng khi phân tích phân phối

**.**
**Được sử dụng khi ước tính tỷ lệ (ratio) của 2 phương sai tổng thể(ratio), sử dụng khi có 2 tổng thể**

**Là phân phối chuẩn, tỷ lệ của phương sai mẫu chia cho tỷ lệ của phương sai tổng thể.**



**Tham số của phân phối : Bậc tự do(degree of freedom) của 2 nhóm.**

Hình dạng của phân phối F


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
48

**2. Lý thuyết cơ bản về phân tích dữ liệu**

**2.1. Khái quát về thống kê học**

**2.2. Th** ~~**ố**~~
**ng kê mô tả**

**2.3. Thống kê suy luận**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
49

**Thống kê mô tảvà thống kê suy luận là các phương pháp giải thích các đặc điểm của**
**tổng thể từ một mẫu.**


**Quy trình phân tích tài liệu**


**Thống kê mô tả(** **記述統計學** **, descriptive statistics)**

Biểu thị bằng Graph, trung vị và sự phân tán.

**Thống kê suy luận(** **推論統計學** **, inferential statistics)**





Dự đoán đặc điểm tổng thể từ một số mẫu, tài liệu và suy ra kết luận.



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
50

**Thống kê mô tả** **là một lý thuyết và phương pháp mà trong đó, bước đầu tiên vẽ biểu đồ từ dữ liệu đã có để**

**hiểu sơ về cấu trúc và hình dạng, sau đó tính toán thông tin cần thiết như tổng hoặc trung bình, đồng thời sắp**

**xếp và tóm tắt chúng bằng các** **giá trị đại diện** **.**

**Graph** **Histogram**

**Box plot**


**Giá trị**

**đại diện**

(Thông tin

được tính toán)


**Khi thể hiện giá trị trung tâm**

**Khi thể hiện mức độ phân tán của dữ liệu**


**Trung bình** (average, mean)

**Median**

**Mode**

**Phương sai** (variance)

**Độ lệch chuẩn** (standard deviation)

**Khoảng biến thiên** (range)

**Khoảng tứ phân vị** (interquartile range : IQR)

**Hệ số biến thiên** (coefficient of variance)


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
51

   **Histogram**

**Phản ánh tổng quan về hình dạng phân phối, chẳng hạn như giá trị trung tâm và sự phân tán dữ liệu.**

**Đặc điểm**

         Chia dữ liệu thành nhiều khoảng và hiển thị tần suất dữ liệu thuộc mỗi khoảng dưới dạng biểu đồ cột.

         Trục Y biểu thị tần số, trục X biểu thị khoảng thời gian.

         Phân phối chuẩn hay không, có Outlier hay không.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
52

   **Box plot**

**Sử dụng khi muốn nắm bắt sơ bộ giá trị trung tâm, hình thái phân tán và để biết có Outlier hay không.**

**Đặc điểm**

         Có thể nắm bắt sơ bộ hình dạng phân phối như sự phân tán dữ liệu, giá trị trung tâm. (có thể kiểm tra tính đối cứng của

phân phối)

         Biết được có tồn tại Outlier hay không.

         Biểu thị 5 đặc điểm chính (Min, Q1, Trung vị, Q3, Max) dưới g=dạng hộp và đường.

                                           - **Outlier**

**Upper Limit**

**Q3**

**Trung vị**

**Q1**

**Lower Limit**

Q3 : Giá trị thứ {(n+1) × 3} / 4, Giá trị thứ Q1 : (n+1)
/ 4

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
53

**1) Giá trị trung tâm:**

   **Trung bình (average, mean)**

     - Tổng tất cả dữ liệu được quan sát chia cho số lượng quan sát.
```
        n

```

`x` `i` `x` : Mean `x` `i`
##### 
```
                             n
  i
```

= `n` 


: i = 1~ n

```
   x
    i
```

=
```
x

```

`n` : Số hạng


: số hạng trong dữ liệu


`x` : Mean

```
x
 i

```
```
i

```
```
n

```
```
n

```

`i 1` =


**Đặc điểm**

        Phản ánh tác động của tất cả dữ liệu.

        Bị ảnh hưởng bởi Outlier.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
54

**1) Giá trị trung tâm**

   **Trung vị (median)**

      Giá trị ở giữa khi dữ liệu quan sát được sắp xếp theo thứ tự kích thước

      Khi có n dữ liệu, thì trung vị là dữ liệu thứ (n+1)/2 .

. Khi n là số lẻ : 2, 3,4, 5, 6, 7, 7, 8, 9 **Median = 6**

. ~~Khi~~ ~~n~~ ~~là~~ ~~số~~ ~~chẵn~~ ~~:~~ ~~2~~, ~~3~~, ~~4~~, ~~5~~, ~~6~~, ~~7~~, ~~7~~, ~~8~~, ~~9~~, ~~9~~ ~~Median~~ = ~~6~~ . ~~5~~
#### ✓

**Đặc điểm**



Không bị ảnh hưởng nhiều bởi Outlier.


**3.0**



#### Sử dụng làm giá trị trung tâm trong phân phối không đối xứng. ✓

**3.5**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
55

**1) Giá trị trung tâm**

    **Mode**

       - Giá trị có tần suất xuất hiện cao nhất trong các dữ liệu quan sát

**Đặc điểm**

        Mode có thể là duy nhất hoặc không.

        ~~Bổ~~ trợ c ~~h~~ o g ~~iá~~ tr ~~ị~~ trung ~~bì~~ n ~~h~~ ~~h~~ o ~~ặ~~ c trung v ~~ị~~ .

✓ ✓ ✓

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
56

**2) Mức độ phân tán của dữ liệu**

   - **Phương sai (variance)**

     - Mức độ phân tán dữ liệu được đo xung quanh giá trị trung bình : trung bình bình phương
các giá trị lệch khỏi giá trị trung bình.

     - Phương sai mẫu bằng tổng biến thiên [ 1)] chia cho bậc tự do [2).]












※ Tại sao phương sai của mẫu lại chia cho (n-1) thay vì n?

𝑿
          - Đối với phương sai mẫu, trung bình tổng thể là ẩn số nên dùng trung bình mẫu ( [ഥ] ) thay cho trung bình

~~tổng~~ ~~thể~~ ~~(μ)~~ .
Điều này làm cho nó nhỏ hơn phương sai thực tế một khoảng (𝑿 [ഥ] -μ) [2] (bỏ qua công thức chứng minh)
Chia cho ( n-1) để điều chỉnh vấn đề này.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
57

**Tham**

**khảo**


**Tham khảo**

**1) Tổng biến động là gì?** Tổng bình phương độ lệch (số hạng – trung bình).

**2) Bậc tự do** (𝒅𝒇 **: degree of freedom) là gì?**

: Là số lượng dữ liệu độc lập cung cấp thông tin về tổng thể trong dữ liệu mẫu theo ước tính thống kê được thực hiện trong thống kê.

<Ví dụ> Gỉa sử lấy 3 số có giá trị trung bình được tính là 5. Trong đó 2 số có thể được lấy làm giá trị tự do.

Tuy nhiên, nếu quy định giá trị trung bình 5 là điều kiện ràng buộc, thì 1 số sẽ được quyết định bởi số còn lại.

Nếu được tự do chọn 8 và 3 thì số còn lại là 4 để đặt mức trung bình là 5

Nếu bạn lấy n cái, vì lý do tượng tự, bậc tự do là n-1, thay vì là n.


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
58

**2) Mức độ phân tán của dữ liệu**

   **Độ lệch chuẩn (standard deviation)**

     - Là thước đo đại diện cho sự phân tán hoặc lây lan quanh giá trị trung bình.

: Lấy căn bậc 2 của phương sai để biết trực quan về mức độ phân tán.


**Đặc điểm**

        Bằng cách lấy căn bậc hai của phương sai,
giá trị luôn lớn hơn hoặc bằng “0”

       - Bị ảnh hưởng bởi Outlier.

**Độ lệch chuẩn (σ)**

*điểm cong đồ thị

평균 (μ)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
59











    - **Khoảng cách so với trung bình**



~~(~~ 1-4.6) = -3.6


3.4



**Trung bình**

**4.6**



**Để loại trừ giá trị âm**



(-3.6) [2] = 12.96 6.76


1.96 5.76 11.56

**Lấy căn bậc 2 → độ lệch chuẩn**


**Bình phương khoảng cách phân tán**




57.08





|𝑿 −𝑿ഥ 𝟐<br>𝒊<br>• Bình phương kh<br>𝒏<br>෍ 𝑿 −𝑿ഥ 𝟐<br>𝒊<br>𝒊=1<br>• Trung bình bình<br>cách phân tán→ p<br>𝒏<br>෍ 𝑿 −𝑿ഥ 𝟐<br>𝒊|Col2|(<br>o|
|---|---|---|
|𝑿 −𝑿ഥ 𝟐<br>𝒊<br>• Bình phương kh<br>𝒏<br>෍ 𝑿 −𝑿ഥ 𝟐<br>𝒊<br>𝒊=1<br>• Trung bình bình<br>cách phân tán→ p<br>𝒏<br>෍ 𝑿 −𝑿ഥ 𝟐<br>𝒊|𝒊=1<br>• Trung bình bình<br>cách phân tán→ p<br>𝒏<br>෍ 𝑿 −𝑿ഥ 𝟐<br>𝒊|𝒊=1<br>• Trung bình bình<br>cách phân tán→ p<br>𝒏<br>෍ 𝑿 −𝑿ഥ 𝟐<br>𝒊|


𝒊=1


**n-1**



4.757


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
60

**2) Mức độ phân tán của dữ liệu**

   **Khoảng biến thiên (range)**

**- Là thước đo độ phân tán đơn giản nhất, bằng giá trị max trừ giá trị min (X** **max** **– X** **min** **)**


**Đặc điểm**

- Bị ảnh hưởng bởi Outlier

**Range =  X** **max** **- X** **min**


<Ví dụ> Ghi chéo về diễn biến mực nước sông Hàn. Biên độ mực nước sông

Hàn?

**18**

**16**

```
      x
```

`max` :Giá trị max trong tập data
```
       x
```

`min` :Giá trị min trong tập data

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
61


**12**

**11**

**9**

**8**

**4**

**1**

**2) Mức độ phân tán của dữ liệu**

   **Khoảng tứ phân vị(interquartile range)**

      - Khi sắp xếp dữ liệu theo thứ tự, các giá trị bằng **¼ và bội của nó** được gọi là “tứ phân vị” .

     - Khoảng tứ phân vị(IQR: interquartile range) = Q3 (3/4 phân vị)     - Q1 (1/4 phân vị)




**Outlier** : điểm vượt quá  Q3 + 1.5 × IQR

**Upper Limit :** giá trị lớn nhất trong  Q3 + 1.5 × IQR

**Q3** : Khi dữ liệu được sắp xếp theo thứ tự, giá trị nằm ở 3/4

thứ tự 3(n+1)/4

**Trung vị** : Giá trị ở trung tâm khi dữ liệu được sắp xếp theo thứ tự

**Q1** : Khi dữ liệu được sắp xếp theo thứ tự, giá trị nằm ở 1/4

thứ tự (n+1)/4

**Lower Limit** : giá trị nhỏ nhất trong   Q1 - 1.5 × IQR


**Đặc điểm**

 - Ít ảnh hưởng bởi Outlier


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
62

**2) Mức độ phân tán của dữ liệu**

   **Hệ số biến thiên (CV, coefficient of variation)**

      Các đặc điểm chất lượng khác nhau có các thang đo khác nhau và theo đó, thang đo độ lệch chuẩn

cũng khác nhau, do đó cân nhắc điều này và,chia cho giá trị trung bình.

→ Độ lệch chuẩn được chuyển đổi thành tỷ lệ gấp vài lần giá trị trung bình và so sánh biến động

giữa các phân bố có đặc điểm chất lượng khác nhau.


~~**Đặ**~~ **c** ~~**điể**~~ **m**

```
                    s
```

~~·~~
~~Thông~~ ~~thường,~~ ~~x100~~ ~~để~~ ~~chuyển~~ ~~thành~~ ~~giá~~ ~~trị(%)~~ ~~.~~ ~~`CV`~~ ~~=~~

- Hệ số biến thiên càng lớn thì biến động càng cao. `x`


※ Chú ý:

        - Nếu giá trị trung bình bằng 0, ngay cả những khác biệt nhỏ cũng có thể thay đổi hệ số biến thiên một cách rất

nhạy cảm.

        - Ngay cả khi đơn vị có mối quan hệ tuyến tính, hệ số biến thiên cũng có thể khác nhau.

|Col1|1|2|3|Trung bình|Độ lệch chuẩn|CV|
|---|---|---|---|---|---|---|
|(℃)|0|10|20|10|10|1|
|(℉)|32|50|68|50|18|0.36|



℉ = (9 ÷ 5) × ℃ +32

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
63

>Data : 1. 기초통계 _ 기술통계 _ 통계량 _ 기초통계량표시

**Stat > Basic Statistics > Display Descriptive Statistics**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
64

**Stat > Basic Statistics > Graphical Summary**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
65


   **Ước lượng điểm:**

**Ước lượng gía trị thực của một tham số chưa biết dưới dạng phỏng đoán bằng cách sử dụng thông**

**tin thu được từ một mẫu.**

**Ví dụ) Tỷ lệ phiếu bầu của ứng cử viên A là 45.1%, độ sâu của sông là 1m.**

      - Ước lượng điểm là một biến cố xác suất có một giá trị từ mẫu nhưng giá trị của nó là không xác định cho đến khi lấy

được mẫu.

Tức là, có nhiều ước lượng điểm cho một tham số.

        - Chưa có khái niệm về sai số trong ước tính chính xác như thế nào.

Tức là, không có khái niệm về mức độ gần đúng của giá trị ước lượng thu được từ mẫu với giá trị thực của tham số.

※ Độ lệch chuẩn của một ước lượng điểm được gọi là sai số chuẩn của giá trị trung bình (SE; the

standard error of the mean) .

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
66

   **Ước lượng khoảng**

**-**
Một phương pháp ước lượng khoảng biến thiên mà một tham số dự kiến sẽ bao gồm **thay vì ước**

**lượng một giá trị đơn lẻ.**

     - Ước lượng khoảng biến thiên được gọi là khoảng tin cậy (confidence interval).

**- Thông thường, ước lượng bằng cách sử dụng giá trị trung bình và sai số chuẩn của giá trị**

**trun** **bình.**
**g**

**Ví dụ) Tỷ lệ phiếu bầu của ứng viên A là 45.1%** **±** **2%(độ tin cậy 95%), độ sâu nước sông 1m** **±** **0.3m(độ**

**tin cậy 90%)**

**※ Độ tin cậy: Xác suất bao gồm giá trị thực của tham số đó trong khoảng tin cậy.**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
67

 **Ước lượng khoảng**

     Khoảng tin cậy 100(1 – α)% của trung bình tổng thểμ được ước tính như sau












~~**Khoảng**~~ ~~**μ**~~ ~~**의**~~ ~~**tin**~~ ~~**90%**~~ ~~**cậy**~~ ~~**90%**~~ ~~**신뢰구간**~~ ~~**của**~~ ~~**μ**~~ **:** **(** _**X**_ **–** 1.645 **∙    ,** _**X**_ **+** 1.645 **∙** ~~**)**~~


~~**Khoảng**~~ ~~**μ**~~ ~~**tin**~~ ~~**90%**~~ ~~**cậy**~~ ~~**90%**~~ ~~**của**~~ ~~**μ**~~










~~**Khoảng**~~ **μ** ~~**의**~~ ~~**tin**~~ ~~**95%**~~ ~~**cậy**~~ ~~**95%**~~ ~~**신뢰구간**~~ ~~**của**~~ ~~**μ**~~ **:** **(** _**X**_ **–** 1.960 **∙    ,** _**X**_ **+** 1.960 **∙** ~~**)**~~


~~**Khoảng**~~ ~~**의**~~ ~~**tin**~~ ~~**95%**~~ ~~**cậy**~~ ~~**95%**~~ ~~**của**~~ ~~**μ**~~










~~**Khoảng**~~ **μ** ~~**의**~~ ~~**tin**~~ ~~**99%**~~ ~~**cậy**~~ ~~**99%**~~ ~~**신뢰구간**~~ ~~**của**~~ ~~**μ**~~ **:** **(** _**X**_ **–** 2.576 **∙    ,** _**X**_ **+** 2.576 **∙** ~~**)**~~


~~**Khoảng**~~ ~~**의**~~ ~~**tin**~~ ~~**99%**~~ ~~**cậy**~~ ~~**99%**~~ ~~**của**~~ ~~**μ**~~




✓ Khoảng tin cậy trong ước lượng khoảng chính là sai số chọn mẫu.

(Sai số xuất hiện khi chỉ lấy một phần của tổng thể) .

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
68

**[Ví dụ] Điểm IQ trung bình của nhân viên LGD**

Anh Son Dae-ri đã điều tra chỉ số IQ trung bình của nhân viên LGD, sau đó viết báo cáo về kết quả của
cuộc khảo sát này.
Trước đây, anh ấy chỉ đưa trung bình mẫu vào báo cáo, nhưng bây giờ, sau khi tham gia một bài giảng
về thống kê cơ bản, anh ấy đã đạt đến trình độ có thể tính toán khoảng tin cậy của điểm IQ trung bình và
đưa ước lượng khoảng vào trong báo cáo.
Bảng dưới đây tóm tắt kết quả khảo sát IQ của nhân viên LGD.

|Kích thước mẫu (n)|Trung bình mẫu ( x )|Phương sai mẫu (s2)|Độlệch chuẩn mẫu (s)|Độlệch chuẩn tổng thể(σ)|
|---|---|---|---|---|
|100|105|2704|52|50|



Ở mức độ tin cậy 95% được ước tính bởi anh Son, khoảng tin cậy của trung bình tổng thể như sau:

**Khoảng tin cậy 95% của μ** = ( 105 – 1.96 x (50/10), 105 + 1.96 x (50/10)) = ( 95.2, 114.8 )

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
69

Ví dụ như trên:

**①** **Nếu độ tin cậy tăng (90% → 95% → 99%) thì độ rộng của khoảng cũng tăng.**
**②** **Ở cùng mức độ tin cậy, nếu số lượng mẫu tăng (400 → 900) thì độ rộng khoảng sẽ giảm.**
**③** **Ở cùng mức độ tin cậy, nếu độ lệch chuẩn tăng (40 → 60) có thể thấy rằng độ rộng của khoảng tăng lên.**

**Khoảng tin cậy 90% của μ**



①

②

③


**Khoảng tin cậy 95% của μ**

**Khoảng tin cậy 99% của μ**

_**n**_ **= 400** **(95%)**

_**n**_ **= 900** **(95%)**

_**σ**_ **= 40** **(95%)**

_**σ**_ **= 60** **(95%)**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
70

 - Mô phỏng khoảng tin cậy;

Hình bên dưới lần lượt thể hiện khoảng tin cậy 95% và khoảng tin cậy 99% thu được bằng cách kiểm tra 50

mẫu thông qua mô phỏng.

Q1. Trong khoảng tin cậy của 50 cái, tỷ lệ bao gồm trung bình tổng thể là bao nhiêu?

Q2. Giải thích ý nghĩa khoảng tin cậy 95%?





**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
71

**3. Kiểm định giả** **thuyết thống kê**

**3.1. Khái quát**

**3.2. Ki** ~~**ể**~~ **m đ**
**ịnh giá trị** **trung bình** **(Z, t, Anova)**

**3.3. Kiểm đ** **ươ** **ồ**
**ịnh quan hệ** **(Phân tích t** **ng quan/h** **i quy)**

**3.4. Kiểm định tỷ** **lệ** **(Tỷ** **lệ, Poisson, Chi-Square)**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
72

 **Giả thuyết**

Nếu mối quan hệ giữa 2 hay nhiều hiện tượng/ biến cố được kiểm chứng bằng cách

quan sát hoặc thực nghiệm,

Thoát khỏi vị trí giả định và trở thành sự thật có giá trị trong một giới hạn nhất định.

 **Loại hình giả thuyết**


Giả thuyết
nghiên cưu

Giả thuyết

thống kê


Giả thuyết được trình bày một cách chung chung, một câu trả lời tạm thời cho một vấn đề nghiên cứu.

 - Cú nổ BigBang đã tạo ra vụ trụ hiện tại.

Giả thuyết trong đó được trình bày bằng cách sử dụng tham số, đối số cụ thể (Giả thuyết

không, giả thuyết nghịch)

 - Giả thuyết ‘’Chiều cao của phụ nũ trưởng thành ở Mỹ là cao’’ → không thể là giả thuyết thống kê.

‘’Chiều cao trung bình của phụ nữ trưởng thành ở Mỹ là 170’’ → Giả thuyết thống kê.

‘’Chiều cao trung bình’’ là tham số (trung bình) thể hiện đặc điểm tổng thể.


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
73

   **Kiểm định giả thuyết thống kê là gì?**

   **Tại sao lại cần kiểm định giả thuyết thống kê:**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
74

   **Mục đích**

① A : Trước cải tiến Mean 5, Phướng sai 2  → Sau khi thiết lập các biện pháp cải thiện, nếu trung bình

② B : Trước cải tiến Mean 5, Phướng sai 1  → Sau khi thiết lập các biện pháp cải thiện, nếu trung bình

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
75

 **Các loại giả thuyết thống kê**


“Điều gì đó có thể được thay đổi một cách đặc
biệt?”

“Nó sẽ giống như “Chắc là nó đó.”

trước đây thôi ~”

     **Các tuyên bố/khẳng định, cho đến hiện tại, không có**
**gì thay đổi hoặc khác biệt.**

      - Thiết lập một sự thật thông thường, được gọi là ‘giả thuyết

không’ .

      - Các khái niệm bình đẳng như ‘Giống nhau’ và ‘ Không có sự

khác biệt’ .

       - Kí hiệu : H 0

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
76


“Sẽ có khác biệt so với

“Sẽ có gì đó khác thôi ~ !”
trước thôi~!”

“Chắc đây là một trường hợp

đặc biệt !”

 - **“** **”**
**Khẳng định mới,** **Giả thuyết cần chứng minh**

 - Các khái niệm không bình đẳng như “Không giống nhau”,

“Có sự khác biệt”.

 - Kí hiệu : H a or H 1

**Để tiến hành kiểm định giả thuyết cho việc lựa chọn nhân tố trọng yếu (vital few) một**
**cách hiệu quả và có hệ thống, cần phải áp dụng dữ liệu có độ tin cậy và kĩ thuật phân**
**tích phù hợp.**

 **Hoạt động**

      Thiết lập giả thuyết về mối quan hệ nhân quả giữa CTQ(critical to quality) và nhân tố tiềm ẩn.

      Lựa chọn dữ liệu cần thiết và phương pháp phân tích dựa trên các giả thuyết.

      Thực hiện phân tích sự khác biệt đáng kể bằng cách sử dụng các phương pháp phân tích định tính/ định
lượng phù hợp.

~~▪~~ ~~**Khái**~~ ~~**quát**~~ ~~**về**~~ ~~**kiểm**~~ ~~**định**~~ ~~**giả**~~ ~~**thuyết**~~ **Lựa chọn dữ liệu cần thiết**












**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
77

 **Phương pháp thiết lập giả thuyết cơ bản**


**①** **Có phải là phân phối**
**chuẩn**

**②** **Trung**
**bình**

|Col1|Col2|
|---|---|
|Gap<br>𝜇<br>𝐴|Mean<br>𝜇<br>𝐵|



**③** **Độ lớn của phương sai**


|ơng sai<br>𝜎<br>𝐴<br>𝜎<br>𝐵|Col2|
|---|---|
|||


Gap phương sai

**④** **Phương thức hồi quy**

Phương thức hồi quy


H
o : Data là Phân phối chuẩn

H
a : Data không phải là Phân phối chuẩn

H
o : Trung bình nhóm A = Trung bình nhóm B

H a : Trung bình nhóm A  Trung bình nhóm B

H
o : Phương sai nhóm A = Phương sai nhóm B

H a : Phương sai nhóm A  Phương sai nhóm B

H
o : Hệ số góc bằng 0

H
a : Hệ số góc khác 0


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
78

**Kiểm định giả thuyết dựa trên phân tích thống kê là sử dụng dữ liệu của mẫu để đưa ra**
**quyết định mang tính thống kê về tổng thể. Vì lý do này, có thể xảy ra các lỗi như dưới đây.**

~~**Lỗi**~~ ~~**sai**~~ ~~**trong**~~ ~~**kiểm**~~ ~~**định**~~ ~~**giả**~~ ~~**thuyết**~~


**Hiện tượng thực tế**

**H** **H**
**o** **a**


**Quyết định mang**

**tính thống kê**


**H**
~~**o**~~

**H**
**a**

|Quyết định đúng|Lỗi loại 2|
|---|---|
|Lỗi loại 1|Quyết định đúng|



                Có bao nhiêu lỗi khi một người vô tội bị kết án?

**Think**

                Có bao nhiêu lỗi khi thủ phạm lại được trắng án và trả tự do?

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
79

 **Thuật ngữ liên quan đến kiểm định giả thuyết**

                  Xác suất chấp nhận giả thuyết không khi nó đúng, **xác suất mà khoảng tin cậy thực**
**sự chứa tham số.(1-α)**

(VD) Trong trường hợp độ tin cậy là 95%, nếu thời gian phát huy hiệu quả sau khi uống Aspirin
được ghi lại 100 lần, thì ít nhất 95 lần phải thuộc khoảng tin cậy ước lượng.




Lỗi bác bỏ ‘giả thuyết không’ khi nó đúng.

(VD) Aspirin A và B có thời gian phát huy hiệu quả là như nhau. Xác suất xác định rằng thời
gian phát huy hiệu quả là khác nhau.

~~Xác~~ ~~suất~~ ~~xác~~ ~~định~~ ~~sản~~ ~~phẩm~~ ~~tốt~~ ~~là~~ ~~sản~~ ~~phẩm~~ ~~lỗi.~~



            Tỷ lệ cho phép tối đa phạm lỗi loại 1.

( 예 ) Aspirin A và B có thời gian phát huy hiệu quả là giống nhau, giá trị tối đa cho phép xác suất đánh
giá sai rằng thời gian phát huy hiệu quả là khác nhau.
※Mức ý nghĩa : thường là 5%.




**Dựa trên giá trị thống kê kiểm định, nếu giả thuyết không là đúng, và chúng ta kết**
**luân rằng nó sai, P-Value là giá trị xác suất tối đa mà phán đoán của chúng ta sai.**

(VD) Giá trị xác suất để xác định rằng thời gian phát huy hiệu quả của Aspirin A và B là khác nhau mặc dù chúng
là như nhau.

**Giá trị tính từ lượng thống kê của mẫu → Giá trị chuẩn hóa(Z, t, F, χ** **[2]** **)**

(VD) Aspirin A và B có cùng thời gian phát huy hiệu quả, nhưng lấy giá trị chuẩn hóa (Z) cho thời
điểm phát huy tác dụng khi dùng Aspirin B.


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
80

 **Thuật ngữ liên quan đến kiểm định giả thuyết**

                  Lỗi loại 2 (β) Lỗi chấp nhận ‘giả thuyết không’ khi nó sai.

<VD> Xác suất cho phép tối đa để chẩn đoán rằng thời gian phát huy hiệu quả của Aspirin A và B
là như nhau, mặc dù chúng là khác nhau.




- ‘ ’
Giả sử giả thuyết không là sai. Xác suất phán định rằng giả thuyết không là sai.
Tức là, xác suất phát hiện sự khác biệt khi ‘Giả thuyết không; khác với thực tế. (Biểu thị
bằng 1-β)

<VD> Aspirin A và B có thời gian phát huy hiệu quả khác nhau, xác suất đánh giá đúng rằng
‘thời gian phát huy hiệu quả là khác nhau’ .


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
81

**Kiểm định giả thuyết dựa vào phân tích mang tính thống kê là so sánh mức ý nghĩa**
**với P-Value, khoảng tin cậy, lượng thống kê được tính toán dựa trên data của mẫu**
**để đưa ra giả thuyết.**



Giả thuyết nghịch Lựa chọn công cụ phân tích thống kê phù hợp để kiểm định giả thuyết

~~Chọn~~ ~~phương~~ ~~pháp~~ ~~phân~~ ~~tích~~ (Xem xét loại data, số lượng nhân tố/mức độ, phép thử trung

bình/phương sai)







- |Thống kê kiểm định| ＞ |Giá trị tới hạn|




Thống kê kiểm định được dùng trong phân tích thống kê : Z, t, F, χ [2]

Khoảng tin cậy được quyết định dựa trên mức ý nghĩa được thiết lập.

ex) Khi mức ý nghĩa là 5% : tính khoảng tin cậy 95% với độ tin cậy

95%

Lựa chọn giả thuyết nghich (Ha)

(Có sự khác biệt đáng kể)

Lựa chọn giả thuyết không (Ho)
(Không có sự khác biệt đáng kể)


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
82

 **Tiêu chí lựa chọn giả thuyết** **(dự trên kiểm định hai phiá với giả thuyết nghịch “≠”)**

**①** **So sánh lượng thống kê kiểm điểm,** **②** **So sánh sử dụng khoảng tin cậy,** **③** **So sánh P-Value và mức ý nghĩa (α)**

**①** **Kiểm định giả thuyết dựa vào thống kê kiểm định**

       |Thống kê kiểm định| ≤ |Giá trị tới hạn (critical value)| : chọn H o, bác bỏ H a

       - | Thống kê kiểm định | ＞ | Giá trị tới hạn | : loại bỏ H o, chọn H a



|hống kê kiểm định<br>H<br>H<br>a<br>o|Thống kê ki<br>H<br>a|
|---|---|
|||


**Giá trị tới hạn** **Giá trị tới hạn**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
83

 **Tiêu chí lựa chọn giả thuyết** **(dự trên kiểm định hai phiá với giả thuyết nghịch “≠”)**

**②** **Kiểm định giả thuyết sử dụng khoảng tin**
**cậy**

       Nếu ‘giả thuyết không’ nằm trong khoảng tin cậy : chọn H o, bác bỏ H a

       Nếu ‘giả thuyết không’ không nằm trong khoảng tin cậy : bác bỏ H o, chọn H a

**H**
**o**


|Col1|Col2|
|---|---|
|Khoảng tin cậy||


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
84


**Chọn H** **a**

**Chọn H** **o**

**Chọn H** **o**

**Chọn H** **a**

 **Tiêu chí lựa chọn giả thuyết** **(dự trên kiểm định hai phiá với giả thuyết nghịch “≠”)**

**③** **Kiểm định giả thuyết sử dụng P-Value**











**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
85

**Ví dụ**

**Nhân viên mới của LG Display, NaLG, đang muốn xác nhận xem có nên dùng aspirin B hay không dựa**

**trên dữ liệu thử nghiệm lâm sàng.**

**(Biết độ lệch chuẩn về thời gian phát huy hiệu quả của Aspirin là 10)**

H
o : Thời gian phát huy hiệu quả của Aspirin B là 120 phút.

H a : Thời gian phát huy hiệu quả của Aspirin B không phải là 120 phút.

          Kịch thước mẫu : 4 người

          - ~~T~~ rung ~~bì~~ n ~~h~~ m ~~ẫ~~ u : ~~125~~ p ~~h~~

          Độ lệch chuẩn mẫu : 9ph



Độ lệch chuẩn tổng thể: 10ph

Mức ý nghĩa : 5%


**H** **a**


**H** **0** **H** **a**





1) Định luật giới hạn trung tâm : Nếu phương pháp lấy n mẫu từ một tổng thể ngẫu nhiên có trung bình μ và độ lệch chuẩn σ được lặp lại vô số lần, thì trung bình mẫu có phân
phối chuẩn với giá trị trung bình là μ, độ lệch chuẩn σ/ 𝑛 .

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
86

**Nhân viên mới của LG Display, NaLG, đang muốn xác nhận xem có nên dùng aspirin B hay không**
**dựa trên dữ liệu thử nghiệm lâm sàng.**
**Ví dụ**
**(Biết độ lệch chuẩn về thời gian phát huy hiệu quả của Aspirin là 10)**


**H** **0** **H** **a**



**H** **a**



~~[=]~~ ~~[𝟓ph]~~










**2.5%** **β/2** **β/2** **2.5%**








**Value**





         - **Thống kê kiểm định Z-Value** **±** **1.0** **＜** **Giá trị tới hạn** **±** **1.96, P-Value 0.318** **＞** **0.05 : Chọn giả thuyết không.**

→ **Thời gian phát huy hiệu quả của Asparin B là 120ph**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
87

**3.1. Kiểm định giả thuyết thống kê :** **Đưa ra quyết định mang tính thống kê– Sự khác biệt**


**Nếu không có sự khác biệt đáng kể giữa các nhóm**


**Nếu có sự khác biệt đáng kể giữa các nhóm**


≒


**(Biến động các nhóm** ≒ **Biến động trong nhóm),**
**→ “Không có sự khác biệt đáng kể”**



**Y**

**Biến động**

**các nhóm**


**Y**

**Biến động**

**các nhóm**


|Col1|(Biến động các nhóm Biến động trong → “Có sự khác biệt đáng kể” ≫|
|---|---|
||Biến độ<br>trong n<br>Biến động<br>trong nhóm|
|||
|||


**X**



**Biến động**
**trong nhóm**

**X**


|Y|Col2|Col3|
|---|---|---|
||||
||||
||||


**Hiểu về phân phối chọn mẫu và áp dụng thống kê kiểm định để tính toán xác suất (p-Value) và đưa ra quyết**
**định dựa trên xác suất thu được.**


**Biến động các nhóm**

**Biến động trong nhóm**


**= Thống kê kiểm định(test statistic)** [1)]


**Xác suất (probability, p-Value)**


1) Là thống kê được sử dụng để xác định phân phối xác suất nhằm kiểm định giả thuyết thống kê.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
88

 **Loại hình**














**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
89


**One-Sample Z-Test : So sánh giá trị trung bình của một nhóm có bằng một gái trị cụ thể**

**Ví dụ**
**hay không (khi biết độ lệch chuẩn tổng thể).**

Giá trị đặc trưng của một linh kiện dùng cho TV có chiều dài ( ㎛ ) và linh kiện được thiết kế với mục tiêu là 300 ㎛ .

Chọn 100 mẫu linh kiện (sampling) và đo chiều dài, ta có giá trị trung bình 303 ㎛, độ lệch chuẩn 10 ㎛ .

Dựa trên dữ liệu lấy mẫu, người ta muốn kiểm tra xem chiều dài trung bình của linh kiện có phải là 300 ㎛ hay

không (Spec : 300 ± 20 ㎛ )

=
(Thông thường độ lệch chuẩn của linh kiện là 9, α 5% )

**①** **Có giống 300** **㎛** **không ? (Kiểm tra hai phía)**

**②** **Có lớn hơn 300** **㎛** **không ? (Kiểm tra một phía)**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
90

**①** **Trường hợp kiểm tra hai phía**

**Stat > Basic Statistics > 1-Sample Z (ex : kiểm tra 2 phía)**



**Mức ý nghĩa dưới 5%**
**Trung bình tổng thể của linh kiện khác giả**
**thuyết không (khác 300) → chọn giả thuyết**
**nghịch.**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
91

**②** **Trường hợp kiểm tra một phía**

**Stat > Basic Statistics > 1-Sample Z (ex : kiểm tra 1 phía)**



**Mức ý nghĩa dưới 5%,**
**Trung bình tổng thể của linh kiện khác giả**
**thuyết không (lớn hơn 300)**
**→ Chọn giả thuyết nghịch**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display** **92**
92

**Hong Gil-Dong, chịu trách nhiệm về bộ phận chất lượng, dự định sử dụng kiểm định giả thuyết thống kê đã học**


**Ví dụthực hành**


**trong khóa BB để xác định xem có điểm bất thường nào trong sản phẩm sau khi sản xuất thử nghiệm sản phẩm**

**mới hay không.**


>Data : 2. 기초통계 _ 평균검정 _t 검정

**Đây là thu thập ngẫu nhiên để kiểm tra tính hợp lệ của các yêu cầu mà khách hàng đã yêu cầu trong quá trình**
**phát triển.**

 - Mục tiêu của H.Length- kích thước bề ngang của kính là 36.75 và Spec là ± 4.00

 - Cùng một sản phẩm, không được có sự khác biệt giữa H.Length và A.Length sau một quá trình xử lí nhất định (Spec ± 0.50)

- Spot.25 là số lượng vết bẩn được tạo ra bằng cách chia bề mặt sản phẩm thành 25 phần bằng nhau.

- Có thể đo liên tục C.RPM, Delay.T và F.Temperature, để xác nhận sơ bộ xem có nhân tố trọng yếu hay không.

Quan sát b ~~ằ~~ ng cách phân loại thành cao/trung bình/th ~~ấ~~ p hoặc 4 ph ~~ầ~~ n b ~~ằ~~ ng nhau.





**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
93

    - **One sample t-Test: So sánh xem gía trị trung bình của một nhóm có bằng một giá trị cụ thể hay không.**

Giá trị mục tiêu của H.Length-kích thước bề ngang của Glass mà khách hàng yêu cầu là 36.75, dung sai ± 4.00.
Hong Gil-Dong BB đã thu thập ngẫu nhiên 58 tấm Glass được sử dụng trong quá trình phát triển và đo kích thước bề
ngang, chiều dài trung bình có phù hợp với mục tiêu 36.75 không?

[Thiết lập giả thuyết]
H o : Trung bình tổng thể của ‘H. Length’là 36.75. H a : Trung bình tổng thể của ‘H. Length’khác 36.75.

**Stat > Basic Statistics > One- Sample t-Test**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
94

[Thiết lập giả thuyết]
H o : Trung bình tổng thể của ‘H. Length’là 36.75. H a : Trung bình tổng thể của ‘H. Length’khác 36.75.

     Mức ý nghĩa dưới 5%, trung bình tổng thể của H.Length là 36.75.

Khi sử dụng khoảng tin cậy để kiểm tra giả thuyết, giả thuyết không
được chấp nhận vì **giá trị giả thuyết không nằm trong khoảng tin cậy.**
→ Trung bình tổng thể của H.Length là 36.75.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
95

    - **Two- Sample t-Test** : **So sánh trung bình của hai nhóm có giống nhau hay không, tiến hành kiểm định giá trị**
**trung bình sau khi kiểm tra Tính phân phối chuẩn, tính đồng nhất phương sai.**

        Về cơ bản, Minitab tiến hành kiểm định với tiền đề là kích thước phương sai là khác nhau,

vì vậy **nếu phương sai của 2 nhóm bằng nhau, hãy kiểm tra ‘giả định phương sai bằng nhau’**
→Có thể kiểm tra nghiêm ngặt hơn trường hợp ‘giả định phương sai bằng nhau’ không được thực hiện.

※ Trong hình bên dưới, trường hợp hai phương sai bằng nhau, diện tích trùng lăp giữa hai phân bố rộng nên xác suất nói
rằng các trung bình tổng thể không bằng nhau là thấp.

Nếu chọn ‘phương sai bằng nhau’ mặc dù không phải phương sai bằng nhau mà là ngược lại, thì khả năng sai sót trong ước
lượng rất cao.

**<Phương sai khác nhau>** **<Phương sai bằng nhau>**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
96

Giá trị mục tiêu của H.Length-kích thước bề ngang của Glass mà khách hàng yêu cầu là 36.75, dung sai ± 4.00.

Glass được nhập từ 2 đối tác là Supplier A và B, dự kiến sẽ có sự khác nhau về độ rộng Glass giữa 2 nhà cung cấp.

Kiểm tra xem giá trị trung bình của ‘H.Length’ có giống nhau giữa 2 nhà cung cấp hay không?

Nếu chúng không bằng nhau, hãy kiểm tra độ dài của nhà cung cấp nào gần với giá trị mục tiêu là 36.75.

[Thiết lập giả thuyết]

H o : Trung bình tổng thể về kích thước bề ngang tấm Glass của 2 nhà cung cấp là giống nhau (μ A      - μ B = 0 or μ A = μ B )

~~H~~ a ~~:~~ ~~Trung~~ ~~bình~~ ~~tổng~~ ~~thể~~ ~~về~~ ~~kích~~ ~~thước~~ ~~bề~~ ~~ngang~~ ~~tấm~~ ~~Glass~~ ~~của~~ ~~2~~ ~~nhà~~ ~~cung~~ ~~cấp~~ ~~là~~ ~~khác~~ ~~nhau~~ ~~(μ~~ ~~A~~ ~~-~~ ~~μ~~ ~~B~~ ~~≠~~ ~~0~~ ~~or~~ ~~μ~~ ~~A~~ ~~≠~~ ~~μ~~ ~~B~~ ~~)~~

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
97

 - **:**
**Two- Sample t-Test**
**①** **Kiểm tra phân phối chuẩn** → ② Kiểm tra tính đồng nhất phương sai giữa 2 nhóm → ③ Kiểm tra giá trị trung bình

**①** **Kiểm tra phân phối chuẩn**

**H** **H**
**o** **: Dữ liệu là phân phối chuẩn** **a** **: Dữ liệu không thỏa mãn phân phối chuẩn**


**Stat > Basic Statistics > Graphycal Summary**


※ Có thể sử dụng Stat > Basic Statistics > Normality Test



        Kết luận : P-Vallue nhỏ hơn mức ý nghĩa 5%
Kích thước ‘H.Length’ tấm Glass của Supply A và Supply B không thỏa mãn phân phối chuẩn (chọn giả
thuyết nghịch)

※ Lý do kiểm tra phân phối chuẩn bằng Two- Sample t-Test : để chọn phương pháp kiểm tra tính đồng nhất phương sai .

(F-Test or Levene’s Test)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
98

 - **:**
**Two- Sample t-Test**

① Kiểm tra phân phối chuẩn → **②** **Kiểm tra tính đồng nhất phương sai giữa 2 nhóm** → ③ Kiểm tra giá trị trung bình

**②** **Kiểm tra tính đồng nhất phương sai**


**H**
**o** **: Phương sai tổng thể giống nhau (σ** **[2]**


**A** **[ = σ]** **[2]**


**H**
**B** **[)]** **o** **: Phương sai tổng thể khác nhau (σ** **[2]**


**A** **[ ≠ σ]** **[2]**


**B** **[)  ]**


※ Trường hợp có 3 đối tượng so sánh, H o “Có ít nhất 1 cái khác những cái còn lạ

**Stat > ANOVA > Test for Equal Variances**

Khẳngng định kết quả Levene Test do vi phạm phân phối chuẩn → Mức ý nghĩa dưới 5%, phương sai của
2 nhóm là như nhau (chọn giả thuyết không)


Note



- Kiểm tra phân phối chuẩn ① 2 nhóm là phân phối chuẩn → F-Test (or Bartlett)
② Có ít nhất 1 nhóm không phải là phân phối chuẩn → Levene Test

Khi kiểm tra tính đồng nhất phương sai nhưng 2 nhóm có phương sai khác nhau, kiểm tra được thực hiện mà không check vào phần ‘ kiểm
tra tính đồng nhất phương sai’.



                 Trường hợp phương sai bằng nhau nhưng lại không check chọn ‘kiểm tra tính đồng nhất’ thì khả năng ‘kiểm định giá trị trung bình’ sai là rất

**LG Display DX Black Belt 과정** cao. **, Copyright@2023, LG Display**
99

 - **:**
**Two- Sample t-Test**

① Kiểm tra phân phối chuẩn → ② Kiểm tra tính đồng nhất phương sai giữa 2 nhóm → **③** **Kiểm tra giá trị trung bình**

**③** **Kiểm tra giá trị trung bình**

H o : Trung bình tổng thể về kích thước tấm Glass của 2 nhà cung cấp là giống nhau. (μ A    - μ B = 0 or μ A = μ B )
H a : Trung bình tổng thể về kích thước tấm Glass của 2 nhà cung cấp là khác nhau (μ A    - μ B ≠ 0 or μ A ≠ μ B )

**Stat > Basic Statistics > Two- Sample t-Test**




✓ 등분산이확인되었다면 “ 등분산가정 ” 을반드시 check!


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
100

 - **:**
**Two- Sample t-Test**

① Kiểm tra phân phối chuẩn → ② Kiểm tra tính đồng nhất phương sai giữa 2 nhóm → **③** **Kiểm tra giá trị trung bình**

H o : Trung bình tổng thể về kích thước tấm Glass của 2 nhà cung cấp là giống nhau. (μ A  - μ B = 0 or μ A = μ B )

H
a : Trung bình tổng thể về kích thước tấm Glass của 2 nhà cung cấp là khác nhau (μ A       - μ B ≠ 0 or μ A ≠ μ B )

**Kết quả**




① Giá trị mục tiêu (=0) của ‘μ A – μ B ‘ nằm trong phạm vi 95%

② P-Value lớn hơn 0.05

→ Mức ý nghĩa dưới 5%, không có sự khác biệt về giá
trị trung bình tổng thể của 2 nhà cung cấp.
(Chọn giả thuyết không)


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
101

※Paired t-Test được sử dụng khi dữ liệu không độc lập

    - **Paired t-Test: Được sử dụng nếu dữ liệu được lặp đi lặp lại hoặc được đo đồng thời từ một thực thể/ đối tượng.**

Hong Gil-Dong BB phản ánh kích thước tấm Glass trong công đoạn tiếp theo bằng với sự thay đổi bề ngang tấm Glass sau khi công đoạn xử lý

nhiệt được thực hiện lên tấm Glass,

Chúng tôi muốn ngăn chặn trước các vấn đề có thể xảy ra trong công đoạn tiếp theo.

      - ‘H.Length’ là giá trị đo bề ngang của tấm Glass trước khi xử lý nhiệt.

      - ‘A.Length’ là giá trị đo bề ngang của tấm Glass sau khi xử lý nhiệt.

Chúng tôi muốn kiểm tra xem quá trình xử lý nhiệt có ảnh hưởng đến kích thước của tấm Glass hay không. Có thể nói rằng kích thước của tấm

Glass trước và sau khi xử lý nhiệt là như nhau không?

[Thiết lập giả thuyết]

Ho : Sau khi xử lý nhiệt, Trung bình tổng thể về kích thước tấm Glass là giống nhau (μ trước - sau = 0)
Ha : Sau khi xử lý nhiệt, Trung bình tổng thể về kích thước tấm Glass là khác nhau (μ trước - sau ≠ 0)

**Stat > Basic Statistics > Paired t-Test**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
102

Ho : Sau khi xử lý nhiệt, Trung bình tổng thể về kích thước tấm Glass là giống nhau (μ trước - sau = 0)
Ha : Sau khi xử lý nhiệt, Trung bình tổng thể về kích thước tấm Glass là khác nhau (μ trước - sau ≠ 0)

|Col1|Kết quả|
|---|---|
|||



Với P-value 0.153, mức ý nghĩa 5%, rất khó để xác định rằng có sự khác biệt về trung bình tổng thể kích thước tấm
Glass sau khi xử lý nhiệt.
Tuy nhiên, sau khi kiểm tra bằng biểu đồ đã tìm thấy điểm bất thường.
→Những giá trị bất thường có sự khác biệt rất lớn hoặc rất nhỏ thì cần điều tra nguyên nhân.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
103

**Sau khi xác định được nguyên nhân cảu Outlier, đưa ra quyết định có nên loại bỏ hay không.**

Kết quả sau khi tham khảo Resume data, hầu hết các bất thường xuất hiện sau khi điều chỉnh công đoạn/quy trình.
Do đó, người ta quyết định thêm điều này vào tiêu chuẩn quản lý quy trình để điểu tra thêm. Người ta đánh gía rằng việc
không phản ánh điều này là phù hợp vì đây là tính huống đặc biệt, cuối cùng họ đã quyết điinhj loại bỏ các giá trị bất
thường.
※ Không được lloại bỏ giá trị bất thường nếu không có cơ sở thực



tế.

|Col1|Col2|Kết quả|
|---|---|---|
||||


Mức ý nghĩa dưới 5%, P-Value 0.000, có thể đánh giá rằng có sự khác biệt về trung bình tổng thể của kích
thước tấm Glass sau khi xử lý nhiệt (chọn giả thuyết nghịch)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
104

**Điều gì xảy ra khi bạn kiểm tra trung bình giữa 2 nhóm cặp bằng Two-Sample t-Test?**

**Kết quả kiểm tra Two-Sample t-Test**

Mức ý nghĩa dưới 5%, không giống với kết quả thử nghiệm bằng Paired t-Test, với kết quả P-Value 0.628 thì
không thể đánh giá rằng có sự khác biệt. (chọn giả thuyết không).

※ Nên sử dụng các phương pháp phân tích thích hợp để phản ánh chính xác môi trường thu thập dữ liệu.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
105

 **Loại hình**


**Tham**

**khảo**
















**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
106


   **Phân tích phương sai (ANOVA : analysis of variance)?**

     Phương pháp phân tích liệu có sự khác biệt về trung bình giữa hai hay nhiều nhóm.

     Phân tích độ lớn tổng biến động gap giữa trung bình các nhóm và trung bình toàn thể

phương sai của toàn bộ các nhóm, bằng cách so sánh sự phân tán của các trung bình

mẫu trong mỗi nhóm.

→ Sử dụng phân phối F.

※Giả sử rằng các nhóm so sánh có cùng phương sai (cần ‘kiểm tra tính đồng nhất

phương sai’)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
107

 **Mục đích**

**Có thể kiểm tra sự khác biệt về trung bình giữa 2 hoặc nhiều nhóm và đưa ra thứ tự ưu tiên cải tiến.**

     Kiểm tra tầm quan trọng của từng yếu tố X đối với giá trị kết quả Y bằng P-Value, và tính toán mức độ đóng góp

vào biến động của giá trị Y đối với mỗi nhân tố X thông qua kết quả ANOVA trong phân tích DOE và phân tích hồi quy.

 **Khái niệm**

Lượng biến động trong dữ liệu mẫu được chia thành ① Biến động giữa các nhóm do các biến độc lập ②
~~Biến~~ ~~động~~ ~~trong~~ ~~nhóm~~ ~~được~~ ~~coi~~ ~~là~~ ~~xảy~~ ~~ra~~ ~~ngẫu~~ ~~nhiên~~ .

→
2 nhóm có thể được cho là khác nhau nếu biến động giữa các nhóm lớn hơn đáng kể so với biến

.
động trong nhóm


**Y**








_y_




**X**

|Col1|Col2|Col3|ng nhóm|Col5|
|---|---|---|---|---|
|x<br>y<br>x 3<br>x<br>x<br>x x|x<br>y<br>x 3<br>x<br>x<br>x x|x<br>y<br>x 3<br>x<br>x<br>x x|B|iến độn|
|x<br>y<br>x 3<br>x<br>x<br>x x|x<br>y<br>x 3<br>x<br>x<br>x x|x<br>y<br>x 3<br>x<br>x<br>x x|||
|y<br>x x<br>y 2 x<br>1<br>x<br>x<br>x<br>x|y<br>x x<br>y 2 x<br>1<br>x<br>x<br>x<br>x|y<br>x x<br>y 2 x<br>1<br>x<br>x<br>x<br>x|||
|x|||||

**1** **2** **3**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
108

 **Phân phối F**

   Tỷ lệ biến động giữa các nhóm và biến động trong nhóm (biến động giữa các nhóm:biến động trong

nhóm) tuân theo phân phối F, là phân phối xác suất của phương sai mẫu.

   Nếu biến động giữa các nhóm lớn hơn đáng kể so với biến động trong nhóm, thì sẽ thiên về phần

đuôi phía bên phải và giả thuyết nghịch được chấp nhận.

→
**Có thể suy luận/kiểm định thống kê.**





**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
109

**Biến động tổng thể trong ANOVA được chia thành biến động giữa các nhóm (biến động**

**giữa các yếu tố) và biến động trong nhóm (biến động do sai số).**

  **Cấu tạo của biến động**




Biến động giữa các nhóm

(SS X )

Biến động toàn bộ


~~Biến~~ ~~động~~ ~~trong~~ ~~nhóm~~

(SS error )


(SS total )



|𝒙ഥ<br>SS<br>total|𝒙ഥ<br>1 i|SS<br>X<br>S<br>E|
|---|---|---|
|𝒙ഥ<br>SS<br>total|𝒙ന<br>S|𝒙ന<br>S|



**Thống kê kiểm định**


_SS_ _x_ / _df_ _x_ _MS_ _x_
= =


/ _df_ _x_ _MS_ _x_ ※ SS(sum of squares) : biến động

= = _F_

/ _df_ _error_ _MS_ _error_ ( _df_ _x_ _df_, _error_ ) DF(degree of freedom) : Bậc tự do
MS(mean of square) : Biến động trung bình (phương sai)


_SS_ _x_ / _df_ _x_ _MS_
=

_SS_ _error_ / _df_ _error_ _MS_


_x_ _x_ _x_

= = _F_

/ _MS_


※ SS(sum of squares) : biến động


_x_


DF(degree of freedom) : Bậc tự do


_error_ _error_


( _df_ _x_ _df_, _error_

_error_


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
110

**Phân tích phương sai (ANOVA) sử dụng bảng phân tích phương sai để tiến hành phân tích**

**sự khác biệt đáng kể về các yếu tố (nhân tố)**

    **Cấu trúc cơ bản bảng ANOVA:**

      - Bảng phân tích phương sai về nhân tố A, một số mức nhân tố a, tổng số thử nghiệm N.

|Nguồn|df|SS|MS|F|P|
|---|---|---|---|---|---|
|Hiệu quảA|a – 1|SS<br>A|MS = SS / df<br>A A A|MS / MS<br>A error||
|Error|N - a|SS<br>error|MS = SS / df<br>error error error|||
|Total|N – 1|SS<br>T||||



**- df** (degree of freedom, Bậc tự do) : số biến có thể thay đổi tự do hoặc số bậc trong một biến, thường là ‘ Số Data – 1’ or ‘số bậc – 1’.

**- SS** (sum of squares) : tổng bình phương, tổng bình phương độ lệch giữa các giá trị đo riêng lẻ với giá trị trung bình trong mẫu.

         - **MS** (mean of squares) :Giá trị có được khi chia tổng bình phương bậc tự do với trung bình bình phương, thường có ý nghĩa như phương sai mẫu.

         - **F** : Thống kê kiểm định, là tỷ lệ giữa biến động trung bình của nhân tố với biến động trung bình của sai số (error)

Biến động trung bình của nhân tố so với biến động trung bình của sai số (error) càng lớn thì giá trị F càng cao.

※ ANOVA

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
111

 - **Phân tích phương sai (ANOVA ; analysis of variance) Tính toán và phân tích thủ công**


**Phân tích sự khác biệt về lượng tĩnh điện (ESD)- là CTQ, về mức biến động**

**theo loại POL (A,B<C) trong mức biến động tổng thể. Hãy vẽ bảng phân tích**

**phương sai.**

**①** **Tìm bậc tự do**


|POL A|POL B|POL C|
|---|---|---|
|47|46|45|
|49|45|43|
||47||
||46||


※ Y : lượng tĩnh điện, X : loại POL (A ~ C)


|Nguồn|df|SS|MS|F|P|
|---|---|---|---|---|---|
|POL|2 = (3 – 1)|||||
|Error|5 = (7 – 2)|||||
|Total|7 = (8 – 1)|||||


**②** **Tìm SS**

|Nguồn|df|SS|MS|F|P|
|---|---|---|---|---|---|
|POL|2|16.0||||
|Error|5|6.0||||
|Total|7|22.0||||



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
112

   - **Phân tích phương sai (ANOVA ; analysis of variance) Tính toán và phân tích thủ công**

**③** **Tìm MS**

|Nguồn|df|SS|MS|F|P|
|---|---|---|---|---|---|
|POL|2|16.0|8.0 = 16.0 / 2|||
|Error|5|6.0|1.2 = 6.0 / 5|||
|Total|7|22.0||||



**④** **Tìm F**

|Nguồn|df|SS|MS|F|P|
|---|---|---|---|---|---|
|POL|2|16.0|8.0|6.67 = 8.0 / 1.2||
|Error|5|6.0|1.2|||
|Total|7|22.0||||



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
113

   **ANOVA khác nhau về phương pháp phân tích tùy thuộc vào số lượng nhân tố, số mức độ và số lần**
**lặp lại của mỗi mức độ có giống nhau hay không.**




Phương pháo kiểm tra giá trị trung bình cộng của hai hay nhiều đối tượng so sánh.

      Khi 1 yếu tố có nhiều hơn 2 mức độ

      - Được sử dụng khi số lần lặp trên mỗi mức độ là như nhau





**Tìm hiểu thuật ngữ**



Được sử dụng khi cân bằng hoặc không cần bằng theo mỗi mức độ.



         **Nhân tố (factor)** : là nguyên nhân trong vố số nguyên nhân được cho là có ảnh hưởng đến kết quả gía trị
Y, nguyên nhân được phản ánh trong thí nghiệm,

         - **Mức độ (level)** : điều kiện của nhân tố để tiến hành thí nghiệm ex. 2 mức độ (10s/ 20s),  3 mức độ (100 độ/
200 độ/ 300 độ)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
114

**1) Phân tích Anova 1 yếu tố** **: Khi 1 nhân tố có 2 mức độ trở lên**

Khi bóc film bảo hộ POL trong công đoạn Module, thường xuyên xảy ra lỗi mạch do tính điện.
Trong số các nhân tố tiềm ẩn gây ra sự số hỏng mạch, kiểm tra xem có sự khác biệt về lượng tính điện (ESD) tùy
thuộc vào từng loại POL hay không. Kiểm tra xem lượng tĩnh điện có bị ảnh hưởng bởi loại POL hay không.?

>Data : 3. 기초통계 _ 평균검정 _ 분산분석 1


Note



Phải tiến hành kiểm tra phân phối chuẩn và tính đồng nhất phương sai trước khi phân tích ANOVA và phải

thõa mãn rằng phương sai là bằng nhau.

**Kết quả phải là phân phối chuẩn và phương sai phải bằng nhau** (p-Value 0.861)


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
115

**1) Phân tích Anova 1 yếu tố** **: Khi 1 nhân tố có 2 mức độ trở lên**


**Stat> ANOVA > One-Way**


**Kết quả**



      Kết luận : Mức ý nghĩa dưới 5%, P-Value 0.014, lượng tĩnh điện thay đổi tùy thuộc vào loại POL (chọn giả thuyết nghịch)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
116

**2) Mô hình tuyến tính tổng quát :** **Khi có 2 nhân tố nhưng không cân bằng theo mỗi mức độ**

Hong Gil-Dong BB, người đã xác nhận rằng có sự khác biệt về lượng tĩnh điện tùy thuộc vào từng loại POL
(công ty A/B/C), trong số các nhân tố tiềm ẩn ảnh hưởng đến lượng tĩnh điện, tiến hành phân tích thêm về các

㎜
yếu tố như độ dày POL (0.10/0.15 ), có hay không việc sử dụng ionizer.

>Data : 3. 기초통계 _ 평균검정 _ 분산분석 1

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
117

**Stat> ANOVA > Genetal Linear Model >Fit Genetal Linear Model**


**Kết quả**



     - Kết luận : **Mức ý nghĩa dưới 5%, P-Value 0.024, loại POL có ý nghĩa nhưng độ** **dày POL và việc có sử** **dụng Ionizer hay**
**không lại không có ý nghĩa.**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
118

 **Loại hình**


**Tham**

**khảo**
















**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
119


**Phân tích tương quan là một thống kê nghiên cứu mối quan hệ tuyến tính giữa 2 biến, ta**
**nói rằng có mối tương quan khi tồn tại mối quan hệ giữa sự thay đổi của X và sự thay đổi**
**của Y.**

  **Thiết lập giả thuyết**

    - **H** **H**
**o** **: Hệ số tương quan giữa 2 biến là 0 (ρ = 0),** **a** **: Hệ số tương quan giữa 2 biến khác 0 (ρ ≠ 0)**

  **Quy trình phân tích**

    Phân tích biểu đồ: Sử dụng Scatter plot.

    Phân tích thống kê : Phân tích tương quan (hệ số tương quan r)



**Hệ số tương quan (r)**

_n_


_i_ − _i_ −

_S_ ( _xy_ ) _i_ = 1

= =


_xy_


( _xy_ )





_i_


( _x_ − _x_ )( _y_ − _y_ )


_x_ _i_ − _x_ _y_ _i_ − _y_


_i_ _i_


_S_ ( _xy_ ) _i_ = 1
_r_ = = =


_S_


1


=



**Tiêu chuẩn phán định (Dựa trên gái trị tuyệt đối)**









_S_ _S_

_x_ _y_










|< 0.4|Không tương quan (little if any correlation)|
|---|---|
|0.4 ~ 0.8|Mối tương quan thấp (low correlation)|
|> 0.8|Mối tương quan cao (high correlation)|



    **Đặc điểm**

       Phạm vị giá trị r là -1 ≤ r ≤ 1

       - ±
Giá trị r là thước đo mối quan hệ tuyến tính giữa X và Y. Khi r = 1, tất cả các điểm đều nằm trên một đường thẳng.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
120

**Trước khi kiểm tra mối tương quan giữa hai biến, cần kiểm tra trước bằng biểu đồ**

**phân tán** **(scatter plot).**

     **Phương pháp giải thích bằng biểu đồ phân tán (scatter plot)**

        **Kiểm tra xem có mối quan hệ tuyến tính giữa X và Y từ hình dạng các điểm nằm rải rác hay không**

và kiểm tra xem đó là mối tương quan thuận (positive) hay nghịch (negative) (hình 1,2).

        **Kiểm tra X và Y có mối quan hệ tuyến tính hay quan hệ đường cong**
trong trường hợp quan hệ đường cong như hình (3) thì việc tìm hệ số tương quan là vô nghĩa.
→ Tiến hành phân tích hồi quy đường cong.

        **Kiểm tra xem có điểm bất thường hoặc sự phân tầng nào không.**
Nếu có điểm bất thường trên biểu đồ phân tán, hãy xác định nguyên nhân và khắc phục chúng.
→ Nếu có nghị ngờ về sự phân tầng, cần phân tích phân tầng bằng cách resume data (hình 4,5).

**Ví dụvề vẽ biểu đồ phân tán**

(1) Tương quan dương (2) Tương quan âm (3) Tương quan cong (4) Điểm bất thường (5) Phân tầng

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
121

**Phân tích tương quan là phân tích mối quan hệ** **tương quan giữa 2 biến và** **không thể** **đảm bảo**
**mối quan hệ** **nhân quả.**

  **Định nghĩa mối quan hệ** **nhân quả** **và mối quan hệ** **tương quan**

    Mối quan hệ tương quan : mối quan hệ giữa hai biến khi một trong số chúng tăng hoặc giảm khi biến kia tăng.

    - Quan hệ nhân quả : đề cập đến mối quan hệ nguyên nhân và kết quả giữa 2 biến.

  - **Khác biệt giữa mối quan hệ** **tương quan và mối quan hệ** **nhân quả**

    Quan hệ tương quan là quan hệ sau khi đo lường dữ liệu và Quan hệ nhân quả là quan hệ cơ chế trước khi đo lường dữ liệu.

    - Quan hệ tương quan đơn giản chỉ ra rằng có một mối quan hệ giữa 2 biến.

    Quan hệ nhân quả được thêm 2 điều kiện vào quan hệ tương quan

     - Đầu tiên, đièu kiện tiền đề về thời gian là nguyên nhân luôn có trước kết quả.

     - Thứ 2, điều kiện loại trừ tương quan giả- tương quan không đúng do ảnh hưởng của biến thứ 3.

Số lượng tội phạm


Số lượng nhà thờ


**Think!**


Thành phố Go-tam đang đấu tranh để giảm tội phạm bạo lực.
Theo kết quả phân tích dữ liệu, người ta thấy rằng số lượng nhà
thờ tăng lên, dân số tăng lên và khi dân số tăng lên thì tội phạm
bạo lực cũng tăng lên. Quan điểm của bạn về vấn đề này là gì?


Dân số


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
122

**[Ví dụ] Hãy cải tiến kết quả hệ số truyền !**

Tiến hành điều tra 5 thành phần ảnh hưởng đến hệ số truyền của sản phẩm (response).
Việc thử nghiệm sau khi điều chỉnh trước 5 thành phần riêng lẻ là rất khó khăn, vì vậy chọn ngẫu nhiên 26 sản phẩm,
và phân tích các thành phần chứa trong các sản phẩm này.
Các nhà điều tra phân chia các nhân tố (thành phần) trọng yếu có ảnh hưởng quan trọng và thử xác nhận xem liệu có
thể đạt được 80% mức độ truyền so với giá trị tiêu chuẩn của các nhân tố quan trọng được chọn về mặt kĩ thuật hay
không.

>Data : 5. 기초통계 _ 관계검정 _ 상관, 회귀분석





**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
123

**①** **Khảo sát tương quan tuyến tính giữa các biến (phân tích biểu đồ)**

**Graph > Scatteplot> Simple**

                                 Response và lng1~lng3 dự kiến sẽ có mối tương quan cao ( ① )

                                 lng4 dự kiến hầu như không tương quan ②

                                 lng5 dự kiến mối tương quan thấp ( ③ )

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
124

**②** **Khảo sát tương quan tuyến tính giữa các biến (phân tích tương quan)**

**Stat > Basic Statistics > Correlation**

                                 Người ta đánh giá rằng lng1~lng3 có mối quan hệ tương qua chặt chẽ,
lng4 không có mối tương quan.

                                 lng5 có mối tương quan thấp, lng1 có mối tương quan cao, còn lại
2,3,4 không có mối tương quan.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
125

**Phân tích hồi quy là dự đoán một phương trình toán học nào đó từ một dữ liệu về mối tương**
**quan giữa các biến cố khi cố gắng cải thiện vấn đề, và đưa ra dự đoán cần thiết hoặc suy luận**
**mang tính thống kê về các lĩnh vực có quan tâm.**



**Thiết lập giả thuyết**

   - **H** **o** **: β(hệ số hồi quy: độ nghiêng) = 0,   H** **a** **: β(hệ số hồi quy : độ nghiêng) ≠ 0**

**Mục tiêu sử dụng**

  Để tìm nhân tố trọng yếu (vital few).

   Để ước lượng và dự đoán giá trị ‘Y’ .

  - Đ ~~ể~~ quy ~~ế~~ t định gía trị ‘Y’ được t ~~ố~~ i ưu hóa từ một giá trị hệ s ~~ố~~ ‘X’ nào đó.

**Quy trình**


_E_ ( _Y_ ) = + 0  1 _X_


**Thiết lập mô hình hồi quy** **Đưa ra mô hình hồi quy** **Dự đoán mô hình hồi quy**



Tuyến tính hoặc phi tuyến tính

: phân tích biểu đồ( biểu đồ phân tán)



Ý nghĩa hồi quy : P-Value

Kiểm định thiếu phù hợp (lack-of-fit)

: P-Value

- **Khả năng giải thích của phương**
**thức hồi quy : R** **[2]**

Đa cộng tuyến (VIF)



- Phân tích Residual

: tính phân phối chuẩn, tính đồng nhất phương sai,

tính độc lập.


: Chỉ phân tích hồi quy đa tuyến

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
126

 **Loại hình**

    **Hồi quy tuyến tính cơ bản:**
: Khi mối quan hệ hàm số là tuyến tính, và có một biến độc lập và một biến
phụ thuộc.
(VD) Chuyển màu của OLED TV = f(cường độ dòng diện)

    **Hồi quy tuyến tính bội**
: Khi mối quan hệ hàm số là tuyến tính, và có 2 biến cố độc lập và một biến cố
~~phụ~~ ~~thuộc~~ .
(VD) Giá cổ phiếu = f(lợi nhuận kinh doanh, doanh thu,…)

    **Hồi quy phi tuyến tính** : Khi mối quan hệ hàm số là quan hệ cong (phi tuyến
tính)







       **Hồi quy Logistic** : Nếu X là dữ liệu liên tục nhưng Y là dữ liệu rời rạc.
(VD) Xuất hiện lỗi hay không = f(cường độ dòng điện)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
127

**Tổng biến động của data được chia thành biến động sai được giải thích dựa trên đường hồi quy**
**và biến động dựa trên sai số không được giải thích bởi đường hồi quy.**

**Tổng biến động (SST) = Biến động hồi quy (SSR) + biến động sai số (SSE)**

Biến động không

được giả thích





Biến động không

được giả thích

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||Tổng<br>biến<br>động<br>của<br>dữ<br>liệu||Biến<br>động<br>được<br>giải<br>thích<br>bởi<br>đường<br>hồi<br>quy||
||||||



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
128

 - **Hệ số xác định (R** **[2]** **)**

    **Thang đo giải thích biến động của phương trình hồi quy chiếm bao nhiêu phần trăm của tổng biến**

**động (Khả năng giải thích).**

   - Có một vấn đề là Khả năng giải thích bị thổi phồng ngay cả khi số lượng các yếu tố (biến độc lập) chỉ đơn

giản là tăng lên.


**SSE**
**=** ~~**1**~~ **-**
**SST**



  - Giá trị dao động từ 0 đến 1, càng gần 1 thì Khả năng gỉai thích càng cao, và ngược lại.

※ Khả năng giải thích thấp có nghĩa là các yếu tố bổ sung ảnh hưởng đến Y (kết quả) phải được tìm ra.

- **Hệ số xác định đã được điều chỉnh (R** **[2]** **adj** **)**


~~**R**~~ ~~**[2]**~~

**=**


**SSR**

**SST**


- Thang đo xác định s ~~ố~~ bi ~~ế~~ n độc lập: s ~~ố~~ lượng bi ~~ế~~ n có hệ s ~~ố~~ xác định đã được đi ~~ề~~ u
chỉnh lớn nhất là tối ưu.

Điều chỉnh bằng cách chia Khả năng giải thích bị phóng đại do số lượng yếu tố (biến
độc lập) cho Bậc tự do.


**R** **[2]**



**[SS]** **[E]** **[ / df]** **[E]**
**adj** **[ = 1 -]**

**SS** **T** **/ df** **T**



~~**[/]**~~ ~~**[(]**~~ **[n-]** ~~**[k]**~~ **[-]** ~~**[1][)]**~~
**= 1 -** ~~**[SS]**~~ **[E]**

**SS** **T** **/ (n-1)**


Giá trị

hệ số
xác định



K : Số biến hệ số hồi quy


**Số lượng biến độc lập tối ưu**


Số lượng biến độc lập


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
129

 **Thiếu yếu tố (lack-of-fit) có nghĩa là “Xác suất không phù hợp để sử dụng mô hình hồi quy này”.**

Có thể đánh giá rằng phương trình hồi quy được ước tính tốt khi không có sự chênh lệch (thiếu) giữa y1 là giá
trị ước tính của Y khi x1 trong phương trình hồi quy với trung bình giá trị ước tính của y được đo nhiều lần khi
x1 thực tế. Nói cách khác, nó là một tiêu chí để xác định xem một mô hình hồi quy có phù hợp để sử dụng hay
không.


**y**


_Phương trình hồi quy_
_ước tính_ ˆ

_y_


_Mức trung bình X_ _i_


_y_ _i_


_Mức ước tính X_ _i_ _y_ ~~ˆ~~ _i_


**x** **i**

**Pure Error (Sai số thuần)**



※ Chỉ áp dụng với sự lặp lại (biến động sai số thuần) ở một hoặc nhiều
cấp độ của biến độc lập.


         - Khi X ở một mức Xi nhất định, y có nhiều giá trị khác nhau, nghĩa là xảy ra biến động gái trị y tại thời điểm này.

        **Lack of Fit (Thiếu yếu tố)**

         - Dữ liệu phải được đo lặp lại nhiều lần.

         - Khi X ở mức cụ thể Xi, thì trung bình của các giá trị Y khi giá trị y được ước tính trong phương trình hồi quy là Xi phải khớp phù hợp.

Lúc đó, sự khác biệt giữa giá trị y được ước tính với giá trị trung bình y được gọi là thiếu phù hợp (thiếu yếu tố).

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
130

 **Thống kê kiểm định thiếu yếu tố (lack-of-fit)**








1)Thống kê kiểm định : thống kê được sử dụng để xác định phân phối xác suất để kiểm định giả thuyết thống kê.

   **Kiểm định thiếu yếu tố (lack-of-fit)**

**Trong kiểm định thiếu yếu tố, giá trị ước lượng của phương**
**trình hồi quy được đánh giá là ước lượng tốt khi không có sự**
**chênh  lệch (thiếu) so với giá trị trung bình.**

                                    - **Tiêu chuẩn phán định : “Thiếu yếu tố” P-Value** **＞** **0.05,**
**Phương trình hồi quy phù hợp.**
※ Trường hợp nhỏ hơn 0.05, phương trình hồi quy ước lượng không phù hợp.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
131

 **Hệ số phóng đại phương sai (VIF) : Thang đo định lượng đa cộng tuyến giữa các yếu tố**
**phù hợp trong phân tích hồi quy bội.**

    **Đa cộng tuyến (multicollinearity),**
    - Hiện tượng trong đó có mối tương quan chặt chẽ giữa các biến độc lập (nhân tố tiềm ẩn) trong
phân tích hồi quy tuyến tính bội.

      **Nếu tồn tại đa cộng tuyến có thể chọn nhân tố trọng yếu sai.**

Ảnh hưởng khi tồn tại đa cộng tuyến
        - Không thể biết được sự khác biệt về hiệu quả ảnh hưởng của từng biến độc lập lên biến phụ thuộc.
        - Khi sai số chuẩn của biến tăng lên, khoảng tin cậy cũng tăng → Khả năng chấp nhận giả thuyết sai cũng tăng.



**Tiêu chuẩn đánh giá**
- VIF ≒ 1 : Rất lý tưởng
- VIF ＞ 5 : Nghi ngờ có tương quan cộng tuyến giữa các yếu tố
- VIF ＞ 10 : Có vấn đề nghiêm trọng về cộng tuyến giữa các
yếu tố


※ [Tham khảo] Mối tương quan giữa các biến càng cao thì VIF càng cao


2

_VIF_ _j_ = 1 ( 1 − _R_ _j_ ), _j_ =,1,2 , _k_

Ở đây, R [2] là ‘hệ số xác định’ được tính toán khi tiến hành

phân tích hồi quy với X j được coi là biến phản hồi y và các

biến còn lại là biến độc lập.



       **Phương pháp giải quyết**

1. Loại bỏ một hoặc một số biến độc lập có tương quan cao. Nói cách khác, loại bỏ các biến độc lập có khả năng giải thích
thấp đối với Y (CTQ).
2. Biến đổi biến số hoặc sử dụng các giá trị quan sát mới.
3. Xác định nguyên nhân của mối tương quan bằng cách xem xét tình hình hiện trạng tại nơi dữ liệu được thu thập, và giải
quyết nó.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
132

   **Tiêu chuẩn các bước đánh giá phương trình hồi quy**

**1) Sự phù hợp của mô hình hồi quy : p-value(phương trình hồi quy, tính thích hợp, hệ số hồi quy), R** **[2]** **, VIF**

① Kiểm tra ý nghĩa phương trình hồi quy : P-Value < 0.05

② Kiểm tra tính thích hợp “Thiếu yếu tố ” P-Value > 0.05

③ Kiểm tra khả năng giải thích của phương trình hồi quy : R-Squared

※Khi tối ưu hóa số lượng biến, kiểm tra R-Squared (adjusted)

④ Kiểm tra ý nghĩa hệ số hồi quy : P-Value < 0.05

⑤ Kiểm tra đa cộng tuyến trong phân tích hồi quy đa biến : VIF < 5

**2) Kết qủa chuẩn đoán mô hình hồi quy : Phân tích Residual (phân phối chuẩn, tính đồng nhất phương**
**sai, tính độc lập)**

       Kiểm tra sự bất thường thông qua biểu đồ Residual.

        Xem xét Residual

① Tính phân phối chuẩn: Residual tuân theo Phân phối chuẩn.

② Tính độc lập : Residual độc lập với nhau. Tức là, Residual không được liên quan đến nhau. (Không tồn tại mối quan hệ hiệp

phương sai)
※ Trường hợp vi phạm tính độc lập, lượng thống kê và 및 R [2] Value sẽ bị đánh giá quá cao.

③ Tính đồng nhất phương sai : Phương sai của Residual là cố định : Phương sai của giá trị Y được đo bằng giá trị X 1 (σ [2] X1 ) =
phương sai của giá trị Y được đo bằng giá trị X 2 (σ [2] X2 )

※ Nếu bất kì kết quả chuẩn đoán nào của mô hình hồi quy, tính phân phối chuẩn, tính đồng nhất về phương sai, tính độc lập bị
vi phạm thì phương trình hồi quy không thể tin cậy được.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
133

**3.3.2. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy tuyến tính đơn**

 Kết qủa chuẩn đoán mô hình hồi quy : Phân tích Residual (tính phân phối chuẩn, tính đồng nhất phương sai,
tính độc lập)

   - Biểu đồ của Residual so với giá trị thích hợp được đánh giá bằng hình dạng biểu đồ phân tán.

※ Residual so với biểu đồ thứ tự cần được kiểm tra trong trường hợp dữ liệu chuỗi thời gian.

**Trường hợp bình thường** **Quan hệ phi tuyến tính**


Residu

al

Residu

al

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
134


Residu

al

Giá trị thích hợp


Giá trị thích hợp


**Tăng/Giảm phương sai** **Quan hệ tuyến tính**

Residu

al


Giá trị thích hợp


Giá trị thích hợp

**3.3.2. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy tuyến tính đơn**

**1) Phân tích hồi quy tuyến tính đơn : Khi 1 biến độc lập/ 1 biến phụ thuộc, đưa ra phương hình quan**
**hệ toán học giữa các biến.**

Trong số 5 thành phần ảnh hưởng đến hệ số truyền (Response) của sản phẩm, tiến hành phân tích hồi quy đơn giữa hệ
số truyền và thành phần có quan hệ tương quan lớn nhất là thành phần số 3.

>Data : 5. 기초통계 _ 관계검정 _ 상관, 회귀분석

**Stat > Regression > Regression > Fit Regression Model**




**①** **Residuals for plots :** sử dụng **‘Deleted’**

         - Regular: Không được sử dụng.

        - Standardized : Sử dụng khi dữ liệu được thu thập trong các trường hợp được
kiểm soát chẳng hạn như thử nghiệm.

             - **Deleted** : Sử dụng khi dữ liệu được thu thập trong các tình huống không được
kiểm soát chẳng hạn như nghiên cứu quan sát.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
135


**②** **Residual plots**

  - Hisxtogram of residuals

  - Nomal probability plot of residuals

  - Residuals versus fits

  - Residuals versus order

**3.3.2. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy tuyến tính đơn**



Tính đồng nhất phương sai


※ Kiểm tra dữ liệu thứ 15 và 17 để xác định xem có nên đưa chúng vào phương trình hồi quy hay
không.


1) Tính thích hợp của mô hình hồi quy tuyến tính : P-Value, R-Squared, RSquared (adjusted), VIF

① Hồi quy có ý nghĩa với P-value 0.000(<0.05)
② Kết quả kiểm tra tính phù hợp P-value 0.558(>0.05)
③ Khả năng giải thích của phương trình hồi quy 71.53%(R-Squared)
④ Hệ số hồi quy (lng3) P-value 0.000(<0.05)
※ Trong phân tích hồi quy bội, cần kiểm tra lại VIF(đa cộng tuyến) ( ＜ 5)

2) Kết quả chuẩn đoán mô hình hồi quy : phân tích Residual (Tính phân phối
chuẩn, tính đồng nhất phương sai, tính độc lập)

  - Cần xác nhận ảnh hưởng của điểm bất thường.

  - Các điều kiện không bị vi phạm nhiều, nếu phân phối chuẩn có đỉnh hơi nhọn cũng
bị xác định là vấn đề.


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
136

**3.3.3. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy tuyến tính bội**

**2) Phân tích hồi quy tuyến tính bội: Khi có hai hoặc nhiều biến độc lập và một biến phụ thuộc, đưa ra**

**phương hình quan hệ toán học giữa các biến.**

**Sử dụng thành phần từ 1-5 có ảnh hưởng đến hệ số truyền của sản phẩm và đưa ra phương trình hồi quy giải thích rõ nhất cho hệ số**
**truyền** (response).

>Data : 5. 기초통계 _ 관계검정 _ 상관, 회귀분석

**Stat > Regression > Regression > Fit Regression Model**



      - **Forward selection** : Chọn theo tuần tự yếu tố đóng góp tốt nhất cho sự phù hợp hồi quy.

      - **Backward elimination** : Trong mô hình bao gồm tất cả yếu tố, các yếu tố có đóng góp nhỏ
nhất cho sự phù hợp hồi quy sẽ được loại bỏ liên tục.

      - **Stepwise regression** : Kết hợp cả hai phần trên

(phương pháp thường được sử dụng)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
137


**3.3.3. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy tuyến tính bội**

**Kết quả**




✓ Kết quả phân tích Residual cho thấy có vấn đề về tính phân phối chuẩn
→ Sau khi kiểm tra các vấn đề của giá trị quan sát thứ 18, nó được xác
đinh là lỗi quan sát và đưa ra quyết định loại bỏ.



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
138

**3.3.3. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy tuyến tính bội**

**Kết quả sau khi loaị bỏ giá trị thứ 18**




1) Tính thích hợp của mô hình hồi quy tuyến tính : P-Value, R-Squared, R-Squared
(adjusted), VIF

① Phương trình hồi quy có ý nghĩa P-value 0.000(<0.05)
② Khả năng giả thích của phương trình hồi quy 99.72%
③ Hệ số hồi quy P-Value 0.000(<0.05) có ý nghĩa
④ VIF(đa cộng tuyến) không có gì đặc biệt ( ＜ 5)

2) Kết quả chuẩn đoán mô hình hồi quy : phân tích Residual (Tính phân phối
chuẩn, tính đồng nhất phương sai, tính độc lập)

                                         - Không vị phạm đáng kể với từng điều kiện

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
139

**3.3.4. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy phi tuyến tính**

**3) Phân tích hồi quy phi tuyến tính : Đưa ra phương trình toán học của mối quan hệ đường cong phi**
**tuyến tính (Lựa chọn mô hình hồi quy sau khi phân tích biểu đồ)**

**[Ví dụ]** >Data : 6. 기초통계 _ 관계검정 _ 비선형회귀분석

Hong Gil-Dong BB tiến hành xử lý đặc biệt trên bề mặt Glass để tăng độ bền của Glass. Khi đó, bề mặt
Glass được xử lý với các nồng độ khác nhau, sau đó đo lường độ bền của Glass. Hãy rút ra biểu thức
liên hệ giữa Nồng độ (X) và cường độ Glass (Y).

**Graph > Scatter Plot > Simple**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
140

**3.3.4. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy phi tuyến tính**

 **Đưa ra mô hình hồi quy phi tuyến tính**

**Stat > Regression > Fitted Line plot**

~~**①**~~ ~~**L**~~ **ựa c** ~~**h**~~ **ọn m** ~~**ô**~~ ~~**hì**~~ **n** ~~**h**~~ ~~**hồi**~~ **quy :** ~~**Q**~~ **ua** ~~**d**~~ **ra** ~~**ti**~~ **c** ~~**②**~~ ~~**L**~~ **ựa c** ~~**h**~~ **ọn m** ~~**ô**~~ ~~**hì**~~ **n** ~~**h**~~ ~~**hồi**~~ **quy :** ~~**C**~~ **u** ~~**bi**~~ **c**




→ Khi so sánh S-Value với giá trị R-Squared(điều chỉnh), S-Value nhỏ, Giá trị R-Squared (adjusted) lớn hơn, thì mô hình Quadratic phù hợp hơn.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
141

**3.3.4. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy phi tuyến tính**

   **Đưa ra mô hình hồi quy phi tuyến tính : Tiến hành phân tích lại mô hình hồi quy Quadratic.**

**Stat > Regression > Fitted Line plot**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
142

**3.3.4. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy phi tuyến tính**

   **Chuẩn đoán mô hình hồi quy của phân tích hồi quy phi tuyến tính**

**Stat > Regression > Fitted Line plot**

**Giải thích**

                                Thỏa mãn mức độ thích hợp, thiếu yếu tố, ý nghĩa của phương trình

hồi quy.

                                Khả năng giải thích của phương trình hồi quy là R-Squared 93.12%

                                Kết quả phân tích Residual, Tính phân phối chuẩn, Tính đồng nhất

phương sai, Tính độc lập đều không có vấn đề lớn.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
143

**3.3.5. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy logistic**

**Phân tích hồi quy logistic(logistic regression)**

    **Định nghĩa** : Sử dụng Phân tích hồi quy logistic khi phân tích mối quan hệ của biến phụ thuộc rời rạc (vd: NG/OK) và
biến độc lập liên tục.

    **Áp dụng** : Khi quyết định Spec dựa trên tiêu chí lựa chọn (hoặc đánh giá) sản phẩm, hoặc tiêu chí đạt/ không đạt.

Xác suất



      
|1.0|Col2|
|---|---|
|1.0<br>0.8<br>0.6<br>0.4<br>0.2|X|
|0.0|0.0|

**Đặc điểm:**

      - Giá trị Y tương ứng bới giá trị X liên tục là một giá trị xác suất.

      - Phân tích hồi quy logistic là một loại Phân tích Phân biệt.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
144


**3.3.5. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy logistic**

**[Ví dụ]** >Data : 7. 기초통계 _ 관계검정 _ 로지스틱회귀분석

Hãy phân tích mối quan hệ giữa CD PAS2 và các vết ố hình pháo hoa.

**Stat > Regression > Binary Fitted Line Plot**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
145

**3.3.5. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy logistic**

Vì có 2 sự kiện phản hồi là NG và OK, tiến hành phân tích hồi quy Logistic.

**Stat > Regression > Binary Logistic Regression > Fit Binary Logistic Model**

                                                      - Phân tích hồi quy logistic thứ tự
: Khi có từ 3 kết quả có thứ tự
như ‘Mạnh’, ;Trung bình’, ‘Yếu’

                                                    - Phân tích hồi quy logistic danh nghĩa
: Khi có từ 3 kết quả nhưng không
theo thứ tự như ‘xướt’ ; ‘rách’, ‘móp’

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
146

**3.3.5. Kiểm định quan hệ: Phân tích hồi quy – Phân tích hồi quy logistic**


**Giải thích**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
147



- Mức ý nghĩa 5%, PAS2 CD P-Value 0.013

Xuất hiện lỗi do kích thước CD PAS2

Khi CD PAS2 được tăng lên ‘1 đơn vị’ thì xác suất xảy ra lỗi sẽ giảm.

- Tỷ lệ chênh lệch > 1 : khi X tăng thì xác suất xảy ra lỗi tăng.

- Tỷ lệ chênh lệch < 1 : khi X tăng thì xác suất xảy ra lỗi giảm.

ex) Nếu tỷ lệ chênh lệch là 1.05 thì xác suất xảy ra lỗi tăng 5% mỗi khi X tăng 1

~~đơn~~ ~~vị~~ .

 - Mô hình được đánh giá là hữu ích vì độ lệch R [2] cao và giá trị AIC thấp.

 - Deviance R [2] : tương ứng với R [2] trong phân tích hồi quy.

Adjusted Deviance R2 : tương ứng với Adjusted- R [2] trong phân tích hồi quy.

AIC(akaike information criteria) : Giá trị càng nhỏ, mô hình càng lớn.

Theo kết quả kiểm tra mức độ thích hợp, Mức ý nghĩa dưới 5%, P-Value

1.000, cho thấy “mô hình phù hợp”.

- H0 : mô hình phù hợp vs H1 : mô hình không phù hợp

[Tham khảo]
- Deviance : Kiểm tra mô hình có phù hợp hay không.
- Pearson : Tương ứng với Residual chuẩn hóa của hồi quy tuyến tính.
- Hosmer-Lemeshow : Kiểm tra mức độ phù hợp của mô hình bằng sự khác

biệt giữa giá trị kì vọng và giá trị quan sát.

 **Loại hình**


**Tham**

**khảo**



















**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
148


   **So sánh xem một tỷ lệ của một nhóm có bằng một tỷ lệ cụ thể hay không.**

**Nếu Glass mua từ 2 Vendor có số lượng vết bẩn từ 5 trở xuống trong ‘Spot.25** **’** **ở vị trí thứ 25 của Glass, thì**
**tính là thông qua.**
**Tỷ lệ thông qua hiện tại là 85%. Hãy kiểm tra tỷ lệ và số lượng sản phẩm có vết ố dưới 5 trong dữ liệu khảo sát.**

>Data : 2. 기초통계 _ 평균검정 _t 검정

**Stat > Tables > Tally Individual Varia** ~~**bles**~~ **Giải thích kết quả One-sample Proportion test**

Không thông qua

|Col1|Thông|
|---|---|
||Không|



                                    Số lượng thông qua : 52 trong 58 cái

                                    Tỷ lệ thông qua : 89.66%

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
149

 **So sánh xem một tỷ lệ của một nhóm có bằng một tỷ lệ cụ thể hay không.**

**Nếu Glass mua từ 2 Vendor có số lượng vết bẩn từ 5 trở xuống trong ‘Spot.25** **’** **ở vị trí thứ 25 của Glass, thì tính là**
**thông qua. Nếu tỷ lệ thông qua sản phẩm Glass đã điều tra là 89,66%, hãy kiểm tra xem nó có giống với 75% (tiêu**
**chuẩn tối thiểu cho quy trình hiện tại).**


**Stat> Basic Statistics > One-sample Proportion**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
150


**Giải thích kết quả One-sample Proportion**

- **Mức ý nghĩa dưới 0.05, P-Value 0.002, chọn giả**
**thuyết nghịch.**

**Tỷ lệ hàng thông qua khác 75%**

 **So sánh tỷ lệ tổng thể của hai nhóm**

Nếu Glass mua từ 2 Vendor có số lượng vết bẩn từ 5 trở xuống trong ‘Spot.25’ ở vị trí thứ 25 của Glass, thì tính là thông qua.
Hãy kiểm tra xem tỷ lệ thông qua của từng nhà cung cấp có giống nhau không?

>Data : 2. 기초통계평균검정 _t 검정

**Stat > Basic Statistocs > Two-sample Proportio** ~~**n**~~ **Giả thích kết quả Two-sample Proportion**

Note



 - Kiểm định chính xác của Fisher được áp dụng nếu np
＜ 5 hoặc n(1-p) ＜ 5.



**Tỷ lệ hàng thông qua của Supplier A và B là giống nhau.**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
151

 **So sánh tỷ lệ khiếm khuyết của một nhóm có bằng với tỷ lệ lỗi khiếm khuyết cụ thể không.**

**[Ví dụ]** >Data : 8. 기초통계 _ 비율검정 _ 포아송비율

**Hong Gil-Dong BB đã ghi nhận số lượng màn hình lỗi hàng quý trong 10 năm qua. Anh ta đặt ra giới hạn cho**
**phép là mỗi quý 20 cái. Nhà máy có đáp ứng được tiêu chuẩn này hay không?**


**Stat > Basic Statistics > One-Sample Poision Rate**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
152


**Giải thích kết quả**

**“Ít hơn 20 màn hình hỏng mỗi quý”**

**2-** 표본 **Kiểm định tỷ lệOne-Sample Poi**

 **So sánh tỷ lệ khiếm khuyết của hai nhóm**

**Hong Gil-Dong BB tính toán số lượng đơn vị bị lỗi mỗi quý cho nhà máy A và cứ 6 tháng một lần cho nhà máy B.**
**Anh ta muốn dự trữ những chiếc TV có ít lỗi hơn. Hãy kiểm tra xem nên lưu kho sản phẩm từ nhà máy A hay nhà**
**máy B.**


>Data : 8. 기초통계 _ 비율검정 _ 포아송비율

**Stat > Basic Statistics > Two-Sample Poision Rate**

Nhập theo tổng số tháng thu thập lối của từng nhà máy.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
153


**Giải thích kết quả**

**Có sự khác nhau trong trung bình số khuyết điểm**

**hàng tháng của nhá máy A và B.**

**Tỷ lệ lỗi của nhà máy A cao hơn.**

 **Chi-square Test kiểm định tính độc lập và tính đồng nhất sử dụng tần số dữ liệu rời rạc.**

**Mục đích**

    Phù hợp để kiểm tra so sánh 2 hoặc nhiều đối tượng, chẳng hạn như phân tích phương sai.

(※Tham khảo phân biệt tính độc lập và tính đồng nhất ở trang sau)
     - Điều tra tần suất các hạng mục khác nhau có cùng xác suất xảy ra, để xác định tần suất của từng hạng mục có
đồng nhất hay không. (Kiểm tra tính đồng nhất)

     - Xem xét nguyên nhân biến động là mối quan hệ phụ thuộc hay độc lập (Kiểm tra tính độc lập)

**Thiết lập giả thuyết**


~~1)~~ ~~Kiểm~~ ~~tra~~ ~~tính~~ ~~đồng~~ ~~nhất~~ ~~của~~ ~~tần~~ ~~số~~

   - H o : P1 = P2 = P3 =  … = Pn

   - H
a : ít nhất 1 cái không giống nhau

**Kiểm định thống kê**


~~2)~~ ~~Kiểm~~ ~~tra~~ ~~tính~~ ~~độc~~ ~~lập~~ ~~của~~ ~~biến~~ ~~số~~

  - H
o : Các yếu tố độc lập (không có mối liên hệ giữa các yếu tố).

- H
a : Các yếu tố phụ thuộc (có mối liên hệ giữa các yếu tố).


_2_

−

_o_ _f_ _e_ _)_


−

_2_ **(Giá trị quan sát – Giá trị mong đợi)²** _(_ _f_ _o_ _f_ _e_ _)_
## ~~ =  = ~~


**(Giá trị quan sát – Giá trị mong đợi)²** _o_ −
~~=~~
### ~~~~


_e_


**Giá trị mong đợi**


_f_


**★** **Chú ý:**

**- Khi gía trị kì vọng nhỏ hơn 5, kết quả phân tích có độ tin cậy thấp.**
**→ Thu thập các mẫu bổ sung để đạt được giá trị mong đợi lớn hơn 5 hoặc tích hợp với các vùng lân cận để phân tích.**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
154

**Tham**

**Khảo**


**※ Phân biệt kiểm tra tính độc lập và kiểm tra tính đồng nhất**

**1) Kiểm tra tính đồng nhất (test of homogeneity)**
**- Các mẫu độc lập được lấy từ** **nhiều tổng thể, nhưng tổng của một nhóm (yếu tố) là cố định và nhóm còn lại được**
**gán theo xác suất.**
[VD]  Để kiểm tra xem các tỷ lệ MBB, BB, GB có giống nhau hay không, ở mỗi công ty A, B, C chọn 100 người làm
mẫu và tổng hợp thành bảng như sau:






|Phân loại|Col2|Belt|Col4|Col5|Total|
|---|---|---|---|---|---|
|Phân loại|Phân loại|MBB|BB|GB|GB|
|Công<br>ty|A|18|37|45|100|
|Công<br>ty|B|10|32|58|100|
|Công<br>ty|C|26|41|33|100|
|Total|Total|54|110|136|300|


**2) Kiểm tra tính độc lập (test of independence)**

**- Là một ‘mẫu đơn’ được lấy từ một tổng thể duy nhất, Thử nghiệm được thực hiện bằng cách trước tiên lấy một mẫu, sau**
**đó phân loại mẫu đó theo các tiêu chí cần nghiên cứu.**

[VD] Thu thập 300 Panel theo kế hoạch cho trước để tìm ra mối liên hệ giữa các loại hình lỗi (A, B, C) và thiết bị (GA, NA,
DA).






|Phân loại|Col2|Thiết bị|Col4|Col5|Tổng|
|---|---|---|---|---|---|
|Phân loại|Phân loại|GA|NA|DA|DA|
|Lỗi|A|62|43|22|127|
|Lỗi|B|31|27|36|94|
|Lỗi|C|42|15|22|79|
|Tổng|Tổng|135|95|80|300|


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
155


    **Kiểm tra tính đồng nhất bằng cách sử dụng tần số của dữ liệu rời rạc.**

**[Ví dụ]** >Data : 2. 기초통계 _ 평균검정 _t 검정

**Hãy kiểm tra xem có sự khác biệt giữa Pass/Fail theo sự thay đổi điều kiện của** **‘** **Delay.T1’ hay không?**
**(Delay 1T~4T mỗi lần lấy 20 mẫu)**

**Stat > Tables > Cross Tabulation and Chi square**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
156

  **Kiểm tra tính đồng nhất bằng cách sử dụng tần số của dữ liệu rời rạc.**

**Gỉai thích kết quả**



**’**

**Sự thay đổi của ‘Delay.T** **không ảnh**
**hưởng đến Pass và Fail**

☞
Giá trị kì vọng nhỏ hơn 5, Phép kiểm
định Chi-Square có thẻ không hợp lệ vì không
thể gải định phân phối chuẩn (Phải xác nhận)

※ Nếu giá trị kì vọng nhỏ hơn 5 thì giải quyết như thế nào?
1. Thu thập thêm data để làm giá trị kì vọng lớn hơn 5.
2. Nếu khó thu thập dữ liệu, tiến hành phân tích bằng cách

kết hợp với các khu vực tương tự.


DF = (số hàng – 1 ) * (số cột – 1)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
157

    **Kiểm tra tính độc lập bằng cách sử dụng tần số của dữ liệu rời rạc.**

**[Ví dụ]** **>Data : Analyze_** **통계적분석**

**Kiểm tra số lương** **‘** **Spot.25’có độc lập với nhau hay không theo** **‘** **Delay.T’ và** **‘** **C.RPM’ (chọn 150 mẫu)**

**Stat > Tables > Cross Tabulation and Chi square**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
158

  **Kiểm tra tính độc lập bằng cách sử dụng tần số của dữ liệu rời rạc.**

**Giải thích kết quả**




 - **P-Value 0.0000, Mức ý nghĩa dưới 5%,**
**Delay.T và C.RPM không độc lập với nhau và**
**có thể ảnh hưởng đến Spot.25 ở các kết hợp**
**phạm vi nhất định.**

☞
Giá trị kì vọng nhỏ hơn 5, Phép kiểm
~~định~~ ~~Chi-Square~~ ~~có~~ ~~thẻ~~ ~~không~~ ~~hợp~~ ~~lệ~~ ~~vì~~ ~~không~~
thể gải định phân phối chuẩn (Phải xác nhận)

※ Nếu giá trị kì vọng nhỏ hơn 5 thì giải quyết như thế nào?
1. Thu thập thêm data để làm giá trị kì vọng lớn hơn 5.
2. Nếu khó thu thập dữ liệu, tiến hành phân tích bằng cách

kết hợp với các khu vực tương tự.



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
159

#### **4. Phương pháp luận 6σ**

**4.1. Tư tưởng trọng tâm**

**4.2. Khái quát phương pháp luận**

**4.3. DMAIC**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
160

**mục tiêu’ và ‘giảm thiểu biến động’, loại bỏ hoàn toàn khuyết điểm để ‘tối đa hóa lợi nhuận’.**






**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
161

**Hoạt động giảm COPQ (cost of poor quality)**



       - **Kiểm**

**tra**

   






Nguyên liệu không phản ánh trong kế hoạch

- Capa Drop do rework Panel


**khoảng 25% lợi nhuận**


**“Chi phí chất lượng truyền thống”**




Sản phẩm trả lại



**Trung bình chi phí COPQ chiếm**


Source : Dr. Mikel J. Harry (Six Sigma Mega Conference)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
162

**Jack Welch**

(Doanh nhân)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
163


**Six Sigma đại diện cho**
**sự chuyển đổi mô hình từ**

**việc sửa chữa một sản**
**ph** ~~**ẩ**~~ **m đ** ~~**ể**~~ **làm cho nó trở**

**nên hoàn hảo thành sửa**
**chữa một quy trình để**

**làm cho nó trở nên hoàn**
**hảo hoặc gần như hoàn**

**hảo.**

**The Foundation of Six Sigma is**



**Nguyên nhân không biết**

**Nguyên nhân không thể**
**kiểm soát**

- **Nguyên nhân không**
**quan trọng**


**Phân loại cái biết và cái không biết**

                                         - ~~**Xá**~~ **c** ~~**đị**~~ **n** ~~**h**~~ ~~**đ**~~ **ược nguy** ~~**ê**~~ **n n** ~~**hâ**~~ **n quan trọng** ~~**(**~~ **n** ~~**hâ**~~ **n t** ~~**ố**~~ **trọng**

**Xác định mức độ ảnh hưởng kết quả từ nguyên nhân**

                    **Tối ưu hóa các yếu tố nguyên nhân để cải tiến hiệu quả mong muốn**

**Nếu có kết quả thì chắc chắn sẽ có nguyên nhân.**
**Nếu biết mối quan hệ đó chúng ta có thể tạo ra gia trị kết quả mong muốn.**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
164

**Nguồn nhân lực giỏi**
(Innovative Quality People using)

**sử dụng process tốt nhất,**

(Innovative Quality Processes to )

**tạo ra giá trị tốt nhất**
(Create values for)

**để cung cấp cho khách hàng và cổ đông**
(Customers and Share holders )

Source : Dr. Mikel J. Harry (Six Sigma Mega Conference)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
165

**DMAIC**

**DMADV**
**DFSS** [1)]

**DIDOV**
(design for six sigma)


**“Các bước của phương pháp luận** (D/M/A/I/C, D/M/A/D/V, D/I/D/O/V)

**là thứ tự kết thúc hoạt động.”**

         - Tham khảo phần phụ lục để biết khái niệm về DMADV và DIDOV.


1) Phương pháp chọn CTQ bằng cách định lượng nhu cầu của khách hàng và đạt được mức độ hoàn thiện thiết kế tiêu chuẩn 6SIGMA trong giai

đoạn thiết kế bằng cách dự đoán và đo lường chất lượng của CTQ.











*Ngoài ra còn có một phương pháp DIDOV học trong khóa học DX MBB
             - Bằng cách thu thập/xử lí dữ liệu quy trình thực.
① Modeling từ quan điểm Y=f(X’s)

② Lựa chọn Feature quan trọng.
③ Tối ưu hóa và kiểm chứng thực tế thông qua DOE.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
166

**Thay đổi tư duy và cách làm việc ! (The Way We Work, The Way We Think)**




- **Đưa ra và chọn CTQ** [1)] **từ ý kiến khách hàng.** .

Thiết lập Spec từ quan điểm khách hàng.

- Cải thiện Net Income thông qua sự hài lòng khách hàng.

Chúng ta xem xét các cơ hội (vấn đề) để cải tiến từ quan điểm rằng kết quả luôn có nguyên nhân.

**Xác định mối quan hệ giữa X và Y.**

**Cải thiện Y thành gía trị mong muốn thông qua việc tối ưu X.**

- ~~Tiế~~ n ~~h~~ ạn ~~h~~ p ~~hâ~~ n ~~tí~~ c ~~h~~ ~~I~~ npu ~~t~~, ~~P~~ rocess, ~~P~~ rocess c ~~ủ~~ a ~~O~~ u ~~t~~ pu ~~t~~ .

- . **Đưa ra nhân tố trọng yếu (vital few) và CTQ từ quan điểm Process.**

Quản lý Process để duy trì liên tục và cải tiến hiệu suất.

Chọn CTQ trong số nhiều chỉt số Output .

Đưa ra nhân tố trọng yếu từ trong nhiều yếu tố X.

Lựa chọn phương án cải tiến tốt nhất trong số nhiều phương án cải tiến.

Sử dụng các kỹ thuật thống kê khi tóm tắt dữ liệu.

Sử dụng kĩ thuật thống kê khi đưa ra quyếtt định.

**Dự đoán và tối ưu hóa các cơ hội cải tiến (vấn đề) thông qua số liệu thống kê.**

※ Flow làm việc: đưa ra cơ hội cải tiến vấn đề, xác định tình hình hiện tại, tìm nguyên nhân, giải quyết chúng và rút ra kết luận.


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
167

**Description**


**Step**

1. Xác định cơ hội cải tiến

2. Chọn CTQ

3. Xác định tiêu chuẩn thực tế và thiết lập mục

tiêu

4. Đưa ra nhân tố tiềm ẩn

5. Lựa chọn nhân tố trọng yếu

6. Chọn phương án tối ưu

7. Đánh giá tính tái hiện

8. Xây dựng kế hoạch quản lý

9. Quản lí và mở rộng áp dụng BP







Xác định bối cảnh lựa chọn dự án và process.

Định nghĩa cơ hội cải tiến

Lựa chọn CTQ liên quan đến yêu cầu khách

~~hàng~~ .

Xác định tiêu chuẩn thực tế CTQ

Cụ thể hóa phương hướng giải quyết và mục tiêu

Đưa ra nhân tố tiềm ẩn để cải thiện CTQ

Phân tính định tính định lượng nhân tố tiềm ẩn

Chọn nhân tố trọng yếu (nguyên nhân gốc rễ) cải thiện

~~CTQ~~

- Đưa ra idea sáng tạo và đánh giá

Chọn phương án tối ưu thông qua thửu nghiệm DOE

Khi đánh giá tính tái hiện : kiểm chứng hiệu quả cải
tiến của Y với CTQ

Tiến hành áp dụng thử phương án tối ưu

Lập kế hoạch quản lý để duy trì thành quả

Áp dụng mở rộng Best Practice



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
168

**4.3. Phương pháp luận : DMAIC_ Step 1. Xác định cơ hội cải tiến**

**[Mục đích]**

         Xác định rõ khu vực đối tượng cần cải tiến của dự án và lập kế hoạch thực hiện đúng.

         Thông qua việc phân tích quy trình, đưa ra các hạng mục Quick Win để cụ thể hóa cơ hội cải
tiến và trực quan hóa thành quả trong giai đoạn.

**[Hoạt động]**

         Viết bản đăng kí

         Phân tích Process

~~Cải~~ ~~tiến~~ ~~độ~~ ~~bền~~ ~~của~~ ~~khối~~ ~~block~~

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
169

**①** **Bản đăng kí**

        Mô tả tính khả thi của việc theo đuổi nhiệm vụ, làm rõ các cơ hội cải tiến có thể tác động đáng kể
đến khách hàng và doanh nghiệp.

        Đặt mục tiêu nhiệm vụ cụ thể và thành lập team, lịch trình.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
170

**②** **Phân tích process**


Inut nguyên liệu và
quản lí.
✓ Nguyên liệu thô


Cho vào thúng

Đóng gói bằng túi

Tìm ra các cơ hội cải tiến
về nguyên liệu thô, kích
thước block, tiêu chuẩn
Spec,...




- Kiểm tra Supplier, Input, Process, Output, Customer của quy trình cần cải

- Thông qua phân tích định tính về quy trình, đưa ra các Quick Win và cụ thể

hóa cơ hội cải tiến.


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
171

**[Định nghĩa]**

         **Thu thập và phân tích tiếng nói của khách hàng để đưa ra các yêu cầu cốt lõi của khách**
**hàng.**

         **Thông qua việc lựa chọn các ứng cử viên CTQ có liên quan đến yêu cầu cốt lõi của khách**
**hàng, CTQ được chọn làm chỉ số có thể thể hiện hiệu quả hoạt động của dự án.**

Tùy theo mục tiêu cải tiến, thông qua phân tích cơ chế lỗi và phân tích quy trình...

① Đưa ra các ứng viên CTQ và đánh giá → Xác nhận CTQ cuối cùng.
~~②~~ ~~Đưa~~ ~~ra~~ ~~các~~ ~~Quick~~ ~~Win~~ ~~và~~ ~~cải~~ ~~tiến~~ .

**[Hoạt động]**

         **Xác định yêu cầu cốt lõi của khách hàng**

         **Lựa chọn CTQ**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
172

  **①** **Xác định yêu cầu cốt lõi của khách hàng**


**Tiếng nói của**

**Khách hàng**

     - Tôi bị mất một vài mảnh

ghép và không thể lắp
ráp hoàn chỉnh được.

     - Khi trẻ em chơi thì nó rất

dễ bị vỡ.

~~•~~ ~~Khó~~ ~~tháo~~ ~~dỡ~~ ~~sau~~ ~~khi~~ ~~đã~~

hoàn thành.

**②** **Lựa chọn CTQ**

~~**CTQ**~~ ~~**1**~~


**Yêu cầu cốt lõi của**

**Khách hàng**

   - Độ bền của các khối thành

phẩm phải cao.

   - Khả năng xử lý hình dạng

khối cần được cải thiện.

~~**Độ**~~ ~~**bền**~~ ~~**thành**~~ ~~**phẩm**~~


Xác định đối tượng khách hàng và xây dựng kế

hoạch hiểu rõ nhu cầu khách hàng.

Đưa ra các
yêu cầu cốt lõi của khách hàng.

CTQ được chọn có thể đại diện cho các yêu cầu cốt

lõi của khách hàng

Lựa chọn chỉ số liên quan đến CTQ

: Output, Process, Input


~~**CTQ**~~ ~~**2**~~


**Độ chính xác kích thước block**

**(dài, rộng, cao)**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
173

**4.3. Phương pháp luận : DMAIC_** **Step 3. Xác định tiêu chuẩn thực tế và đặt mục tiêu**

**[Mục đích]**

          Xác định các chỉ số để lập kế hoạch thu thập dữ liệu và xem xét tính ổn định của dữ liệu.

          Phân tích năng lực quy trình hiện tại theo loại hình dữ liệu để xác định tiêu chuẩn thực tế từ đó
đưa ra mục tiêu.

Tiêu chuẩn thực tế về CTQ và thiết lập mục tiêu.

**[Hoạt động]**

          Thu thập dữ liệu và đánh giá tính ổn định

          Phân tích năng lực quá trình

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
174

**4.3. Phương pháp luận : DMAIC_** **Step 3. Xác định tiêu chuẩn thực tế và đặt mục tiêu**

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**

**①** **Xác định tiêu chuẩn thực tế**

     **Độ bền thành phẩm**
: Mức độ mà sản phẩm hoàn thiện có thể suy trì hình dạng ban đầu khi rơi từ độ cao 1m.

(Nếu một mảnh ghép bị rơi ra thì cũng coi là NG)

**Kết qủa test độ bền sản phẩm Main Stream 000,**

          10% NG (10/100cái) → 1.3σ

**LSL** **USL**

     **Độ chính xác về kích thước khối Block**
: Khác biệt về gía trị thực tế và target của kích thước mỗi mảnh ghép

(rộng, dài, cao)

~~**Z**~~ ~~**=**~~ ~~**2**~~ **.** ~~**73**~~

-3 -2 -1 0 1 2 3

      Lập kế hoạch thu thập dữ liệu cho CTQ và các chỉ số liên quan.

      Xem xét các Outlier và tính ổn định của dữ liệu để xác định giá trị thực tế (base line) trước cải tiến.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
175

**4.3. Phương pháp luận : DMAIC_** **Step 3. Xác định tiêu chuẩn thực tế và đặt mục tiêu**

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**

**②** **Thiết lập mục tiêu**

**To-be**

**As-is**

LSL Target USL

         Đặt mục tiêu cải tiến của CTQ để đạt KPI.

         Xác định mục tiêu mức Sigma bằng cách đặt mục tiêu cải tiến lỗi của

CTQ.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
176

**[Định nghĩa]**

           **Thông qua phân tích dữ liệu phần tầng để lựa chọn các lĩnh vực phân tích**
**trọng tâm và thông qua thảo luận với các nhân viên liên quan để đưa ra các**
**nhân tố tiềm ẩn (potential X’s).**

Rút ra các yếu tố tiềm năng thông qua phân tích phân tầng và 5Why về các chỉ số liên quan đến

CTQ.

**[Hoạt động]**

           **Phân tích phân tầng**

           **Brandstorming**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
177

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**

**①** **Phân tích phân tầng**

**Vẽ đồ thị trung bình và độ phân tán kích thước Block như chiều rộng (X), chiều dàI (Y), chiều**
**cao (Z), từ đó phát hiện ra các khối và trục có độ phân tán lớn.**

**BlockTrục**


**A**

~~**B**~~

**C**


X

Y

Z

X

Y

Z

X

Y

Z

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||


-4.5 -3.6 -2.7 -1.8 -0.9 0.0 0.9 1.8

      Phân tích các biến phân tầng dự kiến ảnh hưởng đến biến động của CTQ.

      Đưa ra các nhân tố tiềm ẩn và lĩnh vực cải tiến tập trung thông qua phân tích phân tầng.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
178

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**

**②** **Đưa ra nhân tố tiềm ẩn**

Đưa ra các nhân tố tiềm ẩn từ quan điểm cơ chế thông qua trao đổi với các chuyên gia trong từng
lĩnh vực.




**(được kiểm chứng trong**

**Quick Win)**

**Chọn nhân tố tiềm ẩn**



**Chọn nhân tố tiềm ẩn**



       - Tìm ra các nhân tố tiềm ẩn bằng kết qủa phân tích định tính và phân tích phân tầng.

       - Tool chủ yếu : Brandstorming, 5Why, sơ đồ tư duy, sơ đồ nhân tố đặc trưng, Logic tree, Mind map,...

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
179

**4.3. Phương pháp luận : DMAIC_ Step 5. Lựa chọn nhân tố trọng yếu**

**[Định nghĩa]**

          **Thiết lập và phân tích kế hoạch kiểm chứng định tính/định lượng phù hợp về các nhân tố**
**tiềm ẩn (potential X’s) được đưa ra, từ đó lựa chọn các nhân tố trọng yếu.**

Chọn nhân tố trọng yếu để cải tiến
CTQ

**[Hoạt động]**

          **Phân tích định lượng**

          **Phân tích định tính**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
180

**4.3. Phương pháp luận : DMAIC_ Step 5. Lựa chọn nhân tố trọng yếu**

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**

**①** **Xây dựng kế hoạch kiểm chứng**






|CTQ<br>(Y)|nhân tố tiềm ẩn<br>(X)|Loại Data|Col4|Phương pháp phân tích/ kiểm chứng|
|---|---|---|---|---|
|CTQ<br>(Y)|nhân tố tiềm ẩn<br>(X)|Y|X|X|
|||Liên tục|Liên tục|Kiểm chứng thống kê – Phân tích hồi quy|
||||Liên tục|Kiểm chứng thống kê – DOE|
||||Rời rạc|Benchmarking|
|||||Phân tíc process|
|||||Hoàn thành kiểm chứng – bước phân tầng|
|||Rời rạc|Liên tục|Kiểm chứng thống kê – Phân tích hồi quy<br>logistic|
||||Rời rạc|Kiểm chứng thống kê – Chi-square|
||||||
||||||
||||||
||||||



      - Thiết lập loại dữ liệu, kĩ thuật phân tích, phương pháp kiểm chứng cho các nhân tố tiềm ẩn.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
181

**4.3. Phương pháp luận : DMAIC_ Step 5. Lựa chọn nhân tố trọng yếu**

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**


**②** **Kiểm tra nhân tố tiềm ẩn**

90

75

60

45

30


**Sự tương tác về chiều ngang**

Trung bình data

115 220


90

75

60

~~45~~

30



|Col1|Time|Col3|
|---|---|---|
|||Nhiệt độ|
||||
||||
||||
||||


60 90 120

      - Thiết lập kế hoạch xác minh kiểm tra mối quan hệ nhân quả giữa các nhân tố tiềm ẩn và

CTQ (tuyến tính, phi tuyến tính), tương tác giữa các yếu tố tiền ẩn với nhau,... Sau đó xem
xét kết quả phân tích để rút ra nguyên nhân gốc rễ.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
182

**4.3. Phương pháp luận : DMAIC_ Step 6. Lựa chọn phương án tối ưu**

**[Mục đích]**

          **Yếu tố thay thế là lựa chọn phương án tối ưu thông qua việc đưa ra các ý**
**tưởng sáng tạo và đánh giá chúng. Còn yếu tố kiểm soát là lựa chọn phương án**
**tối ưu thông qua việc phân tích DOE.**

Tối ưu hóa để cải thiện CTQ

**[Hoạt động]**

          **Tối ưu hóa yếu tố thay thế.**

          **Tối ưu hóa yếu tố kiểm soát.**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
183

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**

    **①** **Tối ưu hóa yếu tố thay thế**

**Thiết kế lại quy trình quản lý và lưu trữ nguyên liệu để duy trì độ tinh khiết của nguyên**
**liệu.**

    - Đối với những nhân tố trọng yếu yêu cầu kiểm tra kỹ lưỡng do có tính mới lạ cao: lựa chọn và cụ thể

hóa phương pháp tối ưu bằng cách vận dụng các nguyên tắc sáng tạo.

    - Tool chính : Benchmarking, TRIZ, Mind map, 6 Thinking Hats,...

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
184

**4.3. Phương pháp luận : DMAIC_ Step 6. Lựa chọn phương án tối ưu**

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**

**②** **Tối ưu hóa yếu tố kiểm soát**

**Đồ thị đường viền của chiều xao, dài, ngang**



**Time**


190

185

180

175

170


175.0 177.5 180.0 182.5 185.0

**Nhiệt độ**

    - Đưa ra giá trị tối ưu từ nhân tố trọng yếu được yêu cầu, sau đó lựa chọn phương án tối ưu bằng

phương pháp đáp ứng bên mặt (RSM), Mixture Design.

    - Tool chính: Response surface method, Mixture Design, Phân tích hồi quy, Tolerance Analysis,..

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
185

**[Mục đích]**

          **Pilot Test được tiến hành để kiểm chứng hiệu quả mong đợi của phương án tối ưu và để**
**xác minh trước những rủi ro có thể xảy ra trong quá trình thực hiện này.**

Kiểm tra cải thiện về Y và CTQ

**[Hoạt động]**

          **Lập kế hoạch và tiến hành Pilot Test**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
186

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**

**①** **Lập kế hoạch Pilot Test**




|Pilot Name|Col2|Người kiểm tra|Col4|
|---|---|---|---|
|Leader||Process Owner||
|Thời gian<br>áp dụng||Phạm vi<br>đối tượng||
|Nội dung|1. Bối cảnh áp dụng<br>2. Nội dung phương án cải tiến<br>3. Phương hướng kiểm chứng<br>4. Vai trò và nhiệm vụ|1. Bối cảnh áp dụng<br>2. Nội dung phương án cải tiến<br>3. Phương hướng kiểm chứng<br>4. Vai trò và nhiệm vụ|1. Bối cảnh áp dụng<br>2. Nội dung phương án cải tiến<br>3. Phương hướng kiểm chứng<br>4. Vai trò và nhiệm vụ|


        Lập kế hoạch Pilot để kiểm chứng khả năng tái hiện của phương án tối ưu.

        Các rủi ro có thể xảy ra trong quá trình MP cũng được xem xét và phản ánh trong quá trình Pilot Test.

        Yêu cầu Pilot Test có thể bao gồm tất cả các biến có thể xảy ra (recommend).

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
187

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**

**②** **Tiến hành Pilot và kiểm chứng**



- **Độ bền của thành phẩm** (KPI)

**Độ chính xác của kích thước**
**Block**

~~**Z**~~ **=** ~~**6**~~ **.** ~~**01**~~


**Kết quả test độ bền Main Stream 000,**

- 1.5% NG (15/1000 cái) → 0% NG(Mức 6σ )

**LSL** **USL**

-3 -2 -1 0 1 2 3


        Dự đoán hiệu quả cải tiến thông qua phân tích kết quả Pilot Test

        Kiểm tra mức độ cải tiến xem nó có đặt Target KPI hay không.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
188

**[Định nghĩa]**

       **Tiến hành phân tích rủi ro tiềm ẩn và lên kế hoạch quản lý nhằm tiến hành áp dụng các**

**phương án tối ưu và duy trì thành quả.**

**[Hoạt động]**

       **Phân tích Risk tiềm ẩn.**

       **Viết bản kế hoạch quản lý.**

Lập kế hoạch quản lý nhân tố trọng yếu và
~~CTQ~~,..

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
189

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**

**①** **Phân tích Risk tiềm ẩn**

**Risk Assessment**









|No|Phương án|Lĩnh vực xảy ra<br>Risk|Risk|Kết quảdựđoán<br>vềRisk|Độ<br>phát<br>sinh|Độ<br>ảnh<br>hưởng|Độ<br>nguy<br>kịch|Phương án giảm Risk|PIC|Note|
|---|---|---|---|---|---|---|---|---|---|---|
|1|||||||||||
|2|||||||||||
|3|||||||||||
|4|||||||||||


※ Độ nguy kịch = Độ phát sinh × Độ ảnh hưởng

           - Rút ra những Risk có thể xảy ra khi áp dụng vào sản xuất hàng loạt từ đó đưa ra các biện pháp đối phó.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
190

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**

**②** **Viết bản kế hoạch quản lý**

**Bản kế hoạch quản lý process**





|Phân loại|No|Đối tượng quản lý|Spec|Đơn vịđo|Phương pháp đo|Chu kì đo|Col8|Người đo|
|---|---|---|---|---|---|---|---|---|
|Phân loại|No|Đối tượng quản lý|Spec|Đơn vịđo|Phương pháp đo|Tần suất|Kích thước<br>mẫu|Kích thước<br>mẫu|
|CTQ|1|Độbền|||||||
|CTQ|2|Độchính xác|||||||
|Yếu tố<br>trọng yếu|1|Độtinh khiết|||||||
|Yếu tố<br>trọng yếu|2|…|||||||
|Yếu tố<br>trọng yếu|3||||||||
|Yếu tố<br>trọng yếu|4||||||||
|Yếu tố<br>trọng yếu|5||||||||
|Chỉsố<br>bổsung|1||||||||
|Chỉsố<br>bổsung|2||||||||
|Chỉsố<br>bổsung|3||||||||
|Chỉsố<br>bổsung|4||||||||



           - Lựa chọn các đối tượng quản lý và thiết lập phương pháp đo lường để quản lý và duy trì liên tục thành

quả sau cải tiến.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
191

**4.3. Phương pháp luận : DMAIC_ Step 9. Quản lý và áp dụng mở rộng BP**

**[Mục đích]**

       **Giám sát và thực hiện quản lý đối với các hạng mục chính theo kế hoạch quản lý, lên kế**
**hoạch mở rộng áp dụng BP.**

**[Hoạt động]**

       **Giám sát và hành động.**

       **Áp dụng mở rộng BP.**

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**


**①** **Giám sát và hành động**

 Giám sát định kì đối tượng quản lý, nếu xuất

hiện Outlier thì xác định nguyên nhân và thực

hiện biện pháp phù hợp.

 Sau khi ổn định hóa công đoạn, tiến hành

chuyển công đoạn từ Process Owner.







**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
192

**4.3. Phương pháp luận : DMAIC_ Step 9. Quản lý và áp dụng mở rộng BP**

**[Ví dụ] Cải tiến độ bền thành phẩm khối block**


**②** **Áp dụng mở rộng Best Practice**

       Tối đa hóa thành quả bằng cách
mở rộng và áp dụng các Best
Practice của dự án.

       Phản ánh các cải tiến trong tiêu
chuẩn công việc.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
193


**구분**

|Col1|Col2|Col3|Col4|* 아|아이|이디|디어생|생성|성일|일: O|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
|-|-|-|-|-|-|-|-|★|●|-|



( ★ 아이디어생성, - 적용완료, ◐ 적용중, - 적용가능, - 관련없음 )

**1. Xác định cơ hội cải tiến**

**2. Lựa chọn CTQ**

**Nắm bắt Process và bối cảnh lựa chọn dự án rồi định nghĩa rõ ràng về cơ hội cải tiến**
**và lựa chọn CTQ liên quan đến nội dung yêu cầu chủ chốt của khách hàng**



**Ý kiến của khách hàng**

**Biểu đồ quan hệ (KJ Method)**

**Đưa ra nội dung yêu cầu chủ**

**chốt khách hàng**

**Đưa ra chỉ số Output**

**Phân tích biểu đồ liên quan**

**Phân tích biểu đồ phân tán/hồi quy**


**1.1 Soạn đơn đăng ký**

**1.2 Phân tích Process**



**Đơn đăng ký Project**

**SIPOC**

- **FDPM**

**Quick Win**


**2.1 Định nghĩa nội**
**dung yêu cầu chủ**
**chốt khách hàng**

**2.2 Lựa chọn CTQ**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
195

#### **1. Xác định cơ hội cải tiến**

**1.1. Soạn đơn đăng ký**

**1.2. Phân tích Process**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
~~196~~

Định nghĩa rõ ràng về lĩnh vực đối tượng cải tiến của Project rồi lập kế hoạch để tiến hành
một cách đúng

Qua phân tích Process, cơ hội cải thiện cụ thể hóa và lấy hạng mục Quick Win mà có thể
thành thực hiện sớm

Đơn đăng ký Project

Cơ hội cải thiện, Quick Win



- Xác định Biz. Issue, định nghĩa Big Y, lựa

chọn Project

- Kĩ thuật tính thỏa đáng xúc tiến dự án

- Đưa ra cơ hội cải tiến có thể gây ảnh hưởng

lớn đến mục tiêu doanh nghiệp

- Thiết lập mục tiêu dự án một cách cụ thể và

phạm vi

- Lập Team và xây dựng kế hoạch dự án



- Xác định Process đối tượng cải tiến và soạn biểu đồ Flow

- Đưa ra Quick Win và cụ thể hóa cơ hội cải tiến thông qua

phân tích định tính của Project


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
197

**Soạn đơn đăng kí** **Phân tích Process**

Phân tích Machanism, SIPOC, FDPM, FBD,…





|Type|Activity|Cơ hội<br>cải tiến|Quick<br>Win|Giải thích|PIC|Lịch<br>trình|
|---|---|---|---|---|---|---|
|A2|||||||
|A3|||||||

|Type|Activity|Cơ hội cải tiến|Quick Win|
|---|---|---|---|
|A1||||
|D1||||
|A2|||Quick Win|
|A3|||Quick Win|
|D2||||


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
198

#### **1.1. Soạn đơn đăng kí**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
199

**Six Sigma Project là: phản ánh Business Issue, cải tiến Process và phải tiếp thu yêu cầu**
**của khách hàng**

      - Có mối quan hệ rõ ràng với yêu cầu của khách hàng quan trọng không?

      - Có mật thiết và có Impact lớn với thành quả doanh nghiệp không?

      - Có liên quan trực tiếp đến công việc, mục tiêu của tổ chức hay các thành

viên không?

      - Có biểu thị bằng chỉ số có thể đo lường được không?

      - Đã có đáp án từ trước chưa? Giả sử nếu có thì không thể trở thành đối tượng của Project được. Hãy cải tiến

ngay lập tức bằng Quick Win

      - Phạm vi vấn đề có thể giải quyết được bằng lịch trình và Resourse đã cho không?

Nếu câu trả lời là “Không” thì hãy chi tiết hóa phạm vi vấn đề và chia nhỏ lịch trình ra theo từng giai đoạn

(Phase 1, Phase 2..) và thực hiện

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
200

**Xuất phát từ quan điểm của khách hàng, đồng thời phải có thể đóng góp vào việc đạt**
**được mục tiêu của tổ chức**




Chiến lược tổ chức
(Y+3, mục tiêu năm tương ứng)


**Đưa ra**

**Big Y**


**Lựa chọn**

**dự án**


**Triển khai**

**Little y**


**Hoạt động**

**cải tiến**





**Six Sigma Project**


*Nguồn : Sửa một phần từ giáo trình 6σ LG Electronic(2020)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
201

**1. Xác định Biz Issue và triển khai Big Y**

**Trong các dự án giải quyết Neck Issue hoặc dự án xúc tiến trọng tâm được triển khai từ đơn vị**
**toàn công ty cho đến đơn vị Team, lựa chọn Big Y**
**Trong số các dự án dưới (little y), lựa chọn 6Sigma Project**

※ Ở công ty bản thân, TDR, dự án xúc tiến trọng tâm là dự án Big Y đại diện, quy mô nhỏ hơn thì là đơn vị Team (hoặc

Task) lựa chọn độ dự án đạt được KPI bằng Big Y

Trong các dự án dưới của Big Y, lựa chọn dự án 6Sigma và xúc tiến





**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
202

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
203

**Ở giai đoạn bắt đầu tiến hành Project, phải nắm rõ bối cảnh xúc tiến, cơ hội cải tiến, mục**
**tiêu/phạm vi/thành quả hoạt động, thành viên Team, kế hoạch xúc tiến,…, phổ biến cụ thể**
**các nội dung hoạt động và phương hướng xúc tiến dự án cho các thành viên và sử dụng các**
**tài liệu cơ bản để Communication**


**1. Bối cảnh xúc tiến** : tài liệu và căn cứ
khách quan về việc “Tại sao phải làm dự án
này? ”
**2. Cơ hội cải tiến** : Tổn thất chung của khách
~~hà~~ ng v ~~à~~ cơ ~~hội~~ ~~B~~ us ~~i~~ ness v ~~ề~~ v ~~ấ~~ n ~~đề~~ n ~~à~~ y

**3. Major Objective và mục tiêu hoạt động** :
Tiêu chuẩn của thành quả

**4. Khái quát hoạt động** : Kĩ thuật phương
hướng tiến hành Project
(cải tiến công đoạn, tái thiết kế, phát triển vật liệu,…)

**5. Phạm vi hoạt động** : Đối tượng hoạt
động và Process

**6. Thành viên Team** : Ai làm gì

**7. Lịch trình theo từng giai đoạn** : Thời
gian, hoạt động chi tiết














**LG Display DX Black Belt 과정, Copyright@2023, LG Display**

|Tên Project|Col2|Col3|Col4|Col5|Col6|Col7|Loại Project|Col9|Col10|Col11|Col12|Thời gian hoạt động|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Leader|Leader||||||Bộ phận|Bộ phận|||||||||
|Bối cảnh tiến hành và cơ hội cải thiện|Bối cảnh tiến hành và cơ hội cải thiện|Bối cảnh tiến hành và cơ hội cải thiện|Bối cảnh tiến hành và cơ hội cải thiện|Bối cảnh tiến hành và cơ hội cải thiện|Bối cảnh tiến hành và cơ hội cải thiện|Bối cảnh tiến hành và cơ hội cải thiện|Bối cảnh tiến hành và cơ hội cải thiện|Bối cảnh tiến hành và cơ hội cải thiện|Bối cảnh tiến hành và cơ hội cải thiện|Cấu thành Team|Cấu thành Team|Cấu thành Team|Cấu thành Team|Cấu thành Team|Cấu thành Team|Cấu thành Team|
|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|Vai trò|Bộ phận|Bộ phận|Tên|Belt|Belt|Tham gia|
|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|Leader|||Hong<br>Gil-dongK|BB|BB|Toàn thời<br>gian trong<br>công ty|
|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|※ Tên TDR|member|||||||
|Major<br>Objective|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|
|Major<br>Objective|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|member|||||||
|Major<br>Objective|KPI|KPI|KPI|Tiêu chuẩn<br>hiện|Tiêu chuẩn<br>hiện|World’s<br>Best|World’s<br>Best|Target|Target|Target|Target|Target|Target|Target|Target|Target|
|Major<br>Objective|KPI|KPI|KPI|Tiêu chuẩn<br>hiện|Tiêu chuẩn<br>hiện|World’s<br>Best|World’s<br>Best|Target|Target|member|||||||
|||||||||||Guide|||||||
||||||||||||||||||
|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Lịch trình theo từng giai đoạn|Lịch trình theo từng giai đoạn|Lịch trình theo từng giai đoạn|Lịch trình theo từng giai đoạn|Lịch trình theo từng giai đoạn|Lịch trình theo từng giai đoạn|Lịch trình theo từng giai đoạn|
|||||||||||Define MeasureAnalyzeImprove Control<br>00/00 00/00 00/00 00/00 00/00 00/0|Define MeasureAnalyzeImprove Control<br>00/00 00/00 00/00 00/00 00/00 00/0|Define MeasureAnalyzeImprove Control<br>00/00 00/00 00/00 00/00 00/00 00/0|Define MeasureAnalyzeImprove Control<br>00/00 00/00 00/00 00/00 00/00 00/0|Define MeasureAnalyzeImprove Control<br>00/00 00/00 00/00 00/00 00/00 00/0|Define MeasureAnalyzeImprove Control<br>00/00 00/00 00/00 00/00 00/00 00/0|Define MeasureAnalyzeImprove Control<br>00/00 00/00 00/00 00/00 00/00 00/0|
|Phạm vi hoạt động|Phạm vi hoạt động|Phạm vi hoạt động|Thành quả hoạt động|Thành quả hoạt động|Thành quả hoạt động|Thành quả hoạt động|Thành quả hoạt động|Thành quả hoạt động|Thành quả hoạt động|Neck Point và nội dung yêu càu hỗ trợ|Neck Point và nội dung yêu càu hỗ trợ|Neck Point và nội dung yêu càu hỗ trợ|Neck Point và nội dung yêu càu hỗ trợ|Neck Point và nội dung yêu càu hỗ trợ|Neck Point và nội dung yêu càu hỗ trợ|Neck Point và nội dung yêu càu hỗ trợ|
||||Định<br>lượng|Định<br>lượng|||||||||||||
||||Định<br>tính|Định<br>tính|||||||||||||

204


**Bối cảnh xúc tiến thì phải mô tả một cách cụ thể và rõ ràng về tình huống cạnh tranh thị**
**trường, xu hướng công nghiệp, ý kiến khách hàng, tính liên quan đến mục tiêu doanh**
**nghiệp và dự án lựa chọn để đảm bảo tính khả thi của dự án.**

**Vision và mục tiêu doanh nghiệp**


✓ Các nội dung phải bao gồm trong bối cảnh tiến hành

  - Tính quan trọng của thi hành dự án này
(xu hướng thị trường và công ty cạnh tranh)



- Hướng kinh doanh của công ty và tính
liên quan đến mục tiêu.

 - Nội dung yêu cầu của khách hàng

- Tính tất yếu về lý do phải thi hành dự
án này vào thời điểm bây giờ.

- Thứ tự ưu tiên của các hoạt động liên
quan đến dự án.

- Thành quả dự đoán qua thi hành dự án



**Xu hướng công nghiệp**





**Công ty cạnh tranh**



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
205

**Là việc kĩ thuật một cách cụ thể tại sao phải làm hoạt động cải tiến và vấn đề của**
**Process hiện tại là vấn đề gì**

cf. Bối cảnh xúc tiến chủ yếu là việc diễn tả mục đích sau khi nắm được tiêu điểm về lợi ích của Business thông qua

thực hiện dự án

       **Cái gì làm sai và hoặc cái gì đang không thể làm?**

       **Cái gì trở thành cơ hội phải được cải tiến?**

       **Do vấn đề này, “khó khăn” của khách hàng là gì?**

       **Khi nào, ở đâu phát sinh vấn đề?**

       **Vấn đề này nghiêm trọng bao nhiêu và phạm vi rộng như thế nào?**

**[Ví dụ] Cải tiến sáng IPS Monitor**

          - **Phát sinh liên tục tình trạng sáng của Model IPS** do vấn đề của System Matching

          Trong lỗi sản phẩm khách hàng, **tỉ trọng lỗi sáng là 50%**, từ tháng 1 năm 00 1, tỉ lệ lỗi là trên 2% và phát sinh liên tục (tiêu chuẩn

công ty khách hàng)

          - Lỗi sáng phát sinh do ① Distortion do công đoạn LCM, ② Distortion do ảnh hưởng môi trường độ tin cậy ③ Distortion khi kết nối
System, ở góc độ thiết kế cơ khí, lựa chọn **đối tượng cải tiến** **①** **và** **③** là có thể cải tiến

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
206

**Là việc viết mục tiêu muốn thành công qua dự án nên mục tiêu đó phải là cụ thể, được**
**đo, có thể thành công trong thời gian thực hiện dự án.**

✓ Chú ý cân nhắc

    - Team thi hành dự án muốn đạt được gì?

    - Thành quả cụ thể và rõ ràng là gì?

(ví dụ: giảm lỗi, tiết kiệm chi phí, Cycle time v.v..)

~~-~~ ~~Thành~~ ~~quả~~ ~~vô~~ ~~hình~~ ~~hoặc~~ ~~định~~ ~~tính~~ ~~mà~~ ~~không~~ ~~thể~~ ~~đo~~ ~~được~~ ~~là~~ ~~gì?~~

**[Ví dụ] Cải tiến sáng IPS Monitor**



|Major Objective|Mục tiêu hoạt động|Col3|Col4|Col5|
|---|---|---|---|---|
|Major Objective|KPI|Mức độ hiện tại|World’s Best|Target|
|Cải tiến sáng IPS Monitor|Tỉ lệ lỗi sáng|2.0%|0.5%|0.2%|


Note


**Điểm khác KPI và CTQ là gì?**
KPI là chỉ số có nghĩa mà có thể biểu hiện thành quả doanh nghiệp, còn CTQ là một chỉ số thường khái
niệm hạ vị so với KPI và có thể đại diện thành quả Project một cách trực tiếp.


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
207

**Thiết lập mục tiêu là việc chọn mục tiêu cải tiến của KPI, thiết lập sau khi phản ánh hiệu quả**

~~수준실적~~

~~**hà**~~ **n** ~~**h**~~ **t** ~~**í**~~ **c** ~~**h**~~ **t** ~~**iê**~~ **u c** ~~**h**~~ **u** ~~**ẩ**~~ **n** ~~**đã**~~ ~~**đ**~~
**dự tính bằng nền móng t** **ược kiểm tra**

**Thiết lập một cách quyết tâm và đổi mới để có thể đạt được mục tiêu dự án cũng như đảm bảo và duy trì**

**vị thế cạnh tranh**

 - Mục tiêu để doanh nghiệp hàng đầu vừa có thể nâng tầm tiêu chuẩn vừa có thể thực hiện phân biệt hóa (định hướng hàng đầu

thế giới)

  - Mục tiêu vừa có thể đạt được mục tiêu dự án, vừa nâng cao tỉ lệ cải tiết mang tính đổi mới so mới tiêu chỉ số hiện tại

**②** **Breakthrough nâng cao thành quả**



~~**Thà**~~ **n** ~~**h**~~ **qu** ~~**ả**~~


**Mục**

**tiêu**

**thường**

**ngày**

**Time**





**World**

**Top**



**Công ty A**

|Col1|B’ Goa|
|---|---|
||A’|
|Goal<br>B||


**①** **Breakthrough**
**kéo về thời điểm đạt được**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
208

**Được soạn thảo để quy định ranh giới của cơ hội cải tiến là từ đâu đến đâu**

✓ Chú ý cân nhắc
       - Điểm bắt đầu và kết thúc của Process là ở đâu?

       - Lĩnh vực nào cũng tổ chức được bao gồm vào dự án?

       - Khách hàng và sản phẩm nào của Process đối tượng được bao gồm?

       - Hoạt động Team phải đạt được ở trong điều kiện giới hạn nào?

**Điểm bắt đầu** ~~**Đ**~~ **iểm kết thúc**

**Phạm vi**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
209

**Là việc lựa chọn thành viên Team sẽ xúc tiến dự án và phân bổ trách nhiệm**

✓ Chú ý cân nhắc

    - Champion, Process Owner, chỉ đạo MBB/BB là ai và có trách nhiệm trong Team như thế nào?

     - Mỗi nhân viên có vai trò gì và sẽ cần ở giai đoạn nào?

    - Team Leader có trách nhiệm gì?

    - Chu kì và phương pháp báo cáo của Team là?

~~-~~ ~~Những~~ ~~dạng~~ ~~thành~~ ~~viên~~ ~~nào~~ ~~sẽ~~ ~~cần~~ ~~ở~~ ~~giai~~ ~~đoạn~~ ~~nào?~~

**※ Vai trò 6Sigma Belt**

**Champion(lãnh đạo và phụ trách)**

                                                - Trách nhiệm tổng quản xúc tiến 6Sigma
trong tổ chức

**Process Owner(Team Leader)** **Master Black Belt**



- Duy trì Process đã được cải tiến và cải tiến liên tục




 - Chỉ đạo Project, đào tạo Belt, xây dựng 6Sigma

 - Leader tiến hành cải tiến lỗi khiếm khuyết/Neck
trong tổ chức

**Black Belt**

 - Leader tiến hành dự án little y trong tổ chức

**Green Belt**

 - Thành viên Team dự án BB



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
210

**SMART” .**
**Sau khi soạn xong bản nháp Đơn đăng ký, đánh giá theo tiêu chuẩn “**

**“SMART**
**” là checklist để đảm bảo đơn đăng ký dự án có hiệu quả và nhất quán với nhau.**

**Specific**



 Có đang giải quyết các vấn đề kinh doanh cụ thể trên
thực tế không? (Don’t boil the Ocean! Tức, quy mô
của dự án dã phù hợp hay chưa?)

**Measurable**



Ví dụ không tốt: Nâng cao hiệu suất Panel

Ví dụ tốt: Giảm lỗi điểm đen thông qua cải tiến lỗi dị vật



     -     Có phải là vấn đề có thể đo lường được không? Đã đo Ví dụ không tốt: “Hãy quan tâm đến sức khỏe của bạn”
~~thành~~ ~~quả~~ ~~hiện~~ ~~tại~~ ~~và~~ ~~đã~~ ~~định~~ ~~ra~~ ~~mục~~ ~~tiêu~~ ~~cải~~ ~~tiến~~ ~~chưa?~~ ~~▪~~ ~~Ví~~ ~~dụ~~ ~~tốt:~~ ~~“Hãy~~ ~~duy~~ ~~trì~~ ~~tỷ~~ ~~lệ~~ ~~mỡ~~ ~~trong~~ ~~cơ~~ ~~thể~~ ~~ở~~ ~~mức~~ ~~10-20%”~~

**Aggressive** **& Attainable**

     -     Mục tiêu có phải là quá dễ đạt được không? Ví dụ không tốt: “Hãy giảm 100% lỗi ngay lập tức”

     -     Mục tiêu liệu có khả năng đạt được hay không? Ví dụ tốt: “Hãy giảm số lượng lỗi xuống 1/8 trong vòng 3 năm”

     Thời gian thực hiện dự án có thực tế không?

**Relevant**    - Ví dụ không tốt: “Tăng doanh thu bán hàng ở khu vực B không

     Dự án có phù hợp với chiến lược kinh doanh không? phải là khu vực chiến lược”

                              Ví dụ tốt: “Tăng 50%” Market Share ở khu vực chiến lược A”

**Time Bound**

     -     Đã quyết định được lịch trình hoàn thành dự án chưa? Ví dụ không tốt: “Giảm cân”

                              Ví dụ tốt: “Giảm 10kg trong vòng 6 tháng.”

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
211

|□ Kết nối TDR toàn công ty<br>Đơn đăng kí Project 6σ<br>□CO/bộ phận doanh nghiệp<br>□✓<br>N eck nội bộ tổ chức|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|□✓<br>Project chứng nhận<br>□ Project thường<br>□ Khác|Col12|Col13|□ Project MBB(ứng viên)<br>□✓ P roject BB(ứng viên)<br>□ Project GB(ứng viên)|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tên Project|Tên Project|Cải tiến sáng IPS Monitor|Cải tiến sáng IPS Monitor|Cải tiến sáng IPS Monitor|Cải tiến sáng IPS Monitor|Cải tiến sáng IPS Monitor|Loại Project|Mfg|Mfg|Mfg|Mfg|Thời gian hoạt động|Thời gian hoạt động|Thời gian hoạt động|2000/00~2000/00|2000/00~2000/00|2000/00~2000/00|
|Leader|Leader|홍길동선임|홍길동선임|홍길동선임|홍길동선임|홍길동선임|Bộ phận|Thiết kế cơ khí/quang học team 1|Thiết kế cơ khí/quang học team 1|Thiết kế cơ khí/quang học team 1|Thiết kế cơ khí/quang học team 1|Thiết kế cơ khí/quang học team 1|Thiết kế cơ khí/quang học team 1|Thiết kế cơ khí/quang học team 1|Thiết kế cơ khí/quang học team 1|Thiết kế cơ khí/quang học team 1|Thiết kế cơ khí/quang học team 1|
|Hiện trạng và vấn đề|Hiện trạng và vấn đề|Hiện trạng và vấn đề|Hiện trạng và vấn đề|Hiện trạng và vấn đề|Hiện trạng và vấn đề|Hiện trạng và vấn đề|Hiện trạng và vấn đề||Thành viên Team|Thành viên Team|Thành viên Team|Thành viên Team|Thành viên Team|Thành viên Team|Thành viên Team|Thành viên Team|Thành viên Team|
|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|Vai trò|Vai trò|Bộ phận|Bộ phận|Bộ phận|Tên|Tên|Belt|Tham<br>gia|
|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|Leader|Leader|Thiết kế cơ khí/quang<br>học team 1|Thiết kế cơ khí/quang<br>học team 1|Thiết kế cơ khí/quang<br>học team 1|홍길동<br>SY|홍길동<br>SY|GB|Fulltime|
|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|• Trong lỗi sản phẩm khách hàng, tỉ trọng lỗi sáng là 50%, từ tháng 1 năm 00 1, tỉ lệ lỗi là<br>trên 2% và phát sinh liên tục (tiêu chuẩn công ty khách hàng)<br>• Lỗi sáng phát sinh do ①Distortion do công đoạn LCM, ②Distortion do ảnh hưởng môi<br>trường độ tin cậy ③Distortion khi kết nối System, ở góc độ thiết kế cơ khí, lựa chọn đối<br>tượng cải tiến ①và ③là có thể cải tiến|Member|Member|Thiết kế cơ khí/quang<br>học team 1|Thiết kế cơ khí/quang<br>học team 1|Thiết kế cơ khí/quang<br>học team 1|슈퍼맨J|슈퍼맨J|GB|Fulltime|
|Major Objective|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|Mục tiêu hoạt động|
|Major Objective|KPI|KPI|KPI|Chỉ số hiện tại|World’s Best|Target|Target|Target|Member|Member|Thiết kế cơ khí/quang<br>học team 2|Thiết kế cơ khí/quang<br>học team 2|Thiết kế cơ khí/quang<br>học team 2|헐크S|헐크S|GB|Parttime|
|Cải tiến lỗi sáng IPS|Tỉ lệ lỗi sáng<br>(FFR)|Tỉ lệ lỗi sáng<br>(FFR)|Tỉ lệ lỗi sáng<br>(FFR)|2.0%|0.5%|0.2%|0.2%|0.2%|0.2%|0.2%|0.2%|0.2%|0.2%|0.2%|0.2%|0.2%|0.2%|
|Cải tiến lỗi sáng IPS|Tỉ lệ lỗi sáng<br>(FFR)|Tỉ lệ lỗi sáng<br>(FFR)|Tỉ lệ lỗi sáng<br>(FFR)|2.0%|0.5%|0.2%|0.2%|0.2%|Member|Member|Team bảo đảm chất<br>lượng|Team bảo đảm chất<br>lượng|Team bảo đảm chất<br>lượng|변사또J|변사또J|No Belt|Parttime|
|Cải tiến lỗi sáng IPS|Tỉ lệ lỗi sáng<br>(FFR)|Tỉ lệ lỗi sáng<br>(FFR)|Tỉ lệ lỗi sáng<br>(FFR)|2.0%|0.5%|0.2%|0.2%|0.2%|Chỉ đạo|Chỉ đạo|Thiết kế cơ khí/quang<br>học team 1|Thiết kế cơ khí/quang<br>học team 1|Thiết kế cơ khí/quang<br>học team 1|코난CY|코난CY|MBB|Parttime|
|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|
|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Khái quát hoạt động|Lịch trình hoạt động theo từng giai đoạn|Lịch trình hoạt động theo từng giai đoạn|Lịch trình hoạt động theo từng giai đoạn|Lịch trình hoạt động theo từng giai đoạn|Lịch trình hoạt động theo từng giai đoạn|Lịch trình hoạt động theo từng giai đoạn|Lịch trình hoạt động theo từng giai đoạn|Lịch trình hoạt động theo từng giai đoạn|Lịch trình hoạt động theo từng giai đoạn|
|1. Rõ ràng hóa tiêu chuẩn phán định sáng (With Customer)<br>2. Đánh giá độ nhấn mặt sau IPS Model<br>3. Đưa ra vật cơ khí LCM và CTQ của quan điểm System để nâng cao chỉ số thực lực<br>sáng<br>4. Ứng dụng phương án cải tiến LCM & System và kiểm chứng|1. Rõ ràng hóa tiêu chuẩn phán định sáng (With Customer)<br>2. Đánh giá độ nhấn mặt sau IPS Model<br>3. Đưa ra vật cơ khí LCM và CTQ của quan điểm System để nâng cao chỉ số thực lực<br>sáng<br>4. Ứng dụng phương án cải tiến LCM & System và kiểm chứng|1. Rõ ràng hóa tiêu chuẩn phán định sáng (With Customer)<br>2. Đánh giá độ nhấn mặt sau IPS Model<br>3. Đưa ra vật cơ khí LCM và CTQ của quan điểm System để nâng cao chỉ số thực lực<br>sáng<br>4. Ứng dụng phương án cải tiến LCM & System và kiểm chứng|1. Rõ ràng hóa tiêu chuẩn phán định sáng (With Customer)<br>2. Đánh giá độ nhấn mặt sau IPS Model<br>3. Đưa ra vật cơ khí LCM và CTQ của quan điểm System để nâng cao chỉ số thực lực<br>sáng<br>4. Ứng dụng phương án cải tiến LCM & System và kiểm chứng|1. Rõ ràng hóa tiêu chuẩn phán định sáng (With Customer)<br>2. Đánh giá độ nhấn mặt sau IPS Model<br>3. Đưa ra vật cơ khí LCM và CTQ của quan điểm System để nâng cao chỉ số thực lực<br>sáng<br>4. Ứng dụng phương án cải tiến LCM & System và kiểm chứng|1. Rõ ràng hóa tiêu chuẩn phán định sáng (With Customer)<br>2. Đánh giá độ nhấn mặt sau IPS Model<br>3. Đưa ra vật cơ khí LCM và CTQ của quan điểm System để nâng cao chỉ số thực lực<br>sáng<br>4. Ứng dụng phương án cải tiến LCM & System và kiểm chứng|1. Rõ ràng hóa tiêu chuẩn phán định sáng (With Customer)<br>2. Đánh giá độ nhấn mặt sau IPS Model<br>3. Đưa ra vật cơ khí LCM và CTQ của quan điểm System để nâng cao chỉ số thực lực<br>sáng<br>4. Ứng dụng phương án cải tiến LCM & System và kiểm chứng|1. Rõ ràng hóa tiêu chuẩn phán định sáng (With Customer)<br>2. Đánh giá độ nhấn mặt sau IPS Model<br>3. Đưa ra vật cơ khí LCM và CTQ của quan điểm System để nâng cao chỉ số thực lực<br>sáng<br>4. Ứng dụng phương án cải tiến LCM & System và kiểm chứng|1. Rõ ràng hóa tiêu chuẩn phán định sáng (With Customer)<br>2. Đánh giá độ nhấn mặt sau IPS Model<br>3. Đưa ra vật cơ khí LCM và CTQ của quan điểm System để nâng cao chỉ số thực lực<br>sáng<br>4. Ứng dụng phương án cải tiến LCM & System và kiểm chứng|Define Measure Analyze Improve Control<br>07/15 08/31 10/19 11/16 12/14 12/28|Define Measure Analyze Improve Control<br>07/15 08/31 10/19 11/16 12/14 12/28|Define Measure Analyze Improve Control<br>07/15 08/31 10/19 11/16 12/14 12/28|Define Measure Analyze Improve Control<br>07/15 08/31 10/19 11/16 12/14 12/28|Define Measure Analyze Improve Control<br>07/15 08/31 10/19 11/16 12/14 12/28|Define Measure Analyze Improve Control<br>07/15 08/31 10/19 11/16 12/14 12/28|Define Measure Analyze Improve Control<br>07/15 08/31 10/19 11/16 12/14 12/28|Define Measure Analyze Improve Control<br>07/15 08/31 10/19 11/16 12/14 12/28|Define Measure Analyze Improve Control<br>07/15 08/31 10/19 11/16 12/14 12/28|
|Phạm vi hoạt động|Phạm vi hoạt động|Phạm vi hoạt động|Thành quả hoạt động|Thành quả hoạt động|Thành quả hoạt động|Thành quả hoạt động|Thành quả hoạt động|Thành quả hoạt động|Neck Point và yêu cầu hỗ trợ|Neck Point và yêu cầu hỗ trợ|Neck Point và yêu cầu hỗ trợ|Neck Point và yêu cầu hỗ trợ|Neck Point và yêu cầu hỗ trợ|Neck Point và yêu cầu hỗ trợ|Neck Point và yêu cầu hỗ trợ|Neck Point và yêu cầu hỗ trợ|Neck Point và yêu cầu hỗ trợ|
|Plus 00 230W<br>IPS Monitor Model|Plus 00 230W<br>IPS Monitor Model|Plus 00 230W<br>IPS Monitor Model|- Đưa ra CTQ linh kiện cơ khí cải tiến sáng<br>- Đảm bảo kĩ thuật Robust Design cân nhắc System<br>Matching|- Đưa ra CTQ linh kiện cơ khí cải tiến sáng<br>- Đảm bảo kĩ thuật Robust Design cân nhắc System<br>Matching|- Đưa ra CTQ linh kiện cơ khí cải tiến sáng<br>- Đảm bảo kĩ thuật Robust Design cân nhắc System<br>Matching|- Đưa ra CTQ linh kiện cơ khí cải tiến sáng<br>- Đảm bảo kĩ thuật Robust Design cân nhắc System<br>Matching|- Đưa ra CTQ linh kiện cơ khí cải tiến sáng<br>- Đảm bảo kĩ thuật Robust Design cân nhắc System<br>Matching|- Đưa ra CTQ linh kiện cơ khí cải tiến sáng<br>- Đảm bảo kĩ thuật Robust Design cân nhắc System<br>Matching|Co-work bảo mật cao của người chuyên môn thiết kế của<br>2 công ty LGD & Customer|Co-work bảo mật cao của người chuyên môn thiết kế của<br>2 công ty LGD & Customer|Co-work bảo mật cao của người chuyên môn thiết kế của<br>2 công ty LGD & Customer|Co-work bảo mật cao của người chuyên môn thiết kế của<br>2 công ty LGD & Customer|Co-work bảo mật cao của người chuyên môn thiết kế của<br>2 công ty LGD & Customer|Co-work bảo mật cao của người chuyên môn thiết kế của<br>2 công ty LGD & Customer|Co-work bảo mật cao của người chuyên môn thiết kế của<br>2 công ty LGD & Customer|Co-work bảo mật cao của người chuyên môn thiết kế của<br>2 công ty LGD & Customer|Co-work bảo mật cao của người chuyên môn thiết kế của<br>2 công ty LGD & Customer|


Source : IT/Mobile 기구 / 광학설계 1 팀이명수주임

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
212

#### **1.2. Phân tích Process**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
213

**Vì process thực tế phức tạp nên phải nắm bắt qua sơ đồ**

**What it could be...** **What you think it is...** **What it actually is...**

**Process lý tưởng** **Cái chúng ta nghĩ** **Process thực tế**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
214

**Tại sao lại cần quan điểm Process?**




~~**Trước**~~ ~~**đây:**~~ ~~**từ**~~ ~~**con**~~ ~~**người**~~ ~~**6Sigma:**~~ ~~**từ**~~ ~~**Process**~~








    - **Thành quả**

      - Từ kiến thức kĩ thuật/kinh nghiệm

      - Từ sự may mắn như phép thuật

    **Thất bại**

      - Không có người này sẽ lớn chuyện

      - Khi có vấn đề mới thì phương án đối ứng

tạm thời…

      - Sự khó khăn của thiếu vật liệu của Process…

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
215



- **Thành quả**

~~-~~ ~~Từ~~ ~~kiến~~ ~~thức~~ ~~Process~~

 - Từ cải tiến Process

**Kiến thức về Process càng**
**nhiều, độ cạnh tranh của tổ**

  - **Làm rõ phạm vi thực hiện và vùng cải tiến của Process**

  - **Phân tích và List-up các chỉ số có thể đo trong Process, và đưa ra nhân tố tiềm ẩn để cải tiến CTQ thông qua phân tích phân tầng,…**

  **Hiểu về mối quan hệ giữa hình dáng tổng thể và giai đoạn chi tiết của Process, định nghĩa rõ ràng về các giai đoạn Process dễ bị bỏ qua**

Thông qua việc này, có thể đưa ra điểm bất hợp lý và cải tiến ngay lập tức

※ Hiểu Process phát sinh thực tế không phải Process trong suy nghĩ hay văn bản, và hiểu về Activity chi tiết

**Thông qua mối quan hệ giữa các giai đoạn, việc giao tiếp giữa các bộ phận chức năng được thuận tiện và có ích khi phân công vai trò**

**của dự án**

  **Tất cả chỉ số Output và Input liên quan đến đối tượng cải tiến**

※ Kiểm thảo từng Activity trong Process từ các yếu tố Input đến Output → Sử dụng Source để đưa ra CTQ sau này (bao gốm đặc tính thay thế, đặc tính giới

hạn) và nhân tố tiềm ẩn

  **Thông qua phân tích Process chi tiết, đưa ra Quick Win có thể “đưa ra thành quả dựa vào việc thực thi nhanh chóng”**

  **Đưa ra dự án cần phải cải tiến thêm**


Note


Quick Win là?

- Cơ hội cải tiến cực kỳ dễ và rõ ràng

- Là cơ hội cải tiến có thể thực hiện một cách nhanh chóng và đơn giản, **trước việc đo lường chi tiết và phân tích của dự án**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
216

 **Process Mapping là,**

**Là việc ghi lại Process đi từ Input đến Output, bằng việc đưa ra các thông tin hay Flow sản phẩm**

**theo thứ tự**

~~•~~
~~**Tính**~~ ~~**cần**~~ ~~**tiết**~~

① Nâng cao hiểu biết về Process đó và có thể thu hẹp Process đối tượng cải thiện

② Có thể ứng dụng cho nắm bắt Input, Output trong Process và tính liên quan giữa process

③ Chỉ định cho Team tập trung vào Process nào hoặc sản phẩm nào

~~④~~ ~~Ch~~ o ~~biết~~ ~~T~~ eam p ~~hải~~ c ~~ải~~ ~~thiệ~~ n ~~lĩ~~ n ~~h~~ vực n ~~à~~ o, c ~~h~~ o ~~biết~~ ~~điể~~ m ~~bắt~~ ~~đầ~~ u v ~~à~~ ~~điể~~ m ~~kết~~ ~~thú~~ c

⑤ Làm rõ về lĩnh vực bên ngoài phạm vi và tài nguyên mà Team có thể sử dụng

  **Tool : SIPOC, FDPM**

※ Ngoài việc phân tích Process, phân tích định tính có thể sử dụng FAST(Function Analysis Structure

Technique) (tham khảo phụ lục)


Note


Định nghĩa Process

- ‘Là chuỗi những hoạt động để đạt được kết quả đặc biệt’

- Là hoạt động (Activities) nhận yếu tố đầu vào (Input) và sáng tạo ra thành quả (Output) mang giá trị
(value) đến cho khách hàng (Customer)


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
217

**Thông qua phân tích nhân tố cấu thành và hoạt động chi tiết của Process, đưa ra Quick**
**Win có thể mang lại thành quả dựa trên cơ hội cải tiến chi tiết (hạng mục) và việc thực**
**hiện nhanh chóng**

  - Vẽ SIPOC và làm rõ Output mà khách hàng mong muốn, sau đó triển khai Process Mapping cho khớp


|Col1|Phân tích Process tổng quát<br>SIPOC<br>Làm rõ phạm vi Project và nhân tố cấu<br>thành Process|Col3|Col4|Col5|Phân tích chi tiết Process<br>FDPM|Col7|
|---|---|---|---|---|---|---|
||Phân tích Process tổng quát<br>SIPOC<br>Làm rõ phạm vi Project và nhân tố cấu<br>thành Process||||||
||Phân tích Process tổng quát<br>SIPOC<br>Làm rõ phạm vi Project và nhân tố cấu<br>thành Process||||||


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
218


   **Định nghĩa: là phương pháp Process Mapping biểu đồ hóa nhân tố cấu thành bằng**
**Process Map tổng quát của vùng phát sinh vấn đề**
**- Chỉ định rõ vùng phát sinh vấn đề (vùng cải tiến) bằng Process của SIPOC**

**Supplier** **Input** **Process** **Output** **Customer**

**Start :** **End :**

   - **Mục đích**

     - Nắm bắt nhân tố cấu thành chủ yếu của Process của vùng (hoặc công đoạn) dự đoán phát sinh vấn đề, có thể biết
được cấu tạo đại khái của toàn thể Process

     - Cung cấp thông tin sơ khai để phân tích thêm Process

   - **Phương pháp soạn thảo**

① Làm rõ Process định cải tiến
② Làm rõ bắt đầu và kết thúc của Process, tức là làm rõ ranh giới của Process
③ Liệt kê Output chủ yếu và Customer
④ Liệt kê Input chủ yếu và Supplier
⑤ Nếu như có thể, đưa ra giai đoạn Process chủ yếu, định danh và chọn thứ tự (Guideline: tối đa 5 ~ 7 giai đoạn)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
219

※ Trường hợp cải tiến lỗi, vẽ Process Map về công phát sinh lỗi hoặc công đoạn dự đoán phát sinh lỗi

**Thông tin yêu cầu** **Thông tin yêu cầu**
###### **S I P O C**


**N** **uồn cun** **cấ**
**g** **g** **p**

**(Supplier)**


**Tài n** **u** **ên** **Kết** **uả** **Khách hàn**
**g** **y** **q** **g**

~~**Process**~~
**(Input)** **(Output)** **(Customer)**


~~**Process**~~
**(Input)**


**Khách hàn**
**g**


☞
Trong yếu tố Input, kiểm tra xem có phải
vì nhân tố đặc biệt sai mà dẫn đến lỗi trên
Process hay không


☞
Yếu tố Output: lựa chọn làm ứng viên CTQ


**Nguồn cung cấp (supplier)**

**Tài nguyên (input)**

**Kết quả(output)**

**Khách hàng (customer)**


Tất cả những người cung cấp tài nguyên cho Process

Là tài liệu, tài nguyên và Data cần thiết cho việc thực hiện Process

Là sản phầm hay linh phụ kiện hữu hình của Service, là kết quả của Process

Tất cả những người nhận sản phẩm Process dù từ nội bộ hay ngoại bộ


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
220

 **Định nghĩa : Là phương pháp Process Mapping biểu đồ hóa bộ phận chủ quan về đưa ra**
**quyết định và thứ tự của Process dưới và hoạt động (Activities) cụ thể liên quan đến Process**
**của SIPOC, sau đó nắm bắt được Flow một cách dễ dàng**


Ex) Process vận chuyện vật phẩm












**Phương pháp soạn thảo**

① Định nghĩa điểm bắt đầu và kết thúc của Process

② Ghi lại giai đoạn (Step) Process theo thứ tự
③ Ghi lại chất liệu trách nhiệm/vị trí tiến hành từng

giai đoạn theo trục ngang
④ Ghi lại nội dung đưa ra quyết định và giái

đoạn/hoạt động cấu thành Process
⑤ Kiểm tra thứ tự hoạt động được tiến hành thực tế
⑥ Biểu thị Flow Process bằng mũi tên

⑦ Ghi lại Inputs, Outputs của Activity

※ Giải thích kí hiệu

Điểm bắt đầu, kết thúc Activity

Đưa ra quyết định Hướng/Flow

Input, Output Điểm kết nối Process

**A1** Số hoạt động **D1** Số đưa ra quyết định

|Bộ phận<br>chủ quản<br>Step|Nhân viên<br>cửa hàng|Người quản<br>lý|Quản lý kho|Người lên<br>kế hoạch|
|---|---|---|---|---|
|Đặt hàng|Kiểm tra đặt hàng<br>A1<br>Đặt hàng||||
|Kiểm tra<br>linh kiện||N<br>D1<br>Phê duyệt đơn<br>Y|A2<br>Đóng gói|A3<br>Nhập hệ thống|
|Giao hàng|N<br>Giao hàng|D2<br>Phê duyệt giao hàn<br>Y|g||


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
221

   **Chú ý cân nhắc**

     **Phải là người thành thạo tham gia thì mới soạn thảo được Process Map đúng nhất.**

        Đối tượng tham gia : người định nghĩa Process (Process Owner), người thực hành Process(Người thực hiện),
người làm thay đổi Process

        Tài liệu tham khảo : Manual người thao tác, Spec. kỹ thuật, tài liệu 5M + 1E

     **Soạn thảo một Process đang thi hành thực tế, chứ không phải là Process suy nghĩ trong đầu**

      - Chỉnh sửa Process Map mà cá nhân suy nghĩ bằng Process Map thực tế thông qua việc xác nhận hiện trạng

       - Process Map không phải việc liệt kê ra các công việc đương nhiên phải thực hiện, mà là biểu đồ hóa các công việc
**đang thực hiện trên thực tế**
~~**-**~~ ~~**Trước**~~ ~~**khi**~~ ~~**phân**~~ ~~**tích**~~ ~~**vấn**~~ ~~**đề**~~ ~~**của**~~ ~~**Process**~~ **,** ~~**phải**~~ ~~**soạn**~~ ~~**thảo**~~ ~~**Process**~~ ~~**một**~~ ~~**cách**~~ ~~**đàng**~~ ~~**hoàng**~~ ~~**đã**~~

✓
**A. Process mình nghĩ** **B. Process trên trực tế** **C. Process lí tưởng**

※ Ở quan điểm phương án giải quyết, cần

cấn nhắc Process lí tưởng coi trọng chức
năng cơ bản mà loại bỏ được tổn thất và
chức năng bổ trợ

     **Phải vẽ chi tiết**
**đến mức Hidden Factory xuất hiện** (tái thao tác, Repair,…)

     **Phải thường xuyên kiểm tra, đổi mới cập nhật Process Map**

       - Process Map lần đầu tiên không thể hoàn hảo tuyệt đối,
Trước khi phân tích, phải kiểm chứng thông qua hoạt động team và phải khảo sát lại kỹ càng

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
222

**Sau khi phân tích Process, tìm ra phần có thể cải tiến ngay lập tức trong Process hiện tại**
**và triển khai hoạt động Quick Win**

   **Quick Win là?**

   - Là cơ hội cải tiến rất dễ và rõ ràng

   - Là cơ hội cải tiến có thể **thực hiện một cách nhanh chóng và đơn giản**, trước việc đo lường chi tiết

và phân tích của dự án

   **Điều kiện thành công Quick Win**

~~-~~ ~~Có~~ ~~sự~~ ~~kiểm~~ ~~soát~~ ~~của~~ ~~Team~~ ~~liên~~ ~~quan~~

   - Có thể mang lại thành công ngay lập tức

   - Có thể thực thi nhanh chóng

   **Đối tượng Quick Win**

**- Thời gian** **:** Chi phí và Cycle Time Process có mỗi liên hệ mật thiết. Cân nhắc phương án có thể tránh được kiểm tra,

Neck, tái thao tác, Stand by, phê duyệt,…

**- Chi phí** **:** Tìm ra tính không hiệu suất của Process, tích cực hóa giảm chi phí đến khi được loại bỏ, Cân nhắc tái thao

tác, gián đoạn, Stand by,…

**- Giá trị gia tăng** **:** Nắm bắt hoạt động giá trị gia tăng chi phí tồn tại trong Process. Cân nhắc giai đoạn tái thao tác, kiểm tra,…

**- Gap giá trị kì vọng :** Hiểu được yêu cầu của khách hàng, cải tiến về các Gap chủ yếu tồn tại giữa- thnhf quả hiện tại của Process

và giá trị kì vọng của khách hàng. Phải tập trung nỗ lực

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
223

#### **2. Lựa chọn CTQ**

**2.1. Đ** **nh n** **hĩa n** **i dun** **êu cầu**
**ị** **g** **ộ** **g** **y**

**chủ chốt khách hàng**

**2.2. Lựa chọn CTQ**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
~~224~~

**​**


**​**


**​**



         
**​**
Thu thập và phân tích ý kiến của khách hàng để rút ra các yêu cầu chủ chốt của khách hàng


**​**


**​**


**​**


**​**

Lựa chọn chỉ tiêu đại diện thành quả Project cho CTQ [1) ] qua phân tích chỉ tiêu Output đã được
liên kết với nội dung yêu cầu chủ chốt của khách hàng.

FMEA, cân nhắc lý thuyết, chỉ số Output Process

Lựa chọn CTQ và Spec CTQ [1)]


**​**


**​**


**​**

- Phân tích yêu cầu chủ chốt của khách hàng


**​**


**​**

- Lựa chọn CTQ

- Kiểm tra tính thỏa đáng của CTQ

- Định nghĩa vận hành CTQ và thiết lập Spec

Phân tích hồi quy/Phân tích hồi quy Logistic


**​**


**​**


**​**


**​**


**​**


**​**


**​**

1) CTQ : Critical to Quality, giá trị đặc tính chủ chốt gây ảnh hưởng đến chất lượng theo quan điểm kinh doanh và khách hàng.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
225

#### **2.1. Định nghĩa nội dung yêu cầu ** **chủ chốt khách hàng**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
226

**Đưa ra các chỉ số Output của Process liên kết với yêu cầu chủ chốt theo quan điểm của khách**
**hàng (CCR) và yêu cầu cốt lõi theo quan điểm kinh doanh (CBR) rồi lựa chọn chỉ sốcó mức**

※ Tham khảo CCR, CBR
**tương quan cao nhất làm CTQ.**


|Col1|Col2|Col3|
|---|---|---|
|1 Cân nhắc về CCR và CBR rồi đưa ra chỉ tiêu Output<br>Giai Trong các chỉ tiêu Output được đưa ra, lựa chọn một hoặc nhiều chỉ tiêu có mức độ ảnh hưởng<br>2<br>đoạn lớn nhất đối với CCR và CBR cho CTQ.<br>Define<br>3 Định nghĩa về Spec mà có thể thỏa mãn khách hàng|1|1|
|1 Cân nhắc về CCR và CBR rồi đưa ra chỉ tiêu Output<br>Giai Trong các chỉ tiêu Output được đưa ra, lựa chọn một hoặc nhiều chỉ tiêu có mức độ ảnh hưởng<br>2<br>đoạn lớn nhất đối với CCR và CBR cho CTQ.<br>Define<br>3 Định nghĩa về Spec mà có thể thỏa mãn khách hàng|3|3|
||||


~~**Gi**~~ **a** ~~**i**~~ ~~**đ**~~ **oạn**

**Measure**


~~**4**~~ **Thiết lập tiêu chuẩn mục tiêu và mức chuẩn**




**Mục tiêu**
**doanh nghiệp**
**Process nội bộ**

|CBR|Output Indicator|CCR|
|---|---|---|
||||
||||
||||
|Làm th<br>để đ|ế nào Làm t|hế nào<br>định|
|Làm th<br>để đ|ịnh để|ịnh để|
|Làm th<br>để đ|||
|lượng|hóa? lượn|g hóa?|
|lượng|||
|lượng|||



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
227


**Needs của**
**khách hàng**



~~**CTQ**~~

**Là quá trinh chuyển đổi ý kiến khách hàng thành nội dung yêu cầu chủ chốt khách hàng,**
**thông qua việc này, đưa ra CTQ đại diện cho thành quả Project**

**Giai đoạn** **Nội dung** **Ví dụ**



- Dịch vụ lộn xộn

~~•~~
~~Giao~~ ~~hàng~~ ~~chậm~~

- Giao hàng trong 24 tiếng kể từ lúc đặt hàng

- Phát hàng đi trong 6 tiếng kể từ lúc tiếp
nhận đặt hàng








**Ý kiến khách hàng**

- Là nội dung mà khách hàng nội/ngoại bộ và
những người liên quan mong muốn, hoặc là nội
dung được phản ánh và trông đợi chu kỳ

~~•~~ ~~**Issue**~~ ~~**khách**~~ ~~**hàng**~~ ~~**chủ**~~ ~~**yếu**~~

 - Vấn đề mà khách hàng đang gặp phải hay
vấn đề quan tâm

**Nội dung yêu cầu chủ chốt của khách hàng**

  - Có thể đo lường được Issue khách hàng chủ yếu và
nội dung yêu cầu chủ chốt của khách hàng liên quan và
làm rõ bằng hình thái chi tiết (yêu cầu định lượng hóa
của khách hàng)

**Giá trị đặc trưng chủ chốt chất lượng**

- Spec mà chúng ta phải tuân theo


※ Trường hợp làm rõ nội dung yêu cầu chủ chốt của khách hàng (CCR, CBR), cũng có thể Skip qua các Activity chính

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
228

#### **2.2. Lựa chọn CTQ**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
229

**CTQ(critical to quality) là giá trị đặc trưng chủ chốt gây ảnh hưởng chủ chốt đến chất**
**lượng của quan điểm khách hàng và Business, là giá trị có thể đo lường được vị trí hạ vị**
**nhất trước khi triển khai vạ vị vấn đề hay Issue**



 - Trong số Customer Needs, là nội dung yêu cầu rất quan trọng, là việc thay đổi từ sản phẩm/service của
chúng ta thành nội dung có thể chỉ số hóa được
- Nhằm thỏa mãn yêu cầu chủ chốt khách hàng, chúng ta phải đo lường định lượng hóa tính năng và thành
quả về Output của Process phải cải tiến, là chỉ số đặc trưng chất lượng được đỉnh nghĩa để có thể biểu thị
được



**Từ ngữ chuyên dụng liên quan đến đặc điểm của CTQ**










**Đặc điểm thay thế**
- Trường hợp việc đo lường trực tiếp CTQ khó khăn hoặc chi phí cao, là
đặc biểm phản ánh rõ việc đo lường dễ dàng thuận tiện và phản ánh rõ
- Khi phân tích Process, chọn ra chỉ số Input/ Output thành trọng tâm CTQ

- **Đặc điểm hạn chế** (Side Effect)
- Đặc tính này nếu tốt lên thì tuyệt nhiên không thể chệch ra
- Khi tối ưu hóa CTQ, nhất định phải cân nhắc kĩ








Tùy vào phạm vi dự án, cũng sẽ có trường hợp CTQ cần phải cải tiến
Ở gia đoạn Define, nếu gặp khó khăn trong việc quyết định thì ở giai đoạn
Measure hay Analyze, thông qua việc phân tích Process và nhân lực, có thể
sẽ phát hiện ra chỉ số đặc điểm chất lượng có gây ảnh hưởng nhiều nhất lên
nội dung yêu cầu chủ chốt khách hàng (CCR, CBR)==




Note


**211**



X 1, X 2,

…


**212**

X 1, X 2,

…


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
230

**1. Mối liên hệ với nội dung yêu cầu chủ chốt khách hàng**




    **Việc ảnh hưởng lớn của việc làm thỏa mãn nội dung yêu cầu chủ chốt khách hàng (CCR, CBR), tức là lựa chọn**
**chỉ số có tính đại diện thành CTQ**

☞
Trước khi lựa chọn CTQ, nhất định phải kiểm chứng về mối quan hệ giữa CTQ và Y (khảo sát lí thuyết, kiểm chứng thống kê,…)

    **Trường hợp không như thế, dù có cải tiến được CTQ vẫn không thể biết được là đã thỏa mãn nội dung yêu cầu**

**chủ chốt khách hàng hay chưa**
**2. Có khả năng đó lường theo chu kì hữu dụng**

    **Có thể đo theo chu kì thích hợp để có thể phân tích và đưa ra quyết định**

~~☞~~ ~~Giá~~ ~~trị~~ ~~đặc~~ ~~trưng~~ ~~được~~ ~~đo~~ ~~một~~ ~~cách~~ ~~không~~ ~~phổ~~ ~~biến~~ ~~nhiều~~ ~~thì~~ ~~không~~ ~~lựa~~ ~~chọn~~ ~~thành~~ ~~CTQ.~~ ~~Phải~~ ~~tìm~~ ~~ra~~ ~~đặc~~ ~~trưng~~ ~~thay~~ ~~thế~~ ~~mà~~ ~~có~~ ~~thể~~ ~~đo~~
lường được theo chu kì và dễ hơn trường hợp kia

**3. Lựa chọn Data mang tính định lượng**

    **Phải lựa chọn loại hình Data có lượng thông tin lớn, thì mới có lợi hơn cho việc phân tích vì có thể lấy được nhiều thông**

**tin bằng Data nhỏ**

    **Trường hợp lựa chọn dữ liệu rời rạc thành CTQ, yêu cầu nhiều Data cho việc phân tích**

☞
Không chọn tỉ lệ lỗi (là đối tượng cải tiến) làm CTQ và trong trường hợp khó đo lường trực tiếp, cần cân nhắc xem có đặc trưng thay thế không
**4. Sử dụng Raw Data để phản ánh hiện trạng thực tế**

    **Sử dụng nguyên Raw Data không phải giá trị trung bình hay giá trị tóm lược (Summary Value) và biểu thị hiện trạng**
**thực tế thành Data**

☞ Không được sử dụng Data giá trị trung bình như Raw Data
Ví dụ, sử dụng giá trị trung bình của Data đo lường thông thường, không được phạm lỗi đưa ra năng lực công đoạn hay lựa chọn Spec

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
231

**Phân tích yêu**
**cầu khách hàng**


**Phân tích**


**Phân tích hiện trạng**


**Phân tích**


**Phân tích**


**Phân tích hệ**


**Process**






VOC : Voice Of Customer

QFD : Quality Function Deployment

FMEA : Failure Mode & Effect Analysis



**Cân nhắc phân tích hiện vật, phân tích**
**Machanism, Data thử nghiệm trước,…**

**Yêu cầu của khách hàng,**
**Benchmarking, đánh giá,…**


1) 7 Loss : Lãng phí sản xuất quá độ, lãng phí chờ, lãng phí vật gia công, lãng phí tồn kho, lãng phí thao tác, lãng phí lỗi
2) 3 Không (Không hợp lí, Không cần thiết, Không đồng nhất) : là hoạt động loại bỏ các yếu tố gây ra việc tăng đơn giá, tăng Lead Time, giảm chất lượng trong sản xuất

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
232

**QFD** **(quality function deployment) là với tư cách triển khai tính năng chất lượng, là phương pháp đưa**
**ra CTQ thông qua chuyển đổi nội dung yêu cầu chủ chốt của khách hàng(CCR,CBR) thành nội dung**
**yêu cầu kỹ thuật (thông số) khi phát triển “Systam/Process mới, sản phẩm,…”**

※ Nội dung QFD: tham khảo phụ lục





**Định nghĩa khách hàng → thu thập VOC → Chuyển đổi**
**chất lượng yêu cầu → Ghi chép đặc trưng chất lượng**


**Phân tích quan hệ→ Nắm bắt mức độ quan trọng chất**

(chất lượng yêu cầu**lượng yêu cầu → Lựa chọn CTQ**
đặc trưng chất lượng)










|[Ví dụ] Phát triển Block kĩ thuật Dynamic để nâng cao lợi ích doanh nghiệp (lựa chọn CTQ)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
|Đặc trưng chất lượng<br>Chất lượng yêu cầu|Tiêu chuẩn<br>thú vị|Thiết kế|Thời gian<br>tuổi thọ|COST|Tính đơn giản<br>liên kết|Tỉ lệ lỗi tính<br>năng|Tính an toàn<br>sản phẩm|Tỉ trọng|
|Cảm giác chạm cao cấp||3||3||||3|
|Máu sắc đẹp||9||3||||4|
|Lắp ráp đơn giản|3|1|||3|||5|
|Cảm giác thích thú liên tục|9||3|||3|3|5|
|Sử dụng lâu dài|||9|||3|3|5|
|Giá thành rẻ|||1|9|1||1|3|
|Độ quan trọng đặc trưng chất<br>lượng|60|50|63|48|18|30|35||
|Lựa chọn CTQ|✓|✓|✓||||||


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
233

**Lựa chọn hạng mục nguy hiểm cao (high RPN) được đưa ra thông qua FMEA** (Failure Mode
and Effects Analysis) **làm CTQ**

☞
Từ hạng mục High RPN được đưa ra thông qua FMEA, đưa ra dự án tải tiến (Y) và CTQ

    - **Đặc trưng**

Là **hoạt động xử lý trước** không phải là hoạt động quản lý sau, **liên tục update** tùy theo bối cảnh Process hay sản
phẩm, tìm ra khiếm khuyết

    - **Chủng loại**

        **Design FMEA  :** Ở giai đoạn phát triển, nhằm đảm bảo độ tin cậy của cấu trúc thiết kế(R&D/bộ phận thiết kế

~~của~~ ~~công~~ ~~ty)~~

        **Process FMEA :** Nhằm cải tiến các vấn đề tiềm ẩn trong công đoạn (phát triển công đoạn, bộ phận sản xuất)

**※ Tham khảo**

          - **Hỏng (Failure) :** Là việc không thể tiến hành tính năng của chức năng mà vật phẩm yêu cầu, phân loại thì có hư hỏng ban đầu, hư hỏng
ngẫu nhiên, hư hỏng mài mòn

          - **Mode hỏng (Failure Mode) : Phương thức/hình thái phát hiện hư hỏng**

          - Ngắn mạch (Short) : trạng thái mạch bị chập
         - Đứt (Open) : trạng thái mạch không kết nối
         - Biến đổi giá trị đặc trưng (Parameter Shift) : bị lệch khỏi trạng thái nhất định thông thường
         - Giá trị đặc trưng không ổn định (Electric Instability) : thay đổi theo thời gian

Note Phân biệt giữa lỗi và hư hỏng:

            - Lỗi : việc lệch ra khỏi quy cách đã được chọn vs Hư hỏng : việc mất tính năng đã được chọn như thiết bị/linh kiện/…

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
234

**Tiêu chuẩn lựa chọn hạng mục**


Độ nghiêm trọng của ảnh hưởng của từng khiếm khuyết/hư hỏng tác động lên
khách hàng
**Thấp (1) ~ Cao (10)**

Khả năng phát sinh của từng khiếm khuyết/hư hỏng
**Thấp (1) ~ Cao (10)**

Ở sản phẩm/Process thực tế, khả năng phát hiện ra khiếm khuyết/hư hỏng trước khi
chuyển đến khách hàng
**Thấp (10) ~ Cao (1)**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
235

**Trong các ứng cử CTQ đã đưa ra sau phân tích yêu cầu khách hàng, phân tích hiện trạng,**
**phân tích Process, thông qua phân tích hồi quy có thể chọn được CTQ có ý nghĩa**

    - **Mục đích**

Thông qua phân tích hồi quy, kiểm chứng xem mối liên hệ giữa CTQ và chỉ số Project (KPI, Y) có ý nghĩa hay không,
nhằm kiểm tra tính thích hợp lựa chọn CTQ

    - **Phương pháp**

       - Sử dụng Data công đoạn, thử ngiệm và Data phân tích của trước đây rồi nắm bắt mối liên hệ giữa CTQ và chỉ số(Y), và

kiểm chứng bằng thống kê

       - Nếu chỉ số (Y) **là dạng liên tục** thì thực hiện **phân tích hồi quy (tuyến tính, phi tuyến tính)**, **là dạng rời rạc** thì thực

hiện **phân tích hồi quy Logistic**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
236

**Phân tích hồi quy tuyến tính đơn**

**(1 biến số độc lập / 1 biến số phụ thuộc)**


**Phân tích hồi quy tuyến tính bội**

**(trên 2 biến số độc lập / 1 biến số phụ thuộc)**




Tiến hành phân tích hồi quy tuyến tính đơn về mỗi ứng cử CTQ 1 và 2.
Kết quả đấy xuất ra hơn 80% lực giải thích của phương thức hồi quy của
c ~~ả~~ ~~2~~ n ~~hâ~~ n ~~tố~~

→ **Phải chọn cả ứng cử CTQ và 2 làm CTQ hay không?**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
237



Tiến hành phân tích hồi quy tuyến tính bội về ứng cử CTQ 1 và 2.
Kết quả VIF đấy lớn hơn 1, tồn tại đa cộng tuyến nên mối quan hệ
~~t~~ ương quan mạn ~~h~~ g ~~iữ~~ a ~~2~~ n ~~hâ~~ n ~~tố~~ ~~đ~~ ược ~~t~~ ạo ra.

→ **Chọn ứng cử CTQ 1 làm CTQ**

**Phân tích hồi quy Logistic**

(Trường hợp Y là dạng rời rạc)



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
238

**1. Sử dụng Spec khách hàng yêu cầu**


※ Cân nhắc vùng tin cậy và áp dụng Margin quan điểm thống kê rồi phán định.



**Khi khách hàng thiết lập sẵn Spec về CTQ và yêu cầu, thì trong Project phải sử dụng đúng Spec của khách hàng**

☞
Tuy nhiên, trường hợp xuất hiện lỗi, khiếm khuyến dù vẫn nằm trong Spec của khách hàng như trước, thì phải tái thiết lập Spec tiêu
chuẩn quản lí mới


**2. Thiết lập Spec tiêu chuẩn quản lí**


※ Cân nhắc vùng tin cậy và áp dụng Margin quan điểm thống kê rồi phán định.



     **Khi không có Spec mà khách hàng yêu cầu hay đang thiết lập và quản lí Spec quản lí tự thân, phải sử dụng**
**đúng Spec quản lí**

☞
Tuy nhiên, nếu Spec quản lí trước được thiết lập không phù hợp, thì phải tái thiết lập tiêu chuẩn quản lí mới

**3. Thiết lập Spec thông qua phân tích Data thực tế**

     **Bằng phương pháp thông thường nhất, thiết lập Spec thông qua phân tích thống kê sử dụng Data công đoạn**
**trước đây và Data phân tích và thực tế,…**

☞
Trường hợp CTQ và chỉ số (Y) đều là dạng liên tục: chủ yếu sử dụng phân tích hồi quy (tuyến tính, phi tuyến tính) rồi đưa ra phương
thức mô hình quy hồi và có thể thiết lập Spec

☞
Trường hợp CTQ là dạng liên tục, chỉ số (Y) là dạng rời rạc (ví dụ như OK/NG): sử dụng phân tích Logistic hoặc 2 Sample t-Test và
có thể thiết lập Spec

**4. Thiết lập Spec thông qua thử nghiệm/đánh giá**

     **Trường hợp không tồn tại Data có thể kiểm thảo, đảm bảo Data và thiết lập Spec thông qua thử nghiệm/đánh giá**
**đơn giản**

☞
Ở thử nghiệm/đánh giá: phải Split CTQ ra để toàn bộ giá trị chỉ số(Y) xuất hiện giống nhau và đánh giá (Trường hợp là rời rạc thì phải
xuất hiện tất cả OK/NG)

☞
Phương pháp thiết lập Spec và phương pháp phân tích giống với phương pháp thiết lập Spec (case 3) thông qua phân tích Data thực tế

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
239

**Ở thiết lập Spec CTQ Spec, sử dụng 95% vùng tin cậy hoặc phương pháp thống kê khác và**
**thiết lập trên mặt lí thuyết.**

 **Thiết lập Spec thông qua phân tích Data _ Trường hợp Y là dạng liên tục**


**Phân tích hồi quy tuyến tính**

❑ Căn cứ lựa chọn Spec
: Mức không phát sinh lỗi bảng phối màu (XXX↓)

❑ Thiết lập Spec : Độ dày ITO thỏa mãn tiêu chuẩn bảng phối

màu (XX.XÅ↓)

**☞** **Đ** ~~**ể**~~ **thỏa mãn bảng ph** ~~**ố**~~ **i màu dưới XXX,**
**thiết lập sao cho độ dày ITO duy trì ởXX.XÅ**

**◆** **Kết quả phân tích hồi quy**

The regression equation is
**Bảng phối màu = 0.XXXX + 0.XXX ITO**
S = 0.000551282 **R-Sq = 80.0%** R-Sq(adj) = 77.2%

**Analysis of Variance**

Source   DF          SS       MS    F **P**

Regression  1   0.0000085  0.0000085 28.05 **0.001**

Error      7   0.0000021  0.0000003

Total      8   0.0000107

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
240



**Thiết lập Spec thông qua phân tích Data _ Trường hợp Y là dạng liên tục**

**Phân tích hồi quy phi tuyến tính**

❑ Căn cứ lựa chọn Spec
: Size bọt khí sau khi khử khí của mức
không phát sinh lỗi (X.XX mm↓)

❑ Thiết lập Spec
Size bọt khí trước khử khí thỏa mãn tiêu chuẩn
Size bọt khí sau khử khí (X.Xmm↓)


➔ Đ ~~ể~~ Size bọt khí sau khử khí thỏa mãn dưới
X.XXmm, Size bọt khí trước khử khí phải được
thiết lập để duy trì dưới X.Xmm




The regression equation is
**Sau khử khí = X.XXX - X.XXX Trước khử khí + X.XXX Trước khử khí **2**

S = 0.0692228 **R-Sq = 96.1%** R-Sq(adj) = 95.0%

**Analysis of Variance**

Source   DF    SS    MS   F **P**

Regression  2 0.835457 0.417729 87.18 **0.000**

Error    7 0.033543 0.004792

Total    9 0.869000

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
241

**Thiết lập Spec thông qua phân tích Data (Trường hợp Y là dạng rời rạc)**

**Phân tích hồi quy Logistic**

❑ Căn cứ lựa chọn Spec
: Giá trị cho phép của tỉ lệ rò rỉ(X% ↓)



❑ Thiết lập Spec : Range độ sáng thoat mãn giá

trị cho phép của tỉ lệ rò rỉ(XXnit↑)

➔ Để quản lí tỉ lệ rò rỉ dưới X%, phải thiết
~~lập~~ ~~sao~~ ~~cho~~ ~~Range~~ ~~(Max~~       - ~~Min)~~ ~~độ~~ ~~sáng~~ ~~ở~~ ~~công~~
đoạn kiểm tra là trên XXnit
```
    이항로지스틱회귀분석
```

Nguồn DF    Phương sai sửa Trung bình sửa Chi-Square **P-Value**
Range độ sáng 1           62.64          62.6411       62.64 **0.000**
Sai số 79           35.81           0.4532
Tổng cộng 80           98.45

Độ lệch Độ lệch
R-Sq   R-Sq(sửa)      AIC
**63.63%** 62.61%     39.81

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
242

    **Thiết lập Spec thông qua phân tích Data (Trường hợp Y là dạng rời rạc)**

**2-sample T-test**

❑ Căn cứ lựa chọn Spec
: Mức không phát sinh lỗi LD thoáng khí

❑ Thiết lập Spec
Độ dài Overlap của mức không phát sinh lỗi LD
thoáng khí (XXX ㎛ ↑)

➔ Phân biệt rõ ràng vùng OK/NG dựa trên sự khác
~~nhau~~ ~~về~~ ~~độ~~ ~~dài~~ ~~Overlap~~, ~~thiết~~ ~~lập~~ ~~sao~~ ~~cho~~ ~~mức~~ ~~chắc~~
chắn OK trên XXX ㎛

**2-sample T-test của độ dài Overlap**
Tiêu chuẩn Tiêu chuẩn
Kết quả Test N      Trung bình Độ lệch Sai số
NG           5           277.0 72.0        32

OK 6 582.5 42.1 17

Chênh lệch = μ (NG) - μ (OK)
Giá trị phỏng tính chênh lệch: - ~~305~~ . ~~5~~
95% CI của chênh lệch: ~~(~~     - ~~394~~ . ~~8~~, - ~~216~~ . ~~2)~~

T-Test của chênh lệch = 0 ( `대` ≠): T-Value = -8.37 **P-Value = 0.000** DF = 6

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
243

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
244

**“Nếu không đo lường được**

**thì không quản lý được**

~~**Nế**~~ **u** ~~**khô**~~ ~~**ả**~~ **n** ~~**đ**~~
**ng qu** ~~**lý**~~ **ược**

**thì không cải tiến được’’**


**Peter Drucker**

**(Mỹ, Nhà kinh doanh/ tác giả)**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
246

**Nắm bắt mức chuẩn** [1)] **và cụ thể hóa mục tiêu, phương hướng cải tiến. Đưa ra nhân tố tiềm**
**ẩn thông qua việc phân tích phân tầng và thảo luận với những người liên quan**



**Phân tích Graph, phân tích phương sai**

**Cây quyết định, Random Forest**

**Brain Writing**

**5Why**

**Sơ đồ nhân tố đặc trưng**

**Logic tree**

**Phương pháp kĩ thuật**


**4.1 Phân tích**

**phân tầng**

**4.2 Brainstorming**


**3.1 Thu thập Data và**
**kiểm thảo tính ổn định**

**3.2 Phân tích năng lực**
**Process**



**Phân tích hệ thống đo lường**

**Định nghĩa vận hành chỉ số**

**đo lường**

**Bảng kế hoạch thu thập Data**

**Sơ đồ quản lý**



**Phân tích năng lực công đoạn**

: Loại liên tục, loại rời rạc

- Benchmarking


1) Mức chuẩn : trước khi bắt đầu dự án, là mức đại diện cho tiêu chuẩn trước khi cải tiến dự án bởi khoảng thời gian ổn định trong khoảng thời gian dài hạn

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
247

#### **3. Nắm bắt mức chuẩn và thiết lập mục tiêu**

**3.1. Thu thập Data và kiểm thảo tính ổn định**

**3.2. Phân tích năng lực Process**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
~~248~~

Định nghĩa CTQ và các chỉ số liên quan đến CTQ, lập kế hoạch thu thập Data và kiểm thảo
tính ổn định của Data

Phân tích năng lực Process hiện tại, nắm bắt mức chuẩn và thiết lập mục tiêu tùy theo từng
loại hình Data

Độ tin cậy của hệ thống đo lường, bảng kế hoạch thu thập Data

Tiêu chuẩn Sigma



- Độ chính xác của hệ thống đo lường và kiểm thảo độ chi

tiết

- Thiết lập kế hoạch thu thập Data

- Kiểm tra giá trị bất thường của Data và đường xu hướng

Phân tích hệ thống đo lường

Định nghĩa vận hành CTQ và chỉ số

liên quan đến CTQ

Bảng kế hoạch thu thập Data

Sơ đồ quản lý



- Tính toán năng lực công đoạn hiện

tại của CTQ

- Thiết lập mục tiêu cải tiến

Phân tích năng lực công đoạn (Dạng liên

tiếp, dạng rời rạc)

- Benchmarking





**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
249

**Kế hoạch thu thập Data** **Kiểm thảo tính ổn định của Data**





|Chỉ số<br>đo|Định nghĩa vận Biế<br>hành phâ|n số<br>n tầng|Hệ thống<br>đo|
|---|---|---|---|
|||||
|||||
|||||


**To-be**

**As-is**

LSL Target USL

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
250

**3.1. Thu thập Data và kiểm thảo tính ổn định**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
251

**Lên kế hoạch thu thập Data để nắm bắt sự biến động của Data,**
**đảm bảo Data có thể nắm bắt được mức chuẩn nhờ vào việc xác nhận xu hướng và những giá trị bất**
**thường của Data thu thập được**




- Bảng kế hoạch thu thập Data: Định nghĩa vận hành, biến số phân tầng

- Hiểu về biến động Process : 5M1E, Sự biến động giữa/trong các nhóm






- Phân phối nhị thức : Vận dụng DPO

- Phân phối Poisson : Y=e- Vận dụng DPU

- Hiệu suất : Vận dụng YNA

- PPM quan sát được










1) Phân tầng (stratification) : Là việc phân loại phân tầng (Sub-Group) của từng nhân tố về biến động chỉ số đo lường và nguyên nhân lỗi

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
252

**Cần tối thiểu hóa sự biến động do hệ thống đo lường để đảm bảo độ tin cậy của Data đo**
**lường (CTQ)**




Nó không chỉ là một dụng cụ đo mà nó bao gồm cả người đo, vật liệu đo và môi trường đo,

v.v

Phân tích phổ của hệ thống đo lường có ảnh hưởng nhiều như thế nào đến phổ của process quan sát được

Sự biến của Data đo được (CTQ) thông qua máy đo lường bao gồm sự biến động của giá trị thực
tế (phụ tùng, Part) và sự biến động do đo lường (Biến động tổng = Biến động thực tế + Biến động

đo lường)
~~→~~ ~~**Nắm**~~ ~~**bắt**~~ ~~**mức**~~ ~~**độ**~~ ~~**biến**~~ ~~**động**~~ ~~**do**~~ ~~**hệ**~~ ~~**thống**~~ ~~**đo**~~ ~~**trong**~~ ~~**số**~~ ~~**các**~~ ~~**biến**~~ ~~**động**~~ ~~**Process**~~ ~~**tổng**~~ ~~**thể**~~


σ [2]
hệ thống đo lường

[= 2]






|Col1|Col2|Col3|Biến|
|---|---|---|---|
|Biến<br>Động<br>Tổng<br>Thể|||Biến<br>Động<br>đo|
|Biến<br>Động<br>Tổng<br>Thể|σ2<br>tổng<br>Biến động<br>= 10|Biến<br>Động<br>Thực<br>Tế|σ2<br>phụ<br>= 8|


Note


Biến động do đo lường có thể làm cho năng lực Process trông tệ hơn so với thực tế,
Phải cải tiến (thiết kế lại) hệ thống đo lường nếu sự biến động đo lường lớn (Cải tiến Process là vấn đề sau đó)


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
253

**Phân tích nhân tố biến động**
**của hệ thống đo lường**


☞
Trường hợp đảm bảo được độ tin cậy về người đo và máy đo thì có thể lược bỏ bước Gage R&R
Tuy nhiên trường hợp áp dụng phương pháp đo mới được phát triển trong Process thì phải tiến hành
bước Gage R&R






















**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
254

**Biến động đo lường của Process/sản phẩm được phân tích trên quan điểm độ**
**chính xác và độ chuẩn xác**

**Độ chính xác(accuracy) : Mức độ gần với giá trị tiêu chuẩn (Vị trí trung tâm)**

  - Độ lệch (bias) : Gap của bình quân giá trị tiêu chuẩn (giá trị xấp xỉ) với giá trị đo được

  - Tính tuyến tính (linearity) : Độ lệch của Gage Range hoặc toàn bộ Spec Limit

  - Tính ổn định (stability) : Biến đổi của vị trí trung tâm theo sự biến đổi của thời gian

**Độ chuẩn xác (precision) : Mức độ của Gap giữa các giá trị đo khi đo lặp lại 1 phụ tùng bằng**

~~**cùng**~~ ~~**1**~~ ~~**máy**~~ ~~**đo**~~ ~~**(Mức**~~ ~~**độ**~~ ~~**phân**~~ ~~**tán)**~~

  - Tính lặp lại (repeatability) : Sự biến động phát sinh khi cùng 1 người đo tiến hành đo lặp lại

  - Tính tái hiện (reproducibility) : Sự biến động phát sinh giữa nhiều người đo với nhau



- - - Độ chính xác thấp Độ chính xác cao Độ chính xác thấp Độ chính xác cao

- - - Độ chuẩn xác thấp Độ chuẩn xác thấp Độ chuẩn xác cao Độ chuẩn xác cao



- Độ chính xác cao

Độ chuẩn xác thấp



Độ chính xác thấp

Độ chuẩn xác cao


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
255

**Độ lêch (Bias) là sự chênh lệch (Bias) giữa giá trị tiêu chuẩn (Reference value) (giá**
**trị thực) và giá trị trung bình của giá trị đo được.**

  **Nội dung cần chuẩn bị để đánh giá độ lệch**

  - Các linh kiện/sản phẩm đã xác định rõ giá trị tham chiếu phải do một người đánh giá

(chuyên gia) đo nhiều lần

  - Đo ít nhất 16 lần


Giá trị tiêu chuẩn (Giá trị thực)

**Tiêu chuẩn phán định độ lệch OK**


Giá trị đo



**Bias = Trung bình giá trị đo – Giá trị tiêu chuẩn (giá trị thực)**

**| Bias |**

- ~~**%Bi**~~ **as** ~~**(PV)**~~ **=** **×** ~~**100**~~

**Process Variation**

×
(Tại đây, PV = 6 Độ lệch chuẩn của Process)

**| Bias |**

- **%Bias(Tol) =** **×** **100**

**Tolerance**

(Tại đây, Tolerance = USL – LSL)


     - Chấp nhận giả thuyết Bias = 0 ở mức có nghĩa cho trước

      - %Bias ＜ 5%

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
256

**[Ví dụ] Để đo ngoại lực CTQ cải tiến lỗi sáng Monitor, sử dụng máy đo có được không?**

➢ Data: 1.Measure_Độ chính xác (Độ lệch)

Kết quả phân tích Mechanism cải tiến lỗi sáng nhằm cải thiện tình trạng lỗi sáng của Monitor,
xác nhận rằng hiện tượng lỗi sáng là do ngoại lực tác động lên sản phẩm,
Từ đó, chọn **ngoại lực** tác động lên hệ thống (system) làm **CTQ** .

Để xác định xem Gage có bị lệch hay không, Data dưới đây là Data do người đánh giá phụ
trách thu thập được thông qua **chọn mẫu chuẩn có giá trị tiêu chuẩn (giá trị thực) = 18**, lấy
Gage Setting làm tiêu chu ~~ẩ~~ n.

   - Data: Một người **đo** mẫu chuẩn **16 lần liên tục** (Tuy nhiên, Gage sử dụng bịchuyển đổi vềđiểm tham chiếu ban
đầu sau mỗi lần đo)

    **Độ lệch chuẩn thực nghiệm** của Process áp dụng Gage **: 1,0**

※ Mẫu chuẩn

       - Định nghĩa: Mẫu dùng khi đánh giá độ chính xác trong đo lường hoặc phân tích

       - Lựa chọn: Với mục đích là phân tích độ chính xác của thiết bị đo, mẫu có giá trị Target của đối tượng đo được chọn làm mẫu chuẩn

※ Cách xác định giá trị tiêu chuẩn (giá trị thực)

       - Đo thông qua thiết bị đo lường tổng quát

       - Nếu không có thiết bị đo lường tổng quát, người đo có tay nghề cao sẽ tiến hành đo lặp đi lặp lại nhiều lần rồi lấy giá trị trung bình

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
257

**Stat > Basic Statistics > 1-Sample Z**

① Trung bình phép đo tại mức có nghĩa cho trước
= Kiểm định giá trị thực

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
258





☞
Kiểm tra bằng cách chọn một trong hai

phương pháp ①, ② dưới đây

- **Tiêu chí phán định OK**
- Kiểm định xem giá trị trung bình của phép đo có khác
với giá trị tiêu chuẩn (giá trị thực) hay không

- %Bias ＜ 5%

**Stat > Basic Statistics > 1-Sample Z**

② Kiểm tra xem ở mức có nghĩa cho trước, Bias = 0 hay không






- **Tiêu chí phán định OK**

- Kiểm định xem giá trị trung bình của Bias

(giá trị đo – 18) có phải là “0” hay không

 - %Bias ＜ 5%


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
259

**Giải thích kết quả độ lệch (bias)**

① Kiểm định xem ở mức có nghĩa cho trước,



**Kiểm định xem có chấp nhận giả thuyết Bias = 0**

**tại mức có nghĩa cho trước hay không**


|Hoặc Không thể cho rằng có độ lệch tại mức có<br>② Kiểm định xem ở mức có nghĩa cho trước, Bias = 0 hay<br>không|Col2|ng|
|---|---|---|
|Hoặc Không thể cho rằng có độ lệch tại mức có<br>② Kiểm định xem ở mức có nghĩa cho trước, Bias = 0 hay<br>không|||
||||



- **%Bias** **＜** **5%**


**| Bias |**


**| Bias |** **0.0146**

**%Bias(PV) =** **Process Variation** **[×]** **[ 100 = ]** **6** **×** **1.00** **×** **100 = 0.243(%)**


**6** **×** **1.00**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
260

**Tính tuyến tính là độ lệch trên toàn bộ Gage Range hoặc Spec Limit**

  **Nội dung chuẩn bị để đánh giá tuyến tính**
  - Được thực hiện bởi một người đánh giá (chuyên gia) từ các mẫu chuẩn có thể truy nguyên
  - Chọn vị trí có thể đo được bằng Gage (ít nhất 3 vùng: low, middle, high) trong phạm vi biến thiên chung
của linh kiện/sản phẩm có thể quan sát được trong Process, sau đó đo lặp đi lặp lại (12 đến 16 lần)


Giá trị

đo




- **Bias** **i** **= Trung bình của giá trị đo thứ i – Giá trị tiêu chuẩn** **i**

- **Linearity = | β** ~~**1**~~ **|** **×** **Process Variation**

(Tại đây, Bias i = β 0 + β 1 (Giá trị tiêu chuẩn),
PV = 6 × Độ lệch chuẩn của Process)

**Linearity**

- **%Linearity =** **×** **100**

**Process Variation**




Gage Range


Giá trị
tiêu chuẩn



      **Tiêu chí phán định tuyến tính OK**
      - Chấp nhận giả thiết Slop = 0 tại mức có nghĩa cho trước

      - %Linearity ＜ 5%
      - Tại mức có nghĩa cho trước, độ lệch của các điểm riêng lẻ không phải đều có ý nghĩa

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
261

**[Ví dụ]** ➢ Data : 2.Measure_Độ chính xác (tính tuyến tính)





**Để kiểm tra tính tuyến tính của Gage đã xác nhận độ lệch ở vị trí tiêu chuẩn, thu được các giá trị đo**
**dưới đây sau khi chọn 5 mẫu chuẩn từ phạm vi sử dụng Gage.**

- Data: 1 người đánh giá đo mẫu chuẩn liên tục 16 lần

- Độ lệch chuẩn ước tính từ đợt kiểm định trước: 0,32

**Stat > Quality Tools > Gage Study > Gage Linearity and Bias Study**

**Tiêu chí phán định OK**
                                          - C ~~hấ~~ p n ~~h~~ ận g ~~i~~ ả t ~~hiế~~ t S ~~l~~ op = 0 tạ ~~i~~ mức có ng

hĩa cho trước




 - %Linearity ＜ 5%

 - Tại mức có nghĩa cho trước, độ lệch của
các điểm riêng lẻ không phải đều có ý nghĩa


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
262

**Giải thích kết quả tuyến tính (trước khi điều chỉnh)**






                                          **Tại mức có nghĩa 5%, độ dốc hồi quy là đáng kể,**
**R** **[2]** **= 80.1%** : Tồn tại mối quan hệ tuyến tính giữa độ
lệch tại 5 điểm tham chiếu trong phạm vi đo của thiết bị.

                                      - **%Linearity = 11.9%**
: Không thỏa mãn tiêu chí tuyến tính OK

                                          **Giả thuyết Bias = 0 không có nghĩa ở các giá trị**
**lớn nhỏ trong số 5 điểm được chọn trong phạm vi đo**

: Ngoại trừ “Giá trị đo = 18” khi đã xác định độ lệch

từtrước, độ lệch của các giá trị lớn và nhỏ là lớn.

※ Cần phải điều chỉnh lại trêntoàn bộ phạm vi đo trong trường hợp là loại điện tử; còn trong trường hợp
Note **Không thỏa mãn tiêu chí tuyến tính OK** là loại cơ học, điều chỉnh phần trọng tâmphạm vi sử dụng thường xuyên.

1. Lấy trọng tâm vào phần độ lệch được đánh giá là quan trọng trong phạm vi đo bằng thiết bị đo, sau đó kiểm tra những mục sau đây ① Giá trị tiêu chuẩn, ②
Vị trí đo, ③ Người đo có sử dụng dụng đo đúng cách hay không, ④ Kiểm tra xem dụng cụ đo có bị mòn không hay không, v.v.
2. Thông qua đó, quyết định những vấn đề như kiểm tra nhu cầu điều chỉnh dụng cụ đo và điều tra các vấn đề tự thể với thiết kế bên trong của dụng cụ đo.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
263

**Phân tích kết quả tuyến tính (sau điều chỉnh)**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
264






**Độ dốc hồi quy không có ý nghĩa**

**tại mức ý nghĩa 5%, R2 = 0,1%**
: Quan hệ tuyến tính của độ lệch được
điều chỉnh

- **%Linearity = 0.0%**
~~:~~ ~~Thỏa~~ ~~mãn~~ ~~tiêu~~ ~~chuẩn~~ ~~tuyến~~ ~~tính~~ ~~OK~~

**Tất cả 5 điểm được chọn trong phạm vi**
**đo đều chấp nhận giả thuyết Bias=0**

**Tính ổn định là sự thay đổi vị trí center theo sự thay đổi của thời gian**

  **Nội dung chuẩn bị để đánh giá tính ổn định**

  - Chọn 1 hoặc 2 bộ phận tiêu chuẩn có khả năng truy nguyên.

   - Đo bộ phận tương ứng ít nhất một lần một ngày trong 20 đến 30 ngày

(Khi đó, xem xét số lượng giá trị quan sát tối thiểu khoảng 20 đến 30 giá trịđể đánh giá độ tính ổn định)

Giá trị

đo

                            - **Soạn Control Chart Xbar -R hoặc I- mR sử**


Thời gian


**dụng giá trị đo thu thập tại từng thời điểm**



      **Tiêu chí phán định tính ổn định OK**
      - Xác nhận không có điểm bất thường /Pattern trong Control Chart đang xem xét

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
265

**[Ví dụ]**  - Data : 3.Measure_Độ chính xác (tính ổn định)





**Để kiểm chứng xem độ lệch và tuyến tính của thiết bị đo có ổn định theo thời gian hay không, người ta lựa**
**chọn một mẫu chuẩn (giá trị tiêu chuẩn = 6) và thu được Data như sau.**

**- Data: Đo mẫu chuẩn 1 ngày 3 lần trong vòng 20 ngày**

**Stat > Control Charts > Variables Chart for Subgroups > Xbar-R**

**Tiêu chí phán định OK**
~~-~~ ~~Xác~~ ~~nhận~~ ~~không~~ ~~có~~ ~~điểm~~ ~~bất~~ ~~thường/~~ ~~Pattern~~ ~~trong~~ ~~Control~~ ~~Chart~~

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
266

**Giải thích kế quả tính ổn định (Control Chart)**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
267






**Không có điểm nào nằm ngoài giới hạn**
**kiểm soát trên Control Chart R,**
**và không có điểm nào nằm ngoài giới**
**hạn kiểm soát trên Control Chart Xbar-R.**

**Đảm bảo tính ổn định của thiết bị đo**
**trong 20 ngày**

**Phân tích độ tinh chỉnh của MSA bằng cách xác nhận thông qua phân tích**
**Gage R&R bằng tính lặp lại và tính tái hiện.**




**Phân tích Crossed**

(Khả năng đo lặp lại)


**Phân tích Nested**

(Không có khả năng đo lặp lại)


**Phân tích Crossed**


**ANOVA** **Xbar-R** **ANOVA**
**Phân tích tính đồng nhất**

 - **Repeatability** **○** **○** **○** **○**

~~▪~~ ~~**Reproducibility**~~


Operators

Operators × Parts



**○** **○** **○** **○**

**○** **×** **×** **×**


         **Phân tích Crossed: Trường hợp** người khác nhau (hoặc cùng một người) **có thể đo cùng một mẫu đồng nhất lặp lại nhiều lần**

**- Phân tích Nested** : **Trường hợp** người khác nhau (hoặc cùng một người) **KHÔNG thể đo cùng một mẫu đồng nhất lặp lại nhiều lần**
ex) Kiểm tra phá hủy, đo tự động In-Line, v.v.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
268

**1) Gage R&R Data liên tục**

  **Lựa chọn mẫu (Part) (Quan trọng nhất!)**

: Thường lựa chọn 10 mẫu đo, sau đó đánh số cho từng mẫu đo .





**Cần chuẩn bị** mẫu **theo kế hoạch từ trước để có thể Cover được toàn bộ phạm vi của sự biến thiên hoặc Spec.**

(không phải Random Sampling)

    - **Người đo**

: Khi thực hiện Project, lựa chọn 2 hoặc 3 người để đo Data (Múc đích để kiểm tra tính tái hiện)

**Chọn ngẫu nhiên một người** không phải là người giỏi nhất cũng không phải người kém nhất trong số những người

thao tác đo thường xuyên. Người đo phải là người **hi** ~~**ể**~~ **u rõ v** ~~**ề**~~ **phương pháp đo m** ~~**ẫ**~~ **u** .

☞
Nếu người đánh giá không biết chính xác cách đo thì sẽ không thể tìm ra vấn đề của công cụ đo

Giả dụbạn đang sử dụng một công cụ đo mới, bạn cần phải được đào tạo trước về cách đo và đảm bảo rằng mình hiểu đầy đủ về nó.

    **Phương pháp đo(blind test)**

: Khi đo, người đo phải không biết mẫu đo mang giá trịđo là gì (Đo mẫu đo theo thứ tự ngẫu nhiên)

    Lựa chọn công cụ đo **(Độ phân giải)**

: Gage đề xuất **biến thiên của Process hoặc 10% Spec. của sai số cho phép hoặc độ phân giải nhỏ hơn chúng** .

Công cụ đo phải có khả năng đo được vạch chia nhỏ hơn so với quy cách tiêu chuẩn (dung sai).

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
269

**1) Gage R&R Data liên tục**

**Chỉ số đánh giá**













|Hạng mục|Công thức|Ý nghĩa|
|---|---|---|
|% Study Var.|σ<br>R&R<br>×<br>100<br>σ<br>Total|Đánh giá dựa trên tiêu chuẩn tổng biến thiên được ước tính từ<br>Gage R&R Study được tiến hành<br>: Xác định tính phù hợp để quản lý công đoạn|
|% Process|σ<br>R&R<br>×<br>100<br>σ<br>historical|Đánh giá dựa trên tiêu chuẩn tổng biến thiên đã xảy ra của Process<br>thực tế đưa ra mẫu:<br>: Xác định tính phù hợp để quản lý công đoạn|
|% Tolerance|5.15σ<br>R&R ×<br>100<br>Tolerance|Đánh giá dựa trên tiêu chuẩn giới hạn cho phép (Spec.)<br>: Xác định tính phù hợp để phán định OK/NG|
|NODC|σ<br>Part<br>×<br>1.414<br>σ<br>R&R|Đánh giá các danh mục riêng biệt mà hệ thống đo có thể phân biệt|


1) NODC : Number Of Distinct Categories (Số lượng danh mục riêng biệt)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
270

**1) Gage R&R Data liên tục**





**Tiêu chuẩn đánh giá**


※ Tiêu chuẩn đánh giá là tiêu chuẩn chung, và tùy từng trường hợp có thể áp
dụng khác nhau. (Một số công tykhách hàng yêu cầu %SV từ 10% trở xuống )






|Hạng mục|Tiêu chuẩn|Giải thích|
|---|---|---|
|% Study Var.<br>% Process<br>% Tolerance|≤ 20%|Hệ thống đo phù hợp|
|% Study Var.<br>% Process<br>% Tolerance|20% ~ 30%|Có thể chấp nhận các điều kiện của hệ thống đo sau khi<br>xem xét, phân loại biến thiên sai số và xác định mức độ<br>ảnh hưởng của giá trị phản hồi|
|% Study Var.<br>% Process<br>% Tolerance|≥ 30%|Hệ thống đo không phù hợp<br>→ Xem xét, phân loại biến thiên sai số đo, sau đó cần cải<br>tiến hệ thống đo|
|NODC|≥ 5|Hệ thống đo phù hợp|


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
271

**[Ví dụ]**


**Đã xác định được độ chính xác của công cụ đo ngoại lực. Bây giờ hãy thử kiểm tra độ tinh chỉnh.**



   - Data : 4.Measure_Gage R&R_Crossed

Kết quả phân tích Mechanism cải tiến lỗi sáng của Monitor đã xác định lỗi sáng là do ngoại lực tác động lên sản phẩm và chọn

ngoại lực tác động lên System làm CTQ.

Data dưới đây là Data thu thập để kiểm chứng Gage R&R đối với ngoại lực.

     - **Chia các giới hạn quy cách tiêu chuẩn (16,5** **±** **0,8)** thành 10 khoảng bằng nhau và chọn ngẫu nhiên một Part từ mỗi phần.

    - Lựa chọn **ngẫu nhiên 3 người đo** trong số những người đánh giá đo trong Process hiện tại, không phân biệt trình độ kỹ năng.

   - Lựa **chọn ngẫu nhiên thứ tự** người đánh giá và thứ tự các bộ phận cần đo rồi tiến hành Blind Test

    - Đào tạo người đánh giá để có thểđo được bằng các phương pháp tiêu chuẩn.

    - Thông tin Process: **Độ lệch chuẩn thực nghiệm = 0,35**

※ Gage R&R(Crossed) tham khảo Block 12

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
272

**Stat > Quality Tools > Gage Study > Gage R&R Study (Crossed)**







       **Phương pháp phân tích**
      - Điểm khác biệt giữa hai phương pháp là sự chênh lệch của
phương pháp tính độ lệch chuẩn cho từng nguồn biến động,
trong trường hợp xem xét số lượng mẫu và số lần lặp lại được
đưa ra theo tiêu chuẩn, sử dụng phương pháp phân tích phương
sai (ANOVA) làm tiêu chuẩn.

      - Phương pháp Xbar-R không xác nhận được tương tác

**Lý do sử dụng 5.15 trong Study**

- Tùy từng trường, sử dụng giá trị từ 4.0 đến 6.0, giá trị này có vai trò
chuyển đổi kết quả của mẫu thành thông tin về Tổng thể (Population).

- 4.00 : 95.44% của tổng thể
5.15 : 99.00% của tổng thể (tiểu chuẩn sử dụng bình thường)
6.00 : 99.73% của tổng thể

**Độ lệch chuẩn quá khứ**
- Sử dụng các bộ phận có trong Study, lựa chọn ước tính độ biến thiên
của công đoạn


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
273

**Giải thích kết quả nghiên cứu Gage R&R (Crossed) - 1**













**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
274

**Giải thích kết quả nghiên cứu Gage R&R (Crossed) - 2**









**Gage hiện tại có thể sử dụng để quản lý công đoạn.**
**Trong số tính tái hiện, nếu tiêu chuẩn thao tác hoặc phương pháp đo**
**lường của người đánh giá theo từng bộ phận được cải tiến thì sẽ có thể kỳ**
**vọng một kết quả tốt hơn.**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
275

**Giải thích kết quả nghiên cứu Gage R&R (Crossed) - 3**





**Ngay cả khi tất cả các giá trị đặc tính Gage R&R đều thỏa mãn, các vấn đề hoặc khả năng cải tiến bổ sung**
**cũng cần được xem xét thông qua biểu đồ.** 

**A**



Thể hiện tỉ trọng của biến thiên đối với mỗi Yield được

xem xét

- Tỷ trọng Gage R&R phải nhỏ hơn so với Bộ phận-vs-Bộ
phận thì mới là lý tưởng



Thể hiện phạm vi giá trị đo của mỗi cá nhân đo

Xác định tính nhất quán và lặp lại của phép đo

Tất cả các điểm phải nằm trong giới hạn kiểm soát thì
mới là lý tưởng

Thể hiện trung bình của giá trị đo của từng cá nhân

~~•~~ ~~Kiểm~~ ~~tra~~ ~~tính~~ ~~nhất~~ ~~quán~~ ~~và~~ ~~độ~~ ~~phù~~ ~~hợp~~ ~~của~~ ~~công~~ ~~cụ~~ ~~đo~~
khi người đo sử dụng

Dạng thức trung bình của từng người đo tại mỗi bộ phận
phải tương đối giống nhau, và hơn 50% của các giá trị
trung bình của người đo vượt ra khỏi giới hạn kiểm soát
mới là lý tưởng

 Không phân biệt người đo mà thể hiện giá trị đo cho
từng bộ phận

 - Phân tán của giá trị đo theo từng bộ phận phải nhỏ và sự
chênh lệch giữa các giá trị trung bình theo từng bộ phận
phải lớn thì mới lý tưởng.

Không phân biệt bộ phận mà thể hiện giá trị đo theo từng
người đo

Nếu đường liên kết giữa các giá trị trung bình của từng
người đo theo phương nằm ngang thì lý tưởng




**B**

**C**

**D**

**E**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
276



  **F** Nếu có nhiều vùng giá trị trung bình của người đo theo
từng bộ phận giao với nhau, thì đánh giá là có tương tác

**Chẩn đoán tính tái hiện và tính lặp lại của hệ thống đo**

**Stat > Quality Tools > Gage Study > Gage Run Chart**





Phương pháp nhập giống với Gage R&R


**Repeatability**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
277

**Giải thích kết quả Gage Run Chart**





**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
278

**2) Gage R&R (dạng rời rạc)**






Người kiểm tra: Toàn bộ người kiểm tra của công đoạn đối tượng cải tiến hoặc Project

Số mẫu: 50% số mẫu được lấy gần mẫu giới hạn

 - Trong trường hợp 30~50 cái OK/NG, thu tập với cùng 1 tỷ trọng (OK : NG = 50:50)

- Trong trường hợp dữ liệu dạng phân loại (Categorical)

① 3 loại (Mạnh.Trung.Yếu) : Mỗi loại có 5 cái

~~Yếu~~
~~Mạnh~~ ~~Trung~~

Giới hạn mẫu Giới hạn mẫu

② 5 loại (Mạnh.Mạnh vừa.Trung.Yếu vừa.Yếu) : Mỗi loại có 3 cái


~~Mạnh~~


~~Mạnh~~ ~~vừa~~ ~~Trung~~ ~~Yếu~~ ~~vừa~~ ~~Yếu~~


Giới hạn mẫu


Giới hạn mẫu Giới hạn mẫu Giới hạn mẫu



       Số lần lặp lại: Kiểm tra lặp lại 2~3 lần (đề xuất 3 lần)

       Tiêu chuẩn đánh giá (tính lặp lại, tính tái hiện, độ nhất quán với
tiêu chuẩn): đề xuất 100%
      - 95%↑ : Đạt, 90%↑ : Sau khi nắm bắt nguyên nhân,
đạt điều kiện kèm theo, 90%↓ : Không đạt

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
279


Note


Nếu độ nhất quán giữa tính lặp lại, tính tái hiện, và
tiêu chuẩn không đạt 100%, lọt lỗi hoặc phát sinh
vấn đề do kiểm tra quá

**[Ví dụ]**  - Data : 5.Measure_Gage R&R_Dạng rời rạc





Để kiểm chứng Gage R&R của thiết bị đo đang vận hành, người ta đã thu thập được Data như sau.

        Các Parts chuẩn bị 15 mẫu chuẩn đã được đánh giá OK/NG (8 mẫu OK, 7 mẫu NG)

         Chọn ngẫu nhiên 3 trong số 15 người đánh giá (hiện tại đang đảm nhiệm vị trí đo trong Process) không phân biệt trình

độ kỹ năng

      - Mỗi người đánh giá đo ngẫu nhiên mỗi mẫu 3 lần mà không biết kết quả đánh giá OK/NG của Parts đã cho, sau đó ghi

chép lại kết quả đánh giá OK/NG Ghi đạt (OK) và không đạt (NG)

**Gage R&R của Data rời rạc**

      - Do kiểm chứng Data rời rạc với năng lực đo lường bị hạn chế nên xác định mục tiêu về độ đồng nhất 100%

làm Target.

      - Thay vì quản lý độ đồng nhất theo từng hạng mục, phải cân nhắc các vấn đề sau:

. Đã chọn được mẫu phù hợp hay chưa?

. Đã tiến hành Randomization và Blind Test một cách chính xác hay chưa?

. Các tiêu chuẩn/quy trình/phương pháp đo lường có rõ ràng không?

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
280

**Stat > Quality Tools > Attribute Agreement Analysis**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
281


**Mục đích chính là đểkiểm tra tiêu chuẩn đo lường**
**cũng như thiết lập và điều chỉnh chính xác quy**

**trình/phương pháp đo lường.**

những người đánh giá

**④** **Đánh giá tính nhất quán đo lường giữa**
**những người đánh giá so với tiêu chuẩn**

: Kiểm thảo mức độ thỏa đáng của hệ thống đo

(Chỉ khả dụng trong trường hợp đánh giá tiêu
chuẩn mẫu được chỉ định)




**Phân tích kết quả Gage R&R (dạng rời rạc) - 1**





**①** **Đánh giá độ đồng nhất đo lường theo từng người đánh giá: Kiểm thảo tính lặp lại của từng người đánh giá**

Vì tất cả người kiểm tra đều không đạt 95% nên

NG

                                           - Cần kiểm tra quy trình đo và phương pháp kiểm

tra của tất cả người đánh giá

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
282

**Phân tích kết quả Gage R&R (dạng rời rạc) - 2**





**②** **Đánh giá Agreement (độ chấp thuận) đo lường so với tiêu chuẩn của từng người đánh giá:**
**Do có thể biết được mức độ tính nhất quán đo nên khi có vấn đề, cần đào tạo lại**

Trong số 15 bài kiểm tra, có 12 bài đồng nhất với tiêu chuẩn

Có xu hướng đánh giá NG

Có xu hướng đánh giá OK

✓ Trong trường hợp có sự khác biệt giữa độ đồng nhất của tiêu chuẩn và độ đồng nhất của từng người

đánh giá, nghi ngờ thiếu hoặc có/không tuân thủ tiêu chuẩn

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
283

**Phân tích kết quả Gage R&R (dạng rời rạc) - 3**





**③** **Đánh giá Agreement đo giữa những người đánh giá: Kiểm thảo tính tái hiện giữa những người đánh giá**

Trường hợp việc đánh giá tính nhất quán trong đo lường giữa những người đánh giá và đánh giá tính đồng nhất đo lường giữa những
người đánh giá so với tiêu chuẩnlà tương tự nhau thì phản ánh tính thỏa đáng của tiêu chuẩn hoặc quy trình đó.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
284

**Phân tích kết quả Gage R&R (dạng rời rạc) - 4**





     **Có vấn đề về tính nhất quán trong đo lường của tất cả người đánh giá, do đó, cần phải kiểm thảo lại**

**quy trình và phương pháp đo lường của từng người đánh giá.**

Khi đó, so sánh chi tiết phương pháp đo của từng người đo sẽ hữu ích, và việc này chủ yếu là do trường hợp tiêu chuẩn đánh

giá đo cá nhân không rõ ràng.

    - Kim có “Khuynh hướng đánh giá NG” và Park có “Khuynh hướng đánh giá OK”, và khuynh hướng này có thể là do tỷ lệ đo

lường không nhất quán cao. Trong trường hợp này, **cần phải đào tạo lại về hướng dẫn tiêu chuẩn** .

     - Việc đánh giá độ đồng nhất giữa những người đánh giá và tính nhất quán đo lường giữa những người đánh giá so với tiêu

chuẩn là như nhau, tuy nhiên do giá trị đó rất thấp ở mức 73,33 nên cần **kiểm thảo lại tiêu chuẩn** .

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
285

**Sự khởi đầu của vấn đề chất lượng!**
**“Bạn có thể làm lại một mặt hàng giống nhau chính xác đến mức nào!”**

~~**Phân**~~ ~~**tán**~~ ~~**Vấn**~~ ~~**đề**~~ ~~**của**~~ ~~**tâm**~~

**và** ~~**giá**~~ ~~**trị**~~ ~~**trung**~~

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
286

**Chất lượng (Quality) và phân tán**
- Nguồn gốc của vấn đề chất lượng: Phát sinh Claim của khách hàng từ khi loài người có thể sản xuất ra các mặt
hàng giống hệt nhau.

 - Gốc rễ của vấn đề chất lượng là có thể làm lại chính xác một mặt hàng giống nhau hay không **→ Vấn đề của phân**

**tán và giá trị trung tâm.**

**Khái niệm của phân tán**
: Gây ra những thao tác không cần thiết liên quan đến các vấn đề phát sinh từData kết quả không cố định và biến động liên tục

→ Phân tán sản phẩm có Output không ổn định là nguyên nhân dẫn đến bất mãn của khách hàng và nó tồn tại trong mọi Process
→ Việc đo lường và hiểu vềphân tán trong Process làm việc sẽ giúp ta biết tiêu cuẩn Output hiện tại là bao nhiêu,
Từ đó giảm sựphân tán và hỗ tr tìm ra những gì cần để giảm thiểu khiếm khuyết.

**Nguyên nhân của phân tán**
: Biến thiên của Output Process là **do sự biến thiên của các nhân tố (Variation)** Process và Input của quá trình Process.


Note



- Nguyên nhân dẫn đến sự biến thiên của **lĩnh vực sản xuất** là

do 5M1E

 - 5M : Man, Machine, Method, Material, Measurement

 - Khác: môi trường,, Energy, Utility (cơ sở vật chất), phương

pháp đo lường, v.v.



- Nguyên nhân dẫn đến sự biến thiên trong **các lĩnh vực phi**

**sản xuất** (kinh doanh, Marketing…) là do 4P

  - 4P : Product, Place, Price, Promotion

  - 4P: Sản phẩm, Địa điểm, Giá cả, Khuyến mãi


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
287

- **Subgroup hợp lý (Rrational subgroup)**
Mẫu được cấu thành chỉ từnhững Data có cùng tính chất như được lấy trong cùng một môi trường, cùng một thời điểm

**Nội dung cần xem xét khi lựa chọn Subgroup hợp lý (Rrational subgroup)**

 - Man: Cách thức làm việc của mỗi người, mức độ hiểu biết của mỗi cá nhân về công việc/công đoạn, năng lực cá nhân

 - Machine: Các yếu tố liên quan đến máy móc như sự khác biệt tính năng giữa các thiết bị/trang bị

 - Material: Thành phần, chất liệu, chất lượng, v.v của nguyên liệu sử dụng

  Method: Phương pháp thực hiện công việc, bố trí công đoạn, phương pháp làm việc, tiêu chuẩn hóa, v.v.

 - Measurement: Độ chính xác của công cụ đo, thiết bị đo

 - Environment: Các yếu tố liên quan đến môi trường Process



    **Ví dụ)** **Xem xét yếu tố biến thiên Process**

      - Biến thiên vị trí: Chênh lệch CD theo vị trí Cell

     - Biến thiên chu kỳ: Biến động giữa các Lot

     - Biến thiên thời gian: Thay đổi hàng ngày



**Lập kế hoạch thu thập Data**

 - Ngày : 2013.6.3 ~ 2013.7.2

 - Subgroup Sample Size: 5 cái

- Số lượng Subgroup: 90 nhóm (6 địa chỉ Cell × 3 Lot × 5 ngày)

→ Tổng cộng 450 (5 × 90) Data được thu thập


Note Những nguyên nhân gây ra biến thiên trong ‘Subgroup hợp lý’ được gọi là 'nguyên nhân ngẫu nhiên (biến thiên
trong nhóm)' và thường rất khó phát hiện hoặc xác định


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
288

**Biến thiên toàn thế được chia thành biến thiên giữa các nhóm và biến thiên trong nhóm, và**
**Khi thu thập Data, phải lập kế hoạch bao gồm càng nhiều biến thể này càng tốt thì mới có**
**thể nắm được rõ tình trạn của Process.**


~~**Cấu**~~ ~~**trúc**~~ ~~**biến**~~ ~~**thiên**~~


❖ **Biến thiên toàn thể (SST) = Biến thiên giữa các**
**nhóm (SSB) + Biến thiên trong nhóm (SSW)**




- Biến thiên giữa các nhóm (SSB): Biến thiên của trung bình giữa các

Rational Subgroup

- Biến thiên trong nhóm (SSW): Biến thiên trongRational Subgroup


|Subgroup(sampling) giữa các nhóm (n= 3)<br>Biến thiên toàn thể|Col2|
|---|---|
|||



LSL T USL

※ SST=Sum of Square Total
SSB=Sum of Square Between
SSW=Sum of Square Within

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
289

**Hiểu được độ lệch chuẩn của biến thiên tổng thể và biến thiên trong nhóm sẽ giúp ích trong**
**việc phân tích tác động của các nhân tố(Factor) cũng như phân tích năng lực công đoạn.**




**Độ lệch chuẩn mẫu (sample stdev.)**


=



`s` =






~~▪~~
~~**Biến**~~ ~~**thiên**~~ ~~**trong**~~ ~~**nhóm**~~ **–** ~~**StDev**~~ **.** ~~**(within)**~~


Là **độ lệch chuẩn khi chọn mẫu qua Sampling một lần** .

Trong trường hợp chọn mẫu nhiều lần, độ lệch chuẩn mẫu của

mỗi Subgroup được tính bằng cách cân nhắc bậc tự do (DOF)

→ **Pooled Standard Deviation**

Phương pháp giống như độ lệch chuẩn trong trường hợp chọn mẫu qua

Sampling một lần. Tính độ lệch chuẩn bằng cách sử dụng




 =



=


`within` =





**Biến thiên toàn thể– StDev.(overall)**


=



 =
```
 overall

```




tổng giá trị trung bình của toàn thể.


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
290

**Định nghĩa vận hành (Operational Definition) xác định những gì cần đo lường và các đặc**
**tính chính của chỉ số đo, cung cấp hướng dẫn rõ ràng về ‘Cái gì, Làm như thế nào, Bao**
**nhiêu và Ai’ làm đố tượng đo lường.**

Làm rõ **Chỉ số đo** (đo cái gì) và **Phương pháp thu thập Data** (đo như thế nào),

**Lượng Data sẽ thu thập** (Sẽ đo bao nhiêu cái) và **Đảm nhiệm thu thập Data** (Ai sẽ đo).

      - Là công cụ Communication cho phép tất cả các bên liên quan không xảy ra hiểu lầm và mơ hồ về đo lường thành quả

dự án để có cùng quan điểm đồng nhất.

      - Giúp thu thập Data không bị hỗn loạn và lãng phí khi xây dựng và thực hiện “ Kế hoạch thu thập dữ liệu” .

**- Xây dựng tính nhất quán và độ tin cậy trong việc thu thập** dữ liệu

_**Định nghĩa vân hành chuyển đổi ý nghĩa của con người thành một khái niệm nào đó**_

**- W. Edwards Deming**

                                           - W. Edwards Deming

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
291

**Cần thiết lập kế hoạch thu thập Data theo đối tượng thu thập Data, phương pháp thu**
**thập Data phù hợp và mục đích sử dụng Data.**


**Phương pháp thu thập**

**Data phù hợp**



Sẽ đo lường tiêu chuẩn hay hiệu suất nào?

Sẽ phân tích nguyên nhân nào gây ra sự kém hiệu quả của quy trình?

Ai sẽ thu thập Data?

Khi nào thu thập? Tần suất thu thập?

- Sẽ thu thập Data ở đâu ?

Kích cỡ Sample (Sample Size) là bao nhiêu? Phương pháp chọn Sample?

Cần hỗ trợ thêm gì không?



                              Nắm bắt xu hướng
**Mục đích sử dụng Data**

                              Nắm bắt phân tán trong Process



                                       Xác định sự thiếu hiệu quả

                                       Nắm bắt quan hệ nhân quả, v.v.

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
292

**Khi xây dựng kế hoạch thu thập Data, ngoài CTQ thì còn phải đưa ra phân tích về chỉ số**
**Output, chỉ số Process và chỉ số Input liên kết với CTQ. Bên cạnh đó còn phải phản ánh**
**được các biến phân tầng dự kiến gây ​ảnh hưởng đến chỉ số đo lường.**






|Chỉ số đo|Định nghĩa|Spec.|Biến<br>phân tầng|Phương<br>pháp đo|Nguồn Data|Thời gian<br>thu thập|Phương pháp<br>Sampling|Kích thước<br>Sample|Người thu<br>thập Data|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||



**Chỉ số đo**

- **Định nghĩa**

**Thông số kỹ thuật**

**Biến phân tầng**

**Phương pháp đo**

**Nguồn Data**

**Thời gian thu thập**

- **Phương pháp Sampling**

**Kích thước Sample**

**Người thu thập Data**


: Chọn CTQ và chỉ số Output/Input liên quan đến CTQ

: Định nghĩa rõ rồi ghi chép lại các chỉ số đo để bất kỳ ai xem cũng có thể biết được

: Điền Spec. của CTQ để đạt mục tiêu hoặc tiêu chuẩn yêu cầu của khách hàng, KPI .

: Đưa ra từ quan điểm 5M1E ※ 5M1E (man, machine, material, method, measurement, environment)

: Mô tả công cụ đo và phương pháp đo

: Điền hệ thống tạo ra Data, tức là nguồn thu thập Data

: Điền thời gian thu thập dữ liệu

: Lên kế hoạch trước và điền phương pháp Sampling

: Điền kích thước Sample của Subgroup và số lượng Subgroup

: Điền người phụ trách thu thập Data


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
293

~~**1)**~~ ~~**Run**~~ ~~**Chart**~~





**Xác định Data công đoạn có xu hướng như thế nào theo thời gian rồi nắm bắt xem có thay đổi công**
**đoạn do nguyên nhân bất thường hay không.**

     Run: Các điểm thuộc cùng một loại đồng nhất xuất hiện liên tiếp trên biểu đồ

     Cung cấp các biểu đồ và phương pháp thử nghiệm xấp xỉ để xác định xem các Subgroup hoặc giá trị riêng lẻ của Process
theo thời gian có phải là Pattern ngẫu nhiên hay không: Xác định xem trong Process chỉ tồn tại các nguyên nhân ngẫu nhiê
n hay có tồn tại các nguyên nhân bất thường của phạm trù đặt biệt hay không

     Phương pháp tạo: Tính giá trị trung bình hoặc trung vị trong nhóm mẫu để hiển thị sự thay đổi của Data theo thời gian

     - K ~~ế~~ t quả ki ~~ể~~ m định

                                          - Test 1: Số lần Run cho số trung vị

→Kiểm tra Cụm (Clustering) và Hỗn hợp (Mixed)

                                       - Test 2: Số Up và Down

→ Kiểm tra Xu hướng (Trend) và Dao động

(Oscillation)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
294

**1. Cụm** : Xảy ra khi Data được tập hợp theo cụm trong một vùng cụ thể và biểu thị sự phân tán do các nguyên nhân bất

thường như **lỗi đo lường và lỗi lấy mẫu → Trong trường hợp xảy ra ​phân cụm, cần kiểm tra xem lịch sử công đoạ**

**n có thay đổi theo thời gian hay không**

**2. Hỗn hợp** : Có khuynh hướng dữ liệu không xuất hiện gần điểm trung vị, trong trường hợp **thu thập Data hỗn hợp từ**

**hai tổng thể**

→ Phân tầng và tách Data

~~**3**~~ **.** ~~**Xu**~~ ~~**hướng**~~ ~~:~~ ~~Data~~ ~~trong~~ ~~một~~ ~~lĩnh~~ ~~vực~~ ~~cụ~~ ~~thể~~ ~~có~~ ~~xu~~ ~~hướng~~ ~~tăng~~ ~~hoặc~~ ~~giảm~~ ~~và~~ ~~xảy~~ ~~ra~~ ~~khi~~ ~~công~~ ~~đoạn~~ ~~nằm~~ ~~ngoài~~ ~~tầm~~ ~~kiểm~~

soát. Nguyên nhân có thể là do **bộ phận bị mòn, giá trị Setting thiết bị bị thay đổi, thay đổi người vận hành**, v.v.

→ Sau khi xây dựng đối sách, kiểm tra xem có cần cải tiến hay không. Sau khi hiện tượng xu hướng được cải t

iến, tiến hành phân tích năng lực Process với Data đã thu thập được

**4. Dao động** : Khi Data thay đổi lên xuống nhanh chóng trong một khu vực cụ thể, điều đó cho thấy **Process không ổn đ**

**ịnh** → Sau khi xây dựng đối sách, kiểm tra xem có cần cải tiến hay không. Sau khi hiện tượng xu hướng được cải tiến, t

iến hành phân tích năng lực Process với Data đã thu thập được


Ghi chú


Bằng cách kiểm tra tính ổn định của Data, không chỉ có thể biết về mức độ hiện tại một cách chính xác hơn mà còn có thể tăng tốc độ

cải tiến công đoạn hoặc Process bằng cách áp dụng các đối sách nhanh chóng với các nhân tố cản trở sự ổn định.


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
295

**1) Biểu đồ chạy**






**[Ví dụ] Trước khi tìm ra mức hiện tại của** **△** **H - độ chênh lệch độ cao giữa Gap CS và Push CS,**

**hãy kiểm tra tính ổn định của Data theo thời gian.**

       - Data : 6.Measure _ Run Chart

**Stat > Quality Tools > Run Chart**

**Sự tồn tại của các cụm có nghĩa ở mức có nghĩa 5%**

**- Cần phân tích Process lấy trọng tâm vào nguyên n**
**hân phân cụm** (Tìm ra nguyên nhân của việc phân cụ
m thông qua phân tích lịch sử công đoạn)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
296

**Mức chuẩn (baseline) là khoảng thời gian ổn định trong khoảng thời gian dài trước**
**khi bắt đầu dự án, đại diện cho tiêu chuẩn trước khi cải tiến dự án. (Về cơ bản, sử**
**dụng mức chuẩn 1~3 tháng)**

※ Tiêu chuẩn hiện tại đơn giản là giá trịkết quả không tính đến trạng thái trong quá khứ (trước khi bắt đầu dự án, thành tích 3 tháng, v.v.)


Trước cải

ti ~~ế~~ n

**mức chuẩn**

(baseline)


Sau cải

ti ~~ế~~ n


Hiệu
quả cải

tiến


Tiêu chuẩn

hiện tại

**※ Trước khi cải tiến, phân tích dữ liệu dài hạn rồi chọn mức chuẩn**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
297

#### **3.2. Phân tích năng lực Process**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
298

**Lựa chọn phân phối thích hợp tùy theo dạng Data, tính ra mức CTQ hiện tại và thiết lập**
**mục tiêu**














Phân phối nhị thức : sử dụng DPO

Phân phối Poisson : sử dụng Y=e [-DPU]

- Yeild : sử dụng Y NA

- PPM quan sát được





**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
299

**1) Kiểm tra tính chuẩn**

   - **Mục đích**






        **Kiểm tra mang tính thống kê: thực hiện phân phối chuẩn toàn bộ, giá trị Z biểu thị năng lực Process sẽ được**

**tính từ phân phối chuẩn**

**- Trường hợp Data liên tục không phải phân phối chuẩn, phải kiểm tra lại Data có bất thường không**

     **Giả thuyết kiểm tra tính chuẩn**

        Tìm ra bằng nguyên lí cơ bản của hiện tượng tự nhiên, đa phần giá trị đặc biệt tồn tại trong thế giới tự nhiên sẽ đi theo

phân phối chuẩn

Vì th ~~ế~~, **vì việc đi theo phân ph** ~~**ố**~~ **i chu** ~~**ẩ**~~ **n là bình thường nên “Giá thuy** ~~**ế**~~ **t không sẽ đi theo phân ph** ~~**ố**~~ **i chu** ~~**ẩ**~~ **n”**

Phân phối nhiệt độ của Seoul tháng 3 (’1990~’2019) Phân phối số câu trả lời bài thi sơ cấp DS (’2017~’2019)

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
300

**[Ví dụ]** **Hãy nắm bắt hình thái phân phối và kiểm tra tính chuẩn của 7 phân phối có trong file ví dụ**

 - Data : 7.Measure_Kiểm tra tính chuẩn


**Stat > Basic Statistics > Normality Test**

**Tiêu chuẩn phán định**
- P-Value ≥ Mức có nghĩa (α) : thỏa mãn phân phối chuẩn
- P-Value ＜ Mức có nghĩa (α) : không thỏa mãn phân phối chuẩn

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
301


**Đường cong kiểm tra tính chuẩn**

**Hình thái phân phối : Việc nắm bắt hình thái phân phối mang tính quan sát thông qua phân**
**tích Graph là quan trọng**






Note


Nếu công đoạn đã được ổn định hóa thì sẽ đi theo phân phối chuẩn, trường hợp không thể như thế, trước tiên phải nắm bắt được

**nguyên nhân không đi theo phân phối chuẩn**

- Kiểm thảo xem có vấn đề ở đo lường hay Sampling không, kiểm thảo độ nghiêng (nắm rõ giá trị bất thường) / độ nhọn (phân

tầng Data)


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
302

**Định nghĩa : Zbench là giá trị biểu thị để có thể só sánh các năng lực Process qua lại**

**Tính : Tính ngược ra giá trị Z tương ứng với xác xuất lệch khỏi Spec(2 trục hoặc đơn trục)**



**②** **Phân phối Z : Kiếm xác xuất lệch khỏi Z** **LSL** **, Z** **USL**





μ 0

*** P** **LSL** **( < Z** **LSL** **) = 3.0%**

|Data thực tế|Col2|
|---|---|
|LSL<br>σ|USL|
|||



**③** **Phân phối Z** **bench** **: Kiếm giá trị Z tương ứng với xác xuất lệch khỏi Z** **LSL** **, Z** **USL**



*** P** **USL** **(** **＞** **Z** **USL** **) = 4.5%**



*** P** **Total** **= P** **LSL** **+ P** **USL** **= 7.5%** ❖ **Z** **bench** **= Giá trị Z**

0 Z bench

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
303

**1) Phân tích năng lực Process _ Phân phối chuẩn**

**[Ví dụ]**   - Data : 8.Measure_Phân tích năng lực công đoạn-1





**Hệ thống đo lường đã thu thập được Data từ Process đã được kiểm chứng nhờRational Subgroup như dưới đây.**

**- Số mẫu/nhóm : n=5,  số nhóm : g=30,  giới hạn quy cách hiện tại : 16.5** **±** **0.8**

- **Flow năng lực công đoạn**
**Data liên tục**




- ~~Kiể~~ m ~~t~~ ra ~~tí~~ n ~~h~~ an ~~t~~ o ~~à~~ n v ~~à~~ ~~tí~~ n ~~h~~ c ~~h~~ u ~~ẩ~~ n, ~~t~~ rư ~~ờ~~ ng ~~h~~ ợp ~~khô~~ ng ~~thỏ~~ a m ~~ã~~ n ~~thì~~ ~~điề~~ u c ~~hỉ~~ n ~~h~~
Process bằng phương pháp phù hợp

: Sử dụng Minitab – Capability Sixpack

- Không chỉ định trung bình quá khứ(historical mean), tính **Z** **bench**

: Sử dụng Minitab – Phân tích năng lực công đoạn



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
304

**1) Phân tích năng lực Process _ Phân phối chuẩn**

**①** **Kiểm tra tính an toàn của Data**

**Stat > Control Tools > Capability Sixpack > Normal**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
305





**1) Phân tích năng lực Process _ Phân phối chuẩn**

**①** **Kiểm tra tính an toàn của Data**

      **Phân tích kết quả Six Pack**

**Kiểm tra tính**

~~**an**~~ ~~**toàn**~~

**Kiểm tra cụm và**
**giá trị bất thường**





**Kiểm tra**
**tính chuẩn**


✓ Process hiện tại thỏa mãn tính chuẩn nhưng có vấn đề về tính an toàn (tùy thời gian)
→ Trước khi phân tích năng lực của Process thực tế, phải tìm và cải tiến nguyên nhân đấy đã

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
306

**1) Phân tích năng lực Process _ Phân phối chuẩn**

**①** **Kiểm tra tính an toàn của Data**





**Thông qua chẩn đoán Six Pack, kiểm tra việc phát sinh nguyên nhân bất thường do không tuân**
**theo tiêu chuẩn quản lí trong quá trình chuyển giao Model riêng biệt, sau khi cải tiến điều này, lại**
**thu thập mẫu bằng phương pháp giống như thế**

        - Data : 9.Measure_Phân tích năng lực công đoạn-2

**Thỏa mãn tất cả tính an toàn và tính chuẩn**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
307

**1) Phân tích năng lực Process _ Phân phối chuẩn**

**②** **Tính Z** **bench**

**Stat > Quality Tools > Capability Analysis > Normal**






**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
308


**2) Phân tích năng lực Process_Phi phân phối chuẩn**






**[Ví dụ]**



- Data : 10.Measure_Phân tích năng lực công đoạn-3


**Hệ thống đo lường thu thập Data từ Process đã được kiểm chứng nhờRational Subgrouping như dưới đây**

**- Số mẫu/nhóm : n=5, Số nhóm : g=30, giới hạn quy cách hiện tại: (LSL, Target) = (10.0, 15.0)**

☞
**Tất cả kết quả kiểm tra tính an toàn và tính**
**chuẩn đều vi phạm**

**→ Response được biết đến là việc tuân theo**

**p** ~~**hâ**~~ **n p** ~~**hối**~~ ~~**W**~~ **e** ~~**ib**~~ **u** ~~**ll**~~ **m** ~~**ột**~~ **c** ~~**á**~~ **c** ~~**h**~~ ~~**th**~~ **ực ng** ~~**hiệ**~~ **m, n** ~~**ê**~~ **n**

**thực thi phân tích năng lực công đoạn dựa**

**trên phi phân phối chuẩn**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
309

**2) Phân tích năng lực Process_Phi phân phối chuẩn**

**①** **Kiểm tra tính an toàn của Data**

**Stat > Quality Tools > Capability Sixpack > Nonnormal…**





**Có thể biết được phân phối Weibull được giả thuyết là phù hợp**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
310

**2) Phân tích năng lực Process_Phi phân phối chuẩn**

**②** **Tính Z** **bench**

**Stat > Quality Tools > Capability Analysis > Nonnormal…**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
311





**3) Phân tích năng lực Process_Trường hợp không có phân phối thích hợp**


**①** **Tính Z** **bench**


**Z**
※ Trường hợp không có loại hình phân bổ phù hợp cho Data đã được đo, tính **bench** bằng
tính năng đã quan sát được (Tổng cộng PPM)


**Trường hợp là phân phối chuẩn** **Trường hợp không có phân phối thích hợp**


Năng lực Process được phỏng
tính ở quan điểm cân nhắc
toàn thể biến động

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
312


Tính ra năng lực Process đã được tính từPPM quan sát được
(Tỉ lệ lỗi : 121,052 PPM)

→ **Z** **bench** **= 1.17**

**Phân tích năng lực công đoạn của Data dạng rời rạc: định nghĩa về khiếm khuyết (Defect)**
**phản ánh yêu cầu thực của khách hàng là rất quan trọng**

※ Phải thu tập thật nhiều Data để nó có thể bao gồm cả nguyên nhân ngẫu nhiên và nguyên nhân bất thường

quan trọng,
Khiếm khuyết (Defect) là phân phối một cách ngẫu nhiên ở Unit, và độc lập tương hỗ ở các Parts

**Giá trị Z của Data thuộc tính (dạng phạm trù)** **Giá trị Z sử dụng Data hiệu suất (Data Yield)**


~~**Tiêu**~~ ~~**chuẩn**~~ ~~**đo**~~






**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
313

**Phân phối nhị thức : Là số trong trường hợp lấy n mẫu ở Lot quy mô lớn hoặc công đoạn tỉ lệ lỗi là**

**p và kiểm tra, sau đó lặp đi lặp lại n lần thử nghiệm “thành công” hay “thất bại” của hàng lỗi để lấy**
**được số “thành công”**

**Phân phối Poisson : Tần suất phát sinh sự kiện nào đó trong đơn vị nhất quán (thời gian, không**
**gian,…)**




|Data<br>Data<br>Data|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Data<br>Data<br>Data|Data<br>Data<br>Data|Data<br>Data<br>Data|Data<br>Data<br>Data|Data<br>Data<br>Data||||
|Data<br>Data<br>Data|Data<br>Data<br>Data|Data<br>Data<br>Data|Data<br>Data<br>Data|Data<br>Data<br>Data||||
|Data<br>Data<br>Data|Data<br>Data<br>Data|Data<br>Data<br>Data|Data<br>Data|Data<br>Data||||
|Data<br>Data<br>Data|Data<br>Data<br>Data|Data<br>Data<br>Data|Data<br>Data|Data|Data|Data|Data|
|||||||||
|||||||||
|||||||||


Sampling Unit Measurement









**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
314

     - DPU là: khi có khiếm khuyết được định nghĩa với Unit đã chọn, nó là đơn vị biểu hiện có một vài khiếm khuyết trên 1 Unit

một cách bình quân

     - DPU là việc biểu thị số khiếm khuyết trung bình tồn tại trên 1 Unit, chú ý **không phải** biểu thị độ lớn của khiếm khuyết đấy

**Số khiếm khu** **ết đư** **c** **hát hi** **n trên tổn** **thể Unit**
**y** **ợ** **p** **ệ** **g**

**DPU =**
**Số Unit tổng thể**

<Ví dụ> Số điểm đen trên mỗi Glass

      **Đơn vị (Unit)** : Là đơn vị tiêu chuẩn đo Output của công việc nhằm nắm bắt mức độ cải tiến/hiện trạng và tiêu chuẩn hiện
tại của Process công việc

        - Là kết quả công việc có liên quan đến kết quả cuối cùng của tổ chức của mình và thỏa mãn khách hàng

        - Quyết định Size cần thiết cho việc đo lường nhằm quản lí có/không có khiếm khuyết (Phải quan sát được và đếm được)

      **Khiếm khuyết (Defect)** : Khiếm khuyết mà kết quả biểu thị không thể thỏa mãn khách hàng là phát sinh do nhấn tố
nguyên nhân hoặc Process

        - Chất lượng của dịch vụ hay sản phẩm tăng theo sự giảm số lượng khiếm khuyết

        - Giả sử dù có Error về dịch vụ hay sản phẩm, nếu không gây bất mãn cho khách hàng thì cái đó không phải khiếm khuyết

        - Dù khách hàng có sử dụng sản phẩm với mục đích không như ban đầu đi chăng nữa, nhưng nếu gây ra bất mãn thì cũng bị phán định là lỗi

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
315

     - DPO là khi có khiểm khuyết được định nghĩa với Unit đã chọn, nó là đơn vị biểu thị rằng có vài khiếm khuyết

trên 1 Opportunity một cách bình quân

**Số khiếm khu** **ết đư** **c** **hát hi** **n trên tổn** **thể Unit**
**y** **ợ** **p** **ệ** **g**

**DPO =**
**×**
**Số toàn bộ Unit** **Số cơ hội**

      **Cơ hội (Opportunity)** : Là tất cả những nơi có thể phát sinh khiếm khuyết khi có 1 Unit

~~<Ví~~ ~~dụ>~~ ~~Số~~ ~~điểm~~ ~~đen~~ ~~trên~~ ~~1~~ ~~Cell~~

     - DPMO là chỉ số hoán đổi DPO thành đơn vị PPM

       - **DPMO = DPO** **×** **1,000,000**

※ Lí do sử dụng DPO và DPMO
: Nhằm cung caaos tiêu chuẩn so sánh được tiêu chuẩn hóa giữa các Unit tương hỗ mà có tính phức tạp khác nhau với các Unit
khác ở sản phẩm hoặc dịch vụ

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
316

**1) Phân tích năng lực Process – Phân phối nhị thức**

_x_ _n_ − _x_
_P_ ( _X_ = _x_ ) = _n_ _C_ _x_ _P_ (1 − _P_ ), _x_ = 0,1,2,3... _n_



−

( _n_ _x_ )! _x_ !


_n_ − _x_ _x_




!


_n_
_C_ =
_n_ _x_

−



  P là xác suất xảy ra hiện trạng đặc biệt,  (1-P) là xác suất không xảy ra hiện trạng đặc biệt

  n = số lượng mẫu thử, x = số lượng lỗi, P = tỉ lệ lỗi của tổng thể→ P(x) là lỗi trong n cái x xác xuất tồn lại cái đó

**Áp dụng Yield : Vì là xác suất có số lỗi của tổng thể là “0”**


0 _n_ − 0
_P_ ( _X_ = 0 ) = _n_ _C_ 0 _P_ 1( − _P_ )

**Ví dụ**


**P(Yield) = (1 - P)** **[n]**


Sản xuất 100ea Glass, thì phát hiện lỗi ở 2ea Glass. Tỉ lệ lỗi là bao nhiêu?
Và nếu như vừa duy trì công đoạn như thế vừa Input 10ea Glass thì Yield dự tính và giá trịZ là bao nhiêu?

           Tỉ lệ lỗi = 2 / 100 = 0.02

Z = 0.9

           P(Yield) = (1-0.02) [10] = 0.817

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
317

**1) Phân tích năng lực Process – Phân phối nhị thức**






**[Ví dụ]**


Ở công đoạn TFT, nếu phát sinh bất thường ở thiết bị sẽ gửi tín hiệu phát sinh bất thường lên màn hình

Monitoring nhờ có hệ thống cảm nhận tự động Engineer nhận được tín hiệu phát sinh bất thường sẽ sử

dụng PC để xử lí bằng điều khiển từ xa.

Hãy tìm giá trị năng lực công đoạn về số lần thất bại điều khiển từ xa.



      - Data : 11.Measure_Phân tích năng lực công đoạn (Phân phối nhị thức)

**Stat > Quality Tools > Capability Analysis > Binomial**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
318

**1) Phân tích năng lực Process – Phân phối nhị thức**






**Phân tích kết quả năng lực công đoạn Data rời rạc (Phân phối nhị thức)**



Nhằm nắm bắt công đoạn có trong tình trạng ổn
định hay không để đánh giá năng lực công đoạn

Bằng việc nhìn vào sự biến đổi tỉ lệ lỗi tích lũy,
để xác định việc lựa chọn số Subgroup để
Sampling đã phù hợp hay chưa

→ Số lượng Subgroup phải từ 17ea thì tỉ lệ lỗi
~~tí~~ c ~~h~~ ~~lũ~~ y m ~~ới~~ ~~đ~~ ược xem ~~là~~ ~~ổ~~ n ~~đị~~ n ~~h~~, n ~~hằ~~ m p ~~hâ~~ n
tích năng lực công đoạn thì dù có ít đi chăng
nữa, Subgroup cũng phải từ 을 17ea trở lên

Là việc đo sự biến đổi của tỉ lệ lỗi tùy vào kích
thước của mẫu, phải ổn định hóa mà không có biến
đổi lớn của tỉ lệ lỗi tùy theo sự biến đổi về kích
thước mẫu
→ Dù kích thước mẫu có tăng, tỉ lệ lỗi vẫn ổn định


**A**

**B**

**C**




**D**    - Biểu thị tỉ lệ lỗi bằng Histogram **E**    - Năng lực công đoạn được biểu thị bằng tỷ lệ lỗi và Z Value

→ Tỷ lệ lỗi công đoạn hiện tại là 22,56%
→ Z Value là 0,7533

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
319

**2) Phân tích năng lực Process _Phân phối Poisson**





−  _x_


_x_


_e_
_P_ ( _X_ = _x_ ) =, _x_ = 0,1,2,3... _n_
_x_ !


= _x_ =, _x_ = 0,1,2,3...

_x_ !


_d_
**※** = _np_ =
_u_



   λ là số Defect trung bình được tính bởi tích của n và p, dù tỷ lệ lỗi (p) và số(n) trường hợp không được biết.

   X là số lượng Defect. Tức, nếu X = 2 thì xảy ra 2 Defect.

   Trong phân phối nhị thức, nếu n lớn và tỷ lệ lỗi p nhỏ thì có thể sử dụng bằng cách tính xấp xỉ bằng phân phối Poisson

**Áp dụng Yield : Vì là xác suất có số Defect của tổng thể là “0”**


_e_ −  0
_P_ _X_ = 0 =

( )
0!


**=**
**P (Yield) =** **e** **[-λ]** **e** **[-d/u]**


**Ví dụ**

Nếu số lượng Point Defect trung bình trên mỗi Panel là 0,8 (λ=0,8, d/u=0,8), thì xác suất và giá trị Z của
trường hợp không có bất kỳ Point Defect nào khi lấy một mẫu ngẫu nhiên trong nhiều Panel là bao nhiêu?
(Khái niệm đồng nhất với Yield)


**P ( X = 0 ) =** **[e]** **[-0.8]** **[ λ]** **[0]**

**0 !**


**= e** **[-0.8]** **= 0.4493 (44.93%)**


**Z = -**

**0.127**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
320

**3.2. Phân tích năng lực Process –** và lập mục tiêu



**2) Phân tích năng lực Process _Phân phối Poisson**



**[Ví dụ]**


**Để tìm hiểu tiêu chuẩn hiện tại của Project để giảm thiểu Point Defect của nhà máy Panel, người ta lấy các**

**Sample trong 100 ngày và ghi lại Point Defect trên mỗi Glass. Hãy tìm giá trị Z của năng lực công đoạn**

**cho số lượng Point Defect trên mỗi Glass.**



       - Data: 12.Measure_Phân tích năng lực công đoạn (Phân phối Poisson)

**Stat > Quality Tools > Capability Analysis > Poisson**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
321

**3.2. Phân tích năng lực Process –** và lập mục tiêu



**2) Phân tích năng lực Process _Phân phối Poisson**

  **Giải thích kết quả**



 Biểu đồ quản lý số Defect trên mỗi đơn vị không
đồng nhất

 Kiểm tra trạng thái quản lý của công đoạn
→ Kiểm tra có/không có sự phân phối ngẫu nhiên
và giá trị bất thường

 Bằng cách xem xét sự thay đổi của
DPU tích lũy, để kiểm tra xem việc lựa
chọn số lượng Subgroup để Samplingcó
phù hợp hay không
→ Có 55 Subgroup phù hợp

Nắm bắt xem DPU có bị ảnh hưởng bởi kích cỡ
của mẫu hay không

→ Phải được phân bố đều xung quanh đường
trung bình
※ DPU phải ngẫu nhiên theo cỡ của mẫu


**A**

**B**

**C**




**D** - Poisson 분포형태표현 **E** - 공정능력은 **평균** **DPU** 값으로나타남


→ 평균 DPU : 0.0263
→ Yield = e [-DPU] = 0.9740, 불량률 = 0.0260

→ **공정능력** **Z** **값은** **1.94**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
322

**3.2. Phân tích năng lực Process –** và lập mục tiêu



**3) Hiệu suất(Yield) : Tỷ lệ hàng chuẩn (OK) trên tổng thể**

  **So sánh khái niệm truyền thống và Six Sigma**







            - **Y** **F** **(final yield)**

            - **Y** **FT** **(first time yield)**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
323



**- Y** **RT** **(rolled throughput yield)**

**- Y** **NA** **(normalized average yield)**

**3.2. Phân tích năng lực Process –** và lập mục tiêu



**3) Hiệu suất (Yield)**

**Để cải thiện COPQ, ngoài hiệu suất của khái niệm truyền thống, cần tập trung vào quản lý và cải tiến Y** **RT** **.**

   - **Y** **F** **(final yield)** : Tính cho từng công đoạn riêng biệt và mang ý nghĩa là số lượng Output so với Input.

   - **Y** **FT** **(first time yield)** : Tính cho từng công đoạn riêng biệt và mang ý nghĩa hiệu suất không được sửa chữa thông qua làm lại.

       - **Y** **RT** **(rolled throughput yield)** : Tỷ lệ để một sản phẩm OK vượt qua tất cả các công đoạn mà

không xảy ra lỗi nào trong từng công đoạn riêng lẻ

       - Là hiệu xuất không sửa sau khi làm lại và đưa ra khả năng Zero Defect

       - Được sử dụng để đánh giá mức chất lượng sau khi tích lũy ở giai đoạn nào đó của công đoạn

theo tuần tự (được biểu thị dưới dạng tích của Y FT )

       - **Y** **NA** **(normalized average yield)** : Hiệu suất trung bình nhân cho công đoạn đơn vị trong công đoạn

liên tục

       - Dùng làm tiêu chí đánh giá mức độ chất lượng của thành phẩm

        - Giá trị tổng quát có thể so sánh với các công đoạn khác, hiệu suất được biểu thị bằng giá trị Z

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
324

**3.2. Phân tích năng lực Process –** và lập mục tiêu



**3) Hiệu suất (Yield)**

       **Hidden Factory là một hoạt động không mang lại giá trị gia tăng, không được tính vào chi phí và**
**thông qua phản ánh điều này, phải tính được lợi nhuận**

<Ví dụ> Làm lại, chỉnh sửa, v.v

**Hidden** Factory

         - Y
F.A = Output / Input = 950 / 1,000 = 95.0%

         - Y FT = (Output – Làm lại) / Input = 900 / 1,000 = 90.0%

→ Hiệu suất theo Y F (output so với input) - khái niệm hiệu suất chung, không phản ánh Loss do làm lại

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
325

**3.2. Phân tích năng lực Process –** và lập mục tiêu



**3) Hiệu suất (Yield)**


**Ví dụ**


**Hãy tìm giá trị YRT và Z của công đoạn bên dưới**








- Y
F.AB = Output / Input = 900 / 1,000 = 90.0%

- Y
FT.A = (Output – Làm lại) / Input = 900 / 1,000 = 90.0%

- Y
FT.B = (Output – Làm lại) / Input = 900 / 950  = 94.7%

- Y RT = Y FT,A × Y FT,B = 0.900 × 0.947 = 85.26%




**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
326

**3.2. Phân tích năng lực Process –** và lập mục tiêu



**3) Hiệu suất (Yield)**

**Ngay cả có cùng năng lực công đoạn, hiệu suất tổng thể sẽ giảm khi số lượng đơn vị công đoạn tăng**
→ **Để nâng cao năng lực công đoạn tổng thể, cần mức ↑ Sigma trên mỗi đơn vị công đoạn, ↓số công đoạn**

**Hiệu**

**suất**







|Z-Value|Số công đoạn|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Z-Value|1|5|10|15|20|25|30|
|1|84.134%|42.157%|17.772%|7.492%|3.158%|1.332%|0.561%|
|2|97.725%|89.131%|79.443%|70.808%|63.112%|56.252%|50.138%|
|3|99.865%|99.327%|98.658%|97.994%|97.335%|96.679%|96.029%|
|4|99.997%|99.984%|99.968%|99.953%|99.937%|99.921%|99.905%|
|5|100.000<br>%|100.000%|100.000%|100.000%|99.999%|99.999%|99.999%|
|6|100.000<br>%|100.000%|100.000%|100.000%|100.000%|100.000%|100.000%|


**Số công đoạn**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
327

**.**
**Nếu đạt được mục tiêu CTQ thì cần kiểm thảo lại xem có đạt được mục tiêu KPI hay không**

    - CTQ liên tục: Xác định mục tiêu mức Sigma sau khi **lập mục tiêu cải tiến tỷ lệ lỗi của CTQ**

    - CTQ rời rạc: Xác định mục tiêu mức Sigma sau khi **lập mục tiêu cải tiến DPMO của CTQ**

**To-be**

**As-is**

LSL Target USL

**Những lỗi khi thiết lập mục tiêu**

     Đặt mục tiêu từ quan điểm dài hạn làm mục tiêu ngắn hạn cần đạt

     Đặt mục tiêu quá dễ đạt được

     Mục tiêu đưa được mà không có sự đồng thuận giữa các thành viên trong nhóm dự án

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
328

#### **4. Đưa ra nhân tố tiềm ẩn**

**4.1. Phân tích phân tầng**

**4.2. Brainstorming**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
329

Thông qua phân tích phân tầng mà phân tích kĩ thuật của Data sau đó thảo luận với

chuyên gia hay các thành viên liên quan,…và đưa ra nhân tố tiềm ẩn (Potential X’s)

Suy luận Machanism thông qua biến số phân tầng có nghĩa và phân tích kĩ thuật

Nhân tố tiềm ẩn



- Phân tích Graph

- Đưa ra biến số phân tầng có ảnh

hưởng lớn

- Phân tích Graph

Phân tích phương sai

Cây quyết định (Decision Tree)

- Random Forest



- Brainstorming

Tiếp cận kĩ thuật

- Brain Writing

5Why



Biểu đồ xương cá

(Causes & Effects Diagram)

- Logic Tree


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
330

#### **4.1. Phân tích phân tầng**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
331

**Mục đích của phân tích phân tầng là định nghĩa vùng vấn đề (phạm vi phân tích) một cách**
**cụ thể sẽ tập trung vào phân tích và giải quyết nguyên nhân gốc rễ bằng cách phân tích**
**Data một cách chi tiết, tiến hành phân tích về biến số phân tầng được phản ánh trong kế**
**hoạch thu thập Data**

    **Biến số phân tầng**
Có thể phân tầng Data theo nhiều tiêu chuẩn, biến số phân tầng thường được chọn bằng những nhân tố
có thể thấy được sau khi phân tích các yếu tố đa góc độ gây ảnh hưởng lên chỉ số liên quan

~~•~~
~~**5M**~~ ~~**1E**~~

      - Man : Phương thức làm việc, mức độ hiểu biết về công việc cá nhân/công đoạn, năng lực cá nhân của con người

      - Machine : Sự khác nhau về tính năng của trang thiết bị, yếu tố liên quan đến máy móc như già hóa thiết bị,…

      - Material : Thành phần vật liệu sử dụng, chất liệu, chất lượng,…

      - Method : Phương pháp tiến hành công việc, bố trí công đoạn, phương pháp thao tác, tiêu chuẩn hóa,…

      - Measurement : Tính chính xác của công cụ đo lường, thiết bị đo lường

      - Environment : Môi trường công việc, yếu tố liên quan đến hoàn cảnh Process như pháp luật

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
332

**Có thể đưa ra nhân tố tiềm ẩn và vùng phát sinh vấn đề thông qua phân tính phân tầng,**
**phân tích phân tầng tiến hành phân tích về biến số phân tầng được phản ảnh trong kế**
**hoạch thu thập Data**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
333

**Sử dụng phương pháp phân tích Graph thích hợp với mục đích phân tích**




               - **[Phân tích tính liên quan giữa biến số]** [: Graph cơ bản của phân tích liên quan, phân ]

tích hồi quy
※ Biểu đồ phân phối biên (Marginal Plot) : Ngoài phân tích tương quan, có thể kiểm tra đến hình

thái phân bổ của từng X,Y

               - **[Nắm bắt hình thái của phân bổ]** [: Graph cơ bản của kiểm chứng tính chuẩn xác]

~~※~~ ~~Trường~~ ~~hợp~~ ~~không~~ ~~phân~~ ~~phối~~ ~~chuẩn~~, ~~có~~ ~~thể~~ ~~xác~~ ~~nhận~~ ~~hình~~ ~~thái~~ ~~của~~ ~~độ~~ ~~nghiêng~~ ~~và~~ ~~độ~~ ~~nhọn~~

               - **[Vị trí trung tâm phân bổ/ nắm bắt phân tán và so sánh giữa các phạm trù về chúng]**

: Graph cơ bản của phân tích sự chênh lệch đáng kể giữa các phạm trù
(Nếu chắc chắn về sự khác biệt về kết quả phân tích, thì không cần phân tích thống kê nữa)

               - **[Trường hợp X,Y tất cả đều là Data dạng rời rạc thì nắm bắt tấn số của Data]**

               - **[Tóm tắt Graph thay đổi của Y theo thời gian trôi qua]**

               - **[Tóm tắt graphic 3 chiều : ]** [Có thể sử dụng nếu có 2 Y hoặc có 2 X]

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
334

**1) Biểu đồ phân tán (Scatter Plot)**



**Nếu gọi Data thực hành, khu vực là Data “dạng rời rạc”, phần còn lại là Data “dạng liên tục”**

**Data dạng liên tục**

**Data dạng rời rạc**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
335

**1) Biểu đồ phân tán**



**Ở phân tích tính tương quan giữa các biến số, có thể sử dụng biểu đồ phân tán, ma trận biểu đồ**

**phân tán, biểu độ phân phối biên,…,**
**Ở biểu đồ phân tán “Simple” có thể tham khảo tính tương quan giữa 2 biến số bằng Graph**

       Question : Mối liên hệ giữa ‘vị’ và ‘hương’ là như thế nào?

**Graph > Scatter Plot > Simple**

→ **Được dự đoán là có tồn tại quan hệ tuyến tính**

**Tức là, được dự đoán rằng hương càng thơm thì vị càng ngon**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
336

**1) Biểu đồ phân tán**



**Nếu sử dụng biểu đồ phân tán “With Groups”, có thể phân biệt bổ sung về ‘vị’ và ‘hương’ theo**

**từng “khu vực” là biến số dạng phạm trù**

       Question : Có căn cứ nào về việc khu vực gây ảnh hưởng đến ‘vị’ hay ‘hương’ không?

**Graph > Scatter Plot > With Groups**

→ **Khu vực 1,2 trông không có khác biệt lớn, khu vực 3 thì vị và**

**hương ưu tú**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
337

**1) Biểu đồ phân tán**



**Nếu lựa chọn ma trận biểu đồ phân tán “Simple” và chỉ định tất cả biến số muốn phân biệt, thì**

**có thể thấy được biểu đồ phân tán giữa các biến số đã được chỉ định một cách dễ dàng**

       Question : Hãy thử xác định tất cả mối quan hệ giữa các Data dạng liên tục đã được cân nhắc

**Graph > Matrix Scatter Plot > Simple**

→ **Dự đoán rằng có mối quan hệ giữa vị - ‘hương’ và ‘nồng độ’**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
338

**1) Biểu đồ phân tán**



**Ở ma trận biểu đồ phân tán “With groups”, thêm biến số dạng phạm trù (khu vực) và có thể xác**

**định tính tương quan**

       Question : Hãy thử xác định tất cả mối quan hệ giữa các Data dạng liên tục đã được cân nhắc tùy
theo khu vực

**Graph > Matrix Scatter Plot > With Groups**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
339

**2) Biểu đồ đường viền**



**Ở “Biểu đồ đường viền”, có thể suy đoán mối quan hệ giữa 2 biến số dạng liên tục thành hình vẽ**

**hình đường viền một cách lập thể**

      Question : Hãy thử xác định mối quan hệ của ‘vị’ tùy theo ‘hương’ và ‘nồng độ’ bằng hình vẽ

**Graph > Contour Plot**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
340

**3) Histogram**



**Nhằm nắm bắt hình thái phân bổ, tiêu biểu sử dụng Histogram**

  Question : Phân bổ của Boarder Gap là hình thái như thế nào?

**Graph > Histogram > Simple**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
341


→ **Có nhiều giá trị tương ứng với 0.1, ngoài ra có các giá trị rải rác**

**3) Histogram**



**Sử dụng Histogram “With Groups” và phân tầng Data tùy theo việc có/không có “Aging Skip” là**

**biến số dạng phạm trù**

  Question : Tùy theo việc có/không có Aging Skip, phân bổ Boarder Gap sẽ khác như thế nào?
(tiến hành Aging Skip, Aging)

**Graph > Histogram > With Groups**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
342



**Mẫu thử Aging Skip: chủ yếu Boarder Gap trở thành 0.1**

**4) Biểu đồ hộp (Box Plot)**



**Nhằm so sánh giữa hình thái phân bổ và phạm trù, có thể sử dụng Box Plot, Interval Plot, biểu đồ**
**từng giá trị, biểu đồ đường,…**

**Hiểu khái niệm**

**“Box Plot: kiểm tra hình thái phân bổ sơ lược của Data, có thể so sánh giữa**

**các phạm trù và nắm bắt được sự tồn tại của giá trị bất thường”**




**Giá trị bất thường** : Điểm thoát khỏi Q3 + 1.5 × IQR**

**Upper Limit :** Giá trị t ~~ố~~ i đa của trong Q3 + 1.5 × IQR

**Q3** : Khi định vị Data theo thứ tự, giá trị có vị trí ở 3/4
Thứ 3(n+1)/4

**Giá trị bậc trung** : Khi định vị Data theo thứ tự, giá trị có vị trí ở giữa

**Q1** : Khi định vị Data theo thứ tự, giá trị có vị trí ở 1/4
Thứ (n+1)/4

**Lower Limit** : Giá trị tối thiểu của trong Q1 - 1.5 × IQR

IQR : Q3 - Q1(Số tứ phân vị)



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
343

**4) Biểu đồ hộp (Box Plot)**




Question : Tùy theo việc có/không có Aging Skip, phân bổ của Boarder Gap sẽ khác như thế nào? Hãy
phân tích bằng Box Plot

**Graph > Box Plot > One Y(With Groups)**


✓

✓

✓

✓



**Trường hợp của mẫu thử Aging Skip: phát sinh giá trị**

**bất thường nên làm rõ nguyên nhân**

**Mẫu thử tiến hành Aging: Trung bình và phân tán**


**Boarder Gap lớn**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
344

**4) Biểu đồ hộp (Box Plot)**




Question : Tùy theo Line Input, phân bổ của Boarder Gap sẽ khác như thế nào? Hãy phân tích bằng
Box Plot

**Graph > Box Plot > One Y(With Groups)**

✓


✓

✓

✓



**Giữa các Line Input không có sự chênh lệch lớn**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
345

**4) Biểu đồ hộp (Box Plot)**




Question : Tùy theo vị trí đo, phân bổ của Boarder Gap sẽ khác như thế nào? Hãy phân tích bằng Box
Plot

**Graph > Box Plot > One Y(With Groups)**

✓


✓

✓

✓



- **Boarder Gap của vị trí 2 lớn hơn so với các vị trí khác**

**Cần đưa ra nguyên nhân của Boarder Gap tùy theo vị trí**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
346

**4) Biểu đồ hộp (Box Plot)**




Question : Tùy vào việc có/không có Aging Skip và vị trí đo, phân bổ của Boarder Gap sẽ khác như thế
nào? Hãy phân tích bằng Box Plot

**Graph > Box Plot > One Y(With Groups)**

✓


✓

✓

✓



**Mẫu thử đã Aging Skip: không có sự chênh lệch lớn ở từng vị trí đo,**

**Mấu thử đã tiến hành Aging: có sự chênh lệch lớn ở từng vị trí**


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
347

**5) Biểu đồ đa biến lượng (Multivariate Chart)**



**Nắm bắt trường hợp mức nhiều nhân tố X thay đổi thì giá trị của nhân tố Y sẽ thay đổi thế nào, nắm**

**bắt mối quan hệ tương hỗ giữa các nhân tố**

   - Phương pháp xác định nguyên nhân biến động chất lượng đa dạng một cách dễ dàng

   - Có ích cho việc nắm bắt hình thái của biến động chất lượng hay chẩn đoán và nguyên nhân của chu kì

    - 각변수의범주별평균을타점해주므로, 변수의효과그리고변수간교호작용판단에유용

   - Phương pháp soạn thảo : Biểu thị ở Graph răng ở mức của từng nhân tố X, giá trị trung bình của nhân tố Y sẽ thay
đổi như thế nào



**[Ví dụ]**



- Data : 15.Measure_Multivariate Chart



Question : Ở công đoạn OCR Direct Bonding, hãy kiểm tra biến đổi cường độ Resin tùy theo thời gian làm cứng
~~Oven~~, ~~chủng~~ ~~loại~~ ~~Resin~~


**Stat > Quality Tools >Multi – Vari Chart**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
348


→ **Thay đổi trung bình tùy theo thời gian làm cứng lớn**
→ (Có thể là nguyên nhân quan trọng đối với sự thay đổi trung bình Process)

**Phân biệt Within, Between Variation của CTQ, có thể phân biệt độ lớn biến động bắt**

**nguồn từ biến số phân tầng**

**→ Phân tích chênh lệch đáng kể mang tính thống kê về biến số phân tầng và đồng thời nắm bắt tỉ lệ**

**đóng góp**


**Y**





_y_

**X**






|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|x<br>y x<br>x 3<br>x<br>x<br>x<br>x|x<br>y x<br>x 3<br>x<br>x<br>x<br>x|x<br>y x<br>x 3<br>x<br>x<br>x<br>x|Betwe|en Variat|
|x<br>y x<br>x 3<br>x<br>x<br>x<br>x|x<br>y x<br>x 3<br>x<br>x<br>x<br>x|x<br>y x<br>x 3<br>x<br>x<br>x<br>x|||
|x<br>y x<br>2<br>x<br>y x<br>1 x<br>x<br>x|x<br>y x<br>2<br>x<br>y x<br>1 x<br>x<br>x|x<br>y x<br>2<br>x<br>y x<br>1 x<br>x<br>x|||
||||||


**1** **2** **3**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
349

|Col1|Biến động<br>toàn thể|
|---|---|
|||

 - **Phương pháp**

**Đánh giá nhân tố tiềm ẩn của đa số có tính liên quan cao với CTQ, có thể kiểm tra thứ tự ảnh**
**hưởng đóng góp vào biến động CTQ từng nhân tố tiềm ẩn**

 - **Phương pháp**

**①** **Nhập Data : Nhập CTQ (ΔH) Data và nhân tố tiềm ẩn (X’s) liên quan đến CTQ**

                                                                 - Data : ’14. 4/3~ 7/3

                                                                 - Model : 23”


Oven Slot

: 34ea


Stage(F, B)
: Front = 1, Back = 2


Lot ID


Vị trí Panel

: 1 ~ 32ea


Tầng Pre-Bake

: 1, 2, 3 tầng


**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
350

 - **Phương pháp**

**②** **Phân tích phương sai : Thực thi phân tích Model tuyến tính thường (GLM) ở Minitab**



**Minitab: Start > ANOVA > Main Effect Plot**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
351


**Minitab: Start > ANOVA > General linear model > Fit General linear model**

**Thứ tự độ lớn của biến số phân tầng gây ảnh hưởng**

~~**lên**~~ ~~**△**~~ ~~**H**~~

**Panel > Tầng Pre-Bake > Lot > Stage(F,B) > Oven Slot**

Phải phân tích thêm về **Panel, Pre-Bake,**

**Lot** có ảnh hưởng cao

 - **Phương pháp**

**③** **Phân tích Graph Panel – Biểu đồ đường viền (Contour Plot)**


**Biểu đồ đường viền** **△** **H**









**Khi phân tích biểu đồ đường viền về phân**

**tns (Panel) bên trong Glass,**

**Bên trái thấp, bên phải cao**

**<Quick Win>**

 **Điều chỉnh Gap chiếu sáng và lượng chiếu**

**sáng từng Shot và căn chỉnh giá trị trung bình**

**từng Shot đợt 1**

|4|Col2|3|2|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|8||7||6||
|Sho<br>12|t2|11|10|10|Sh|
|Sho<br>12|t2|11|10|10||
|16||15|14|14||
|20||19|18|18||
|24||23|22|22||
|Sho<br>28|t3|27|26|26|Sh|
|Sho<br>28|t3|27|26|26||
|32||31|30|30||



**[Độ cao Gap CS]**



**[Độ cao Touch CS]**



**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
352

   - **Phương pháp**

**④** **Phân tích Graph Lot - Run Chart : Kiểm tra lịch sử công đoạn về biến động bất thường**

                                            **Kết quả kiểm tra lịch sử công đoạn ΔH**

ⓐ Bù quang lượng (42→40mj)

ⓑ Bù quang lượng (40→42mj)

ⓒ Drop ánh sáng máy chiếu sáng

→ Drop án ~~h~~ sáng ~~d~~ o ô n ~~hiễ~~ m M ~~i~~ rror

ⓓ Biến động Line RGB toàn công đoạn (RED#12 → #5)

ⓔ Bù quang lượng (42→43mj)

ⓕ Bù quang lượng (43→42mj)

ⓖ Drop ánh sáng máy chiếu sáng + Biến động Line RGB

(RED#12 → #5)

→ Drop ánh sáng do ô nhiễm Mirror

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
353

#### **4.2. Brainstorming**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
354

**4 nguyên tắc cơ bản**

**①** **Tuyệt đối cấm phê phán tốt xấu.**
**③** **Truy cầu về lượng hơn chất.**


**②** **Hoan nghênh những suy nghĩ tự do thoải mái không bị trói buộc theo**
**khuôn khổ.**
**④** **Nắm bắt cơ hội trong ý tưởng của người khác để phát triển.**


**1. Brain Writing**

(6·3·5 Method)

**2. 5Why**

**3. Biểu đồ xương cá**
(Fishbone Diagram)

**4. Logic Tree**


Brain Writing là phương pháp mà Holliger của Đức đã phát minh dựa trên việc lấy gợi ý từ Brainstorming
năm 1968. Có 6 người tham gia, trong yên lặng, mỗi người đưa ra 3 ý tưởng lần lượt trong 5 phút.
Đó là một kỹ thuật phát triển tư duy cá nhân thành tư duy nhóm

Là phương pháp : Hỏi liên tục về kết quả phân tích phân tầng, biến số phân tầng có nghĩa, liên
tục hỏi “Tại sao? Tại sao lại lại phát sinh sự chênh lệch?” cho đến khi nào có được câu trả lời là
“Không biết” và đưa ra nhân tố cơ bản

Là việc biểu thị quá trình tìm ra nguyên nhân gốc rễ của vấn đề bằng hình vẽ, phạm trù hóa nguyên nhân
tiềm ẩn của vấn đề theo thứ tự, sau khi viết lại tất cả các vấn đề trong Process thuộc phạm trù đó, tiến
hành theo phương thức tìm ra nguyên nhân cơ bản chủ yếu

Phương pháp phân tích phân biệt hạng mục chủ yếu theo hình thức Tree tùy theo phương thức tư duy của
MECE
: Khi 5M1E, 4P, Process Sequence, Brainstorming, cân nhắc và soạn thảo hạng mục chủ yếu được đưa ra


**5. Tiếp cận kĩ thuật** Mục đích: Thông qua phân tích Process và Machanism,…, triển khai nội dung định phải làm rõ để giải
quyết dự án, liên kết các lí luận vật lí/hóa học có liên quan lại và thiết lập giả thuyết, đưa ra phương thức
lí luận

※ Nội dung chi tiết về Brain Writing, 5Why, biểu đồ xương cá, Logic Tree: tham khảo phụ lục

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
355

**Thông qua phân tích Process và Machanism,…, triển khai nội dung định phải làm rõ để giải**
**quyết dự án, liên kết các lí luận vật lí/hóa học có liên quan lại và thiết lập giả thuyết, đưa ra**
**phương thức lí luận**

    **Lựa chọn Model lí luận**
      - Liên kết các nguyên tắc cơ bản/lí luận của vật lí, hóa học và đưa ra phương thức lí luận, lựa chọn phương thức lí luận
có liên quan và giải quyết vấn đề sau khi tìm kiếm luận văn kĩ thuật

      - Trường hợp không đưa ra theo phương thức lí luận, phỏng đoán Pattern đại diện có liên quan đến sự di chuyển của
CTQ bằng Logic vừa duy trì tính phù hợp về vật lí, hóa học, vừa đúng trên phương diện diễn dịch

※ Pattern đại diện

**Tăng, giảm đơn thuần** **Đơn chóp (Unimodal)** **Đa chóp (Bimodal)** **Bão hòa** **Chu kì đơn**

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
356

tích Machanism,
tiến hành cải tiến nhanh chóng bằng Quick Win,
với nhân tố nào không cải tiến cơ bản bằng
Quick Win được thì tiến hành Step sau

**LG Display DX Black Belt 과정, Copyright@2023, LG Display**
357


