Câu 1: trả về score tốt hơn:
pac man k dừng lại: kiểm tra nếu action bằng stop thì trả về âm vô cùng
neus bước tiếp thep pacman trùng với ghost trả về âm vô cùng


duyệt toàn bộ chuỗi thức ăn trả về khoảng cách thức ăn gần nhất, đổi dấu để khoảng cách thức ăn nhỏ nhất luôn là số lớn nhất
Câu 2
hàm minimax trả về (score,action)
kết quả cuối lấy [score,action][1]=action

kiểm tra điều kiện thoát khỏi đệ quy: đã đủ dộ sâu, thua hoặc thắng
có 1 biến maximizing để biết được đó là tầng pacman hay không 
ở tầng pacaman tính tất cả điểm của nước di tiếp theo, gọi tầng ghost kế tiếp 
lấy điểm cao nhất
tìm điểm cao nhất tương ứng với action nào thì trả về


sang tầng ghosht
kiểm tra nếu đã thực hiện đủ ghost thì gọi lại pacman và giảm depth đi 1
không thì lấy tất cả điểm của ghost, gọi lại ghost mới
lấy điểm nhỏ nhất và action tương đương


Câu 3 anphabeta
Thêm vào ở đầu vào có anpha bằng âm vô cùng beta bằng dương vô cùng
ở tầng pac man duyệt lần lượt: nếu có score lớn hơn anpha thì thay anpha mới bằng số dó
				nếu score đó lớn hơn beta thì hủy k duyệt tiếp
ở tầng pac man duyệt lần lượt: nếu có score nhỏ hơn beta thì thay beta mới bằng số dó
				nếu score đó nhỏ hơn anpha thì hủy k duyệt tiếp


Câu 4
ở tầng pacman trả về trung bình cộng điểm của các nước đi của ghost



câu 5

Tinhs điểm ban đầu:bằng score hiện tại - (số thức ăn còn cần phải ăn * 1 số cơ sở)
có số điểm cơ sở cho thức ăn,capsule, ghost
có trọng số cơ sở cho thức ăn,capsule, ghost
duyệt list thức ăn: Gần hơn là tốt hơn(tính tất cả)
duyệt capsule: gần hơn là tốt hơn(tính tất cả)
duyệt ghost: xa hơn là tốt hơn
		nếu khoảng cách quá gần thì trả về score âm vô cùng

